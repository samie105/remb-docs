---
title: "Data sources"
source: "https://www.prisma.io/docs/orm/prisma-schema/overview/data-sources"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/overview/data-sources"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:42:34.375Z"
content_hash: "841cf7a19713ff84603f2ea969a1a014bf7da42bea9d7143521898fa2a6c7386"
menu_path: ["Data sources"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-schema/overview/index.md", "title": "Overview of Prisma Schema"}
nav_next: {"path": "prisma/docs/orm/prisma-schema/overview/generators/index.md", "title": "Generators"}
---

Overview

Data sources enable Prisma to connect to your database. This page explains how to configure data sources in your Prisma schema

A data source determines how Prisma ORM connects to your database, and is represented by the [`datasource`](prisma/docs/orm/reference/prisma-schema-reference/index.md#datasource) block in the Prisma schema. Connection details (such as the database URL) are configured in [Prisma Config](prisma/docs/orm/reference/prisma-config-reference/index.md). The following data source uses the `postgresql` provider:

```
datasource db {
  provider = "postgresql"
}
```

A Prisma schema can only have _one_ data source. However, you can:

-   [Override the database connection when creating your `PrismaClient`](prisma/docs/orm/reference/prisma-client-reference/index.md)
-   [Specify a different **database** for Prisma Migrate's shadow database if you are working with cloud-hosted development databases](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database/index.md#cloud-hosted-shadow-databases-must-be-created-manually)

## [Securing database connections](#securing-database-connections)

Some data source `provider`s allow you to configure your connection with SSL/TLS **by specifying certificate locations in your connection configuration**.

-   [Configuring an SSL connection with PostgreSQL](prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md#common-patterns)
-   [Configuring an SSL connection with MySQL](prisma/docs/orm/core-concepts/supported-databases/mysql/index.md#common-patterns)
-   [Configure a TLS connection with Microsoft SQL Server](prisma/docs/orm/core-concepts/supported-databases/sql-server/index.md#connection-details)

See the database-specific documentation above for examples of SSL/TLS connection configuration in Prisma Config.

[

Overview of Prisma Schema

The Prisma schema is the main method of configuration when using Prisma. It is typically called schema.prisma and contains your database connection and data model

](prisma/docs/orm/prisma-schema/overview/index.md)[

Generators

Generators in your Prisma schema specify what assets are generated when the \`prisma generate\` command is invoked. This page explains how to configure generators

](prisma/docs/orm/prisma-schema/overview/generators/index.md)

### On this page

[Securing database connections](#securing-database-connections)
