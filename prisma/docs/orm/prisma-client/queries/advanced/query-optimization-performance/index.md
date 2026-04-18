---
title: "Query optimization"
source: "https://www.prisma.io/docs/orm/prisma-client/queries/advanced/query-optimization-performance"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/queries/advanced/query-optimization-performance"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:55.186Z"
content_hash: "1831d26c50b40b5371be3337e4b457a43adf5954ba0d84098ed8f916e55e4ce3"
menu_path: ["Query optimization"]
section_path: []
---
This page covers identifying and optimizing query performance with Prisma ORM.

[Query Insights](https://www.prisma.io/docs/query-insights) is built into Prisma Postgres and shows you which queries are slow, how expensive they are, and what to fix. It works out of the box for raw SQL, but to see Prisma ORM operations (model name, action, query shape) you need one extra step.

### [Enabling Prisma ORM attribution](#enabling-prisma-orm-attribution)

Install `@prisma/sqlcommenter-query-insights`:

```
npm install @prisma/sqlcommenter-query-insights
```

Then pass it to the `comments` option in your `PrismaClient` constructor:

```
import { prismaQueryInsights } from "@prisma/sqlcommenter-query-insights";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient({
  adapter: myAdapter, // driver adapter or Accelerate URL required
  comments: [prismaQueryInsights()],
});
```

This adds a SQL comment to every query containing the model, action, and parameterized query shape. Query Insights uses these annotations to trace SQL back to the exact Prisma call that generated it — even when a single Prisma call produces multiple SQL statements.

#### [Let your AI agent handle setup](#let-your-ai-agent-handle-setup)

Copy this prompt into your AI coding assistant:

```
Install and configure @prisma/sqlcommenter-query-insights in my project so I can
see Prisma ORM queries in Query Insights. Docs: https://www.prisma.io/docs/query-insights
```

Common causes of slow queries:

*   Over-fetching data
*   Missing indexes
*   Not caching repeated queries
*   Full table scans

Use [Query Insights](https://www.prisma.io/docs/query-insights) to identify which queries are affected and what to change.

It is generally more performant to read and write large amounts of data in bulk - for example, inserting `50,000` records in batches of `1000` rather than as `50,000` separate inserts. `PrismaClient` supports the following bulk queries:

*   [`createMany()`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#createmany)
*   [`createManyAndReturn()`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#createmanyandreturn)
*   [`deleteMany()`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#deletemany)
*   [`updateMany()`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#updatemany)
*   [`updateManyAndReturn()`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#updatemanyandreturn)
*   [`findMany()`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#findmany)

Creating multiple instances of `PrismaClient` can exhaust your database connection pool, especially in serverless or edge environments, potentially slowing down other queries. Learn more in the [serverless challenge](https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#the-serverless-challenge).

For applications with a traditional server, instantiate `PrismaClient` once and reuse it throughout your app instead of creating multiple instances. For example, instead of:

```
async function getPosts() {
  const prisma = new PrismaClient();
  await prisma.post.findMany();
}

async function getUsers() {
  const prisma = new PrismaClient();
  await prisma.user.findMany();
}
```

Define a single `PrismaClient` instance in a dedicated file and re-export it for reuse:

```
export const prisma = new PrismaClient();
```

Then import the shared instance:

```
import { prisma } from "db.ts";

async function getPosts() {
  await prisma.post.findMany();
}

async function getUsers() {
  await prisma.user.findMany();
}
```

For serverless development environments with frameworks that use HMR (Hot Module Replacement), ensure you properly handle a [single instance of Prisma in development](https://www.prisma.io/docs/orm/more/troubleshooting/nextjs#best-practices-for-using-prisma-client-in-development).

The n+1 problem occurs when looping through query results and performing one additional query **per result**.

### [Using `findUnique()` with the fluent API](#using-findunique-with-the-fluent-api)

Prisma's dataloader automatically batches `findUnique()` queries in the same tick. Use the fluent API to return related data:

```
// Instead of findMany per user, use:
return context.prisma.user
  .findUnique({ where: { id: parent.id } })
  .posts();
```

### [Using JOINs with `relationLoadStrategy`](#using-joins-with-relationloadstrategy)

```
const posts = await prisma.post.findMany({
  relationLoadStrategy: "join",
  where: { authorId: parent.id },
});
```

*   All criteria of the `where` filter are on scalar fields (unique or non-unique) of the same model you're querying.
*   All criteria use the `equal` filter, whether that's via the shorthand or explicit syntax `(where: { field: <val>, field1: { equals: <val> } })`.
*   No boolean operators or relation filters are present.

Automatic batching of `findUnique()` is particularly useful in a **GraphQL context**. GraphQL runs a separate resolver function for every field, which can make it difficult to optimize a nested query.

For example - the following GraphQL runs the `allUsers` resolver to get all users, and the `posts` resolver **once per user** to get each user's posts (n+1):

```
query {
  allUsers {
    id,
    posts {
      id
    }
  }
}
```

The `allUsers` query uses `user.findMany(..)` to return all users:

```
const Query = objectType({
  name: "Query",
  definition(t) {
    t.nonNull.list.nonNull.field("allUsers", {
      type: "User",
      resolve: (_parent, _args, context) => {
        return context.prisma.user.findMany();
      },
    });
  },
});
```

This results in a single SQL query:

```
{
  timestamp: 2021-02-19T09:43:06.332Z,
  query: 'SELECT `dev`.`User`.`id`, `dev`.`User`.`email`, `dev`.`User`.`name` FROM `dev`.`User` WHERE 1=1 LIMIT ? OFFSET ?',
  params: '[-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
```

However, the resolver function for `posts` is then invoked **once per user**. This results in a `findMany()` query **✘ per user** rather than a single `findMany()` to return all posts by all users (expand CLI output to see queries).

```
const User = objectType({
  name: "User",
  definition(t) {
    t.nonNull.int("id");
    t.string("name");
    t.nonNull.string("email");
    t.nonNull.list.nonNull.field("posts", {
      type: "Post",
      resolve: (parent, _, context) => {
        return context.prisma.post.findMany({
          where: { authorId: parent.id || undefined },
        });
      },
    });
  },
});
```

```
{
  timestamp: 2021-02-19T09:43:06.343Z,
  query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
  params: '[1,-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
{
  timestamp: 2021-02-19T09:43:06.347Z,
  query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
  params: '[3,-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
{
  timestamp: 2021-02-19T09:43:06.348Z,
  query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
  params: '[2,-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
{
  timestamp: 2021-02-19T09:43:06.348Z,
  query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
  params: '[4,-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
{
  timestamp: 2021-02-19T09:43:06.348Z,
  query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
  params: '[5,-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
// And so on
```

#### [Solution 1: Batching queries with the fluent API](#solution-1-batching-queries-with-the-fluent-api)

Use `findUnique()` in combination with [the fluent API](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries#fluent-api) (`.posts()`) as shown to return a user's posts. Even though the resolver is called once per user, the Prisma dataloader in Prisma Client **✔ batches the `findUnique()` queries**.

```
const User = objectType({
  name: "User",
  definition(t) {
    t.nonNull.int("id");
    t.string("name");
    t.nonNull.string("email");
    t.nonNull.list.nonNull.field("posts", {
      type: "Post",
      resolve: (parent, _, context) => {
        return context.prisma.post.findMany({
          where: { authorId: parent.id || undefined }, 
        }); 
        return context.prisma.user 
          .findUnique({
            where: { id: parent.id || undefined }, 
          }) 
          .posts(); 
      }, 
    });
  },
});
```

```
{
  timestamp: 2021-02-19T09:59:46.340Z,
  query: 'SELECT `dev`.`User`.`id`, `dev`.`User`.`email`, `dev`.`User`.`name` FROM `dev`.`User` WHERE 1=1 LIMIT ? OFFSET ?',
  params: '[-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
{
  timestamp: 2021-02-19T09:59:46.350Z,
  query: 'SELECT `dev`.`User`.`id` FROM `dev`.`User` WHERE `dev`.`User`.`id` IN (?,?,?) LIMIT ? OFFSET ?',
  params: '[1,2,3,-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
{
  timestamp: 2021-02-19T09:59:46.350Z,
  query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` IN (?,?,?) LIMIT ? OFFSET ?',
  params: '[1,2,3,-1,0]',
  duration: 0,
  target: 'quaint::connector::metrics'
}
```

If the `posts` resolver is invoked once per user, the dataloader in Prisma Client groups `findUnique()` queries with the same parameters and selection set. Each group is optimized into a single `findMany()`.

#### [Solution 2: Using JOINs to perform queries](#solution-2-using-joins-to-perform-queries)

You can perform the query with a [database join](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview) by setting `relationLoadStrategy` to `"join"`, ensuring that only **one** query is executed against the database.

```
const User = objectType({
  name: "User",
  definition(t) {
    t.nonNull.int("id");
    t.string("name");
    t.nonNull.string("email");
    t.nonNull.list.nonNull.field("posts", {
      type: "Post",
      resolve: (parent, _, context) => {
        return context.prisma.post.findMany({
          relationLoadStrategy: "join",
          where: { authorId: parent.id || undefined },
        });
      },
    });
  },
});
```

### [Avoiding n+1 in loops](#avoiding-n1-in-loops)

Don't loop with separate queries:

```
// BAD: n+1 queries
const users = await prisma.user.findMany({});
users.forEach(async (usr) => {
  const posts = await prisma.post.findMany({ where: { authorId: usr.id } });
});
```

Use `include` or `in` filter instead:

```
// GOOD: 2 queries with include
const usersWithPosts = await prisma.user.findMany({
  include: { posts: true },
});

// GOOD: 2 queries with in filter
const users = await prisma.user.findMany({});
const posts = await prisma.post.findMany({
  where: { authorId: { in: users.map(u => u.id) } },
});

// BEST: 1 query with join
const posts = await prisma.post.findMany({
  relationLoadStrategy: "join",
  where: { authorId: { in: users.map(u => u.id) } },
});
```

This is not an efficient way to query. Instead, you can:

*   Use nested reads ([`include`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#include) ) to return users and related posts
*   Use the [`in`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#in) filter
*   Set the [`relationLoadStrategy`](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview) to `"join"`

#### [Solving n+1 with `include`](#solving-n1-with-include)

You can use `include` to return each user's posts. This only results in **two** SQL queries - one to get users, and one to get posts. This is known as a [nested read](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-reads).

```
const usersWithPosts = await prisma.user.findMany({
  include: {
    posts: true,
  },
});
```

```
SELECT "public"."User"."id", "public"."User"."email", "public"."User"."name" FROM "public"."User" WHERE 1=1 OFFSET $1
SELECT "public"."Post"."id", "public"."Post"."title", "public"."Post"."authorId" FROM "public"."Post" WHERE "public"."Post"."authorId" IN ($1,$2,$3,$4) OFFSET $5
```

#### [Solving n+1 with `in`](#solving-n1-with-in)

If you have a list of user IDs, you can use the `in` filter to return all posts where the `authorId` is `in` that list of IDs:

```
const users = await prisma.user.findMany({});

const userIds = users.map((x) => x.id);

const posts = await prisma.post.findMany({
  where: {
    authorId: {
      in: userIds,
    },
  },
});
```

```
SELECT "public"."User"."id", "public"."User"."email", "public"."User"."name" FROM "public"."User" WHERE 1=1 OFFSET $1
SELECT "public"."Post"."id", "public"."Post"."createdAt", "public"."Post"."updatedAt", "public"."Post"."title", "public"."Post"."content", "public"."Post"."published", "public"."Post"."authorId" FROM "public"."Post" WHERE "public"."Post"."authorId" IN ($1,$2,$3,$4) OFFSET $5
```

#### [Solving n+1 with `relationLoadStrategy: "join"`](#solving-n1-with-relationloadstrategy-join)

You can perform the query with a [database join](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview) by setting `relationLoadStrategy` to `"join"`, ensuring that only **one** query is executed against the database.

```
const users = await prisma.user.findMany({});

const userIds = users.map((x) => x.id);

const posts = await prisma.post.findMany({
  relationLoadStrategy: "join",
  where: {
    authorId: {
      in: userIds,
    },
  },
});
```
