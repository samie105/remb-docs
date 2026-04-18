---
title: "Drizzle <> Xata"
source: "https://orm.drizzle.team/docs/connect-xata"
canonical_url: "https://orm.drizzle.team/docs/connect-xata"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:00.450Z"
content_hash: "dd85e6a747216a517e216023d618f23cd731d943e1c3cbeb9d35f6de723d80a1"
menu_path: ["Drizzle <> Xata"]
section_path: []
nav_prev: {"path": "drizzle/docs/connect-supabase/index.md", "title": "Drizzle <> Supabase"}
nav_next: {"path": "drizzle/docs/connect-pglite/index.md", "title": "Drizzle <> PGlite"}
---

This guide assumes familiarity with:

*   Database [connection basics](drizzle/docs/connect-overview/index.md) with Drizzle
*   Drizzle PostgreSQL drivers - [docs](drizzle/docs/get-started-postgresql/index.md)

**[Xata](https://xata.io/)** is a PostgreSQL database platform designed to help developers operate and scale databases with enhanced productivity and performance. Xata provides features like instant copy-on-write database branches, zero-downtime schema changes, data anonymization, AI-powered performance monitoring, and BYOC.

Checkout official **[Xata + Drizzle](https://xata.io/documentation/quickstarts/drizzle)** docs.

#### Step 1 - Install packages[](#step-1---install-packages)

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

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

```
import { drizzle } from 'drizzle-orm/postgres-js'

const db = drizzle(process.env.DATABASE_URL);

const allUsers = await db.select().from(...);
```

If you need to provide your existing driver:

```
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

const client = postgres(process.env.DATABASE_URL)
const db = drizzle({ client });

const allUsers = await db.select().from(...);
```

#### What’s next?[](#whats-next)


