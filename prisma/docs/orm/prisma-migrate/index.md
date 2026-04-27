---
title: "Overview of Prisma Migrate"
source: "https://www.prisma.io/docs/orm/prisma-migrate"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:34:23.547Z"
content_hash: "96e934c1c0b9ea41856e973863c31e8ba7b13f11f2bc609f6b07bb45f5f6f054"
menu_path: ["Overview of Prisma Migrate"]
section_path: []
content_language: "en"
---
## Overview of Prisma Migrate

Learn everything you need to know about Prisma Migrate

Prisma Migrate enables you to:

-   Keep your database schema in sync with your [Prisma schema](https://www.prisma.io/docs/orm/prisma-schema/overview) as it evolves
-   Maintain existing data in your database

Prisma Migrate generates [a history of `.sql` migration files](https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories), and plays a role in both [development and production](https://www.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production).

Prisma Migrate can be considered a _hybrid_ database schema migration tool, meaning it has both of _declarative_ and _imperative_ elements:

-   Declarative: The data model is described in a declarative way in the [Prisma schema](https://www.prisma.io/docs/orm/prisma-schema/overview). Prisma Migrate generates SQL migration files from that data model.
-   Imperative: All generated SQL migration files are fully customizable. Prisma Migrate hence provides the flexibility of an imperative migration tool by enabling you to modify what and how migrations are executed (and allows you to run custom SQL to e.g. make use of native database feature, perform data migrations, ...).

If you are prototyping, consider using the [`db push`](https://www.prisma.io/docs/orm/reference/prisma-cli-reference#db-push) command - see [Schema prototyping with `db push`](https://www.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema) for examples.

See the [Prisma Migrate reference](https://www.prisma.io/docs/orm/reference/prisma-cli-reference#prisma-migrate) for detailed information about the Prisma Migrate CLI commands.

Does not apply for MongoDB

Instead of `migrate dev` and related commands, use [`db push`](https://www.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema) for [MongoDB](https://www.prisma.io/docs/orm/core-concepts/supported-databases/mongodb).
