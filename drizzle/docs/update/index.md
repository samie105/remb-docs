---
title: "SQL Update"
source: "https://orm.drizzle.team/docs/update"
canonical_url: "https://orm.drizzle.team/docs/update"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:25:46.668Z"
content_hash: "302960a4af5accdcd59f41817a3781cb669fcf24d23a8781cf2ed198e454b47e"
menu_path: ["SQL Update"]
section_path: []
nav_prev: {"path": "drizzle/docs/insert/index.md", "title": "SQL Insert"}
nav_next: {"path": "drizzle/docs/delete/index.md", "title": "SQL Delete"}
---

## SQL Update

```
await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'));
```

The object that you pass to `update` should have keys that match column names in your database schema. Values of `undefined` are ignored in the object: to set a column to `null`, pass `null`. You can pass SQL as a value to be used in the update object, like this:

```
await db.update(users)
  .set({ updatedAt: sql`NOW()` })
  .where(eq(users.name, 'Dan'));
```

### Limit[](#limit)

PostgreSQL

MySQL

SQLite

SingleStore

MSSQL

CockroachDB

Use `.limit()` to add `limit` clause to the query - for example:

```
await db.update(usersTable).set({ verified: true }).limit(2);
```

```
update "users" set "verified" = $1 limit $2;
```

### Order By[](#order-by)

Use `.orderBy()` to add `order by` clause to the query, sorting the results by the specified fields:

```
import { asc, desc } from 'drizzle-orm';

await db.update(usersTable).set({ verified: true }).orderBy(usersTable.name);
await db.update(usersTable).set({ verified: true }).orderBy(desc(usersTable.name));

// order by multiple fields
await db.update(usersTable).set({ verified: true }).orderBy(usersTable.name, usersTable.name2);
await db.update(usersTable).set({ verified: true }).orderBy(asc(usersTable.name), desc(usersTable.name2));
```

```
update "users" set "verified" = $1 order by "name";
update "users" set "verified" = $1 order by "name" desc;

update "users" set "verified" = $1 order by "name", "name2";
update "users" set "verified" = $1 order by "name" asc, "name2" desc;
```

### Returning[](#returning)

PostgreSQL

SQLite

MySQL

SingleStore

MSSQL

CockroachDB

You can update a row and get it back in PostgreSQL and SQLite:

```
const updatedUserId: { updatedId: number }[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .returning({ updatedId: users.id });
```

### Output[](#output)

MSSQL

You can update a row and get back the row before updated and after:

```
type User = typeof users.$inferSelect;

const updatedUserId: User[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .output();
```

To return partial users after update:

```
const updatedUserId: { inserted: { updatedId: number }}[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .output({ inserted: { updatedId: users.id }});
```

To return rows that were in database before update:

```
type User = typeof users.$inferSelect;

const updatedUserId: { deleted: User }[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .output({ deleted: true });
```

To return both previous and new version on a row:

```
type User = typeof users.$inferSelect;

const updatedUserId: { deleted: User, inserted: User }[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .output({ deleted: true, inserted: true });
```

## `with update` clause[](#with-update-clause)

Using the `with` clause can help you simplify complex queries by splitting them into smaller subqueries called common table expressions (CTEs):

```
const averagePrice = db.$with('average_price').as(
        db.select({ value: sql`avg(${products.price})`.as('value') }).from(products)
);

const result = await db.with(averagePrice)
		.update(products)
		.set({
			cheap: true
		})
		.where(lt(products.price, sql`(select * from ${averagePrice})`))
		.returning({
			id: products.id
		});
```

```
with "average_price" as (select avg("price") as "value" from "products") 
update "products" set "cheap" = $1 
where "products"."price" < (select * from "average_price") 
returning "id"
```

## Update … from[](#update--from)

PostgreSQL

MySQL

SQLite

SingleStore

MSSQL

CockroachDB

As the SQLite documentation mentions:

> The UPDATE-FROM idea is an extension to SQL that allows an UPDATE statement to be driven by other tables in the database. The “target” table is the specific table that is being updated. With UPDATE-FROM you can join the target table against other tables in the database in order to help compute which rows need updating and what the new values should be on those rows

Similarly, the PostgreSQL documentation states:

> A table expression allowing columns from other tables to appear in the WHERE condition and update expressions

Drizzle also supports this feature starting from version `drizzle-orm@0.36.3`

```
await db
  .update(users)
  .set({ cityId: cities.id })
  .from(cities)
  .where(and(eq(cities.name, 'Seattle'), eq(users.name, 'John')))
```

```
update "users" set "city_id" = "cities"."id" 
from "cities" 
where ("cities"."name" = $1 and "users"."name" = $2)

-- params: [ 'Seattle', 'John' ]
```

You can also alias tables that are joined (in PG, you can also alias the updating table too).

```
const c = alias(cities, 'c');
await db
  .update(users)
  .set({ cityId: c.id })
  .from(c);
```

```
update "users" set "city_id" = "c"."id" 
from "cities" "c"
```

PostgreSQL

MySQL

SQLite

SingleStore

MSSQL

CockroachDB

In Postgres, you can also return columns from the joined tables.

```
const updatedUsers = await db
  .update(users)
  .set({ cityId: cities.id })
  .from(cities)
  .returning({ id: users.id, cityName: cities.name });
```

```
update "users" set "city_id" = "cities"."id" 
from "cities" 
returning "users"."id", "cities"."name"
```
