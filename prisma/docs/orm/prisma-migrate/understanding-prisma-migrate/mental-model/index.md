---
title: "Understanding Migrations"
source: "https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:10.885Z"
content_hash: "3d58b7b8165dd47c09ae9e56eecf7798f29ce3b02bee83104b2bfc281b007aef"
menu_path: ["Understanding Migrations"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-migrate/getting-started/index.md", "title": "Getting started with Prisma Migrate"}
nav_next: {"path": "prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories/index.md", "title": "Migration histories"}
---

Database migrations are a controlled set of changes that modify and evolve the structure of your database schema. Migrations help you transition your database schema from one state to another. For example, within a migration you can create or remove tables and columns, split fields in a table, or add types and constraints to your database.

### [Patterns for evolving database schemas](#patterns-for-evolving-database-schemas)

For migrations, there are two main types of migrations that can be made:

*   **Model/Entity-first migration:** with this pattern, you define the structure of the database schema with code and then use a migration tool to generate the SQL, for example, for syncing your application and database schema.

![Model-first migration flow](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/entity-first-migration-flow.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

*   **Database-first migration:** with this pattern, you define the structure of your database and apply it to your database using SQL. You then _introspect_ the database to generate the code that describes the structure of your database to sync your application and database schema.

![Database-first migration flow](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/database-first-migration-flow.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

The migration files (SQL) should ideally be stored together with your application code. They should also be tracked in version control and shared with the rest of the team working on the application. Migrations provide _state management_ which helps you to track the state of the database.

Migrations also allow you to replicate the state of a database at a specific point in time which is useful when collaborating with other members of the team, e.g. switching between different branches. For further information on database migrations, see the [Prisma Data Guide](https://www.prisma.io/dataguide/types/relational/what-are-database-migrations).

Prisma Migrate is a database migration tool that supports the _model/ entity-first_ migration pattern to manage database schemas in your local environment and in production.

The workflow when using Prisma Migrate in your project would be iterative and look like this:

### [Local development environment (Feature branch)](#local-development-environment-feature-branch)

*   Evolve your Prisma schema
*   Use either [`prisma migrate dev`](#track-your-migration-history-with-prisma-migrate-dev) or [`prisma db push`](#prototype-your-schema) to sync your Prisma schema with the database schema of your local development database

### [Preview/ staging environment(Feature pull request)](#preview-staging-environmentfeature-pull-request)

1.  Push your changes to the feature pull request
2.  Use a CI system (e.g. GitHub Actions) to sync your Prisma schema and migration history with your preview database using `prisma migrate deploy`

### [Production (main branch)](#production-main-branch)

*   Merge your application code from the feature branch to your main branch.
*   Use a CI system (e.g. GitHub Actions) to sync your Prisma schema and migration history with your production database using `prisma migrate deploy`

![Prisma Migrate workflow](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/prisma-migrate-lifecycle.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Prisma Migrate uses the following pieces of state to track the state of your database schema:

*   **Prisma schema**: your source of truth that defines the structure of the database schema.
*   **Migrations history**: SQL files in your `prisma/migrations` folder representing the history of changes made to your database schema.
*   **Migrations table**: `prisma_migrations` table in the database that stores metadata for migrations that have been applied to the database.
*   **Database schema**: the state of the database.

![Prisma Migrate "state management"](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/prisma-migrate-state-mgt.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

*   Ideally, you should use one database per environment. For example, you might have a separate database for development, preview, and production environments.
*   The databases you use in development environments are disposable — you can easily create, use, and delete databases on demand.
*   The database configuration used in each environments should be consistent. This is important to ensure a certain migration that moves across the workflow yields the same changes to the database.
*   The Prisma schema serves as the source of truth — describing the shape of your [database schema](https://www.prisma.io/dataguide/intro/database-glossary#schema).

This section describes how you can evolve your database schema in different environments: development, staging, and production, using Prisma Migrate.

### [Prisma Migrate in a development environment (local)](#prisma-migrate-in-a-development-environment-local)

#### [Track your migration history with `prisma migrate dev`](#track-your-migration-history-with-prisma-migrate-dev)

The [`prisma migrate dev`](prisma/docs/orm/reference/prisma-cli-reference/index.md#migrate-dev) command allows you to track the changes you make to your database. The `prisma migrate dev` command automatically generates SQL migration files (saved in `/prisma/migrations`) and applies them to the database. When a migration is applied to the database, the migrations table (`_prisma_migrations`) in your database is also updated.

![Prisma Migrate dev flow](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/prisma-migrate-dev-flow.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

The `prisma migrate dev` command tracks the state of the database using the following pieces of state:

*   the Prisma schema
*   the migrations history
*   the migrations table
*   the database schema

You can customize migrations before you apply them to the database using the `--create-only` flag. For example, you might want to edit a migration if you want to rename columns without incurring any data loss or load database extensions (in PostgreSQL) and database views (currently not supported).

Under the hood, Prisma Migrate uses a [shadow database](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database/index.md) to detect a [schema drift](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database/index.md#detecting-schema-drift) and generate new migrations.

If `prisma migrate dev` detects a schema drift or a migration history conflict, you will be prompted to reset (drop and recreate your database) your database to sync the migration history and the database schema.

Expand to see the shadow database explained using a cartoon

![A cartoon that shows how the shadow database works.](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/shadow-database.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

#### [Resolve schema drifts](#resolve-schema-drifts)

A schema drift occurs when the expected database schema is different from what is in the migration history. For example, this can occur when you manually update the database schema without also updating the Prisma schema and `prisma/migrations` accordingly.

For such instances, you can use the [`prisma migrate diff`](prisma/docs/orm/reference/prisma-cli-reference/index.md#migrate-diff) command to compare your migration history and revert changes made to your database schema.

![Revert database schema with migrate diff](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/prisma-migrate-diff-flow.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

You can use `migrate diff` to generate the SQL that either:

*   Reverts the changes made in the database schema to synchronize it with the current Prisma schema
*   Moves your database schema forward to apply missing changes from the Prisma schema and `/migrations`

You can then apply the changes to your database using [`prisma db execute`](prisma/docs/orm/reference/prisma-cli-reference/index.md#db-execute) command.

#### [Prototype your schema](#prototype-your-schema)

The [`prisma db push`](prisma/docs/orm/reference/prisma-cli-reference/index.md#db-push) command allows you to sync your Prisma schema and database schema without persisting a migration (`/prisma/migrations`). The `prisma db push` command tracks the state of the database using the following pieces of state:

*   the Prisma schema
*   the database schema

![prisma db push development flow](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/db-push-flow.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

The `prisma db push` command is useful when:

*   You want to **quickly prototype and iterate** on schema design locally without the need to deploy these changes to other environments such as other developers, or staging and production environments.
*   You are prioritizing reaching a **desired end-state** and not the changes or steps executed to reach that end-state (there is no way to preview changes made by `prisma db push`)
*   You do not need to control how schema changes impact data. There is no way to orchestrate schema and data migrations - if `prisma db push` anticipates that changes will result in data loss, you can either accept data loss with the `--accept-data-loss` option or stop the process - there is no way to customize the changes.

If the `prisma db push` command detects destructive change to your database schema, it will prompt you to reset your database. For example, this will happen when you add a required field to a table with existing content without providing a default value.

### [Prisma Migrate in a staging and production environment](#prisma-migrate-in-a-staging-and-production-environment)

#### [Sync your migration histories](#sync-your-migration-histories)

The [`prisma migrate deploy`](prisma/docs/orm/reference/prisma-cli-reference/index.md#migrate-deploy) command allows you to sync your migration history from your development environment with your database in your **staging or production environment**.

Under the hood, the `migrate deploy` command:

1.  Compares already applied migrations (captured `_prisma_migrations`) and the migration history (`/prisma/migrations`)
2.  Applies pending migrations
3.  Updates `_prisma_migrations` table with the new migrations

![Workflow of Prisma Migrate](https://www.prisma.io/docs/img/orm/prisma-migrate/workflows/deploy-db.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

The command should be run in an automated CI/ CD environment, for example GitHub Actions.

If you don't have a migration history (`/migrations`), i.e using `prisma db push`, you will have to continue using `prisma db push` in your staging and production environments. Beware of the changes being applied to the database schema as some of them might be destructive. For example, `prisma db push` can't tell when you're performing a column rename. It will prompt a database reset (drop and re-creation).


