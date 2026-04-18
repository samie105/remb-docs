---
title: "Drizzle ORM - DrizzleORM v0.27.2 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0272"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0272"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:10:40.795Z"
content_hash: "19bacdf4a9036c5ac687e3d989a95600328efab7b27b716047d4b1771ca5e6f4"
menu_path: ["Drizzle ORM - DrizzleORM v0.27.2 release"]
section_path: []
nav_prev: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0162/index.md", "title": "Drizzle ORM - DrizzleORM v0.16.2 release"}
nav_next: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0280/index.md", "title": "Drizzle ORM - DrizzleORM v0.28.0 release"}
---

DrizzleORM v0.27.2 release

Jul 12, 2023

## 🎉 Added support for `UNIQUE` constraints in PostgreSQL, MySQL, SQLite

For PostgreSQL, unique constraints can be defined at the column level for single-column constraints, and in the third parameter for multi-column constraints. In both cases, it will be possible to define a custom name for the constraint. Additionally, PostgreSQL will receive the `NULLS NOT DISTINCT` option to restrict having more than one NULL value in a table. [Reference](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-UNIQUE-CONSTRAINTS)

Examples that just shows a different `unique` usage. Please don’t search a real usage for those tables

```
// single column
const table = pgTable('table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull().unique(),
  state: char('state', { length: 2 }).unique('custom'),
  field: char('field', { length: 2 }).unique('custom_field', { nulls: 'not distinct' }),
});
// multiple columns
const table = pgTable('table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  state: char('state', { length: 2 }),
}, (t) => ({
  first: unique('custom_name').on(t.name, t.state).nullsNotDistinct(),
  second: unique('custom_name1').on(t.name, t.state),
}));
```

For MySQL, everything will be the same except for the `NULLS NOT DISTINCT` option. It appears that MySQL does not support it

Examples that just shows a different `unique` usage. Please don’t search a real usage for those tables

```
// single column
const table = mysqlTable('table', {
    id: serial('id').primaryKey(),
    name: text('name').notNull().unique(),
    state: text('state').unique('custom'),
    field: text('field').unique('custom_field'),
});
// multiple columns
const table = mysqlTable('cities1', {
    id: serial('id').primaryKey(),
    name: text('name').notNull(),
    state: text('state'),
}, (t) => ({
    first: unique().on(t.name, t.state),
    second: unique('custom_name1').on(t.name, t.state),
}));
```

In SQLite unique constraints are the same as unique indexes. As long as you can specify a name for the unique index in SQLite - we will treat all unique constraints as unique indexes in internal implementation

```
// single column
const table = sqliteTable('table', {
    id: int('id').primaryKey(),
    name: text('name').notNull().unique(),
    state: text('state').unique('custom'),
    field: text('field').unique(),
});
// multiple columns
const table = sqliteTable('table', {
    id: int('id').primaryKey(),
    name: text('name').notNull(),
    state: text('state'),
}, (t) => ({
    first: unique().on(t.name, t.state),
    second: unique('custom').on(t.name, t.state),
}));
```


