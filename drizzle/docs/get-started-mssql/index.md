---
title: "Drizzle <> MSSQL"
source: "https://orm.drizzle.team/docs/get-started-mssql"
canonical_url: "https://orm.drizzle.team/docs/get-started-mssql"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:40:20.817Z"
content_hash: "af25dd0566ea0c769db4a0e379e1826c9426a5346ea35da0c7890b63225aa88d"
menu_path: ["Drizzle <> MSSQL"]
section_path: []
content_language: "en"
nav_prev: {"path": "../get-started-sqlite/index.md", "title": "Drizzle <> SQLite"}
nav_next: {"path": "../get-started-cockroach/index.md", "title": "Drizzle <> PostgreSQL"}
---

WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.2` and higher.

Drizzle has native support for MSSQL connections with the `mssql` driver.

#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm@beta mssql
npm i -D drizzle-kit@beta
```

```
yarn add drizzle-orm@beta mssql
yarn add -D drizzle-kit@beta
```

```
pnpm add drizzle-orm@beta mssql
pnpm add -D drizzle-kit@beta
```

```
bun add drizzle-orm@beta mssql
bun add -D drizzle-kit@beta
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

```typescript
// Make sure to install the 'mssql' package 
import { drizzle } from 'drizzle-orm/node-mssql';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```

```typescript
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/node-mssql';

// You can specify any property from the mssql connection options
const db = drizzle({ 
  connection: { 
    connectionString: process.env.DATABASE_URL,
    ssl: true
  }
});
 
const result = await db.execute('select 1');
```

IMPORTANT

As long as the `node-mssql` driver requires `await` on `Pool` initialization, we need to `await` it before each request - unless you are providing your own Pool instance to Drizzle. In that case, when you want to access `db.$client`, you first need to `await` it, and then use it

```ts
const awaitedClient = await db.$client;
const response = awaitedClient.query...
```

If you need to provide your existing driver:

```typescript
// Make sure to install the 'mssql' package 
import { drizzle } from "drizzle-orm/node-mssql";
import type { ConnectionPool } from 'mssql';

const pool = await mssql.connect(connectionString);
const db = drizzle({ client: pool });
 
const result = await db.execute('select 1');
```

#### What’s next?[](#whats-next)
