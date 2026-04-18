---
title: "Drizzle <> PostgreSQL"
source: "https://orm.drizzle.team/docs/get-started-cockroach"
canonical_url: "https://orm.drizzle.team/docs/get-started-cockroach"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:02.391Z"
content_hash: "a0299ce221fd41f888c62bed58d9f11a8247b0e39def02a88b7906f8f4a5087a"
menu_path: ["Drizzle <> PostgreSQL"]
section_path: []
---
## Drizzle <> PostgreSQL

WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.2` and higher.

Drizzle has native support for PostgreSQL connections with the `node-postgres` driver.

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

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

```
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/cockroach';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```

```
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

```
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
