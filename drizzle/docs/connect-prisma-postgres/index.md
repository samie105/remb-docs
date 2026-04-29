---
title: "Drizzle <> Prisma Postgres"
source: "https://orm.drizzle.team/docs/connect-prisma-postgres"
canonical_url: "https://orm.drizzle.team/docs/connect-prisma-postgres"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:31:23.430Z"
content_hash: "caed94323d88cdc32c5da716dc93ea3c11a1eb4ab489b100bed66ae6c0a5be0f"
menu_path: ["Drizzle <> Prisma Postgres"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/connect-vercel-postgres/index.md", "title": "Drizzle <> Vercel Postgres"}
nav_next: {"path": "drizzle/docs/connect-supabase/index.md", "title": "Drizzle <> Supabase"}
---

This guide assumes familiarity with:

-   Database [connection basics](../connect-overview/index.md) with Drizzle
-   Prisma Postgres serverless database - [website](https://prisma.io/postgres)
-   Prisma Postgres direct connections - [docs](https://www.prisma.io/docs/postgres/database/direct-connections)
-   Drizzle PostgreSQL drivers - [docs](../get-started-postgresql/index.md)

Prisma Postgres is a serverless database built on [unikernels](https://www.prisma.io/blog/announcing-prisma-postgres-early-access). It has a large free tier, [operation-based pricing](https://www.prisma.io/blog/operations-based-billing) and no cold starts.

You can connect to it using either the [`node-postgres`](https://node-postgres.com/) or [`postgres.js`](https://github.com/porsager/postgres) drivers for PostgreSQL.

Prisma Postgres also has a [serverless driver](https://www.prisma.io/docs/postgres/database/serverless-driver) that will be supported with Drizzle ORM in the future.

#### Step 1 - Install packages[](#step-1---install-packages)

node-postgres (pg)

postgres.js

```
npm i drizzle-orm pg
npm i -D drizzle-kit
```

```
yarn add drizzle-orm pg
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm pg
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm pg
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

node-postgres (pg)

postgres.js

```typescript
// Make sure to install the 'pg' package 
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
const db = drizzle({ client: pool });
 
const result = await db.execute('select 1');
```

```typescript
// Make sure to install the 'postgres' package
import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';

const queryClient = postgres(process.env.DATABASE_URL);
const db = drizzle({ client: queryClient });

const result = await db.execute('select 1');
```

#### What’s next?[](#whats-next)
