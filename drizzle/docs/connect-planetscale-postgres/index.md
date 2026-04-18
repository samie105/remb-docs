---
title: "Drizzle <> PlanetScale Postgres"
source: "https://orm.drizzle.team/docs/connect-planetscale-postgres"
canonical_url: "https://orm.drizzle.team/docs/connect-planetscale-postgres"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:27.727Z"
content_hash: "1122c4be7e70635e63be57ec7bb38e49694b9486ee1e7518d126590ccfaeb4cc"
menu_path: ["Drizzle <> PlanetScale Postgres"]
section_path: []
---
This guide assumes familiarity with:

*   Database [connection basics](https://orm.drizzle.team/docs/connect-overview) with Drizzle
*   PlanetScale Postgres database - [docs](https://planetscale.com/docs/postgres)
*   Drizzle PostgreSQL drivers - [docs](https://orm.drizzle.team/docs/get-started-postgresql)

PlanetScale offers both MySQL (Vitess) and PostgreSQL databases. This page covers connecting to PlanetScale Postgres.

For PlanetScale MySQL, see the [PlanetScale MySQL connection guide](https://orm.drizzle.team/docs/connect-planetscale).

With Drizzle ORM you can connect to PlanetScale Postgres using:

*   The standard `node-postgres` driver
*   The `@neondatabase/serverless` driver for serverless environments

For detailed instructions on creating a PlanetScale Postgres database and obtaining credentials, see the [PlanetScale Postgres documentation](https://planetscale.com/docs/postgres/tutorials/planetscale-postgres-drizzle).

## node-postgres[](#node-postgres)

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

```
npm i drizzle-orm pg -D drizzle-kit @types/pg
```

```
yarn add drizzle-orm pg -D drizzle-kit @types/pg
```

```
pnpm add drizzle-orm pg -D drizzle-kit @types/pg
```

```
bun add drizzle-orm pg -D drizzle-kit @types/pg
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

Connection URL

With config

With existing client

```
import { drizzle } from 'drizzle-orm/node-postgres';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```

```
import { drizzle } from 'drizzle-orm/node-postgres';

const db = drizzle({
  connection: {
    connectionString: process.env.DATABASE_URL,
    ssl: true
  }
});

const result = await db.execute('select 1');
```

```
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
const db = drizzle({ client: pool });

const result = await db.execute("select 1");
```

## Neon serverless driver[](#neon-serverless-driver)

PlanetScale Postgres also supports connections via the [Neon serverless driver](https://planetscale.com/docs/postgres/connecting/neon-serverless-driver). This is a good option for serverless environments like Vercel Functions, Cloudflare Workers, or AWS Lambda.

The driver supports two modes:

*   **HTTP mode** — Faster for single queries and non-interactive transactions
*   **WebSocket mode** — Required for interactive transactions or session-based features

#### Step 1 - Install packages[](#step-1---install-packages-1)

npm

yarn

pnpm

bun

```
npm i drizzle-orm @neondatabase/serverless -D drizzle-kit
```

```
yarn add drizzle-orm @neondatabase/serverless -D drizzle-kit
```

```
pnpm add drizzle-orm @neondatabase/serverless -D drizzle-kit
```

```
bun add drizzle-orm @neondatabase/serverless -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query-1)

Neon HTTP

Neon WebSockets

```
import { neon, neonConfig } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';

// Required for PlanetScale Postgres connections
neonConfig.fetchEndpoint = (host) => `https://${host}/sql`;

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle({ client: sql });

const result = await db.execute('select 1');
```

Connection URL format

postgresql://{username}:{password}@{host}:{port}/postgres?sslmode=verify-full

Connection ports

PlanetScale Postgres supports two connection ports:

`5432`: Direct connection to PostgreSQL. Total connections are limited by your cluster’s `max_connections` setting.

`6432`: Connection via PgBouncer for connection pooling. Recommended when you have many simultaneous connections.

#### What’s next?[](#whats-next)
