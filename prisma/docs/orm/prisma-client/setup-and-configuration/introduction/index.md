---
title: "Introduction to Prisma Client"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:39:26.937Z"
content_hash: "96b4a1a58b5af6099ae6b20e0b9da5e4801d697709a579e4adf37a5240ddd1f6"
menu_path: ["Introduction to Prisma Client"]
section_path: []
tab_variants: ["Prisma Config","Prisma Schema","PostgreSQL","MySQL / MariaDB","SQLite","npm","npm","pnpm","yarn","bun","PostgreSQL","MySQL / MariaDB","SQLite","PostgreSQL (Edge)","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/error-formatting/index.md", "title": "Configuring error formatting"}
nav_next: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/read-replicas/index.md", "title": "Read replicas"}
---

Setup and Configuration

Learn how to set up and configure Prisma Client in your project

Prisma Client is an auto-generated and type-safe query builder that's _tailored_ to your data. The easiest way to get started with Prisma Client is by following the **[Quickstart](https://www.prisma.io/docs/prisma-orm/quickstart/sqlite)**.

[Quickstart (5 min)](https://www.prisma.io/docs/prisma-orm/quickstart/sqlite)

In order to set up Prisma Client, you need a Prisma Config and a [Prisma schema file](prisma/docs/orm/prisma-schema/overview/index.md):

[Install the Prisma CLI](prisma/docs/orm/reference/prisma-cli-reference/index.md), the Prisma Client library, and the [driver adapter](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md) for your database:

Prisma Client is based on the models in Prisma Schema. To provide the correct types, you need generate the client code:

This will create a `generated` directory based on where you set the `output` to in the Prisma Schema. Any time your import Prisma Client, it will need to come from this generated client API.

With the client generated, import it along with your [driver adapter](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md) and create a new instance:

Find out what [driver adapter](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md) is needed for your database.

Your application should generally only create **one instance** of `PrismaClient`. How to achieve this depends on whether you are using Prisma ORM in a [long-running application](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md#prismaclient-in-long-running-applications) or in a [serverless environment](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md#prismaclient-in-serverless-environments).

Creating multiple instances of `PrismaClient` will create multiple connection pools and can hit the connection limit for your database. Too many connections may start to **slow down your database** and eventually lead to errors such as:

```
Error in connector: Error querying the database: db error: FATAL: sorry, too many clients already
   at PrismaClientFetcher.request
```

Once you have instantiated `PrismaClient`, you can start sending queries in your code:

```
// run inside `async` function
const newUser = await prisma.user.create({
  data: {
    name: "Alice",
    email: "alice@prisma.io",
  },
});

const users = await prisma.user.findMany();
```

Whenever you make changes to your database that are reflected in the Prisma schema, you need to manually re-generate Prisma Client to update the generated code in your output directory:
