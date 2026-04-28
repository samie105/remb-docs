---
title: "Database connections"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:44:33.283Z"
content_hash: "c71d29b9365e5f6908ceebb21daff646030025990b586bf1b44bcc921646d521"
menu_path: ["Database connections"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/database-polyfills/index.md", "title": "Database polyfills"}
nav_next: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management/index.md", "title": "Connection management"}
---

# Connection URL to your database using PgBouncer.
DATABASE_URL="postgres://root:password@127.0.0.1:54321/postgres?pgbouncer=true"

# Direct connection URL to the database used for Prisma CLI commands. 
DIRECT_URL="postgres://root:password@127.0.0.1:5432/postgres"
```

Configure `prisma.config.ts` to point to the direct connection string. Prisma CLI commands always read from this configuration.

prisma.config.ts

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DIRECT_URL"),
  },
});
```

At runtime, instantiate Prisma Client with a driver adapter (for example, `@prisma/adapter-pg`) that uses the pooled connection string:

src/db/client.ts

```
import { PrismaClient } from "../prisma/generated/client";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
export const prisma = new PrismaClient({ adapter });
```

### [PgBouncer](#pgbouncer)

PostgreSQL only supports a certain amount of concurrent connections, and this limit can be reached quite fast when the service usage goes up – especially in [serverless environments](#serverless-environments-faas).

[PgBouncer](https://www.pgbouncer.org/) holds a connection pool to the database and proxies incoming client connections by sitting between Prisma Client and the database. This reduces the number of processes a database has to handle at any given time. PgBouncer passes on a limited number of connections to the database and queues additional connections for delivery when connections become available. To use PgBouncer, see [Configure Prisma Client with PgBouncer](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer/index.md).

### [AWS RDS Proxy](#aws-rds-proxy)

Due to the way AWS RDS Proxy pins connections, [it does not provide any connection pooling benefits](prisma/docs/orm/prisma-client/deployment/caveats-when-deploying-to-aws-platforms/index.md#aws-rds-proxy) when used together with Prisma Client.
