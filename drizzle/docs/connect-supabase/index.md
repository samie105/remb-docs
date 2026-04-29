---
title: "Drizzle <> Supabase"
source: "https://orm.drizzle.team/docs/connect-supabase"
canonical_url: "https://orm.drizzle.team/docs/connect-supabase"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:32:29.867Z"
content_hash: "c9c3ddbba83761a1064b8a36c39bb3ffbee08f745657e66c4e8c9842c8ddfe31"
menu_path: ["Drizzle <> Supabase"]
section_path: []
content_language: "en"
nav_prev: {"path": "../connect-prisma-postgres/index.md", "title": "Drizzle <> Prisma Postgres"}
nav_next: {"path": "../connect-xata/index.md", "title": "Drizzle <> Xata"}
---

This guide assumes familiarity with:

-   Database [connection basics](../connect-overview/index.md) with Drizzle
-   Drizzle PostgreSQL drivers - [docs](../get-started-postgresql/index.md)

According to the **[official website](https://supabase.com/docs)**, Supabase is an open source Firebase alternative for building secure and performant Postgres backends with minimal configuration.

Checkout official **[Supabase + Drizzle](https://supabase.com/docs/guides/database/connecting-to-postgres#connecting-with-drizzle)** docs.

#### Step 1 - Install packages[](#step-1---install-packages)

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

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

```typescript
import { drizzle } from 'drizzle-orm/postgres-js'

const db = drizzle(process.env.DATABASE_URL);

const allUsers = await db.select().from(...);
```

If you need to provide your existing driver:

```typescript
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

const client = postgres(process.env.DATABASE_URL)
const db = drizzle({ client });

const allUsers = await db.select().from(...);
```

If you decide to use connection pooling via Supabase (described [here](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler)), and have “Transaction” pool mode enabled, then ensure to turn off prepare, as prepared statements are not supported.

```typescript
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

// Disable prefetch as it is not supported for "Transaction" pool mode 
const client = postgres(process.env.DATABASE_URL, { prepare: false })
const db = drizzle({ client });

const allUsers = await db.select().from(...);
```

Connect to your database using the Connection Pooler for **serverless environments**, and the Direct Connection for **long-running servers**.

#### What’s next?[](#whats-next)
