---
title: "Operating against partial structures of your model types"
source: "https://www.prisma.io/docs/orm/prisma-client/type-safety/operating-against-partial-structures-of-model-types"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/type-safety/operating-against-partial-structures-of-model-types"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:40:18.569Z"
content_hash: "27c286447043e861afa3f5294161ed6d8a9669c5785778b32936cac13530d628"
menu_path: ["Operating against partial structures of your model types"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/type-safety/index.md", "title": "Type safety Overview"}
nav_next: {"path": "prisma/docs/orm/prisma-client/type-safety/prisma-type-system/index.md", "title": "How to use Prisma ORM's type system"}
---

Type Safety

This page documents various scenarios for using the generated types from the Prisma namespace

When using Prisma Client, every model from your [Prisma schema](prisma/docs/orm/prisma-schema/overview/index.md) is translated into a dedicated TypeScript type. For example, assume you have the following `User` and `Post` models:

```
model User {
  id    Int     @id
  email String  @unique
  name  String?
  posts Post[]
}

model Post {
  id        Int     @id
  author    User    @relation(fields: [userId], references: [id])
  title     String
  published Boolean @default(false)
  userId    Int
}
```

The Prisma Client code that's generated from this schema contains this representation of the `User` type:

```
export type User = {
  id: string;
  email: string;
  name: string | null;
};
```

### [Description](#description)

In some scenarios, you may need a _variation_ of the generated `User` type. For example, when you have a function that expects an instance of the `User` model that carries the `posts` relation. Or when you need a type to pass only the `User` model's `email` and `name` fields around in your application code.

### [Solution](#solution)

As a solution, you can customize the generated model type using Prisma Client's helper types.

The `User` type only contains the model's [scalar](prisma/docs/orm/prisma-schema/data-model/models/index.md#scalar-fields) fields, but doesn't account for any relations. That's because [relations are not included by default](https://www.prisma.io/docs/v6/orm/prisma-client/queries/select-fields#return-the-default-fields) in Prisma Client queries.

However, sometimes it's useful to have a type available that **includes a relation** (i.e. a type that you'd get from an API call that uses [`include`](https://www.prisma.io/docs/v6/orm/prisma-client/queries/select-fields#return-nested-objects-by-selecting-relation-fields)). Similarly, another useful scenario could be to have a type available that **includes only a subset of the model's scalar fields** (i.e. a type that you'd get from an API call that uses [`select`](https://www.prisma.io/docs/v6/orm/prisma-client/queries/select-fields#select-specific-fields)).

One way of achieving this would be to define these types manually in your application code:

```
// 1: Define a type that includes the relation to `Post`
type UserWithPosts = {
  id: string;
  email: string;
  name: string | null;
  posts: Post[];
};

// 2: Define a type that only contains a subset of the scalar fields
type UserPersonalData = {
  email: string;
  name: string | null;
};
```

While this is certainly feasible, this approach increases the maintenance burden upon changes to the Prisma schema as you need to manually maintain the types. A cleaner solution to this is to use the `UserGetPayload` type that is generated and exposed by Prisma Client under the `Prisma` namespace in combination with TypeScript's `satisfies` operator.

The following example uses the `satisfies` operator to create two type-safe objects and then uses the `Prisma.UserGetPayload` utility function to create a type that can be used to return all users and their posts.

```
import { Prisma } from "@prisma/client";

// 1: Define a type that includes the relation to `Post`
const userWithPosts = { include: { posts: true } } satisfies Prisma.UserDefaultArgs;

// 2: Define a type that only contains a subset of the scalar fields
const userPersonalData = { select: { email: true, name: true } } satisfies Prisma.UserDefaultArgs;

// 3: This type will include a user and all their posts
type UserWithPosts = Prisma.UserGetPayload<typeof userWithPosts>;
```

The main benefits of the latter approach are:

-   Cleaner approach as it leverages Prisma Client's generated types
-   Reduced maintenance burden and improved type safety when the schema changes

### [Description](#description-1)

When doing [`select`](prisma/docs/orm/reference/prisma-client-reference/index.md#select) or [`include`](prisma/docs/orm/reference/prisma-client-reference/index.md#include) operations on your models and returning these variants from a function, it can be difficult to gain access to the return type, e.g:

```
// Function definition that returns a partial structure
async function getUsersWithPosts() {
  const users = await prisma.user.findMany({ include: { posts: true } });
  return users;
}
```

Extracting the type that represents "users with posts" from the above code snippet requires some advanced TypeScript usage:

```
// Function definition that returns a partial structure
async function getUsersWithPosts() {
  const users = await prisma.user.findMany({ include: { posts: true } });
  return users;
}

// Extract `UsersWithPosts` type with
type ThenArg<T> = T extends PromiseLike<infer U> ? U : T;
type UsersWithPosts = ThenArg<ReturnType<typeof getUsersWithPosts>>;

// run inside `async` function
const usersWithPosts: UsersWithPosts = await getUsersWithPosts();
```

### [Solution](#solution-1)

You can use native the TypeScript utility type [`Awaited`](https://www.typescriptlang.org/docs/handbook/utility-types.html#awaitedtype) and [`ReturnType`](https://www.typescriptlang.org/docs/handbook/utility-types.html#returntypetype) to solve the problem elegantly:

```
type UsersWithPosts = Awaited<ReturnType<typeof getUsersWithPosts>>;
```
