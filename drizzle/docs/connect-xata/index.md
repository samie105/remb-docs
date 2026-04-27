---
title: "Drizzle <> Xata"
source: "https://orm.drizzle.team/docs/connect-xata"
canonical_url: "https://orm.drizzle.team/docs/connect-xata"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:33:37.377Z"
content_hash: "f6a8b711d7ae9e69d5bee6ad7efd2ed6c76ee531e20db0373a4e9580adb3ecad"
menu_path: ["Drizzle <> Xata"]
section_path: []
content_language: "en"
---
This guide assumes familiarity with:

-   Database [connection basics](https://orm.drizzle.team/docs/connect-overview) with Drizzle
-   Drizzle PostgreSQL drivers - [docs](https://orm.drizzle.team/docs/get-started-postgresql)

**[Xata](https://xata.io/)** is a PostgreSQL database platform designed to help developers operate and scale databases with enhanced productivity and performance. Xata provides features like instant copy-on-write database branches, zero-downtime schema changes, data anonymization, AI-powered performance monitoring, and BYOC.

Checkout official **[Xata + Drizzle](https://xata.io/documentation/quickstarts/drizzle)** docs.

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

#### What’s next?[](#whats-next)
