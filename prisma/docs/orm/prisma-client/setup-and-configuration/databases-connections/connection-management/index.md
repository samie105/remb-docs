---
title: "Connection management"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:44:29.283Z"
content_hash: "60d623a99dbbcd131a729822b0647fbee5d3c028519fa04f0e1bc8c13324b6e8"
menu_path: ["Connection management"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md", "title": "Database connections"}
nav_next: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool/index.md", "title": "Connection pool"}
---

Setup and Configuration

Database Connections

This page explains how database connections are handled with Prisma Client and how to manually connect and disconnect your database

`PrismaClient` connects and disconnects from your data source using the following two methods:

-   [`$connect()`](../../../../reference/prisma-client-reference/index.md)
-   [`$disconnect()`](../../../../reference/prisma-client-reference/index.md)

In most cases, you **do not need to explicitly call these methods**. `PrismaClient` automatically connects when you run your first query, creates a [connection pool](../connection-pool/index.md), and disconnects when the Node.js process ends.

See the [connection management guide](../index.md) for information about managing connections for different deployment paradigms (long-running processes and serverless functions).

**Questions answered in this page**

-   When should I call $connect and $disconnect?
-   How does Prisma manage connection pools?
-   How to handle connections in serverless?

It is not necessary to call [`$connect()`](../../../../reference/prisma-client-reference/index.md) thanks to the _lazy connect_ behavior: The `PrismaClient` instance connects lazily when the first request is made to the API (`$connect()` is called for you under the hood).

### [Calling `$connect()` explicitly](#calling-connect-explicitly)

If you need the first request to respond instantly and cannot wait for a lazy connection to be established, you can explicitly call `prisma.$connect()` to establish a connection to the data source:

```
const prisma = new PrismaClient();

// run inside `async` function
await prisma.$connect();
```

When you call [`$disconnect()`](../../../../reference/prisma-client-reference/index.md) , Prisma Client:

1.  Runs the [`beforeExit` hook](#exit-hooks)
2.  Closes all connections in the pool

In a long-running application such as a GraphQL API, which constantly serves requests, it does not make sense to `$disconnect()` after each request - it takes time to establish a connection, and doing so as part of each request will slow down your application.

### [Calling `$disconnect()` explicitly](#calling-disconnect-explicitly)

In most long-running or serverless apps you should **not** call `$disconnect()` after each request, so connections can be reused. In some situations it **does** make sense to call it explicitly—for example, when creating a temporary `PrismaClient` and then immediately releasing its resources (e.g. in [Cloudflare Workers](../../../deployment/edge/deploy-to-cloudflare/index.md), where `ctx.waitUntil(prisma.$disconnect())` is recommended).

Another scenario is a script that:

1.  Runs **infrequently** (for example, a scheduled job to send emails each night), which means it does not benefit from a long-running connection to the database _and_
2.  Exists in the context of a **long-running application**, such as a background service. If the application never shuts down, Prisma Client never disconnects.

The following script creates a new instance of `PrismaClient`, performs a task, and then disconnects - which closes the connection pool:

```
import { PrismaClient } from "../prisma/generated/client";

const prisma = new PrismaClient();
const emailService = new EmailService();

async function main() {
  const allUsers = await prisma.user.findMany();
  const emails = allUsers.map((x) => x.email);

  await emailService.send(emails, "Hello!");
}

main()
  .then(async () => {
    await prisma.$disconnect();  
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect(); 
    process.exit(1);
  });
```

If the above script runs multiple times in the context of a long-running application _without_ calling `$disconnect()`, a new connection pool is created with each new instance of `PrismaClient`.

The `beforeExit` hook runs when Prisma ORM is triggered externally (e.g. via a `SIGINT` signal) to shut down, and allows you to run code _before_ Prisma Client disconnects - for example, to issue queries as part of a graceful shutdown of a service:

```
const prisma = new PrismaClient();

prisma.$on("beforeExit", async () => {
  console.log("beforeExit hook");
  // PrismaClient still available
  await prisma.message.create({
    data: {
      message: "Shutting down server",
    },
  });
});
```
