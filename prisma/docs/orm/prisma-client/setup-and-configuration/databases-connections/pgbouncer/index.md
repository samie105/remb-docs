---
title: "Configure Prisma Client with PgBouncer"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:44:36.451Z"
content_hash: "f9c91238338df1e75624609eb3a5174b34ea080a5a8f612367139d9cf1a72065"
menu_path: ["Configure Prisma Client with PgBouncer"]
section_path: []
content_language: "en"
---
Setup and Configuration

Database Connections

Configure Prisma Client with PgBouncer and other poolers: when to use pgbouncer=true, required transaction mode, prepared statements, and Prisma Migrate workarounds

An external connection pooler like PgBouncer holds a connection pool to the database, and proxies incoming client connections by sitting between Prisma Client and the database. This reduces the number of processes a database has to handle at any given time.

Usually, this works transparently, but some connection poolers only support a limited set of functionality. One common feature that external connection poolers do not support are named prepared statements, which Prisma ORM uses. For these cases, Prisma ORM can be configured to behave differently.

**Questions answered in this page**

-   How do I configure Prisma with PgBouncer?
-   Do I need `pgbouncer=true`, and if so, when?
-   How does Prisma Migrate work with PgBouncer?

### [Set PgBouncer to transaction mode](#set-pgbouncer-to-transaction-mode)

For Prisma Client to work reliably, PgBouncer must run in [**Transaction mode**](https://www.pgbouncer.org/features.html).

Transaction mode offers a connection for every transaction – a requirement for the Prisma Client to work with PgBouncer.

### [Add `pgbouncer=true` for PgBouncer versions below `1.21.0`](#add-pgbouncertrue-for-pgbouncer-versions-below-1210)

To use Prisma Client with PgBouncer, add the `?pgbouncer=true` flag to the PostgreSQL connection URL:

```
postgresql://USER:PASSWORD@HOST:PORT/DATABASE?pgbouncer=true
```

### [Configure `max_prepared_statements` in PgBouncer to be greater than zero](#configure-max_prepared_statements-in-pgbouncer-to-be-greater-than-zero)

Prisma uses prepared statements, and setting [`max_prepared_statements`](https://www.pgbouncer.org/config.html) to a value greater than `0` enables PgBouncer to use those prepared statements.

### [Prisma Migrate and PgBouncer workaround](#prisma-migrate-and-pgbouncer-workaround)

Prisma Migrate uses **database transactions** to check out the current state of the database and the migrations table. However, the Schema Engine is designed to use a **single connection to the database**, and does not support connection pooling with PgBouncer. If you attempt to run Prisma Migrate commands in any environment that uses PgBouncer for connection pooling, you might see the following error:

```
Error: undefined: Database error
Error querying the database: db error: ERROR: prepared statement "s0" already exists
```

To work around this issue, configure a **direct** connection for Prisma CLI commands in `prisma.config.ts`, while Prisma Client continues to use the PgBouncer URL via a driver adapter.

.env

```
# PgBouncer (pooled) connection string used by Prisma Client.
DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE?pgbouncer=true"

# Direct database connection string used by Prisma CLI. 
DIRECT_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE"
```

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

src/db/client.ts

```
import { PrismaClient } from "../prisma/generated/client";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
export const prisma = new PrismaClient({ adapter });
```

With this setup, PgBouncer stays in the path for runtime traffic, while Prisma CLI commands (`prisma migrate dev`, `prisma db push`, `prisma db pull`, and so on) always use the direct connection string defined in `prisma.config.ts`.

### [PgBouncer with different database providers](#pgbouncer-with-different-database-providers)

There are sometimes minor differences in how to connect directly to a Postgres database that depend on the provider hosting the database.

Below are links to information on how to set up these connections with providers who have setup steps not covered here in our documentation:

-   [Connecting directly to a PostgreSQL database hosted on Digital Ocean](https://github.com/prisma/prisma/issues/6157)
-   [Connecting directly to a PostgreSQL database hosted on ScaleGrid](https://github.com/prisma/prisma/issues/6701#issuecomment-824387959)

Supabase's Supavisor behaves similarly to [PgBouncer](#pgbouncer). You can add `?pgbouncer=true` to your connection pooled connection string available via your [Supabase database settings](https://supabase.com/dashboard/project/_/settings/database).

Although Prisma ORM does not have explicit support for other connection poolers, if the limitations are similar to the ones of [PgBouncer](#pgbouncer) you can usually also use `pgbouncer=true` in your connection string to put Prisma ORM in a mode that works with them as well.
