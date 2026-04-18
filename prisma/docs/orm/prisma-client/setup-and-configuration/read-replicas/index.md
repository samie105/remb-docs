---
title: "Read replicas"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/read-replicas"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/read-replicas"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:41.824Z"
content_hash: "8a085ff23774153e99cc1befc953de407fd86c62e74d3a4813ea94bfda74263d"
menu_path: ["Read replicas"]
section_path: []
---
Setup and Configuration

Learn how to set up and use read replicas with Prisma Client

Read replicas enable you to distribute workloads across database replicas for high-traffic workloads. The [read replicas extension](https://github.com/prisma/extension-read-replicas), `@prisma/extension-read-replicas`, adds support for read-only database replicas to Prisma Client.

If you run into a bug or have feedback, create a GitHub issue [here](https://github.com/prisma/extension-read-replicas/issues/new).

Install the extension:

Initialize the extension by extending your Prisma Client instance and provide the extension with full `PrismaClient` instances for your read replicas. The default approach is to use driver adapters:

```
import { readReplicas } from "@prisma/extension-read-replicas";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "./generated/prisma/client";

// Create main client with adapter
const mainAdapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});

const mainClient = new PrismaClient({ adapter: mainAdapter });

// Create replica client with adapter
const replicaAdapter = new PrismaPg({
  connectionString: process.env.REPLICA_URL!,
});

const replicaClient = new PrismaClient({ adapter: replicaAdapter });

// Extend main client with read replicas
const prisma = mainClient.$extends(readReplicas({ replicas: [replicaClient] }));

// Query is run against the database replica
await prisma.post.findMany();

// Query is run against the primary database
await prisma.post.create({
  data: {
    /** */
  },
});
```

All read operations (e.g. `findMany`) are executed against the database replica. All write operations (e.g. `create`, `update`) and `$transaction` queries are executed against your primary database.

The `replicas` property accepts an array of `PrismaClient` instances for all your database replicas:

```
import { readReplicas } from "@prisma/extension-read-replicas";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "./generated/prisma/client";

// Create main client
const mainAdapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});
const mainClient = new PrismaClient({ adapter: mainAdapter });

// Create multiple replica clients
const replicaAdapter1 = new PrismaPg({
  connectionString: process.env.DATABASE_URL_REPLICA_1!,
});
const replicaClient1 = new PrismaClient({ adapter: replicaAdapter1 });

const replicaAdapter2 = new PrismaPg({
  connectionString: process.env.DATABASE_URL_REPLICA_2!,
});
const replicaClient2 = new PrismaClient({ adapter: replicaAdapter2 });

// Configure multiple replicas
const prisma = mainClient.$extends(
  readReplicas({
    replicas: [replicaClient1, replicaClient2],
  }),
);
```

If you have more than one read replica configured, a database replica will be randomly selected to execute your query.

You can use the `$primary()` method to explicitly execute a read operation against your primary database:

```
const posts = await prisma.$primary().post.findMany();
```

You can use the `$replica()` method to explicitly execute your query against a replica instead of your primary database:

```
const result = await prisma.$replica().user.findFirst(...)
```

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/setup-and-configuration/read-replicas.mdx)
