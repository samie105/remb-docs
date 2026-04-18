---
title: "SQL Delete"
source: "https://orm.drizzle.team/docs/delete"
canonical_url: "https://orm.drizzle.team/docs/delete"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:47.816Z"
content_hash: "bd33f0834c0dd7434edd885aa3adef0e6dfdf974ca6dc936795d0bb0e40fb577"
menu_path: ["SQL Delete"]
section_path: []
nav_prev: {"path": "drizzle/docs/update/index.md", "title": "SQL Update"}
nav_next: {"path": "drizzle/docs/operators/index.md", "title": "Filter and conditional operators"}
---

## SQL Delete

You can delete all rows in the table:

```
await db.delete(users);
```

And you can delete with filters and conditions:

```
await db.delete(users).where(eq(users.name, 'Dan'));
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
await db.delete(users).where(eq(users.name, 'Dan')).limit(2);
```

```
delete from "users" where "users"."name" = $1 limit $2;
```

### Order By[](#order-by)

Use `.orderBy()` to add `order by` clause to the query, sorting the results by the specified fields:

```
import { asc, desc } from 'drizzle-orm';

await db.delete(users).where(eq(users.name, 'Dan')).orderBy(users.name);
await db.delete(users).where(eq(users.name, 'Dan')).orderBy(desc(users.name));

// order by multiple fields
await db.delete(users).where(eq(users.name, 'Dan')).orderBy(users.name, users.name2);
await db.delete(users).where(eq(users.name, 'Dan')).orderBy(asc(users.name), desc(users.name2));
```

```
delete from "users" where "users"."name" = $1 order by "name";
delete from "users" where "users"."name" = $1 order by "name" desc;

delete from "users" where "users"."name" = $1 order by "name", "name2";
delete from "users" where "users"."name" = $1 order by "name" asc, "name2" desc;
```

### Returning[](#returning)

PostgreSQL

SQLite

MySQL

SingleStore

MSSQL

CockroachDB

You can delete a row and get it back in PostgreSQL and SQLite:

```
const deletedUser = await db.delete(users)
  .where(eq(users.name, 'Dan'))
  .returning();

// partial return
const deletedUserIds: { deletedId: number }[] = await db.delete(users)
  .where(eq(users.name, 'Dan'))
  .returning({ deletedId: users.id });
```

## Output[](#output)

MSSQL

You can insert a row and get it back in PostgreSQL and SQLite like such:

```
await db.insert(users).values({ name: "Dan" }).output();

// partial return
await db.insert(users).values({ name: "Partial Dan" }).output({ insertedId: users.id });
```

## WITH DELETE clause[](#with-delete-clause)

Using the `with` clause can help you simplify complex queries by splitting them into smaller subqueries called common table expressions (CTEs):

```
const averageAmount = db.$with('average_amount').as(
  db.select({ value: sql`avg(${orders.amount})`.as('value') }).from(orders)
);

const result = await db
	.with(averageAmount)
	.delete(orders)
	.where(gt(orders.amount, sql`(select * from ${averageAmount})`))
	.returning({
		id: orders.id
	});
```

```
with "average_amount" as (select avg("amount") as "value" from "orders") 
delete from "orders" 
where "orders"."amount" > (select * from "average_amount") 
returning "id"
```


