---
title: "Drizzle extension for Prisma"
source: "https://orm.drizzle.team/docs/prisma"
canonical_url: "https://orm.drizzle.team/docs/prisma"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:18:09.829Z"
content_hash: "fa465e3b8f87fa08bfb2ea246d001840c45bdc6c1f179147d21b4776e36b0e2e"
menu_path: ["Drizzle extension for Prisma"]
section_path: []
nav_prev: {"path": "drizzle/docs/effect-schema/index.md", "title": "effect-schema"}
nav_next: {"path": "drizzle/docs/eslint-plugin/index.md", "title": "ESLint Drizzle Plugin"}
---

## Drizzle extension for Prisma

If you have an existing project with Prisma and want to try Drizzle or gradually adopt it, you can use our first-class extension that will add Drizzle API to your Prisma client. It will allow you to use Drizzle alongside your Prisma queries reusing your existing DB connection.

## How to use[](#how-to-use)

#### Install dependencies[](#install-dependencies)

You need to install Drizzle itself and a generator package that will create Drizzle schema from the Prisma schema.

npm

yarn

pnpm

bun

```
npm i drizzle-orm@latest
npm i -D drizzle-prisma-generator
```

```
yarn add drizzle-orm@latest
yarn add -D drizzle-prisma-generator
```

```
pnpm add drizzle-orm@latest
pnpm add -D drizzle-prisma-generator
```

```
bun add drizzle-orm@latest
bun add -D drizzle-prisma-generator
```

#### Update your Prisma schema[](#update-your-prisma-schema)

Add Drizzle generator to your Prisma schema. `output` is the path where generated Drizzle schema TS files will be placed.

```
generator client {
  provider = "prisma-client-js"
}

generator drizzle {
  provider = "drizzle-prisma-generator"
  output   = "./drizzle" // Where to put generated Drizle tables
}

// Rest of your Prisma schema

datasource db {
  provider = "postgresql"
  url      = env("DB_URL")
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}

...
```

#### Generate Drizzle schema[](#generate-drizzle-schema)

```
prisma generate
```

#### Add Drizzle extension to your Prisma client[](#add-drizzle-extension-to-your-prisma-client)

PostgreSQL

MySQL

SQLite

```
import { PrismaClient } from '@prisma/client';
import { drizzle } from 'drizzle-orm/prisma/pg';

const prisma = new PrismaClient().$extends(drizzle());
```

#### Run Drizzle queries via `prisma.$drizzle` ✨[](#run-drizzle-queries-via-prismadrizzle-)

In order to use Drizzle query builder, you need references to Drizzle tables. You can import them from the output path that you specified in the generator config.

```
import { User } from './drizzle';

await prisma.$drizzle.insert().into(User).values({ email: 'sorenbs@drizzle.team', name: 'Søren' });
const users = await prisma.$drizzle.select().from(User);
```

## Limitations[](#limitations)

*   [Relational queries](drizzle/docs/rqb/index.md) are not supported due to a [Prisma driver limitation](https://github.com/prisma/prisma/issues/17576). Because of it, Prisma is unable to return query results in array format, which is required for relational queries to work.
*   In SQLite, `.values()` (e.g. `await db.select().from(table).values()`) is not supported, because of the same reason as above.
*   [Prepared statements](drizzle/docs/perf-queries/index.md#prepared-statement) support is limited - `.prepare()` will only build the SQL query on Drizzle side, because there is no Prisma API for prepared queries.
