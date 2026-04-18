---
title: "Drizzle <> MSSQL"
source: "https://orm.drizzle.team/docs/get-started-mssql"
canonical_url: "https://orm.drizzle.team/docs/get-started-mssql"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:07.760Z"
content_hash: "f31669458a95e7ef8e7840f8827df7d4273c88e931b73214b994e5daf80eb1d6"
menu_path: ["Drizzle <> MSSQL"]
section_path: []
---
WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.2` and higher.

Drizzle has native support for MSSQL connections with the `mssql` driver.

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

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

mssql

mssql with config

```
// Make sure to install the 'mssql' package 
import { drizzle } from 'drizzle-orm/node-mssql';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```

```
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

```
const awaitedClient = await db.$client;
const response = awaitedClient.query...
```

If you need to provide your existing driver:

```
// Make sure to install the 'mssql' package 
import { drizzle } from "drizzle-orm/node-mssql";
import type { ConnectionPool } from 'mssql';

const pool = await mssql.connect(connectionString);
const db = drizzle({ client: pool });
 
const result = await db.execute('select 1');
```

#### What’s next?[](#whats-next)
