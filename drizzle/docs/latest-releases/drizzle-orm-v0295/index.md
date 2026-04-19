---
title: "Drizzle ORM - DrizzleORM v0.29.5 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0295"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0295"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:12:57.251Z"
content_hash: "105e9557ad3561a692da46bafbb07cfbb72e97d3c728d80c449d061dc6d43946"
menu_path: ["Drizzle ORM - DrizzleORM v0.29.5 release"]
section_path: []
nav_prev: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0294/index.md", "title": "Drizzle ORM - DrizzleORM v0.29.4 release"}
nav_next: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0300/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.0 release"}
---

DrizzleORM v0.29.5 release

Mar 6, 2024

## New Features

### 🎉 WITH UPDATE, WITH DELETE, WITH INSERT

You can now use `WITH` statements with [INSERT](drizzle/docs/insert/index.md#with-insert-clause), [UPDATE](drizzle/docs/update/index.md#with-update-clause) and [DELETE](drizzle/docs/delete/index.md#with-delete-clause) statements

Usage examples

```
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

```
with "average_amount" as (select avg("amount") as "value" from "orders") 
delete from "orders" 
where "orders"."amount" > (select * from "average_amount") 
returning "id";
```

For more examples for all statements, check docs:

*   [with insert docs](drizzle/docs/insert/index.md#with-insert-clause)
*   [with update docs](drizzle/docs/update/index.md#with-update-clause)
*   [with delete docs](drizzle/docs/delete/index.md#with-delete-clause)

### 🎉 Possibility to specify custom schema and custom name for migrations table

*   **Custom table for migrations**

By default, all information about executed migrations will be stored in the database inside the `__drizzle_migrations` table, and for PostgreSQL, inside the `drizzle` schema. However, you can configure where to store those records.

To add a custom table name for migrations stored inside your database, you should use the `migrationsTable` option

Usage example

```
await migrate(db, {
	migrationsFolder: './drizzle',
	migrationsTable: 'my_migrations',
});
```

*   **Custom schema for migrations**

> Works only with PostgreSQL databases

To add a custom schema name for migrations stored inside your database, you should use the `migrationsSchema` option

Usage example

```
await migrate(db, {
	migrationsFolder: './drizzle',
	migrationsSchema: 'custom',
});
```

### 🎉 SQLite Proxy bacth and Relational Queries support

You can find more information about SQLite proxy in [docs](drizzle/docs/get-started-sqlite/index.md#http-proxy).

*   You can now use `.query.findFirst` and `.query.findMany` syntax with sqlite proxy driver
    
*   SQLite Proxy supports batch requests, the same as it’s done for all other drivers. Check full [docs](drizzle/docs/batch-api/index.md)
    
    You will need to specify a specific callback for batch queries and handle requests to proxy server:
    

```
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
