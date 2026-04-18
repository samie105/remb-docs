---
title: "Use Prisma Postgres with Bun"
source: "https://bun.com/docs/guides/ecosystem/prisma-postgres"
canonical_url: "https://bun.com/docs/guides/ecosystem/prisma-postgres"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:06.407Z"
content_hash: "265fd3376c02dcb33e38984363f60354ee98bb60cf0b6f0476b527137a0089f5"
menu_path: ["Use Prisma Postgres with Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/react/index.md", "title": "Build a React app with Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/sentry/index.md", "title": "Add Sentry to a Bun app"}
---

**Note** — At the moment Prisma needs Node.js to be installed to run certain generation code. Make sure Node.js is installed in the environment where you’re running `bunx prisma` commands.

1

Create a new project

First, create a directory and initialize it with `bun init`.

terminal

```
mkdir prisma-postgres-app
cd prisma-postgres-app
bun init
```

2

Install Prisma dependencies

Then install the Prisma CLI (`prisma`), Prisma Client (`@prisma/client`), and the accelerate extension as dependencies.

terminal

```
bun add -d prisma
bun add @prisma/client @prisma/extension-accelerate
```

3

Initialize Prisma with PostgreSQL

We’ll use the Prisma CLI with `bunx` to initialize our schema and migration directory. We’ll be using PostgreSQL as our database.

terminal

```
bunx --bun prisma init --db
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
	provider = "postgresql"
	url      = env("DATABASE_URL")
}

model User { 
	id    Int     @id @default(autoincrement()) 
	email String  @unique
	name  String?
} 
```

4

Configure database connection

Set up your Postgres database URL in the `.env` file.

.env

```
DATABASE_URL="postgresql://username:password@localhost:5432/mydb?schema=public"
```

5

Create and run database migration

Then generate and run initial migration.This will generate a `.sql` migration file in `prisma/migrations`, and execute the migration against your Postgres database.

terminal

```
bunx --bun prisma migrate dev --name init
```

```
Environment variables loaded from .env
Prisma schema loaded from prisma/schema.prisma
Datasource "db": PostgreSQL database "mydb", schema "public" at "localhost:5432"

Applying migration `20250114141233_init`

The following migration(s) have been created and applied from new schema changes:

prisma/migrations/
  └─ 20250114141233_init/
    └─ migration.sql

Your database is now in sync with your schema.

✔ Generated Prisma Client (6.17.1) to ./generated in 18ms
```

6

Generate Prisma Client

As indicated in the output, Prisma re-generates our _Prisma client_ whenever we execute a new migration. The client provides a fully typed API for reading and writing from our database. You can manually re-generate the client with the Prisma CLI.

terminal

```
bunx --bun prisma generate
```

7

Initialize Prisma Client with Accelerate

Now we need to create a Prisma client instance. Create a new file `prisma/db.ts` to initialize the PrismaClient with the Postgres adapter.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)prisma/db.ts

```
import { PrismaClient } from "./generated/client";
import { withAccelerate } from '@prisma/extension-accelerate'

export const prisma = new PrismaClient().$extends(withAccelerate())
```

8

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

9

Run and test the application

Let’s run this script with `bun run`. Each time we run it, a new user is created.

terminal

```
bun run index.ts
```

```
There are 1 users in the database.
```

terminal

```
bun run index.ts
```

```
There are 2 users in the database.
```

terminal

```
bun run index.ts
```

```
There are 3 users in the database.
```

* * *

That’s it! Now that you’ve set up Prisma Postgres using Bun, we recommend referring to the [official Prisma Postgres docs](https://www.prisma.io/docs/postgres) as you continue to develop your application.

Was this page helpful?
