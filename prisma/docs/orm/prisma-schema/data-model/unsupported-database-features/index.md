---
title: "Unsupported database features (Prisma Schema)"
source: "https://www.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:42:28.426Z"
content_hash: "6c24810f07d41f50b46d59097a1be1045ff8cdde92c144bc587276d5e753a3c1"
menu_path: ["Unsupported database features (Prisma Schema)"]
section_path: []
content_language: "en"
---
Data Model

How to support database features that do not have an equivalent syntax in Prisma Schema Language

Not all database functions and features of Prisma ORM's supported databases have a Prisma Schema Language equivalent. Refer to the [database features matrix](https://www.prisma.io/docs/orm/reference/database-features) for a complete list of supported features.

Prisma Schema Language supports several [functions](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions) that you can use to set the default value of a field. The following example uses the Prisma ORM-level `uuid()` function to set the value of the `id` field:

```
model Post {
  id String @id @default(uuid())
}
```

However, you can also use **native database functions** to define default values with [`dbgenerated(...)`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#dbgenerated) on relational databases (MongoDB does not have the concept of database-level functions). The following example uses the PostgreSQL `gen_random_uuid()` function to populate the `id` field:

```
model User {
  id String @id @default(dbgenerated("gen_random_uuid()")) @db.Uuid
}
```

### [When to use a database-level function](#when-to-use-a-database-level-function)

There are two reasons to use a database-level function:

-   There is no equivalent Prisma ORM function (for example, `gen_random_bytes` in PostgreSQL).
    
-   You cannot or do not want to rely on functions such `uuid()` and `cuid()`, which are only implemented at a Prisma ORM level and do not manifest in the database.
    
    Consider the following example, which sets the `id` field to a randomly generated `UUID`:
    
    ```
    model Post {
      id String @id @default(uuid())
    }
    ```
    
    The UUID is _only_ generated if you use Prisma Client to create the `Post`. If you create posts in any other way, such as a bulk import script written in plain SQL, you must generate the UUID yourself.
    

### [Enable PostgreSQL extensions for native database functions](#enable-postgresql-extensions-for-native-database-functions)

In PostgreSQL, some native database functions are part of an extension. For example, in PostgreSQL versions 12.13 and earlier, the `gen_random_uuid()` function is part of the [`pgcrypto`](https://www.postgresql.org/docs/10/pgcrypto.html) extension.

To use a PostgreSQL extension, you must first install it on the file system of your database server.

You can then activate the extension by installing it via a [customized migration](https://www.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations). Add the following SQL to your migration file:

```
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

If your project uses [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate), you must [install the extension as part of a migration](https://www.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions) . Do not install the extension manually, because it is also required by the shadow database.

Prisma Migrate returns the following error if the extension is not available:

```
Migration `20210221102106_failed_migration` failed to apply cleanly to a temporary database.
Database error: Error querying the database: db error: ERROR: type "pgcrypto" does not exist
```

Some database types of relational databases, such as `polygon` or `geometry`, do not have a Prisma Schema Language equivalent. Use the [`Unsupported`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#unsupported) field type to represent the field in your Prisma schema:

```
model Star {
  id       Int                    @id @default(autoincrement())
  position Unsupported("circle")? @default(dbgenerated("'<(10,4),11>'::circle")) 
}
```

The `prisma migrate dev` and `prisma db push` command will both create a `position` field of type `circle` in the database. However, the field will not be available in the generated Prisma Client.

Some features, like SQL views, cannot be represented in the Prisma schema. If your project uses [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate), you must [include unsupported features as part of a migration](https://www.prisma.io/docs/orm/prisma-migrate/workflows/unsupported-database-features) .
