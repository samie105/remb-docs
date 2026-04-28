---
title: "Drizzle ORM - Count rows"
source: "https://orm.drizzle.team/docs/guides/count-rows"
canonical_url: "https://orm.drizzle.team/docs/guides/count-rows"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:58:05.750Z"
content_hash: "657ba768e52b4a0648cdd72d04924737aa8a626c821697405d659a5342df3b4c"
menu_path: ["Drizzle ORM - Count rows"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/guides/conditional-filters-in-query/index.md", "title": "Drizzle ORM - Conditional filters in query"}
nav_next: {"path": "drizzle/docs/guides/cursor-based-pagination/index.md", "title": "Drizzle ORM - SQL Cursor-based pagination"}
---

Drizzle | Count rows

To count all rows in table you can use `count()` function or `sql` operator like below:

```ts
import { count, sql } from 'drizzle-orm';
import { products } from './schema';

const db = drizzle(...);

await db.select({ count: count() }).from(products);

// Under the hood, the count() function casts its result to a number at runtime.
await db.select({ count: sql`count(*)`.mapWith(Number) }).from(products);
```

```ts
// result type
type Result = {
  count: number;
}[];
```

```sql
select count(*) from products;
```

```ts
import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

export const products = pgTable('products', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  discount: integer('discount'),
  price: integer('price').notNull(),
});
```

To count rows where the specified column contains non-NULL values you can use `count()` function with a column:

```ts
await db.select({ count: count(products.discount) }).from(products);
```

```ts
// result type
type Result = {
  count: number;
}[];
```

```sql
select count("discount") from products;
```

Drizzle has simple and flexible API, which lets you create your custom solutions. In PostgreSQL and MySQL `count()` function returns bigint, which is interpreted as string by their drivers, so it should be casted to integer:

```ts
import { AnyColumn, sql } from 'drizzle-orm';

const customCount = (column?: AnyColumn) => {
  if (column) {
    return sql<number>`cast(count(${column}) as integer)`; // In MySQL cast to unsigned integer
  } else {
    return sql<number>`cast(count(*) as integer)`; // In MySQL cast to unsigned integer
  }
};

await db.select({ count: customCount() }).from(products);
await db.select({ count: customCount(products.discount) }).from(products);
```

```sql
select cast(count(*) as integer) from products;
select cast(count("discount") as integer) from products;
```

In SQLite, `count()` result returns as integer.

```ts
import { sql } from 'drizzle-orm';

await db.select({ count: sql<number>`count(*)` }).from(products);
await db.select({ count: sql<number>`count(${products.discount})` }).from(products);
```

```sql
select count(*) from products;
select count("discount") from products;
```

IMPORTANT

By specifying `sql<number>`, you are telling Drizzle that the **expected** type of the field is `number`.  
If you specify it incorrectly (e.g. use `sql<string>` for a field that will be returned as a number), the runtime value won’t match the expected type. Drizzle cannot perform any type casts based on the provided type generic, because that information is not available at runtime.

If you need to apply runtime transformations to the returned value, you can use the [`.mapWith()`](drizzle/docs/sql/index.md#sqlmapwith) method.

To count rows that match a condition you can use `.where()` method:

```ts
import { count, gt } from 'drizzle-orm';

await db
  .select({ count: count() })
  .from(products)
  .where(gt(products.price, 100));
```

```sql
select count(*) from products where price > 100
```

This is how you can use `count()` function with joins and aggregations:

```ts
import { count, eq } from 'drizzle-orm';
import { countries, cities } from './schema';

// Count cities in each country
await db
  .select({
    country: countries.name,
    citiesCount: count(cities.id),
  })
  .from(countries)
  .leftJoin(cities, eq(countries.id, cities.countryId))
  .groupBy(countries.id)
  .orderBy(countries.name);
```

```sql
select countries.name, count("cities"."id") from countries
  left join cities on countries.id = cities.country_id
  group by countries.id
  order by countries.name;
```

```ts
import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

export const countries = pgTable('countries', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
});

export const cities = pgTable('cities', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  countryId: integer('country_id').notNull().references(() => countries.id),
});
```
