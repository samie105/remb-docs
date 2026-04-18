---
title: "Introduction to Prisma Client"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:37.875Z"
content_hash: "1579fda72140eddb34d411862f4e90fa2a9094bf9d67c45944cc5b49a1ca970c"
menu_path: ["Introduction to Prisma Client"]
section_path: []
---
Setup and Configuration

Learn how to set up and configure Prisma Client in your project

Prisma Client is an auto-generated and type-safe query builder that's _tailored_ to your data. The easiest way to get started with Prisma Client is by following the **[Quickstart](https://www.prisma.io/docs/prisma-orm/quickstart/sqlite)**.

[Quickstart (5 min)](https://www.prisma.io/docs/prisma-orm/quickstart/sqlite)

In order to set up Prisma Client, you need a Prisma Config and a [Prisma schema file](https://www.prisma.io/docs/orm/prisma-schema/overview):

[Install the Prisma CLI](https://www.prisma.io/docs/orm/reference/prisma-cli-reference), the Prisma Client library, and the [driver adapter](https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers) for your database:

Prisma Client is based on the models in Prisma Schema. To provide the correct types, you need generate the client code:

This will create a `generated` directory based on where you set the `output` to in the Prisma Schema. Any time your import Prisma Client, it will need to come from this generated client API.

With the client generated, import it along with your [driver adapter](https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers) and create a new instance:

Find out what [driver adapter](https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers) is needed for your database.

Your application should generally only create **one instance** of `PrismaClient`. How to achieve this depends on whether you are using Prisma ORM in a [long-running application](https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#prismaclient-in-long-running-applications) or in a [serverless environment](https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#prismaclient-in-serverless-environments).

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

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/setup-and-configuration/introduction.mdx)
