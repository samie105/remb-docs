---
title: "Drizzle <> PostgreSQL"
source: "https://orm.drizzle.team/docs/get-started-cockroach"
canonical_url: "https://orm.drizzle.team/docs/get-started-cockroach"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:39:47.680Z"
content_hash: "eb14b61b2e1fd2a26e5705914fd382d17757086597f2e0660e20a6e0d6b84e51"
menu_path: ["Drizzle <> PostgreSQL"]
section_path: []
content_language: "en"
nav_prev: {"path": "../get-started-mssql/index.md", "title": "Drizzle <> MSSQL"}
nav_next: {"path": "../get-started-singlestore/index.md", "title": "Drizzle <> SingleStore"}
---

## Drizzle <> PostgreSQL

WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.2` and higher.

Drizzle has native support for PostgreSQL connections with the `node-postgres` driver.

#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm@beta pg
npm i -D drizzle-kit@beta @types/pg
```

```
yarn add drizzle-orm@beta pg
yarn add -D drizzle-kit@beta @types/pg
```

```
pnpm add drizzle-orm@beta pg
pnpm add -D drizzle-kit@beta @types/pg
```

```
bun add drizzle-orm@beta pg
bun add -D drizzle-kit@beta @types/pg
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

node-postgres

node-postgres with config

```typescript
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/cockroach';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```

```typescript
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/cockroach';

// You can specify any property from the node-postgres connection options
const db = drizzle({ 
  connection: { 
    connectionString: process.env.DATABASE_URL,
    ssl: true
  }
});
 
const result = await db.execute('select 1');
```

If you need to provide your existing driver:

```typescript
// Make sure to install the 'pg' package 
import { drizzle } from "drizzle-orm/cockroach";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
const db = drizzle({ client: pool });
 
const result = await db.execute('select 1');
```

#### What’s next?[](#whats-next)
