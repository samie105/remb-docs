---
title: "Baselining a database"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/baselining"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/baselining"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:29.043Z"
content_hash: "f64c6435be05f797328079debed879765989ead033e3d575c01bac15e3c93e44"
menu_path: ["Baselining a database"]
section_path: []
---
Workflows

How to initialize a migration history for an existing database that contains important data.

Baselining is the process of initializing a migration history for a database that:

*   ✔ Existed before you started using Prisma Migrate
*   ✔ Contains data that must be maintained (like production), which means that the database cannot be reset

Baselining tells Prisma Migrate to assume that one or more migrations have **already been applied**. This prevents generated migrations from failing when they try to create tables and fields that already exist.

Since this is working with development database, the assumption is that the database can be reset and reseeded.

Baselining is part of [adding Prisma Migrate to a project with an existing database](https://www.prisma.io/docs/orm/prisma-migrate/getting-started#adding-to-an-existing-project).

When you add Prisma Migrate to an existing project, your initial migration contains all the SQL required to recreate the state of the database **before you started using Prisma Migrate**:

![The image shows a database labelled 'Existing database', and a list of existing database features next to it - 24 tables, 13 relationships, 92 fields, 3 indexes. An arrow labelled 'represented by' connects the database features list to a box that represents a migration. The existing databases's features are represented by a single migration.](https://www.prisma.io/docs/img/orm/prisma-migrate/workflows/existing-database.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

You need this initial migration to create and reset **development environments**:

![The image shows a migration history with three migrations. Each migration is represented by a file icon and a name, and all migrations are surrounded by a box labelled 'migration history'. The first migration has an additional label: "State of database before Prisma Migrate", and the two remaining migrations are labelled "Generated as part of the Prisma Migrate workflow". An arrow labelled "prisma migrate dev" connects the migration history box to a database labelled "new development database", signifying that all three migrations are applied to the development database - none are skipped.](https://www.prisma.io/docs/img/orm/prisma-migrate/workflows/new-dev-db.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

However, when you `prisma migrate deploy` your migrations to databases that already exist and _cannot_ be reset - such as production - you **do not want to include the initial migrations**.

The target database already contains the tables and columns created by the initial migration, and attempting to create these elements again will most likely result in an error.

![A migration history represented by three migration files (file icon and name), surrounded by a a box labelled 'migration history'. The first migration is marked 'do not apply', and the second two migrations are marked 'apply'. An arrow labelled with the command 'prisma migrate deploy' points from the migration history to a database labelled 'production'.](https://www.prisma.io/docs/img/orm/prisma-migrate/workflows/deploy-db.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Baselining solves this problem by telling Prisma Migrate to pretend that the initial migration(s) **have already been applied**.

To create a baseline migration:

*   If you already have a `prisma/migrations` folder, delete, move, rename, or archive this folder.
*   Create a new `prisma/migrations` directory.
*   Then create another new directory with your preferred name. What's important is to use a prefix of `0_` so that Prisma migrate applies migrations in a [lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order). You can use a different value such as the current timestamp.
*   Generate a migration and save it to a file using `prisma migrate diff`:

*   Run the `prisma migrate resolve` command for each migration that should be ignored:

This command adds the target migration to the `_prisma_migrations` table and marks it as applied. When you run `prisma migrate deploy` to apply new migrations, Prisma Migrate:

1.  Skips all migrations marked as 'applied', including the baseline migration
2.  Applies any new migrations that come _after_ the baseline migration

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-migrate/workflows/baselining.mdx)
