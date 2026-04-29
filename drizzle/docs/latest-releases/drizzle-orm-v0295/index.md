---
title: "Drizzle ORM - DrizzleORM v0.29.5 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0295"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0295"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:12:07.976Z"
content_hash: "dcdb8a9ef181a7e3360654de8738f5afd0dc1332742482c8d9c364e1ecd7d303"
menu_path: ["Drizzle ORM - DrizzleORM v0.29.5 release"]
section_path: []
content_language: "en"
nav_prev: {"path": "../drizzle-orm-v0294/index.md", "title": "Drizzle ORM - DrizzleORM v0.29.4 release"}
nav_next: {"path": "../drizzle-orm-v0300/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.0 release"}
---

DrizzleORM v0.29.5 release

Mar 6, 2024

## New Features

### 🎉 WITH UPDATE, WITH DELETE, WITH INSERT

You can now use `WITH` statements with [INSERT](../../insert/index.md#with-insert-clause), [UPDATE](../../update/index.md#with-update-clause) and [DELETE](../../delete/index.md#with-delete-clause) statements

Usage examples

```ts
const averageAmount = db.$with('average_amount').as(
	db.select({ value: sql`avg(${orders.amount})`.as('value') }).from(orders),
);

const result = await db
	.with(averageAmount)
	.delete(orders)
	.where(gt(orders.amount, sql`(select * from ${averageAmount})`))
	.returning({
		id: orders.id,
	});
```

```sql
with "average_amount" as (select avg("amount") as "value" from "orders") 
delete from "orders" 
where "orders"."amount" > (select * from "average_amount") 
returning "id";
```

For more examples for all statements, check docs:

-   [with insert docs](../../insert/index.md#with-insert-clause)
-   [with update docs](../../update/index.md#with-update-clause)
-   [with delete docs](../../delete/index.md#with-delete-clause)

### 🎉 Possibility to specify custom schema and custom name for migrations table

-   **Custom table for migrations**

By default, all information about executed migrations will be stored in the database inside the `__drizzle_migrations` table, and for PostgreSQL, inside the `drizzle` schema. However, you can configure where to store those records.

To add a custom table name for migrations stored inside your database, you should use the `migrationsTable` option

Usage example

```ts
await migrate(db, {
	migrationsFolder: './drizzle',
	migrationsTable: 'my_migrations',
});
```

-   **Custom schema for migrations**

> Works only with PostgreSQL databases

To add a custom schema name for migrations stored inside your database, you should use the `migrationsSchema` option

Usage example

```ts
await migrate(db, {
	migrationsFolder: './drizzle',
	migrationsSchema: 'custom',
});
```

### 🎉 SQLite Proxy bacth and Relational Queries support

You can find more information about SQLite proxy in [docs](../../get-started-sqlite/index.md#http-proxy).

-   You can now use `.query.findFirst` and `.query.findMany` syntax with sqlite proxy driver
    
-   SQLite Proxy supports batch requests, the same as it’s done for all other drivers. Check full [docs](../../batch-api/index.md)
    
    You will need to specify a specific callback for batch queries and handle requests to proxy server:
    

```ts
import { drizzle } from 'drizzle-orm/sqlite-proxy';

type ResponseType = { rows: any[][] | any[] }[];

const db = drizzle(
	async (sql, params, method) => {
		// single query logic
	},
	// new batch callback
	async (
		queries: {
			sql: string;
			params: any[];
			method: 'all' | 'run' | 'get' | 'values';
		}[],
	) => {
		try {
			const result: ResponseType = await axios.post(
				'http://localhost:3000/batch',
				{ queries },
			);

			return result;
		} catch (e: any) {
			console.error('Error from sqlite proxy server:', e);
			throw e;
		}
	},
);
```

And then you can use `db.batch([])` method, that will proxy all queries

> Response from the batch should be an array of raw values (an array within an array), in the same order as they were sent to the proxy server
