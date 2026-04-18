---
title: "Database drivers"
source: "https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers"
canonical_url: "https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:52.223Z"
content_hash: "3113b0f20d9dfe5aed4292e9d4b7375399beaedaed6f38100c25e06c27c0f90a"
menu_path: ["Database drivers"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/more/releases/index.md", "title": "ORM releases and maturity levels"}
nav_next: {"path": "prisma/docs/orm/core-concepts/supported-databases/mongodb/index.md", "title": "MongoDB"}
---

Prisma Client can connect and run queries against your database using JavaScript database drivers via **driver adapters**. Adapters act as _translators_ between Prisma Client and the JavaScript database driver.

Prisma Client will use the Query Engine to transform the Prisma Client query to SQL and run the generated SQL queries via the JavaScript database driver.

![Query flow from the user application to the database using Prisma Client and driver adapters](https://www.prisma.io/docs/img/orm/core-concepts/databases/images/drivers/qe-query-engine-adapter.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

There are two different types of driver adapters:

*   [Database driver adapters](#database-driver-adapters)
*   [Serverless driver adapters](#serverless-driver-adapters)

> **Note**: Driver adapters enable [edge deployments](prisma/docs/orm/prisma-client/deployment/edge/overview/index.md) of applications that use Prisma ORM.

### [Database driver adapters](#database-driver-adapters)

You can connect to your database using a Node.js-based driver from Prisma Client using a database driver adapter. Prisma maintains the adapters for the following drivers:

*   PostgreSQL
    *   [`pg`](prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md#using-driver-adapters)
*   Prisma Postgres
    *   [`@prisma/adapter-ppg`](https://www.prisma.io/docs/postgres/database/serverless-driver#use-with-prisma-orm)
*   MySQL/MariaDB
    *   [`mariadb`](prisma/docs/orm/core-concepts/supported-databases/mysql/index.md#using-driver-adapters)
*   SQLite
    *   [`better-sqlite3`](prisma/docs/orm/core-concepts/supported-databases/sqlite/index.md#using-driver-adapters)
    *   [`libSQL`](prisma/docs/orm/core-concepts/supported-databases/sqlite/index.md#using-driver-adapters) (Turso)
*   MS SQL Server
    *   [`node-mssql`](prisma/docs/orm/core-concepts/supported-databases/sql-server/index.md#using-driver-adapters)

### [Serverless driver adapters](#serverless-driver-adapters)

Database providers, such as Neon and PlanetScale, allow you to connect to your database using other protocols besides TCP, such as HTTP and WebSockets. These database drivers are optimized for connecting to your database in serverless and edge environments.

Prisma ORM maintains the following serverless driver adapters:

*   [Prisma Postgres](https://www.prisma.io/docs/postgres/database/serverless-driver#use-with-prisma-orm)
*   [Neon](prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md#neon) (and Vercel Postgres)
*   [PlanetScale](prisma/docs/orm/core-concepts/supported-databases/mysql/index.md#planetscale)
*   [Cloudflare D1](prisma/docs/orm/core-concepts/supported-databases/sqlite/index.md#cloudflare-d1)

### [Community-maintained database driver adapters](#community-maintained-database-driver-adapters)

You can also build your own driver adapter for the database you're using. The following is a list of community-maintained driver adapters:

*   [TiDB Cloud Serverless Driver](https://github.com/tidbcloud/prisma-adapter)
*   [PGlite - Postgres in WASM](https://github.com/lucasthevenet/pglite-utils/tree/main/packages/prisma-adapter)

Refer to the following pages to learn more about how to use the specific driver adapters with the specific database providers:

*   [PostgreSQL](prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md#using-driver-adapters)
*   [Prisma Postgres](https://www.prisma.io/docs/postgres/database/serverless-driver#use-with-prisma-orm)
*   [MySQL/MariaDB](prisma/docs/orm/core-concepts/supported-databases/mysql/index.md#using-driver-adapters)
*   [MS SQL Server](prisma/docs/orm/core-concepts/supported-databases/sql-server/index.md#using-driver-adapters)
*   [Neon](prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md#neon)
*   [PlanetScale](prisma/docs/orm/core-concepts/supported-databases/mysql/index.md#planetscale)
*   [Turso](prisma/docs/orm/core-concepts/supported-databases/sqlite/index.md#turso-libsql)
*   [Cloudflare D1](prisma/docs/orm/core-concepts/supported-databases/sqlite/index.md#cloudflare-d1)
*   [CockroachDB](prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md#cockroachdb)

### [New driver adapters API in v6.6.0](#new-driver-adapters-api-in-v660)

In [v6.6.0](https://github.com/prisma/prisma/releases/tag/6.6.0), we introduced a simplified version for instantiating Prisma Client when using driver adapters. You now don't need to create an instance of the driver/client to pass to a driver adapter, instead you can just create the driver adapter directly (and pass the driver's options to it if needed).

Here is an example using the `@prisma/adapter-libsql` adapter:

#### [Before 6.6.0](#before-660)

Earlier versions of Prisma ORM required you to first instantiate the driver itself, and then use that instance to create the Prisma driver adapter. Here is an example using the `@libsql/client` driver for LibSQL:

```
import { createClient } from "@libsql/client";
import { PrismaLibSQL } from "@prisma/adapter-libsql";
import { PrismaClient } from "../prisma/generated/client";

// Old way of using driver adapters (before 6.6.0)
const driver = createClient({
  url: env.LIBSQL_DATABASE_URL,
  authToken: env.LIBSQL_DATABASE_TOKEN,
});
const adapter = new PrismaLibSQL(driver);

const prisma = new PrismaClient({ adapter });
```

#### [6.6.0 and later](#660-and-later)

As of the 6.6.0 release, you instantiate the driver adapter _directly_ with the options of your preferred JS-native driver.:

```
import { PrismaLibSQL } from "@prisma/adapter-libsql";
import { PrismaClient } from "../generated/prisma/client";

const adapter = new PrismaLibSQL({
  url: env.LIBSQL_DATABASE_URL,
  authToken: env.LIBSQL_DATABASE_TOKEN,
});

const prisma = new PrismaClient({ adapter });
```

### [Driver adapters and database connection configuration](#driver-adapters-and-database-connection-configuration)

In Prisma ORM 7, the database connection URL is configured in [`prisma.config.ts`](prisma/docs/orm/reference/prisma-config-reference/index.md). However, when using a driver adapter, the connection string needs to be provided in your _application code_ when the driver adapter is set up initially.

Here is how this is done for the `pg` driver and the `@prisma/adapter-pg` adapter:

```
import "dotenv/config";
import { PrismaClient } from "../generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
const prisma = new PrismaClient({ adapter });
```

See the docs for the driver adapter you're using for concrete setup instructions.

### [Driver adapters and custom output paths](#driver-adapters-and-custom-output-paths)

In Prisma ORM 7, the recommended approach is to use a custom output path for Prisma Client. The default output path is `../generated/prisma`.

Let's assume you have `output` in your Prisma schema set to `../generated/prisma`:

```
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}
```

You can reference Prisma Client using a relative path from your application code:

```
import { PrismaClient } from "./generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
const client = new PrismaClient({ adapter });
```

Alternatively, you can use a linked dependency for cleaner imports.

Now, you should be able to reference your generated client using `db`!

```
import { PrismaClient } from "db";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
const client = new PrismaClient({ adapter });
```

### [Driver adapters and specific frameworks](#driver-adapters-and-specific-frameworks)

#### [Nuxt](#nuxt)

Using a driver adapter with [Nuxt](https://nuxt.com/) to deploy to an edge function environment does not work out of the box, but adding the `nitro.experimental.wasm` configuration option fixes that:

```
export default defineNuxtConfig({
  // ...
  nitro: {
    // ...
    experimental: {
      wasm: true,
    },
  },
  // ...
});
```

### [Driver adapters and TypedSQL](#driver-adapters-and-typedsql)

[TypedSQL](prisma/docs/orm/prisma-client/using-raw-sql/typedsql/index.md) lets you write fully type-safe SQL queries that integrate directly with Prisma Client. This feature is useful if you want the flexibility of writing SQL while still benefiting from Prisma's type-safety.

You can also use driver adapters together with TypedSQL to connect through JavaScript database drivers. TypedSQL works with all supported driver adapters except `@prisma/adapter-better-sqlite3`. For SQLite support, use [`@prisma/adapter-libsql`](https://www.npmjs.com/package/@prisma/adapter-libsql) instead.
