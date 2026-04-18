---
title: "Drizzle"
source: "https://supabase.com/docs/guides/database/drizzle"
canonical_url: "https://supabase.com/docs/guides/database/drizzle"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:28.838Z"
content_hash: "d942a1a64f1ac143f42eba5c3b6271cd1b8471df7d4d8dbd034d559f4c725ae9"
menu_path: ["Database","Database","ORM Quickstarts","ORM Quickstarts","Drizzle","Drizzle"]
section_path: ["Database","Database","ORM Quickstarts","ORM Quickstarts","Drizzle","Drizzle"]
nav_prev: {"path": "supabase/docs/guides/database/debugging-performance/index.md", "title": "Debugging performance issues"}
nav_next: {"path": "supabase/docs/guides/database/extensions/index.md", "title": "Postgres Extensions Overview"}
---

# 

Drizzle

* * *

### Connecting with Drizzle[#](#connecting-with-drizzle)

[Drizzle ORM](https://github.com/drizzle-team/drizzle-orm) is a TypeScript ORM for SQL databases designed with maximum type safety in mind. You can use their ORM to connect to your database.

If you plan on solely using Drizzle instead of the Supabase Data API (PostgREST), you can turn off the latter in the [API Settings](/dashboard/project/_/settings/api).

1

### Install

Install Drizzle and related dependencies.

```
1npm i drizzle-orm postgres2npm i -D drizzle-kit
```

2

### Create your models

Create a `schema.ts` file and define your models.

```
1import { pgTable, serial, text, varchar } from "drizzle-orm/pg-core";23export const users = pgTable('users', {4  id: serial('id').primaryKey(),5  fullName: text('full_name'),6  phone: varchar('phone', { length: 256 }),7});
```

3

### Connect

Connect to your database using the Connection Pooler.

From the project [**Connect** panel](/dashboard/project/_?showConnect=true), copy the URI from the "Shared Pooler" option and save it as the `DATABASE_URL` environment variable. Remember to replace the password placeholder with your actual database password.

In local SUPABASE\_DB\_URL require to be adapted to work with Docker resolver

```
1import 'dotenv/config'23import { drizzle } from 'drizzle-orm/postgres-js'4import postgres from 'postgres'56let connectionString = process.env.DATABASE_URL7if (host.includes('postgres:postgres@supabase_db_')) {8  const url = URL.parse(host)!9  url.hostname = url.hostname.split('_')[1]10  connectionString = url.href11}1213// Disable prefetch as it is not supported for "Transaction" pool mode14export const client = postgres(connectionString, { prepare: false })15export const db = drizzle(client);
```


