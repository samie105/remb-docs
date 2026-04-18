---
title: "Query performance"
source: "https://orm.drizzle.team/docs/perf-queries"
canonical_url: "https://orm.drizzle.team/docs/perf-queries"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:18:02.368Z"
content_hash: "3487e356829e68c954bb4f1372895c1d0b83173193cd856424f2ff29304f56c2"
menu_path: ["Query performance"]
section_path: []
nav_prev: {"path": "drizzle/docs/rqb/index.md", "title": "Drizzle Queries"}
nav_next: {"path": "drizzle/docs/perf-serverless/index.md", "title": "Drizzle Serverless performance"}
---

## Query performance

When it comes to **Drizzle** — we’re a thin TypeScript layer on top of SQL with almost 0 overhead and to make it actual 0, you can utilise our prepared statements API.

**When you run a query on the database, there are several things that happen:**

*   all the configurations of the query builder got concatenated to the SQL string
*   that string and params are sent to the database driver
*   driver compiles SQL query to the binary SQL executable format and sends it to the database

With prepared statements you do SQL concatenation once on the Drizzle ORM side and then database driver is able to reuse precompiled binary SQL instead of parsing query all the time. It has extreme performance benefits on large SQL queries.

Different database drivers support prepared statements in different ways and sometimes Drizzle ORM you can go [**faster than better-sqlite3 driver.**](https://twitter.com/_alexblokh/status/1593593415907909634)

## Prepared statement[](#prepared-statement)

PostgreSQL

MySQL

SQLite

SingleStore

```
const db = drizzle(...);

const prepared = db.select().from(customers).prepare("statement_name");

const res1 = await prepared.execute();
const res2 = await prepared.execute();
const res3 = await prepared.execute();
```

```
const db = drizzle(...);

const prepared = db.select().from(customers).prepare();

const res1 = await prepared.execute();
const res2 = await prepared.execute();
const res3 = await prepared.execute();
```

```
const db = drizzle(...);

const prepared = db.select().from(customers).prepare();

const res1 = prepared.all();
const res2 = prepared.all();
const res3 = prepared.all();
```

```
const db = drizzle(...);

const prepared = db.select().from(customers).prepare();

const res1 = await prepared.execute();
const res2 = await prepared.execute();
const res3 = await prepared.execute();
```

## Placeholder[](#placeholder)

Whenever you need to embed a dynamic runtime value - you can use the `sql.placeholder(...)` api

PostgreSQL

MySQL

SQLite

SingleStore

```
import { sql } from "drizzle-orm";

const p1 = db
  .select()
  .from(customers)
  .where(eq(customers.id, sql.placeholder('id')))
  .prepare("p1")

await p1.execute({ id: 10 }) // SELECT * FROM customers WHERE id = 10
await p1.execute({ id: 12 }) // SELECT * FROM customers WHERE id = 12

const p2 = db
  .select()
  .from(customers)
  .where(sql`lower(${customers.name}) like ${sql.placeholder('name')}`)
  .prepare("p2");

await p2.execute({ name: '%an%' }) // SELECT * FROM customers WHERE name ilike '%an%'
```

```
import { sql } from "drizzle-orm";

const p1 = db
  .select()
  .from(customers)
  .where(eq(customers.id, sql.placeholder('id')))
  .prepare()

await p1.execute({ id: 10 }) // SELECT * FROM customers WHERE id = 10
await p1.execute({ id: 12 }) // SELECT * FROM customers WHERE id = 12

const p2 = db
  .select()
  .from(customers)
  .where(sql`lower(${customers.name}) like ${sql.placeholder('name')}`)
  .prepare();

await p2.execute({ name: '%an%' }) // SELECT * FROM customers WHERE name ilike '%an%'
```

```
import { sql } from "drizzle-orm";

const p1 = db
  .select()
  .from(customers)
  .where(eq(customers.id, sql.placeholder('id')))
  .prepare()

p1.get({ id: 10 }) // SELECT * FROM customers WHERE id = 10
p1.get({ id: 12 }) // SELECT * FROM customers WHERE id = 12

const p2 = db
  .select()
  .from(customers)
  .where(sql`lower(${customers.name}) like ${sql.placeholder('name')}`)
  .prepare();

p2.all({ name: '%an%' }) // SELECT * FROM customers WHERE name ilike '%an%'
```

```
import { sql } from "drizzle-orm";

const p1 = db
  .select()
  .from(customers)
  .where(eq(customers.id, sql.placeholder('id')))
  .prepare()

await p1.execute({ id: 10 }) // SELECT * FROM customers WHERE id = 10
await p1.execute({ id: 12 }) // SELECT * FROM customers WHERE id = 12

const p2 = db
  .select()
  .from(customers)
  .where(sql`lower(${customers.name}) like ${sql.placeholder('name')}`)
  .prepare();

await p2.execute({ name: '%an%' }) // SELECT * FROM customers WHERE name ilike '%an%'
```

