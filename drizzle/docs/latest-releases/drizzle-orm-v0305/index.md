---
title: "Drizzle ORM - DrizzleORM v0.30.5 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0305"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0305"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:03.761Z"
content_hash: "fa49c63edae9664e0da64a00b4ed34b169e829dbc4a902dfeba367a75f78fb6b"
menu_path: ["Drizzle ORM - DrizzleORM v0.30.5 release"]
section_path: []
nav_prev: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0303/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.3 release"}
nav_next: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0304/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.4 release"}
---

DrizzleORM v0.30.5 release

Mar 27, 2024

## New Features

### `$onUpdate` functionality for PostgreSQL, MySQL and SQLite

Adds a dynamic update value to the column. The function will be called when the row is updated, and the returned value will be used as the column value if none is provided. If no `default` (or `$defaultFn`) value is provided, the function will be called when the row is inserted as well, and the returned value will be used as the column value.

> Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`.

```
const usersOnUpdate = pgTable('users_on_update', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  updateCounter: integer('update_counter').default(sql`1`).$onUpdateFn(() => sql`update_counter + 1`),
  updatedAt: timestamp('updated_at', { mode: 'date', precision: 3 }).$onUpdate(() => new Date()),
  alwaysNull: text('always_null').$type<string | null>().$onUpdate(() => null),
});
```

## Fixes

*   Insertions on columns with the smallserial datatype are not optional - [#1848](https://github.com/drizzle-team/drizzle-orm/issues/1848)
