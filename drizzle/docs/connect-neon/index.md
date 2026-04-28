---
title: "Drizzle <> Neon Postgres"
source: "https://orm.drizzle.team/docs/connect-neon"
canonical_url: "https://orm.drizzle.team/docs/connect-neon"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:29:08.613Z"
content_hash: "06e2a999c7591d698b8aded5a98677cbccc3318dcf8ae81ae2e0e267fb778525"
menu_path: ["Drizzle <> Neon Postgres"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/connect-planetscale-postgres/index.md", "title": "Drizzle <> PlanetScale Postgres"}
nav_next: {"path": "drizzle/docs/connect-vercel-postgres/index.md", "title": "Drizzle <> Vercel Postgres"}
---

## Drizzle <> Neon Postgres

Drizzle has native support for Neon connections with the `neon-http` and `neon-websockets` drivers. These use the **neon-serverless** driver under the hood.

With the `neon-http` and `neon-websockets` drivers, you can access a Neon database from serverless environments over HTTP or WebSockets instead of TCP.  
Querying over HTTP is faster for single, non-interactive transactions.

If you need session or interactive transaction support, or a fully compatible drop-in replacement for the `pg` driver, you can use the WebSocket-based `neon-serverless` driver.  
You can connect to a Neon database directly using [Postgres](drizzle/docs/get-started/postgresql-new/index.md)

For an example of using Drizzle ORM with the Neon Serverless driver in a Cloudflare Worker, **[see here.](http://driz.link/neon-cf-ex)**  
To use Neon from a serverful environment, you can use the PostgresJS driver, as described in Neon’s **[official Node.js docs](https://neon.tech/docs/guides/node)** — see **[docs](#postgresjs)**.

#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm @neondatabase/serverless
npm i -D drizzle-kit
```

```
yarn add drizzle-orm @neondatabase/serverless
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm @neondatabase/serverless
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm @neondatabase/serverless
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

Neon HTTP

Neon Websockets

node-postgres

postgres.js

```typescript
import { drizzle } from 'drizzle-orm/neon-http';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```

```typescript
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/node-postgres';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```

```typescript
// Make sure to install the 'postgres' package
import { drizzle } from 'drizzle-orm/postgres-js';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```

If you need to provide your existing drivers:

Neon HTTP

Neon Websockets

node-postgres

postgres.js

```typescript
import { neon } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle({ client: sql });

const result = await db.execute('select 1');
```

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
