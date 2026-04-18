---
title: "Development and production"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:40.933Z"
content_hash: "8b3d543889aff9c319d32722d6d085eccbd15ab10eabeb53b563a81209484ada"
menu_path: ["Development and production"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-migrate/workflows/customizing-migrations/index.md", "title": "Customizing migrations"}
nav_next: {"path": "prisma/docs/orm/prisma-migrate/workflows/generating-down-migrations/index.md", "title": "Generating down migrations"}
---

Workflows

How to use Prisma Migrate commands in development and production environments

In a development environment, use the `migrate dev` command to generate and apply migrations:

### [Create and apply migrations](#create-and-apply-migrations)

This command:

*   Reruns the existing migration history in the [shadow database](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database/index.md) in order to detect schema drift (edited or deleted migration file, or a manual changes to the database schema)
*   Applies pending migrations to the shadow database (for example, new migrations created by colleagues)
*   If it detects changes to the Prisma schema, it generates a new migration from these changes
*   Applies all unapplied migrations to the development database and updates the `_prisma_migrations` table
*   Triggers the generation of artifacts (for example, Prisma Client)

The `migrate dev` command will prompt you to reset the database in the following scenarios:

*   Migration history conflicts caused by [modified or missing migrations](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories/index.md#do-not-edit-or-delete-migrations-that-have-been-applied)
*   The database schema has drifted away from the end-state of the migration history

### [Reset the development database](#reset-the-development-database)

You can also `reset` the database yourself to undo manual changes or `db push` experiments by running:

This command:

*   Drops the database/schema¹ if possible, or performs a soft reset if the environment does not allow deleting databases/schemas\*
*   Creates a new database/schema¹ with the same name if the database/schema¹ was dropped
*   Applies all migrations
*   Runs seed scripts

For a simple and integrated way to re-create data in your development database as often as needed, check out our [seeding guide](prisma/docs/orm/prisma-migrate/workflows/seeding/index.md).

### [Customizing migrations](#customizing-migrations)

Sometimes, you need to modify a migration **before applying it**. For example:

*   You want to introduce a significant refactor, such as changing blog post tags from a `String[]` to a `Tag[]`
*   You want to [rename a field](prisma/docs/orm/prisma-migrate/workflows/customizing-migrations/index.md#example-rename-a-field) (by default, Prisma Migrate will drop the existing field)
*   You want to [change the direction of a 1-1 relationship](prisma/docs/orm/prisma-migrate/workflows/customizing-migrations/index.md#example-change-the-direction-of-a-1-1-relation)
*   You want to add features that cannot be represented in Prisma Schema Language - such as a stored procedure or a trigger.

The `--create-only` command allows you to create a migration without applying it:

To apply the edited migration, run `prisma migrate dev` again.

Refer to [Customizing migrations](prisma/docs/orm/prisma-migrate/workflows/customizing-migrations/index.md) for examples.

### [Team development](#team-development)

See: [Team development with Prisma Migrate](prisma/docs/orm/prisma-migrate/workflows/development-and-production/index.md) .

In production and testing environments, use the `migrate deploy` command to apply migrations:

`migrate deploy` should generally be part of an automated CI/CD pipeline, and we do not recommend running this command locally to deploy changes to a production database.

This command:

*   Compares applied migrations against the migration history and **warns** if any migrations have been modified:
    
    ```
    WARNING The following migrations have been modified since they were applied:
    20210313140442_favorite_colors
    ```
    
*   Applies pending migrations
    

The `migrate deploy` command:

*   **Does not** issue a warning if an already applied migration is _missing_ from migration history
*   **Does not** detect drift (production database schema differs from migration history end state - for example, due to a hotfix)
*   **Does not** reset the database or generate artifacts (such as Prisma Client)
*   **Does not** rely on a shadow database

See also:

*   [Prisma Migrate in deployment](prisma/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate/index.md)
*   [Production troubleshooting](prisma/docs/orm/prisma-migrate/workflows/patching-and-hotfixing/index.md)

### [Advisory locking](#advisory-locking)

Prisma Migrate makes use of advisory locking when you run production commands such as:

*   `prisma migrate deploy`
*   `prisma migrate dev`
*   `prisma migrate resolve`

This safeguard ensures that multiple commands cannot run at the same time - for example, if you merge two pull requests in quick succession.

Advisory locking has a **10 second timeout** (not configurable), and uses the default advisory locking mechanism available in the underlying provider:

*   [PostgreSQL](https://www.postgresql.org/docs/9.4/explicit-locking.html#ADVISORY-LOCKS)
*   [MySQL](https://dev.mysql.com/doc/refman/5.7/en/locking-functions.html)
*   [Microsoft SQL server](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-getapplock-transact-sql?view=sql-server-ver15)

Prisma Migrate's implementation of advisory locking is purely to avoid catastrophic errors - if your command times out, you will need to run it again.

Since `5.3.0`, the advisory locking can be disabled using the [`PRISMA_SCHEMA_DISABLE_ADVISORY_LOCK` environment variable](prisma/docs/orm/reference/environment-variables-reference/index.md#prisma_schema_disable_advisory_lock)

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-migrate/workflows/development-and-production.mdx)

