---
title: "CRUD"
source: "https://www.prisma.io/docs/orm/prisma-client/queries/crud"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/queries/crud"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:40.252Z"
content_hash: "0a58a46fe33c5a52879d4ee8a5c04df25799802777d826d5b2064ff6a20cfe1d"
menu_path: ["CRUD"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/observability-and-logging/sql-comments/index.md", "title": "SQL comments"}
nav_next: {"path": "prisma/docs/orm/prisma-client/queries/aggregation-grouping-summarizing/index.md", "title": "Aggregation, grouping, and summarizing"}
---

This page describes how to perform CRUD operations with Prisma Client:

*   [Create](#create) - Insert records
*   [Read](#read) - Query records
*   [Update](#update) - Modify records
*   [Delete](#delete) - Remove records

See the [Prisma Client API reference](prisma/docs/orm/reference/prisma-client-reference/index.md) for detailed method documentation.

### [Create a single record](#create-a-single-record)

```
const user = await prisma.user.create({
  data: {
    email: "elsa@prisma.io",
    name: "Elsa Prisma",
  },
});
```

The `id` is auto-generated. Your schema determines which fields are mandatory.

### [Create multiple records](#create-multiple-records)

```
const createMany = await prisma.user.createMany({
  data: [
    { name: "Bob", email: "bob@prisma.io" },
    { name: "Yewande", email: "yewande@prisma.io" },
  ],
  skipDuplicates: true, // Skip records with duplicate unique fields
});
// Returns: { count: 2 }
```

### [Create and return multiple records](#create-and-return-multiple-records)

Supported by PostgreSQL, CockroachDB, and SQLite.

```
const users = await prisma.user.createManyAndReturn({
  data: [
    { name: "Alice", email: "alice@prisma.io" },
    { name: "Bob", email: "bob@prisma.io" },
  ],
});
```

See [Nested writes](prisma/docs/orm/prisma-client/queries/relation-queries/index.md#nested-writes) for creating records with relations.

### [Get record by ID or unique field](#get-record-by-id-or-unique-field)

```
// By unique field
const user = await prisma.user.findUnique({
  where: { email: "elsa@prisma.io" },
});

// By ID
const user = await prisma.user.findUnique({
  where: { id: 99 },
});
```

### [Get all records](#get-all-records)

```
const users = await prisma.user.findMany();
```

### [Get first matching record](#get-first-matching-record)

```
const user = await prisma.user.findFirst({
  where: { posts: { some: { likes: { gt: 100 } } } },
  orderBy: { id: "desc" },
});
```

### [Filter records](#filter-records)

```
// Single field filter
const users = await prisma.user.findMany({
  where: { email: { endsWith: "prisma.io" } },
});

// Multiple conditions with OR/AND
const users = await prisma.user.findMany({
  where: {
    OR: [{ name: { startsWith: "E" } }, { AND: { profileViews: { gt: 0 }, role: "ADMIN" } }],
  },
});

// Filter by related records
const users = await prisma.user.findMany({
  where: {
    email: { endsWith: "prisma.io" },
    posts: { some: { published: false } },
  },
});

// Filter by geometry (PostgreSQL with PostGIS)
const nearbyLocations = await prisma.location.findMany({
  where: {
    position: {
      near: {
        point: [13.4, 52.5],
        maxDistance: 1000, // meters
      },
    },
  },
});
```

See [Filtering and sorting](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting) for more examples, or [Working with geometry fields](prisma/docs/orm/prisma-client/special-fields-and-types/working-with-geometry-fields/index.md) for spatial queries.

### [Select fields](#select-fields)

```
const user = await prisma.user.findUnique({
  where: { email: "emma@prisma.io" },
  select: { email: true, name: true },
});
// Returns: { email: 'emma@prisma.io', name: "Emma" }
```

```
const users = await prisma.user.findMany({
  where: { role: "ADMIN" },
  include: { posts: true },
});
```

See [Select fields](https://www.prisma.io/docs/v6/orm/prisma-client/queries/select-fields) and [Relation queries](prisma/docs/orm/prisma-client/queries/relation-queries/index.md) for more.

### [Update a single record](#update-a-single-record)

```
const updateUser = await prisma.user.update({
  where: { email: "viola@prisma.io" },
  data: { name: "Viola the Magnificent" },
});
```

### [Update multiple records](#update-multiple-records)

```
const updateUsers = await prisma.user.updateMany({
  where: { email: { contains: "prisma.io" } },
  data: { role: "ADMIN" },
});
// Returns: { count: 19 }
```

### [Update and return multiple records](#update-and-return-multiple-records)

Supported by PostgreSQL, CockroachDB, and SQLite.

```
const users = await prisma.user.updateManyAndReturn({
  where: { email: { contains: "prisma.io" } },
  data: { role: "ADMIN" },
});
```

### [Upsert (update or create)](#upsert-update-or-create)

```
const upsertUser = await prisma.user.upsert({
  where: { email: "viola@prisma.io" },
  update: { name: "Viola the Magnificent" },
  create: { email: "viola@prisma.io", name: "Viola the Magnificent" },
});
```

### [Atomic number operations](#atomic-number-operations)

```
await prisma.post.updateMany({
  data: {
    views: { increment: 1 },
    likes: { increment: 1 },
  },
});
```

See [Relation queries](prisma/docs/orm/prisma-client/queries/relation-queries/index.md) for connecting and disconnecting related records.

### [Delete a single record](#delete-a-single-record)

The following query uses [`delete()`](prisma/docs/orm/reference/prisma-client-reference/index.md#delete) to delete a single `User` record:

```
const deleteUser = await prisma.user.delete({
  where: {
    email: "bert@prisma.io",
  },
});
```

Attempting to delete a user with one or more posts result in an error, as every `Post` requires an author - see [cascading deletes](#cascading-deletes-deleting-related-records).

### [Delete multiple records](#delete-multiple-records)

The following query uses [`deleteMany()`](prisma/docs/orm/reference/prisma-client-reference/index.md#deletemany) to delete all `User` records where `email` contains `prisma.io`:

```
const deleteUsers = await prisma.user.deleteMany({
  where: {
    email: {
      contains: "prisma.io",
    },
  },
});
```

Attempting to delete a user with one or more posts result in an error, as every `Post` requires an author - see [cascading deletes](#cascading-deletes-deleting-related-records).

### [Delete all records](#delete-all-records)

The following query uses [`deleteMany()`](prisma/docs/orm/reference/prisma-client-reference/index.md#deletemany) to delete all `User` records:

```
const deleteUsers = await prisma.user.deleteMany({});
```

Be aware that this query will fail if the user has any related records (such as posts). In this case, you need to [delete the related records first](#cascading-deletes-deleting-related-records).

The following query uses [`delete()`](prisma/docs/orm/reference/prisma-client-reference/index.md#delete) to delete a single `User` record:

```
const deleteUser = await prisma.user.delete({
  where: {
    email: "bert@prisma.io",
  },
});
```

However, the example schema includes a **required relation** between `Post` and `User`, which means that you cannot delete a user with posts:

```
The change you are trying to make would violate the required relation 'PostToUser' between the `Post` and `User` models.
```

To resolve this error, you can:

*   Make the relation optional:
    
    ```
    model Post {
      id       Int   @id @default(autoincrement())
      author   User? @relation(fields: [authorId], references: [id]) 
      authorId Int?
      author   User  @relation(fields: [authorId], references: [id]) 
      authorId Int
    }
    ```
    
*   Change the author of the posts to another user before deleting the user.
    
*   Delete a user and all their posts with two separate queries in a transaction (all queries must succeed):
    
    ```
    const deletePosts = prisma.post.deleteMany({
      where: {
        authorId: 7,
      },
    });
    
    const deleteUser = prisma.user.delete({
      where: {
        id: 7,
      },
    });
    
    const transaction = await prisma.$transaction([deletePosts, deleteUser]);
    ```
    

### [Delete all records from all tables](#delete-all-records-from-all-tables)

Sometimes you want to remove all data from all tables but keep the actual tables. This can be particularly useful in a development environment and whilst testing.

The following shows how to delete all records from all tables with Prisma Client and with Prisma Migrate.

#### [Deleting all data with `deleteMany()`](#deleting-all-data-with-deletemany)

When you know the order in which your tables should be deleted, you can use the [`deleteMany`](prisma/docs/orm/reference/prisma-client-reference/index.md#deletemany) function. This is executed synchronously in a [`$transaction`](prisma/docs/orm/prisma-client/queries/transactions/index.md) and can be used with all types of databases.

```
const deletePosts = prisma.post.deleteMany();
const deleteProfile = prisma.profile.deleteMany();
const deleteUsers = prisma.user.deleteMany();

// The transaction runs synchronously so deleteUsers must run last.
await prisma.$transaction([deleteProfile, deletePosts, deleteUsers]);
```

✅ **Pros**:

*   Works well when you know the structure of your schema ahead of time
*   Synchronously deletes each tables data

❌ **Cons**:

*   When working with relational databases, this function doesn't scale as well as having a more generic solution which looks up and `TRUNCATE`s your tables regardless of their relational constraints. Note that this scaling issue does not apply when using the MongoDB connector.

> **Note**: The `$transaction` performs a cascading delete on each models table so they have to be called in order.

#### [Deleting all data with raw SQL / `TRUNCATE`](#deleting-all-data-with-raw-sql--truncate)

If you are comfortable working with raw SQL, you can perform a `TRUNCATE` query on a table using [`$executeRawUnsafe`](prisma/docs/orm/prisma-client/using-raw-sql/raw-queries/index.md#executerawunsafe).

In the following examples, the first tab shows how to perform a `TRUNCATE` on a Postgres database by using a `$queryRaw` look up that maps over the table and `TRUNCATES` all tables in a single query.

The second tab shows performing the same function but with a MySQL database. In this instance the constraints must be removed before the `TRUNCATE` can be executed, before being reinstated once finished. The whole process is run as a `$transaction`

✅ **Pros**:

*   Scalable
*   Very fast

❌ **Cons**:

*   Can't undo the operation
*   Using reserved SQL key words as tables names can cause issues when trying to run a raw query

#### [Deleting all records with Prisma Migrate](#deleting-all-records-with-prisma-migrate)

If you use Prisma Migrate, you can use `migrate reset`, this will:

1.  Drop the database
2.  Create a new database
3.  Apply migrations
4.  Seed the database with data

### [Create a deeply nested tree of records](#create-a-deeply-nested-tree-of-records)

*   A single `User`
*   Two new, related `Post` records
*   Connect or create `Category` per post

```
const u = await prisma.user.create({
  include: {
    posts: {
      include: {
        categories: true,
      },
    },
  },
  data: {
    email: "emma@prisma.io",
    posts: {
      create: [
        {
          title: "My first post",
          categories: {
            connectOrCreate: [
              {
                create: { name: "Introductions" },
                where: {
                  name: "Introductions",
                },
              },
              {
                create: { name: "Social" },
                where: {
                  name: "Social",
                },
              },
            ],
          },
        },
        {
          title: "How to make cookies",
          categories: {
            connectOrCreate: [
              {
                create: { name: "Social" },
                where: {
                  name: "Social",
                },
              },
              {
                create: { name: "Cooking" },
                where: {
                  name: "Cooking",
                },
              },
            ],
          },
        },
      ],
    },
  },
});
```


