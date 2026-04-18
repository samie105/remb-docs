---
title: "Drizzle ORM - undefined"
source: "https://orm.drizzle.team/docs/migrate/components"
canonical_url: "https://orm.drizzle.team/docs/migrate/components"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:16:51.069Z"
content_hash: "3baa598ba8d6ea1be5db4db2a29519e470f3fe88651989a03008c2bf1532fc94"
menu_path: ["Drizzle ORM - undefined"]
section_path: []
nav_prev: {"path": "drizzle/docs/latest-releases/drizzle-orm-v03010/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.10 release"}
nav_next: {"path": "drizzle/docs/migrate/migrate-from-prisma/index.md", "title": "Migrate from Prisma to Drizzle"}
---

## Npm[](#npm)

npm

yarn

pnpm

bun

```
npm i drizzle-orm
```

```
yarn add drizzle-orm
```

```
pnpm add drizzle-orm
```

```
bun add drizzle-orm
```

npm

yarn

pnpm

bun

```
npm i drizzle-orm -D drizzle-kit
```

```
yarn add drizzle-orm -D drizzle-kit
```

```
pnpm add drizzle-orm -D drizzle-kit
```

```
bun add drizzle-orm -D drizzle-kit
```

## AnchorCards[](#anchorcards)

## Callout[](#callout)

Callout example

Callout example

Callout example

IMPORTANT

Callout example

WARNING

Callout example

## CodeTabs with CodeTab[](#codetabs-with-codetab)

index.ts

schema.ts

```
import * as schema from './schema';
import { drizzle } from 'drizzle-orm/...';

const db = drizzle(client, { schema });

const result = await db.query.users.findMany({
	with: {
		posts: true
	},
});
```

```
[{
	id: 10,
	name: "Dan",
	posts: [
		{
			id: 1,
			content: "SQL is awesome",
			authorId: 10,
		},
		{
			id: 2,
			content: "But check relational queries",
			authorId: 10,
		}
	]
}]
```

```
import { integer, serial, text, pgTable } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name').notNull(),
});

export const usersRelations = relations(users, ({ many }) => ({
	posts: many(posts),
}));

export const posts = pgTable('posts', {
	id: serial('id').primaryKey(),
	content: text('content').notNull(),
	authorId: integer('author_id').notNull(),
});

export const postsRelations = relations(posts, ({ one }) => ({
	author: one(users, { fields: [posts.authorId], references: [users.id] }),
}));
```

## IsSupportedChipGroup[](#issupportedchipgroup)

PostgreSQL

SQLite

MySQL

## Section[](#section)

For codeblocks connection

```
import { sql } from "drizzle-orm";
import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
int1: integer('int1').default(42),
int2: integer('int2').default(sql`(abs(42))`)
});
```

```
CREATE TABLE `table` (
  `int1` integer DEFAULT 42,
  `int2` integer DEFAULT (abs(42))
);
```

## Tabs with Tab and Section[](#tabs-with-tab-and-section)

PostgreSQL

MySQL

SQLite

```
import { sql } from "drizzle-orm";
import { integer, uuid, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
  integer1: integer('integer1').default(42),
  integer2: integer('integer2').default(sql`'42'::integer`),
  uuid1: uuid('uuid1').defaultRandom(),
  uuid2: uuid('uuid2').default(sql`gen_random_uuid()`),
});
```

```
CREATE TABLE IF NOT EXISTS "table" (
  "integer1" integer DEFAULT 42,
  "integer2" integer DEFAULT '42'::integer,
  "uuid1" uuid DEFAULT gen_random_uuid(),
  "uuid2" uuid DEFAULT gen_random_uuid()
);
```

```
import { sql } from "drizzle-orm";
import { int, time, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable("table", {
  int: int("int").default(42),
  time: time("time").default(sql`cast("14:06:10" AS TIME)`),
});
```

```
CREATE TABLE `table` (
  `int` int DEFAULT 42,
  `time` time DEFAULT cast("14:06:10" AS TIME)
);
```

```
import { sql } from "drizzle-orm";
import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
  int1: integer('int1').default(42),
  int2: integer('int2').default(sql`(abs(42))`)
});
```

```
CREATE TABLE `table` (
  `int1` integer DEFAULT 42,
  `int2` integer DEFAULT (abs(42))
);
```

## SimpleLinkCards[](#simplelinkcards)

## Steps[](#steps)

With h4 headers

#### Install babel plugin[](#install-babel-plugin)

It’s necessary to bundle SQL migration files as string directly to your bundle.

```
npm install babel-plugin-inline-import
```

#### Update config files.[](#update-config-files)

You will need to update `babel.config.js`, `metro.config.js` and `drizzle.config.ts` files

```
module.exports = function (api) {
  api.cache(true);

  return {
    presets: ["babel-preset-expo"],
    plugins: [["inline-import", { extensions: [".sql"] }]], // <-- add this
  };
};
```

## YoutubeCards[](#youtubecards)

## Collapsable code block[](#collapsable-code-block)

```
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Product {
  id              Int           @id @default(autoincrement())
  name            String
  supplierId      Int
  unitPrice       Decimal       @db.Decimal(10, 4)
  unitsInStock    Int

  supplier        Supplier?     @relation(fields: [supplierId], references: [id])
  orderDetails    OrderDetail[]

  @@map("products")
}

model Supplier {
  id           Int       @id @default(autoincrement())
  companyName  String
  city         String
  country      String

  products     Product[]

  @@map("suppliers")
}

model OrderDetail {
  orderId   Int
  productId Int
  quantity  Int

  order   Order   @relation(fields: [orderId], references: [id])
  product Product @relation(fields: [productId], references: [id])

  @@id([orderId, productId])
  @@map("order_details")
}

model Order {
  id             Int       @id @default(autoincrement())
  orderDate      DateTime  @db.Date
  shippedDate    DateTime? @db.Date
  shipAddress    String
  shipPostalCode String?
  shipCountry    String

  orderDetails OrderDetail[]

  @@map("orders")
}
```

Expand


