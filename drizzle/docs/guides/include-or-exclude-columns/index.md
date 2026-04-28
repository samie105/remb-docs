---
title: "Drizzle ORM - Include or Exclude Columns in Query"
source: "https://orm.drizzle.team/docs/guides/include-or-exclude-columns"
canonical_url: "https://orm.drizzle.team/docs/guides/include-or-exclude-columns"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:00:19.979Z"
content_hash: "c42ee4b71b9123694b71d872990f2bd5cc859094f970face5416e70d02ddbf56"
menu_path: ["Drizzle ORM - Include or Exclude Columns in Query"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/guides/gel-ext-auth/index.md", "title": "Drizzle ORM - Gel auth extension"}
nav_next: {"path": "drizzle/docs/guides/incrementing-a-value/index.md", "title": "Drizzle ORM - SQL Increment value"}
---

Drizzle | Include or Exclude Columns in Query

Drizzle has flexible API for including or excluding columns in queries. To include all columns you can use `.select()` method like this:

```ts
import { posts } from './schema';

const db = drizzle(...);

await db.select().from(posts);
```

```ts
// result type
type Result = {
  id: number;
  title: string;
  content: string;
  views: number;
}[];
```

```ts
import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  content: text('content').notNull(),
  views: integer('views').notNull().default(0),
});
```

To include specific columns you can use `.select()` method like this:

```ts
await db.select({ title: posts.title }).from(posts);
```

```ts
// result type
type Result = {
  title: string;
}[];
```

To include all columns with extra columns you can use `getColumns()` utility function like this:

IMPORTANT

`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](drizzle/docs/upgrade-v1/index.md))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`

```ts
import { getColumns, sql } from 'drizzle-orm';

await db
  .select({
    ...getColumns(posts),
    titleLength: sql<number>`length(${posts.title})`,
  })
  .from(posts);
```

```ts
// result type
type Result = {
  id: number;
  title: string;
  content: string;
  views: number;
  titleLength: number;
}[];
```

To exclude columns you can use `getColumns()` utility function like this:

IMPORTANT

`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](drizzle/docs/upgrade-v1/index.md))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`

```ts
import { getColumns } from 'drizzle-orm';

const { content, ...rest } = getColumns(posts); // exclude "content" column

await db.select({ ...rest }).from(posts); // select all other columns
```

```ts
// result type
type Result = {
  id: number;
  title: string;
  views: number;
}[];
```

This is how you can include or exclude columns with joins:

```ts
import { eq, getColumns } from 'drizzle-orm';
import { comments, posts, users } from './db/schema';

// exclude "userId" and "postId" columns from "comments"
const { userId, postId, ...rest } = getColumns(comments);

await db
  .select({
    postId: posts.id, // include "id" column from "posts"
    comment: { ...rest }, // include all other columns
    user: users, // equivalent to getColumns(users)
  })
  .from(posts)
  .leftJoin(comments, eq(posts.id, comments.postId))
  .leftJoin(users, eq(users.id, posts.userId));
```

```ts
// result type
type Result = {
  postId: number;
  comment: {
    id: number;
    content: string;
    createdAt: Date;
  } | null;
  user: {
    id: number;
    name: string;
    email: string;
  } | null;
}[];
```

```ts
import { integer, pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  email: text('email').notNull(),
});

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  content: text('content').notNull(),
  views: integer('views').notNull().default(0),
  userId: integer('user_id').notNull().references(() => users.id),
});

export const comments = pgTable('comments', {
  id: serial('id').primaryKey(),
  postId: integer('post_id').notNull().references(() => posts.id),
  userId: integer('user_id').notNull().references(() => users.id),
  content: text('content').notNull(),
  createdAt: timestamp('created_at').notNull().defaultNow(),
});
```

Drizzle has useful relational queries API, that lets you easily include or exclude columns in queries. This is how you can include all columns:

```ts
import * as schema from './schema';

const db = drizzle(..., { schema });

await db.query.posts.findMany();
```

```ts
// result type
type Result = {
  id: number;
  title: string;
  content: string;
  views: number;
}[]
```

```ts
import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  content: text('content').notNull(),
  views: integer('views').notNull().default(0),
});
```

This is how you can include specific columns using relational queries:

```ts
await db.query.posts.findMany({
  columns: {
    title: true,
  },
});
```

```ts
// result type
type Result = {
  title: string;
}[]
```

This is how you can include all columns with extra columns using relational queries:

```ts
import { sql } from 'drizzle-orm';

await db.query.posts.findMany({
  extras: {
    titleLength: sql<number>`length(${posts.title})`.as('title_length'),
  },
});
```

```ts
// result type
type Result = {
  id: number;
  title: string;
  content: string;
  views: number;
  titleLength: number;
}[];
```

This is how you can exclude columns using relational queries:

```ts
await db.query.posts.findMany({
  columns: {
    content: false,
  },
});
```

```ts
// result type
type Result = {
  id: number;
  title: string;
  views: number;
}[]
```

This is how you can include or exclude columns with relations using relational queries:

```ts
import * as schema from './schema';

const db = drizzle(..., { schema });

await db.query.posts.findMany({
  columns: {
    id: true, // include "id" column
  },
  with: {
    comments: {
      columns: {
        userId: false, // exclude "userId" column
        postId: false, // exclude "postId" column
      },
    },
    user: true, // include all columns from "users" table
  },
});
```

```ts
// result type
type Result = {
  id: number;
  user: {
    id: number;
    name: string;
    email: string;
  };
  comments: {
    id: number;
    content: string;
    createdAt: Date;
  }[];
}[]
```

```ts
import { relations } from 'drizzle-orm';
import { integer, pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  email: text('email').notNull(),
});

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  content: text('content').notNull(),
  views: integer('views').notNull().default(0),
  userId: integer('user_id').notNull().references(() => users.id),
});

export const comments = pgTable('comments', {
  id: serial('id').primaryKey(),
  postId: integer('post_id').notNull().references(() => posts.id),
  userId: integer('user_id').notNull().references(() => users.id),
  content: text('content').notNull(),
  createdAt: timestamp('created_at').notNull().defaultNow(),
});

export const usersRelations = relations(users, ({ many }) => ({
  posts: many(posts),
  comments: many(comments),
}));

export const postsRelations = relations(posts, ({ many, one }) => ({
  comments: many(comments),
  user: one(users, { fields: [posts.userId], references: [users.id] }),
}));

export const commentsRelations = relations(comments, ({ one }) => ({
  post: one(posts, { fields: [comments.postId], references: [posts.id] }),
  user: one(users, { fields: [comments.userId], references: [users.id] }),
}));
```

This is how you can create custom solution for conditional select:

```ts
import { posts } from './schema';

const searchPosts = async (withTitle = false) => {
  await db
    .select({
      id: posts.id,
      ...(withTitle && { title: posts.title }),
    })
    .from(posts);
};

await searchPosts();
await searchPosts(true);
```

```ts
// result type
type Result = {
  id: number;
  title?: string | undefined;
}[];
```

```ts
import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  content: text('content').notNull(),
  views: integer('views').notNull().default(0),
});
```
