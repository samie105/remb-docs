---
title: "Drizzle ORM - Count rows"
source: "https://orm.drizzle.team/docs/guides/count-rows"
canonical_url: "https://orm.drizzle.team/docs/guides/count-rows"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:46.773Z"
content_hash: "08e8111e8fa33d94a0280aa38de55998701b135423b343d31655f44eb067c0f6"
menu_path: ["Drizzle ORM - Count rows"]
section_path: []
nav_prev: {"path": "drizzle/docs/guides/conditional-filters-in-query/index.md", "title": "Drizzle ORM - Conditional filters in query"}
nav_next: {"path": "drizzle/docs/guides/cursor-based-pagination/index.md", "title": "Drizzle ORM - SQL Cursor-based pagination"}
---

Drizzle | Count rows

PostgreSQL

MySQL

SQLite

To count all rows in table you can use `count()` function or `sql` operator like below:

index.ts

schema.ts

```
import { count, sql } from 'drizzle-orm';
import { products } from './schema';

const db = drizzle(...);

await db.select({ count: count() }).from(products);

// Under the hood, the count() function casts its result to a number at runtime.
await db.select({ count: sql`count(*)`.mapWith(Number) }).from(products);
```

```
// result type
type Result = {
  count: number;
}[];
```

```
select count(*) from products;
```

```
import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

export const products = pgTable('products', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  discount: integer('discount'),
  price: integer('price').notNull(),
});
```

To count rows where the specified column contains non-NULL values you can use `count()` function with a column:

```
await db.select({ count: count(products.discount) }).from(products);
```

```
// result type
type Result = {
  count: number;
}[];
```

```
select count("discount") from products;
```

Drizzle has simple and flexible API, which lets you create your custom solutions. In PostgreSQL and MySQL `count()` function returns bigint, which is interpreted as string by their drivers, so it should be casted to integer:

```
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

```
select cast(count(*) as integer) from products;
select cast(count("discount") as integer) from products;
```

In SQLite, `count()` result returns as integer.

```
import { sql } from 'drizzle-orm';

await db.select({ count: sql<number>`count(*)` }).from(products);
await db.select({ count: sql<number>`count(${products.discount})` }).from(products);
```

```
select count(*) from products;
select count("discount") from products;
```

IMPORTANT

By specifying `sql<number>`, you are telling Drizzle that the **expected** type of the field is `number`.  
If you specify it incorrectly (e.g. use `sql<string>` for a field that will be returned as a number), the runtime value won’t match the expected type. Drizzle cannot perform any type casts based on the provided type generic, because that information is not available at runtime.

If you need to apply runtime transformations to the returned value, you can use the [`.mapWith()`](drizzle/docs/sql/index.md#sqlmapwith) method.

To count rows that match a condition you can use `.where()` method:

```
import { count, gt } from 'drizzle-orm';

await db
  .select({ count: count() })
  .from(products)
  .where(gt(products.price, 100));
```

```
select count(*) from products where price > 100
```

This is how you can use `count()` function with joins and aggregations:

index.ts

schema.ts

```
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

```
select countries.name, count("cities"."id") from countries
  left join cities on countries.id = cities.country_id
  group by countries.id
  order by countries.name;
```

```
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


