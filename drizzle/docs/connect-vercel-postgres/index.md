---
title: "Drizzle <> Vercel Postgres"
source: "https://orm.drizzle.team/docs/connect-vercel-postgres"
canonical_url: "https://orm.drizzle.team/docs/connect-vercel-postgres"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:33:37.070Z"
content_hash: "bafb9a1dcff6264e2046b9524b8576d6c04e3efb2d151a29baf935b12f115ba2"
menu_path: ["Drizzle <> Vercel Postgres"]
section_path: []
content_language: "en"
nav_prev: {"path": "../connect-neon/index.md", "title": "Drizzle <> Neon Postgres"}
nav_next: {"path": "../connect-prisma-postgres/index.md", "title": "Drizzle <> Prisma Postgres"}
---

According to their **[official website](https://vercel.com/docs/storage/vercel-postgres)**, Vercel Postgres is a serverless SQL database designed to integrate with Vercel Functions.

Drizzle ORM natively supports both **[@vercel/postgres](https://vercel.com/docs/storage/vercel-postgres)** serverless driver with `drizzle-orm/vercel-postgres` package and **[`postgres`](#postgresjs)** or **[`pg`](#node-postgres)** drivers to access Vercel Postgres through `postgesql://`

Check out the official **[Vercel Postgres + Drizzle](https://vercel.com/docs/storage/vercel-postgres/using-an-orm#drizzle)** docs.

#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm @vercel/postgres
npm i -D drizzle-kit
```

```
yarn add drizzle-orm @vercel/postgres
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm @vercel/postgres
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm @vercel/postgres
bun add -D drizzle-kit
```

#### Step 2 - Prepare Vercel Postgres[](#step-2---prepare-vercel-postgres)

Setup a project according to the **[official docs.](https://vercel.com/docs/storage/vercel-postgres/quickstart)**

#### Step 3 - Initialize the driver and make a query[](#step-3---initialize-the-driver-and-make-a-query)

```typescript
import { drizzle } from 'drizzle-orm/vercel-postgres';

const db = drizzle();

const result = await db.execute('select 1');
```

If you need to provide your existing driver:

```typescript
import { sql } from '@vercel/postgres';
import { drizzle } from 'drizzle-orm/vercel-postgres';

const db = drizzle({ client: sql })

const result = await db.execute('select 1');
```

With **[@vercel/postgres](https://vercel.com/docs/storage/vercel-postgres)** severless package you can access Vercel Postgres from either serverful or serverless environments with no TCP available, like Cloudflare Workers, through websockets.

If you’re about to use Vercel Postgres from a _serverfull_ environment, you can do it either with `@vercel/postgres` or directly access the DB through `postgesql://` with either **[`postgres`](#postgresjs)** or **[`pg`](#node-postgres)**.

#### What’s next?[](#whats-next)
