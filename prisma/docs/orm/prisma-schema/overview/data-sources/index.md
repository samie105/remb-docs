---
title: "Data sources"
source: "https://www.prisma.io/docs/orm/prisma-schema/overview/data-sources"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/overview/data-sources"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:44.256Z"
content_hash: "8e4e639560079f4e44f5f1c4098fff5370522ab816fd299830bbede7c5cd1728"
menu_path: ["Data sources"]
section_path: []
---
Overview

Data sources enable Prisma to connect to your database. This page explains how to configure data sources in your Prisma schema

A data source determines how Prisma ORM connects to your database, and is represented by the [`datasource`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#datasource) block in the Prisma schema. Connection details (such as the database URL) are configured in [Prisma Config](https://www.prisma.io/docs/orm/reference/prisma-config-reference). The following data source uses the `postgresql` provider:

```
datasource db {
  provider = "postgresql"
}
```

A Prisma schema can only have _one_ data source. However, you can:

*   [Override the database connection when creating your `PrismaClient`](https://www.prisma.io/docs/orm/reference/prisma-client-reference)
*   [Specify a different **database** for Prisma Migrate's shadow database if you are working with cloud-hosted development databases](https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#cloud-hosted-shadow-databases-must-be-created-manually)

## [Securing database connections](#securing-database-connections)

Some data source `provider`s allow you to configure your connection with SSL/TLS **by specifying certificate locations in your connection configuration**.

*   [Configuring an SSL connection with PostgreSQL](https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#common-patterns)
*   [Configuring an SSL connection with MySQL](https://www.prisma.io/docs/orm/core-concepts/supported-databases/mysql#common-patterns)
*   [Configure a TLS connection with Microsoft SQL Server](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sql-server#connection-details)

See the database-specific documentation above for examples of SSL/TLS connection configuration in Prisma Config.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-schema/overview/data-sources.mdx)

[

Overview of Prisma Schema

The Prisma schema is the main method of configuration when using Prisma. It is typically called schema.prisma and contains your database connection and data model

](https://www.prisma.io/docs/orm/prisma-schema/overview)[

Generators

Generators in your Prisma schema specify what assets are generated when the \`prisma generate\` command is invoked. This page explains how to configure generators

](https://www.prisma.io/docs/orm/prisma-schema/overview/generators)

### On this page

[Securing database connections](#securing-database-connections)
