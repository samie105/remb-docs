---
title: "Table schemas"
source: "https://orm.drizzle.team/docs/schemas"
canonical_url: "https://orm.drizzle.team/docs/schemas"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:22:52.497Z"
content_hash: "8e7199beb82d44e1793c3fdebe5e2153379c2c5e6b849a12eb2a419f6aeea1a6"
menu_path: ["Table schemas"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/views/index.md", "title": "Views"}
nav_next: {"path": "drizzle/docs/relations-v2/index.md", "title": "Drizzle relations"}
---

## Table schemas

If you declare an entity within a schema, query builder will prepend schema names in queries:  
`select * from "schema"."users"`

PostgreSQL

MySQL

SQLite

SingleStore

MSSQL

CockroachDB

```ts
import { serial, text, pgSchema } from "drizzle-orm/pg-core";

export const mySchema = pgSchema("my_schema");

export const colors = mySchema.enum('colors', ['red', 'green', 'blue']);

export const mySchemaUsers = mySchema.table('users', {
  id: serial('id').primaryKey(),
  name: text('name'),
  color: colors('color').default('red'),
});
```

```sql
CREATE SCHEMA "my_schema";

CREATE TYPE "my_schema"."colors" AS ENUM ('red', 'green', 'blue');

CREATE TABLE "my_schema"."users" (
  "id" serial PRIMARY KEY,
  "name" text,
  "color" "my_schema"."colors" DEFAULT 'red'
);
```

```ts
import { int, text, mysqlSchema } from "drizzle-orm/mysql-core";

export const mySchema = mysqlSchema("my_schema")

export const mySchemaUsers = mySchema.table("users", {
  id: int("id").primaryKey().autoincrement(),
  name: text("name"),
});
```

```sql
CREATE SCHEMA "my_schema";

CREATE TABLE "my_schema"."users" (
  "id" serial PRIMARY KEY,
  "name" text
);
```

SQLite does not have support for schemas 😕

```ts
import { int, text, singlestoreSchema } from "drizzle-orm/singlestore-core";

export const mySchema = singlestoreSchema("my_schema")

export const mySchemaUsers = mySchema.table("users", {
  id: int("id").primaryKey().autoincrement(),
  name: text("name"),
});
```

```sql
CREATE SCHEMA "my_schema";

CREATE TABLE "my_schema"."users" (
  "id" serial PRIMARY KEY,
  "name" text
);
```

```ts
import { int, text, mssqlSchema } from "drizzle-orm/mssql-core";

export const mySchema = mssqlSchema("my_schema")

export const mySchemaUsers = mySchema.table("users", {
  id: int().primaryKey(),
  name: text(),
});
```

```sql
CREATE SCHEMA [my_schema];

CREATE TABLE [my_schema].[users] (
  [id] int PRIMARY KEY,
  [name] text
);
```

```ts
import { int4, text, cockroachSchema } from "drizzle-orm/cockroach-core";

export const mySchema = cockroachSchema("my_schema");

export const colors = mySchema.enum('colors', ['red', 'green', 'blue']);

export const mySchemaUsers = mySchema.table('users', {
  id: int4().primaryKey(),
  name: text(),
  color: colors().default('red'),
});
```

```sql
CREATE SCHEMA "my_schema";

CREATE TYPE "my_schema"."colors" AS ENUM ('red', 'green', 'blue');

CREATE TABLE "my_schema"."users" (
  "id" serial PRIMARY KEY,
  "name" text,
  "color" "my_schema"."colors" DEFAULT 'red'
);
```
