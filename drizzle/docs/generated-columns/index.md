---
title: "Generated Columns"
source: "https://orm.drizzle.team/docs/generated-columns"
canonical_url: "https://orm.drizzle.team/docs/generated-columns"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:39:14.764Z"
content_hash: "0f60104a461796722f70acb5c6ab03255df5bc84fe1ae2ece16e91a9e0e5705c"
menu_path: ["Generated Columns"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/set-operations/index.md", "title": "Set Operations"}
nav_next: {"path": "drizzle/docs/transactions/index.md", "title": "Transactions"}
---

#### Database side[](#database-side)

**Types**: `STORED` only

**How It Works**

-   Automatically computes values based on other columns during insert or update.

**Capabilities**

-   Simplifies data access by precomputing complex expressions.
-   Enhances query performance with index support on generated columns.

**Limitations**

-   Cannot specify default values.
-   Expressions cannot reference other generated columns or include subqueries.
-   Schema changes required to modify generated column expressions.
-   Cannot directly use in primary keys, foreign keys, or unique constraints

For more info, please check [PostgreSQL](https://www.postgresql.org/docs/current/ddl-generated-columns.html) docs

#### Drizzle side[](#drizzle-side)

In Drizzle you can specify `.generatedAlwaysAs()` function on any column type and add a supported sql query, that will generate this column data for you.

#### Features[](#features)

This function can accept generated expression in 2 ways:

IMPORTANT

What was changed starting from 1.0.0-beta.12 version

In previous versions, `.generatedAlwaysAs()` also accepted literals as expressions.

**`string`**

```ts
export const test = pgTable("test", {
    generatedName: text("gen_name").generatedAlwaysAs(`'hello world!'`),
});
```

```sql
CREATE TABLE "test" (
    "gen_name" text GENERATED ALWAYS AS ('hello world!') STORED
);
```

**`sql`** tag - if you want drizzle to escape some values for you

```ts
export const test = pgTable("test", {
    generatedName: text("gen_name").generatedAlwaysAs(sql`'hello "world"!'`),
});
```

```sql
CREATE TABLE "test" (
    "gen_name" text GENERATED ALWAYS AS ('hello "world"!') STORED
);
```

**`callback`** - if you need to reference columns from a table

```ts
export const test = pgTable("test", {
    name: text("first_name"),
    generatedName: text("gen_name").generatedAlwaysAs(
      (): SQL => sql`'hi, ' || ${test.name} || '!'`
    ),
});
```

```sql
CREATE TABLE "test" (
    "first_name" text,
    "gen_name" text GENERATED ALWAYS AS ('hi, ' || "test"."first_name" || '!') STORED
);
```

**Example** generated columns with full-text search

```typescript
import { SQL, sql } from "drizzle-orm";
import { customType, index, integer, pgTable, text } from "drizzle-orm/pg-core";

const tsVector = customType<{ data: string }>({
  dataType() {
    return "tsvector";
  },
});

export const test = pgTable(
  "test",
  {
    id: integer("id").primaryKey().generatedAlwaysAsIdentity(),
    content: text("content"),
    contentSearch: tsVector("content_search", {
      dimensions: 3,
    }).generatedAlwaysAs(
      (): SQL => sql`to_tsvector('english', ${test.content})`
    ),
  },
  (t) => [
    index("idx_content_search").using("gin", t.contentSearch)
  ]
);
```

```sql
CREATE TABLE "test" (
	"id" integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY (sequence name "test_id_seq" INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START WITH 1 CACHE 1),
	"content" text,
	"content_search" "tsvector" GENERATED ALWAYS AS (to_tsvector('english', "test"."content")) STORED
);
--> statement-breakpoint
CREATE INDEX "idx_content_search" ON "test" USING gin ("content_search");
```

#### Database side[](#database-side-1)

**Types**: `STORED`, `VIRTUAL`

**How It Works**

-   Defined with an expression in the table schema.
-   Virtual columns are computed during read operations.
-   Stored columns are computed during write operations and stored.

**Capabilities**

-   Used in SELECT, INSERT, UPDATE, and DELETE statements.
-   Can be indexed, both virtual and stored.
-   Can specify NOT NULL and other constraints.

**Limitations**

-   Cannot directly insert or update values in a generated column

For more info, please check [MySQL Alter Generated](https://dev.mysql.com/doc/refman/8.4/en/alter-table-generated-columns.html) docs and [MySQL create generated](https://dev.mysql.com/doc/refman/8.4/en/create-table-generated-columns.html) docs

#### Drizzle side[](#drizzle-side-1)

In Drizzle you can specify `.generatedAlwaysAs()` function on any column type and add a supported sql query, that will generate this column data for you.

#### Features[](#features-1)

This function can accept generated expression in 2 ways:

IMPORTANT

What was changed starting from 1.0.0-beta.12 version

In previous versions, `.generatedAlwaysAs()` also accepted literals as expressions.

**`string`**

```ts
export const test = mysqlTable("test", {
    generatedName: text("gen_name").generatedAlwaysAs(`'hello world!'`),
});
```

```sql
CREATE TABLE "test" (
    "gen_name" text GENERATED ALWAYS AS ('hello world!') VIRTUAL
);
```

**`sql`** tag - if you want drizzle to escape some values for you

```ts
export const test = mysqlTable("test", {
    generatedName: text("gen_name").generatedAlwaysAs(sql`'hello "world"!'`),
});
```

```sql
CREATE TABLE `test` (
    `gen_name` text GENERATED ALWAYS AS ('hello "world"!') VIRTUAL
);
```

**`callback`** - if you need to reference columns from a table

```ts
export const test = mysqlTable("test", {
    name: text("first_name"),
    generatedName: text("gen_name").generatedAlwaysAs(
      (): SQL => sql`'hi, ' || ${test.name} || '!'`
    ),
});
```

```sql
CREATE TABLE `test` (
  `first_name` text,
  `gen_name` text GENERATED ALWAYS AS ('hi, ' || `test`.`first_name` || '!') VIRTUAL
);
```

#### Limitations[](#limitations)

Drizzle Kit will also have limitations for `push` command:

1.  You can’t change the generated constraint expression and type using `push`. Drizzle-kit will ignore this change. To make it work, you would need to `drop the column`, `push`, and then `add a column with a new expression`. This was done due to the complex mapping from the database side, where the schema expression will be modified on the database side and, on introspection, we will get a different string. We can’t be sure if you changed this expression or if it was changed and formatted by the database. As long as these are generated columns and `push` is mostly used for prototyping on a local database, it should be fast to `drop` and `create` generated columns. Since these columns are `generated`, all the data will be restored
2.  `generate` should have no limitations

```typescript
export const users = mysqlTable("users", {
    id: int("id"),
    id2: int("id2"),
    name: text("name"),
    storedGenerated: text("stored_gen").generatedAlwaysAs(
      (): SQL => sql`concat(${users.name}, ' ', 'hello')`,
      { mode: "stored" }
    ),
    virtualGenerated: text("virtual_gen").generatedAlwaysAs(
      (): SQL => sql`concat(${users.name}, ' ', 'hello')`,
      { mode: "virtual" }
    ),
});
```

```sql
CREATE TABLE `users` (
  `id` int,
  `id2` int,
  `name` text,
  `stored_gen` text GENERATED ALWAYS AS (concat(`users`.`name`, ' ', 'hello')) STORED,
  `virtual_gen` text GENERATED ALWAYS AS (concat(`users`.`name`, ' ', 'hello')) VIRTUAL
);
```

#### Database side[](#database-side-2)

**Types**: `STORED`, `VIRTUAL`

**How It Works**

-   Defined with an expression in the table schema.
-   Virtual columns are computed during read operations.
-   Stored columns are computed during write operations and stored.

**Capabilities**

-   Used in SELECT, INSERT, UPDATE, and DELETE statements.
-   Can be indexed, both virtual and stored.
-   Can specify NOT NULL and other constraints.

**Limitations**

-   Cannot directly insert or update values in a generated column

For more info, please check [SQLite](https://www.sqlite.org/gencol.html) docs

#### Drizzle side[](#drizzle-side-2)

In Drizzle you can specify `.generatedAlwaysAs()` function on any column type and add a supported sql query, that will generate this column data for you.

#### Features[](#features-2)

This function can accept generated expression in 2 ways:

IMPORTANT

What was changed starting from 1.0.0-beta.12 version

In versions before 1.0.0-beta.12, `.generatedAlwaysAs()` also accepted literals as expressions.

**`string`**

```ts
export const test = sqliteTable("test", {
    id: int("id").primaryKey(),
    generatedName: text("gen_name").generatedAlwaysAs(`'hello world!'`),
});
```

```sql
CREATE TABLE `test` (
    `id` integer PRIMARY KEY,
    `gen_name` text GENERATED ALWAYS AS ('hello world!') VIRTUAL
);
```

**`sql`** tag - if you want drizzle to escape some values for you

```ts
export const test = sqliteTable("test", {
    id: int("id").primaryKey(),
    generatedName: text("gen_name").generatedAlwaysAs(sql`'hello "world"!'`),
});
```

```sql
CREATE TABLE `test` (
  `id` integer PRIMARY KEY,
  `gen_name` text GENERATED ALWAYS AS ('hello "world"!') VIRTUAL
);
```

**`callback`** - if you need to reference columns from a table

```ts
export const test = sqliteTable("test", {
    name: text("first_name"),
    generatedName: text("gen_name").generatedAlwaysAs(
      (): SQL => sql`'hi,' || ${test.name} || '!'`
    ),
});
```

```sql
CREATE TABLE `test` (
  `first_name` text,
  `gen_name` text GENERATED ALWAYS AS ('hi,' || "first_name" || '!') VIRTUAL
);
```

#### Limitations[](#limitations-1)

Drizzle Kit will also have limitations for `push` and `generate` command:

1.  You can’t change the generated constraint expression with the stored type in an existing table. You would need to delete this table and create it again. This is due to SQLite limitations for such actions. We will handle this case in future releases (it will involve the creation of a new table with data migration).
2.  You can’t add a `stored` generated expression to an existing column for the same reason as above. However, you can add a `virtual` expression to an existing column.
3.  You can’t change a `stored` generated expression in an existing column for the same reason as above. However, you can change a `virtual` expression.
4.  You can’t change the generated constraint type from `virtual` to `stored` for the same reason as above. However, you can change from `stored` to `virtual`.

```typescript
export const users = sqliteTable("users", {
  id: int("id"),
  name: text("name"),
  storedGenerated: text("stored_gen").generatedAlwaysAs(
    (): SQL => sql`${users.name} || 'hello'`,
    { mode: "stored" }
  ),
  virtualGenerated: text("virtual_gen").generatedAlwaysAs(
    (): SQL => sql`${users.name} || 'hello'`,
    { mode: "virtual" }
  ),
});
```

```sql
CREATE TABLE `users` (
    `id` integer,
    `name` text,
    `stored_gen` text GENERATED ALWAYS AS ("name" || 'hello') STORED,
    `virtual_gen` text GENERATED ALWAYS AS ("name" || 'hello') VIRTUAL
);
```

Work in Progress

#### Database side[](#database-side-3)

**Types**: `PERSISTED`, `VIRTUAL`

**How It Works**

-   Defined with an expression in the table schema.
-   Virtual columns are computed during read operations.
-   Persisted columns are computed during write operations and stored.

For more info, please check [MSSQL](https://learn.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table?view=sql-server-ver17) docs

#### Drizzle side[](#drizzle-side-3)

In Drizzle you can specify `.generatedAlwaysAs()` function on any column type and add a supported sql query, that will generate this column data for you.

#### Features[](#features-3)

This function can accept generated expression in 2 ways:

IMPORTANT

What was changed starting from 1.0.0-beta.12 version

In previous versions, `.generatedAlwaysAs()` also accepted literals as expressions.

**`string`**

```ts
export const test = mssqlTable("test", {
    generatedName: text("gen_name").generatedAlwaysAs(`'hello world!'`),
});
```

```sql
CREATE TABLE [test] (
    [gen_name] AS ('hello world!')
);
```

**`sql`** tag - if you want drizzle to escape some values for you

```ts
export const test = mssqlTable("test", {
    id: int("id"),
    generatedName: text("gen_name").generatedAlwaysAs(sql`hello "world"!`),
});
```

```sql
CREATE TABLE [test] (
    [id] int,
    [gen_name] AS ('hello "world"!') 
);
```

**`callback`** - if you need to reference columns from a table

```ts
export const test = mssqlTable("test", {
    name: text("first_name"),
    generatedName: text("gen_name").generatedAlwaysAs(
      (): SQL => sql`concat('hi,', ' ', ${test.name}, '!')`
    ),
});
```

```sql
CREATE TABLE [test] (
	[first_name] text,
	[gen_name] AS (concat('hi,', ' ', [test].[first_name], '!')) 
);
```

In Drizzle you can specify `.generatedAlwaysAs()` function on any column type and add a supported sql query, that will generate this column data for you.

#### Features[](#features-4)

This function can accept generated expression in 2 ways:

IMPORTANT

What was changed starting from 1.0.0-beta.12 version

In previous versions, `.generatedAlwaysAs()` also accepted literals as expressions.

**`string`**

```ts
export const test = cockroachTable("test", {
    generatedName: text("gen_name").generatedAlwaysAs(`'hello world!'`),
});
```

```sql
CREATE TABLE "test" (
	"gen_name" string GENERATED ALWAYS AS ('hello world!') STORED
);
```

**`sql`** tag - if you want drizzle to escape some values for you

```ts
export const test = cockroachTable("test", {
    generatedName: text("gen_name").generatedAlwaysAs(sql`'hello "world"!'`),
});
```

```sql
CREATE TABLE "test" (
    "gen_name" string GENERATED ALWAYS AS ('hello "world"!') STORED
);
```

**`callback`** - if you need to reference columns from a table

```ts
export const test = cockroachTable("test", {
    name: text("first_name"),
    generatedName: text("gen_name").generatedAlwaysAs(
      (): SQL => sql`'hi, ' || ${test.name} || '!'`
    ),
});
```

```sql
CREATE TABLE "test" (
	"first_name" string,
	"gen_name" string GENERATED ALWAYS AS ('hi, ' || "test"."first_name" || '!') STORED
);
```

**Example** generated columns with full-text search

```typescript
import { SQL, sql } from "drizzle-orm";
import { customType, index, int4, cockroachTable, text } from "drizzle-orm/cockroach-core";

const tsVector = customType<{ data: string }>({
  dataType() {
    return "tsvector";
  },
});

export const test = cockroachTable(
  "test",
  {
    id: int4().primaryKey().generatedAlwaysAsIdentity(),
    content: text("content"),
    contentSearch: tsVector("content_search", {
      dimensions: 3,
    }).generatedAlwaysAs(
      (): SQL => sql`to_tsvector('english', ${test.content})`
    ),
  },
  (t) => [
    index("idx_content_search").using("gin", t.contentSearch)
  ]
);
```

```sql
CREATE TABLE "test" (
	"id" int4 PRIMARY KEY GENERATED ALWAYS AS IDENTITY (INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START WITH 1 CACHE 1),
	"content" string,
	"content_search" tsvector GENERATED ALWAYS AS (to_tsvector('english', "test"."content")) STORED
);
CREATE INDEX "idx_content_search" ON "test" USING gin ("content_search");
```
