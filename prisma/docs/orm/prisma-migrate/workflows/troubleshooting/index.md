---
title: "Troubleshooting"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/troubleshooting"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/troubleshooting"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:41:59.123Z"
content_hash: "b833c14d51887518e4b935517a3dda61163261edd62ec1ca209ba07682fc3ef9"
menu_path: ["Troubleshooting"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-migrate/workflows/squashing-migrations/index.md", "title": "Squashing migrations"}
nav_next: {"path": "prisma/docs/orm/prisma-migrate/workflows/unsupported-database-features/index.md", "title": "Unsupported database features (Prisma Migrate)"}
---

Workflows

Troubleshooting issues with Prisma Migrate in a development environment.

This guide describes how to resolve issues with Prisma Migrate in a development environment, which often involves resetting your database. For production-focused troubleshooting, see:

-   [Production troubleshooting](../patching-and-hotfixing/index.md)
-   [Patching / hotfixing production databases](../patching-and-hotfixing/index.md)

## [Handling migration history conflicts](#handling-migration-history-conflicts)

A migration history conflict occurs when there are discrepancies between the **migrations folder in the file system** and the **`_prisma_migrations` table in the database**.

#### [Causes of migration history conflict in a development environment](#causes-of-migration-history-conflict-in-a-development-environment)

-   A migration that has already been applied is later modified
-   A migration that has already been applied is missing from the file system

In a development environment, switching between feature branches can result in a history conflict because the `_prisma_migrations` table contains migrations from `branch-1`, and switching to `branch-2` might cause some of those migrations to disappear.

#### [Fixing a migration history conflict in a development environment](#fixing-a-migration-history-conflict-in-a-development-environment)

If Prisma Migrate detects a migration history conflict when you run `prisma migrate dev`, the CLI will ask to reset the database and reapply the migration history.

Database schema drift occurs when your database schema is out of sync with your migration history - the database schema has 'drifted away' from the source of truth.

#### [Causes of schema drift in a development environment](#causes-of-schema-drift-in-a-development-environment)

Schema drift can occur if:

-   The database schema was changed _without_ using migrations - for example, by using [`prisma db push`](../../../reference/prisma-cli-reference/index.md#db-push) or manually changing the database schema.

#### [Fixing schema drift in a development environment](#fixing-schema-drift-in-a-development-environment)

If you made manual changes to the database that you do not want to keep, or can easily replicate in the Prisma schema:

-   Reset your database:

-   Replicate the changes in the Prisma schema and generate a new migration:

If you made manual changes to the database that you want to keep, you can:

-   Introspect the database:

Prisma will update your schema with the changes made directly in the database.

-   Generate a new migration to include the introspected changes in your migration history:

Prisma Migrate will prompt you to reset, then applies all existing migrations and a new migration based on the introspected changes. Your database and migration history are now in sync, including your manual changes.

#### [Causes of failed migrations in a development environment](#causes-of-failed-migrations-in-a-development-environment)

A migration might fail if:

-   You [modify a migration before running it](../customizing-migrations/index.md) and introduce a syntax error
-   You add a mandatory (`NOT NULL`) column to a table that already has data
-   The migration process stopped unexpectedly
-   The database shut down in the middle of the migration process

Each migration in the `_prisma_migrations` table has a `logs` column that stores the error.

#### [Fixing failed migrations in a development environment](#fixing-failed-migrations-in-a-development-environment)

The easiest way to handle a failed migration in a developer environment is to address the root cause and reset the database. For example:

-   If you introduced a SQL syntax error by manually editing the database, update the `migration.sql` file that failed and reset the database:

-   If you introduced a change in the Prisma schema that cannot be applied to a database with data (for example, a mandatory column in a table with data):
    -   Delete the `migration.sql` file.
    -   Modify the schema - for example, add a default value to the mandatory field.
    -   Migrate:

Prisma Migrate will prompt you to reset the database and re-apply all migrations.

-   If something interrupted the migration process, reset the database:

You might see the following error if you attempt to run Prisma Migrate commands in an environment that uses PgBouncer for connection pooling:

```
Error: undefined: Database error
Error querying the database: db error: ERROR: prepared statement "s0" already exists
```

See [Prisma Migrate and PgBouncer workaround](../../../prisma-client/setup-and-configuration/databases-connections/pgbouncer/index.md) for further information and a workaround.
