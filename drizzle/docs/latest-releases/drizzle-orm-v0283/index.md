---
title: "Drizzle ORM - DrizzleORM v0.28.3 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0283"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0283"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:15.126Z"
content_hash: "0daa7206b3a3c1ed8ba9c19806c1743181778f91145bcd283c86bb35f89c77ea"
menu_path: ["Drizzle ORM - DrizzleORM v0.28.3 release"]
section_path: []
nav_prev: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0282/index.md", "title": "Drizzle ORM - DrizzleORM v0.28.2 release"}
nav_next: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0284/index.md", "title": "Drizzle ORM - DrizzleORM v0.28.4 release"}
---

DrizzleORM v0.28.3 release

Aug 22, 2023

## Fixes

*   Fixed sqlite-proxy and SQL.js response from `.get()` when the result is empty

## New Features

### 🎉 Added SQLite simplified query API

### 🎉 Added `.$defaultFn()` / `.$default()` methods to column builders

For more information check docs for [PostgreSQL](drizzle/docs/column-types/pg/index.md#default-value), [MySQL](drizzle/docs/column-types/mysql/index.md#default-value) and [SQLite](drizzle/docs/column-types/sqlite/index.md#default-value).

You can specify any logic and any implementation for a function like `cuid()` for runtime defaults. Drizzle won’t limit you in the number of implementations you can add.

> Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```
import { varchar, mysqlTable } from "drizzle-orm/mysql-core";
import { createId } from '@paralleldrive/cuid2';

const table = mysqlTable('table', {
	id: varchar('id', { length: 128 }).$defaultFn(() => createId()),
});
```

### 🎉 Added `table.$inferSelect` / `table._.inferSelect` and `table.$inferInsert` / `table._.inferInsert` for more convenient table model type inference

*   🛠 Deprecated `InferModel` type in favor of more explicit `InferSelectModel` and `InferInsertModel`

```
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

*   🛠 Disabled `.d.ts` files bundling

