---
title: "Drizzle ORM - DrizzleORM v0.28.3 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0283"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0283"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:09:21.167Z"
content_hash: "8c5b3bb7cc9a3d49735d82fef25db7bbc56cd189cc58c91cb04fa9cb31a0615f"
menu_path: ["Drizzle ORM - DrizzleORM v0.28.3 release"]
section_path: []
content_language: "en"
---
DrizzleORM v0.28.3 release

Aug 22, 2023

## Fixes

-   Fixed sqlite-proxy and SQL.js response from `.get()` when the result is empty

## New Features

### 🎉 Added SQLite simplified query API

### 🎉 Added `.$defaultFn()` / `.$default()` methods to column builders

For more information check docs for [PostgreSQL](https://orm.drizzle.team/docs/column-types/pg#default-value), [MySQL](https://orm.drizzle.team/docs/column-types/mysql#default-value) and [SQLite](https://orm.drizzle.team/docs/column-types/sqlite#default-value).

You can specify any logic and any implementation for a function like `cuid()` for runtime defaults. Drizzle won’t limit you in the number of implementations you can add.

> Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```ts
import { varchar, mysqlTable } from "drizzle-orm/mysql-core";
import { createId } from '@paralleldrive/cuid2';

const table = mysqlTable('table', {
	id: varchar('id', { length: 128 }).$defaultFn(() => createId()),
});
```

### 🎉 Added `table.$inferSelect` / `table._.inferSelect` and `table.$inferInsert` / `table._.inferInsert` for more convenient table model type inference

-   🛠 Deprecated `InferModel` type in favor of more explicit `InferSelectModel` and `InferInsertModel`

```ts
import { InferSelectModel, InferInsertModel } from 'drizzle-orm'

const usersTable = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  verified: boolean('verified').notNull().default(false),
  jsonb: jsonb('jsonb').$type<string[]>(),
  createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
});

type SelectUser = typeof usersTable.$inferSelect;
type InsertUser = typeof usersTable.$inferInsert;

type SelectUser2 = InferSelectModel<typeof usersTable>;
type InsertUser2 = InferInsertModel<typeof usersTable>;
```

-   🛠 Disabled `.d.ts` files bundling
