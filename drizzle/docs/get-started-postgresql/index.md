---
title: "Drizzle <> PostgreSQL"
source: "https://orm.drizzle.team/docs/get-started-postgresql"
canonical_url: "https://orm.drizzle.team/docs/get-started-postgresql"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:46.351Z"
content_hash: "bdc09d623fe5aba3bb27496fcca5a53798f517d8a9f864fcdb1529f517e049a6"
menu_path: ["Drizzle <> PostgreSQL"]
section_path: []
nav_prev: {"path": "drizzle/docs/migrations/index.md", "title": "Drizzle migrations fundamentals"}
nav_next: {"path": "drizzle/docs/get-started-gel/index.md", "title": "Drizzle <> Gel"}
---

Drizzle has native support for PostgreSQL connections with the `node-postgres` and `postgres.js` drivers.

There are a few differences between the `node-postgres` and `postgres.js` drivers that we discovered while using both and integrating them with the Drizzle ORM. For example:

*   With `node-postgres`, you can install `pg-native` to boost the speed of both `node-postgres` and Drizzle by approximately 10%.
*   `node-postgres` supports providing type parsers on a per-query basis without globally patching things. For more details, see [Types Docs](https://node-postgres.com/features/queries#types).
*   `postgres.js` uses prepared statements by default, which you may need to opt out of. This could be a potential issue in AWS environments, among others, so please keep that in mind.
*   If there’s anything else you’d like to contribute, we’d be happy to receive your PRs [here](https://github.com/drizzle-team/drizzle-orm-docs/pulls)

## node-postgres[](#node-postgres)

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

```
npm i drizzle-orm pg
npm i -D drizzle-kit @types/pg
```

```
yarn add drizzle-orm pg
yarn add -D drizzle-kit @types/pg
```

```
pnpm add drizzle-orm pg
pnpm add -D drizzle-kit @types/pg
```

```
bun add drizzle-orm pg
bun add -D drizzle-kit @types/pg
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

node-postgres

node-postgres with config

```
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/node-postgres';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```

```
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/node-postgres';

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
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
const db = drizzle({ client: pool });
 
const result = await db.execute('select 1');
```

## postgres.js[](#postgresjs)

#### Step 1 - Install packages[](#step-1---install-packages-1)

npm

yarn

pnpm

bun

```
npm i drizzle-orm postgres
npm i -D drizzle-kit
```

```
yarn add drizzle-orm postgres
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm postgres
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm postgres
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query-1)

postgres.js

postgres.js with config

```
import { drizzle } from 'drizzle-orm/postgres-js';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```

```
import { drizzle } from 'drizzle-orm/postgres-js';

// You can specify any property from the postgres-js connection options
const db = drizzle({ 
  connection: { 
    url: process.env.DATABASE_URL, 
    ssl: true 
  }
});

const result = await db.execute('select 1');
```

If you need to provide your existing driver:

```
// Make sure to install the 'postgres' package
import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';

const queryClient = postgres(process.env.DATABASE_URL);
const db = drizzle({ client: queryClient });

const result = await db.execute('select 1');
```

#### What’s next?[](#whats-next)


