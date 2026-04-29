---
title: "Getting started with Prisma Migrate"
source: "https://www.prisma.io/docs/orm/prisma-migrate/getting-started"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/getting-started"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:34:26.158Z"
content_hash: "3fa4fd6b97fdc81bbaf6f22977bc470faaf379a7b4be9907df64b00b3d8455c5"
menu_path: ["Getting started with Prisma Migrate"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "../index.md", "title": "Overview of Prisma Migrate"}
nav_next: {"path": "../understanding-prisma-migrate/mental-model/index.md", "title": "Understanding Migrations"}
---

Learn how to migrate your schema in a development environment using Prisma Migrate

To get started with Prisma Migrate, start by adding some models to your `schema.prisma`

schema.prisma

```
datasource db {
  provider = "postgresql"
}

model User { 
  id    Int    @id @default(autoincrement()) 
  name  String
  posts Post[]
}

model Post { 
  id        Int     @id @default(autoincrement()) 
  title     String
  published Boolean @default(true) 
  authorId  Int
  author    User    @relation(fields: [authorId], references: [id]) 
} 
```

### [Create an initial migration](#create-an-initial-migration)

Create an initial migration using the `prisma migrate` command:

This will generate a migration with the appropriate commands for your database.

migration.sql

```
CREATE TABLE "User" (
  "id" SERIAL,
  "name" TEXT NOT NULL,
  PRIMARY KEY ("id")
);
-- CreateTable
CREATE TABLE "Post" (
  "id" SERIAL,
  "title" TEXT NOT NULL,
  "published" BOOLEAN NOT NULL DEFAULT true,
  "authorId" INTEGER NOT NULL,
  PRIMARY KEY ("id")
);
-- AddForeignKey
ALTER TABLE
  "Post"
ADD
  FOREIGN KEY("authorId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

Your Prisma schema is now in sync with your database schema and you have initialized a migration history:

```
migrations/
  └─ 20210313140442_init/
    └─ migration.sql
```

> **Note**: The folder name will be different for you. Folder naming is in the format of YYYYMMDDHHMMSS\_your\_text\_from\_name\_flag.

### [Additional migrations](#additional-migrations)

Now say you add additional fields to your model

schema.prisma

```
model User {
  id       Int    @id @default(autoincrement())
  jobTitle String
  name     String
  posts    Post[]
}
```

You can run `prisma migrate` again to update your migrations

migration.sql

```
  -- AlterTable
ALTER TABLE
  "User"
ADD
  COLUMN "jobTitle" TEXT NOT NULL;
```

Your Prisma schema is once again in sync with your database schema, and your migration history contains two migrations:

```
migrations/
  └─ 20210313140442_init/
    └─ migration.sql
  └─ 20210313140442_added_job_title/
    └─ migration.sql
```

### [Committing to versions control](#committing-to-versions-control)

Your migration history can be [committed to version control](../understanding-prisma-migrate/migration-histories/index.md#committing-the-migration-history-to-source-control) and use to [deploy changes to test environments and production](../workflows/development-and-production/index.md#production-and-testing-environments).

It's possible to integrate Prisma migrations to an existing project.

### [Introspect to create or update your Prisma schema](#introspect-to-create-or-update-your-prisma-schema)

Make sure your Prisma schema is in sync with your database schema. This should already be true if you are using a previous version of Prisma Migrate.

### [Create a baseline migration](#create-a-baseline-migration)

Create a baseline migration that creates an initial history of the database before using Prisma migrate. This migrations contains the data that must be maintained, which means the database cannot be reset. This tells Prisma migrate to assume that one or more migrations have **already been applied**. This prevents generated migrations from failing when they try to create tables and fields that already exist.

To create a baseline migration:

-   If you already have a `prisma/migrations` folder, delete, move, rename, or archive this folder.
-   Create a new `prisma/migrations` directory.
-   Then create another new directory with your preferred name. What's important is to use a prefix of `0_` so that Prisma migrate applies migrations in a [lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order). You can use a different value such as the current timestamp.
-   Generate a migration and save it to a file using `prisma migrate diff`:

-   Review the generated migration.

### [Work around features not supported by Prisma Schema Language](#work-around-features-not-supported-by-prisma-schema-language)

To include [unsupported database features](../workflows/unsupported-database-features/index.md) that already exist in the database, you must replace or modify the initial migration SQL:

-   Open the `migration.sql` file generated in the [Create a baseline migration](#create-a-baseline-migration) section.
    
-   Modify the generated SQL. For example:
    
    -   If the changes are minor, you can append additional custom SQL to the generated migration. The following example creates a trigger function:

migration.sql

```
/* Generated migration SQL */

CREATE OR REPLACE FUNCTION notify_on_insert() 
RETURNS TRIGGER AS $$ 
BEGIN
  PERFORM pg_notify('new_record', NEW.id::text); 
  RETURN NEW; 
END; 
$$ LANGUAGE plpgsql; 
```

-   If the changes are significant, it can be easier to replace the entire migration file with the result of a database dump:
    
    -   [`mysqldump`](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)
    -   [`pg_dump`](https://www.postgresql.org/docs/12/app-pgdump.html).
    
    When using `pg_dump` for this, you'll need to update the `search_path` as follows with this command: `SELECT pg_catalog.set_config('search_path', '', false);`, otherwise you'll run into the following error: `The underlying table for model '_prisma_migrations' does not exist.`
    

### [Apply the initial migrations](#apply-the-initial-migrations)

To apply your initial migration(s):

-   Run the following command against your database:

-   Review the database schema to ensure the migration leads to the desired end-state (for example, by comparing the schema to the production database).

The new migration history and the database schema should now be in sync with your Prisma schema.

### [Commit the migration history and Prisma schema](#commit-the-migration-history-and-prisma-schema)

Commit the following to source control:

-   The entire migration history folder
-   The `schema.prisma` file

-   Refer to the [Deploying database changes with Prisma Migrate](../../prisma-client/deployment/deploy-database-changes-with-prisma-migrate/index.md) guide for more on deploying migrations to production.
-   Refer to the [Production Troubleshooting](../workflows/patching-and-hotfixing/index.md#fixing-failed-migrations-with-migrate-diff-and-db-execute) guide to learn how to debug and resolve failed migrations in production using `prisma migrate diff`, `prisma db execute` and/ or `prisma migrate resolve`.
