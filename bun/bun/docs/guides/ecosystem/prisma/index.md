---
title: "Use Prisma with Bun"
source: "https://bun.com/docs/guides/ecosystem/prisma"
canonical_url: "https://bun.com/docs/guides/ecosystem/prisma"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:32.097Z"
content_hash: "321aa8a2a78178bbb4ab7c6aca00647b78d946f3693e17973310521ceace9cac"
menu_path: ["Use Prisma with Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/pm2/index.md", "title": "Run Bun as a daemon with PM2"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/qwik/index.md", "title": "Build an app with Qwik and Bun"}
---

**Note** — Prisma’s dynamic subcommand loading system currently requires npm to be installed alongside Bun. This affects certain CLI commands like `prisma init`, `prisma migrate`, etc. Generated code works perfectly with Bun using the new `prisma-client` generator.

1

Create a new project

Prisma works out of the box with Bun. First, create a directory and initialize it with `bun init`.

terminal

```
mkdir prisma-app
cd prisma-app
bun init
```

2

Install Prisma dependencies

Then install the Prisma CLI (`prisma`), Prisma Client (`@prisma/client`), and the LibSQL adapter as dependencies.

terminal

```
bun add -d prisma
bun add @prisma/client @prisma/adapter-libsql
```

3

Initialize Prisma with SQLite

We’ll use the Prisma CLI with `bunx` to initialize our schema and migration directory. For simplicity we’ll be using an in-memory SQLite database.

terminal

```
bunx --bun prisma init --datasource-provider sqlite
```

This creates a basic schema. We need to update it to use the new Rust-free client with Bun optimization. Open `prisma/schema.prisma` and modify the generator block, then add a `User` model.

![https://mintcdn.com/bun-1dd33a4e/nIz6GtMH5K-dfXeV/icons/ecosystem/prisma.svg?fit=max&auto=format&n=nIz6GtMH5K-dfXeV&q=85&s=c37203455320f85a20a7b29ce374661c](https://mintcdn.com/bun-1dd33a4e/nIz6GtMH5K-dfXeV/icons/ecosystem/prisma.svg?fit=max&auto=format&n=nIz6GtMH5K-dfXeV&q=85&s=c37203455320f85a20a7b29ce374661c)prisma/schema.prisma

```
  generator client {
    provider = "prisma-client"
    output = "./generated"
    engineType = "client"
    runtime = "bun"
  }

  datasource db {
    provider = "sqlite"
    url      = env("DATABASE_URL")
  }

  model User { 
    id    Int     @id @default(autoincrement()) 
    email String  @unique
    name  String?
  } 
```

4

Create and run database migration

Then generate and run initial migration.This will generate a `.sql` migration file in `prisma/migrations`, create a new SQLite instance, and execute the migration against the new instance.

terminal

```
 bunx --bun prisma migrate dev --name init
```

```
Environment variables loaded from .env
Prisma schema loaded from prisma/schema.prisma
Datasource "db": SQLite database "dev.db" at "file:./dev.db"

SQLite database dev.db created at file:./dev.db

Applying migration `20251014141233_init`

The following migration(s) have been created and applied from new schema changes:

prisma/migrations/
 └─ 20251014141233_init/
   └─ migration.sql

Your database is now in sync with your schema.

✔ Generated Prisma Client (6.17.1) to ./generated in 18ms
```

5

Generate Prisma Client

As indicated in the output, Prisma re-generates our _Prisma client_ whenever we execute a new migration. The client provides a fully typed API for reading and writing from our database. You can manually re-generate the client with the Prisma CLI.

terminal

```
bunx --bun prisma generate
```

6

Initialize Prisma Client with LibSQL

Now we need to create a Prisma client instance. Create a new file `prisma/db.ts` to initialize the PrismaClient with the LibSQL adapter.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)prisma/db.ts

```
import { PrismaClient } from "./generated/client";
import { PrismaLibSQL } from "@prisma/adapter-libsql";

const adapter = new PrismaLibSQL({ url: process.env.DATABASE_URL || "" });
export const prisma = new PrismaClient({ adapter });
```

7

Create a test script

Let’s write a script to create a new user, then count the number of users in the database.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import { prisma } from "./prisma/db";

// create a new user
await prisma.user.create({
  data: {
    name: "John Dough",
    email: `john-${Math.random()}@example.com`,
  },
});

// count the number of users
const count = await prisma.user.count();
console.log(`There are ${count} users in the database.`);
```

8

Run and test the application

Let’s run this script with `bun run`. Each time we run it, a new user is created.

terminal

```
bun run index.ts
```

```
Created john-0.12802932895402364@example.com
There are 1 users in the database.
```

terminal

```
bun run index.ts
```

```
Created john-0.8671308799782803@example.com
There are 2 users in the database.
```

terminal

```
bun run index.ts
```

```
Created john-0.4465968383115295@example.com
There are 3 users in the database.
```

* * *

That’s it! Now that you’ve set up Prisma using Bun, we recommend referring to the [official Prisma docs](https://www.prisma.io/docs/orm/prisma-client) as you continue to develop your application.


