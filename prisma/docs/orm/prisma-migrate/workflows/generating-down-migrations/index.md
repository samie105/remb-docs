---
title: "Generating down migrations"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/generating-down-migrations"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/generating-down-migrations"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:41:21.638Z"
content_hash: "bc6324cb02a5b2e59d83a9115a4ef93860c39461f88ac76359daadd7aacd588b"
menu_path: ["Generating down migrations"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-migrate/workflows/development-and-production/index.md", "title": "Development and production"}
nav_next: {"path": "prisma/docs/orm/prisma-migrate/workflows/native-database-functions/index.md", "title": "Native database functions"}
---

Workflows

How to generate a down migration SQL file that reverses a given migration file

When generating a migration SQL file, you may wish to also create a "down migration" SQL file that reverses the schema changes in the corresponding "up migration" file. Note that "down migrations" are also sometimes called "migration rollbacks".

This guide explains how to use Prisma Migrate's [`migrate diff` command](../../../reference/prisma-cli-reference/index.md#migrate-diff) to create a down migration, and how to apply it to your production database with the [`db execute`](../../../reference/prisma-cli-reference/index.md#db-execute) command in the case of a failed up migration.

When generating a down migration file, there are some considerations to be aware of:

-   The down migration can be used to revert your database schema after a failed migration using the steps in [How to apply your down migration to a failed migration](#how-to-apply-your-down-migration-to-a-failed-migration). This requires the use of the `migrate resolve` command, which can only be used on failed migrations. If your up migration was successful and you want to revert it, you will instead need to revert your `schema.prisma` file to its state before the up migration, and generate a new migration with the `migrate dev` command.
-   The down migration will revert your database schema, but other changes to data and application code that are carried out as part of the up migration will not be reverted. For example, if you have a script that changes data during the migration, this data will not be changed back when you run the down migration.
-   You will not be able to use `migrate diff` to revert manually changed or added SQL in your migration files. If you have any custom additions, such as a view or trigger, you will need to:
    -   Create the down migration following [the instructions below](#how-to-generate-and-run-down-migrations)
    -   Create the up migration using [`migrate dev --create-only`](../../../reference/prisma-cli-reference/index.md), so that it can be edited before it is applied to the database
    -   Manually add your custom SQL to the up migration (e.g. adding a view)
    -   Manually add the inverted custom SQL to the down migration (e.g. dropping the view)

This section describes how to generate a down migration SQL file along with the corresponding up migration, and then run it to revert your database schema after a failed up migration on production.

As an example, take the following Prisma schema with a `User` and `Post` model as a starting point:

schema.prisma

```
model Post {
  id       Int     @id @default(autoincrement())
  title    String  @db.VarChar(255)
  content  String?
  author   User    @relation(fields: [authorId], references: [id])
  authorId Int
}

model User {
  id    Int     @id @default(autoincrement())
  name  String?
  posts Post[]
}
```

You will need to create the down migration first, before creating the corresponding up migration.

### [Generating the migrations](#generating-the-migrations)

-   Edit your Prisma schema to make the changes you require for your up migration. In this example, you will add a new `Profile` model:
    
    schema.prisma
    
    ```
    model Post {
      id       Int     @id @default(autoincrement())
      title    String  @db.VarChar(255)
      content  String?
      author   User    @relation(fields: [authorId], references: [id])
      authorId Int
    }
    
    model Profile { 
      id     Int     @id @default(autoincrement()) 
      bio    String?
      user   User    @relation(fields: [userId], references: [id]) 
      userId Int     @unique
    } 
    
    model User {
      id      Int      @id @default(autoincrement())
      name    String?
      posts   Post[]
      profile Profile?
    }
    ```
    
-   Generate the SQL file for the down migration. To do this, you will use `migrate diff` to make a comparison:
    
    -   from the newly edited schema
    -   to the state of the schema after the last migration
    
    and output this to a SQL script, `down.sql`.
    
    There are two potential options for specifying the 'to' state:
    
    -   Using `--to-migrations`: this makes a comparison to the state of the migrations given in the migrations directory. This is the preferred option, as it is more robust. To use this option, run:

-   Using `--to-config-datasource` (Prisma v7) or `--to-schema-datasource` (Prisma 6): this makes a comparison to the state of the database. This does not require a shadow database, but it does rely on the database having an up-to-date schema. To use this option, run:

-   Generate and apply the up migration with a name of `add_profile`:

This will create a new `<timestamp>_add_profile` directory inside the `prisma/migrations` directory, with your new `migration.sql` up migration file inside.

-   Copy your `down.sql` file into the new directory along with the up migration file.

### [How to apply your down migration to a failed migration](#how-to-apply-your-down-migration-to-a-failed-migration)

If your previous up migration failed, you can apply your down migration on your production database with the following steps:

To apply the down migration on your production database after a failed up migration:

-   Use `db execute` to run your `down.sql` file on the database server (using the database URL configured in `prisma.config.ts`):

-   Use `migrate resolve` to record that you rolled back the up migration named `add_profile`:
