---
title: "SQL Select"
source: "https://orm.drizzle.team/docs/select"
canonical_url: "https://orm.drizzle.team/docs/select"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:21:08.531Z"
content_hash: "9ebe8500e3ad6fbb188c279785fde7f49818bf3e467691abe81912ea1c00ac9c"
menu_path: ["SQL Select"]
section_path: []
nav_prev: {"path": "drizzle/docs/rqb-v2/index.md", "title": "Drizzle Queries"}
nav_next: {"path": "drizzle/docs/insert/index.md", "title": "SQL Insert"}
---

## SQL Select

Drizzle provides you the most SQL-like way to fetch data from your database, while remaining type-safe and composable. It natively supports mostly every query feature and capability of every dialect, and whatever it doesn’t support yet, can be added by the user with the powerful [`sql`](drizzle/docs/sql/index.md) operator.

For the following examples, let’s assume you have a `users` table defined like this:

PostgreSQL

MySQL

SQLite

SingleStore

MSSQL

CockroachDB

```
import { pgTable, serial, text } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age'),
});
```

```
import { mysqlTable, serial, text, int } from 'drizzle-orm/mysql-core';

export const users = mysqlTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: int('age'),
});
```

```
import { sqliteTable, integer, text } from 'drizzle-orm/sqlite-core';

export const users = sqliteTable('users', {
  id: integer('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age'),
});
```

```
import { singlestoreTable, serial, text, int } from 'drizzle-orm/singlestore-core';

export const users = singlestoreTable('users', {
  id: int('id').primaryKey(),
  name: text('name').notNull(),
  age: int('age'),
});
```

```
import { mssqlTable, int, text } from 'drizzle-orm/mssql-core';

export const users = pgTable('users', {
  id: int().primaryKey(),
  name: text().notNull(),
  age: int(),
});
```

```
import { cockroachTable, int4, text } from 'drizzle-orm/cockroach-core';

export const users = pgTable('users', {
  id: int4().primaryKey(),
  name: text().notNull(),
  age: int4(),
});
```

### Basic select[](#basic-select)

Select all rows from a table including all columns:

```
const result = await db.select().from(users);
/*
  {
    id: number;
    name: string;
    age: number | null;
  }[]
*/
```

```
select "id", "name", "age" from "users";
```

Notice that the result type is inferred automatically based on the table definition, including columns nullability.

Drizzle always explicitly lists columns in the `select` clause instead of using `select *`.  
This is required internally to guarantee the fields order in the query result, and is also generally considered a good practice.

### Partial select[](#partial-select)

In some cases, you might want to select only a subset of columns from a table. You can do that by providing a selection object to the `.select()` method:

```
const result = await db.select({
  field1: users.id,
  field2: users.name,
}).from(users);

const { field1, field2 } = result[0];
```

```
select "id", "name" from "users";
```

Like in SQL, you can use arbitrary expressions as selection fields, not just table columns:

```
const result = await db.select({
  id: users.id,
  lowerName: sql<string>`lower(${users.name})`,
}).from(users);
```

```
select "id", lower("name") from "users";
```

IMPORTANT

By specifying `sql<string>`, you are telling Drizzle that the **expected** type of the field is `string`.  
If you specify it incorrectly (e.g. use `sql<number>` for a field that will be returned as a string), the runtime value won’t match the expected type. Drizzle cannot perform any type casts based on the provided type generic, because that information is not available at runtime.

If you need to apply runtime transformations to the returned value, you can use the [`.mapWith()`](drizzle/docs/sql/index.md#sqlmapwith) method.

Info

Starting from `v1.0.0-beta.1` you can use `.as()` for columns:

```
const result = await db.select({
  id: users.id,
  lowerName: users.name.as("lower"),
}).from(users);
```

### Conditional select[](#conditional-select)

You can have a dynamic selection object based on some condition:

```
async function selectUsers(withName: boolean) {
  return db
    .select({
      id: users.id,
      ...(withName ? { name: users.name } : {}),
    })
    .from(users);
}

const users = await selectUsers(true);
```

### Distinct select[](#distinct-select)

You can use `.selectDistinct()` instead of `.select()` to retrieve only unique rows from a dataset:

```
await db.selectDistinct().from(users).orderBy(users.id, users.name);

await db.selectDistinct({ id: users.id }).from(users).orderBy(users.id);
```

```
select distinct "id", "name" from "users" order by "id", "name";

select distinct "id" from "users" order by "id";
```

In PostgreSQL, you can also use the `distinct on` clause to specify how the unique rows are determined:

IMPORTANT

`distinct on` clause is only supported in PostgreSQL.

```
await db.selectDistinctOn([users.id]).from(users).orderBy(users.id);
await db.selectDistinctOn([users.name], { name: users.name }).from(users).orderBy(users.name);
```

```
select distinct on ("id") "id", "name" from "users" order by "id";
select distinct on ("name") "name" from "users" order by "name";
```

### Advanced select[](#advanced-select)

Powered by TypeScript, Drizzle APIs let you build your select queries in a variety of flexible ways.

Sneak peek of advanced partial select, for more detailed advanced usage examples - see our [dedicated guide](drizzle/docs/guides/include-or-exclude-columns/index.md).

IMPORTANT

`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](drizzle/docs/upgrade-v1/index.md))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`

  

example 1

example 2

example 3

example 4

```
import { getColumns, sql } from 'drizzle-orm';

await db.select({
    ...getColumns(posts),
    titleLength: sql<number>`length(${posts.title})`,
  }).from(posts);
```

```
import { getColumns } from 'drizzle-orm';

const { content, ...rest } = getColumns(posts); // exclude "content" column
await db.select({ ...rest }).from(posts); // select all other columns
```

```
await db.query.posts.findMany({
  columns: {
    title: true,
  },
});
```

```
await db.query.posts.findMany({
  columns: {
    content: false,
  },
});
```

### Filters[](#filters)

You can filter the query results using the [filter operators](drizzle/docs/operators/index.md) in the `.where()` method:

```
import { eq, lt, gte, ne } from 'drizzle-orm';

await db.select().from(users).where(eq(users.id, 42));
await db.select().from(users).where(lt(users.id, 42));
await db.select().from(users).where(gte(users.id, 42));
await db.select().from(users).where(ne(users.id, 42));
...
```

```
select "id", "name", "age" from "users" where "id" = 42;
select "id", "name", "age" from "users" where "id" < 42;
select "id", "name", "age" from "users" where "id" >= 42;
select "id", "name", "age" from "users" where "id" <> 42;
```

All filter operators are implemented using the [`sql`](drizzle/docs/sql/index.md) function. You can use it yourself to write arbitrary SQL filters, or build your own operators. For inspiration, you can check how the operators provided by Drizzle are [implemented](https://github.com/drizzle-team/drizzle-orm/blob/main/drizzle-orm/src/sql/expressions/conditions.ts).

```
import { sql } from 'drizzle-orm';

function equals42(col: Column) {
  return sql`${col} = 42`;
}

await db.select().from(users).where(sql`${users.id} < 42`);
await db.select().from(users).where(sql`${users.id} = 42`);
await db.select().from(users).where(equals42(users.id));
await db.select().from(users).where(sql`${users.id} >= 42`);
await db.select().from(users).where(sql`${users.id} <> 42`);
await db.select().from(users).where(sql`lower(${users.name}) = 'aaron'`);
```

```
select "id", "name", "age" from "users" where 'id' < 42;
select "id", "name", "age" from "users" where 'id' = 42;
select "id", "name", "age" from "users" where 'id' = 42;
select "id", "name", "age" from "users" where 'id' >= 42;
select "id", "name", "age" from "users" where 'id' <> 42;
select "id", "name", "age" from "users" where lower("name") = 'aaron';
```

All the values provided to filter operators and to the `sql` function are parameterized automatically. For example, this query:

```
await db.select().from(users).where(eq(users.id, 42));
```

will be translated to:

```
select "id", "name", "age" from "users" where "id" = $1; -- params: [42]
```

Inverting condition with a `not` operator:

```
import { eq, not, sql } from 'drizzle-orm';

await db.select().from(users).where(not(eq(users.id, 42)));
await db.select().from(users).where(sql`not ${users.id} = 42`);
```

```
select "id", "name", "age" from "users" where not ("id" = 42);
select "id", "name", "age" from "users" where not ("id" = 42);
```

You can safely alter schema, rename tables and columns and it will be automatically reflected in your queries because of template interpolation, as opposed to hardcoding column or table names when writing raw SQL.

### Combining filters[](#combining-filters)

You can logically combine filter operators with `and()` and `or()` operators:

```
import { eq, and, sql } from 'drizzle-orm';

await db.select().from(users).where(
  and(
    eq(users.id, 42),
    eq(users.name, 'Dan')
  )
);
await db.select().from(users).where(sql`${users.id} = 42 and ${users.name} = 'Dan'`);
```

```
select "id", "name", "age" from "users" where "id" = 42 and "name" = 'Dan';
select "id", "name", "age" from "users" where "id" = 42 and "name" = 'Dan';
```

```
import { eq, or, sql } from 'drizzle-orm';

await db.select().from(users).where(
  or(
    eq(users.id, 42), 
    eq(users.name, 'Dan')
  )
);
await db.select().from(users).where(sql`${users.id} = 42 or ${users.name} = 'Dan'`);
```

```
select "id", "name", "age" from "users" where "id" = 42 or "name" = 'Dan';
select "id", "name", "age" from "users" where "id" = 42 or "name" = 'Dan';
```

### Advanced filters[](#advanced-filters)

In combination with TypeScript, Drizzle APIs provide you powerful and flexible ways to combine filters in queries.

Sneak peek of conditional filtering, for more detailed advanced usage examples - see our [dedicated guide](drizzle/docs/guides/conditional-filters-in-query/index.md).

example 1

example 2

```
const searchPosts = async (term?: string) => {
  await db
    .select()
    .from(posts)
    .where(term ? ilike(posts.title, term) : undefined);
};
await searchPosts();
await searchPosts('AI');
```

```
const searchPosts = async (filters: SQL[]) => {
  await db
    .select()
    .from(posts)
    .where(and(...filters));
};
const filters: SQL[] = [];
filters.push(ilike(posts.title, 'AI'));
filters.push(inArray(posts.category, ['Tech', 'Art', 'Science']));
filters.push(gt(posts.views, 200));
await searchPosts(filters);
```

### Limit & offset[](#limit--offset)

MSSQL

Use `.limit()` and `.offset()` to add `limit` and `offset` clauses to the query - for example, to implement pagination:

```
await db.select().from(users).limit(10);
await db.select().from(users).limit(10).offset(10);
```

```
select "id", "name", "age" from "users" limit 10;
select "id", "name", "age" from "users" limit 10 offset 10;
```

### Fetch & offset[](#fetch--offset)

MSSQL

In MSSQL, `FETCH` and `OFFSET` are part of the `ORDER BY` clause, so they can only be used after the `.orderBy()` function

```
await db.select().from(users).orderBy(asc(users.id)).offset(5);
await db.select().from(users).orderBy(asc(users.id)).offset(5).fetch(10);
```

```
select [id], [name], [age] from [users] offset 5 rows;
select [id], [name], [age] from [users] offset 5 rows fetch next 10 rows;
```

### Top[](#top)

MSSQL

Limits the rows returned in a query result set to a specified number of rows

```
await db.select().from(users).top(10);
```

```
select top (10) [id], [name], [age] from [users];
```

### Order By[](#order-by)

Use `.orderBy()` to add `order by` clause to the query, sorting the results by the specified fields:

```
import { asc, desc } from 'drizzle-orm';

await db.select().from(users).orderBy(users.name);
await db.select().from(users).orderBy(desc(users.name));

// order by multiple fields
await db.select().from(users).orderBy(users.name, users.name2);
await db.select().from(users).orderBy(asc(users.name), desc(users.name2));
```

```
select "id", "name", "age" from "users" order by "name";
select "id", "name", "age" from "users" order by "name" desc;

select "id", "name", "age" from "users" order by "name", "name2";
select "id", "name", "age" from "users" order by "name" asc, "name2" desc;
```

Powered by TypeScript, Drizzle APIs let you implement all possible SQL pagination and sorting approaches.

Sneak peek of advanced pagination, for more detailed advanced usage examples - see our dedicated [limit offset pagination](drizzle/docs/guides/limit-offset-pagination/index.md) and [cursor pagination](drizzle/docs/guides/cursor-based-pagination/index.md) guides.

example 1

example 2

example 3

example 4

```
await db
  .select()
  .from(users)
  .orderBy(asc(users.id)) // order by is mandatory
  .limit(4) // the number of rows to return
  .offset(4); // the number of rows to skip
```

```
const getUsers = async (page = 1, pageSize = 3) => {
  await db.query.users.findMany({
    orderBy: (users, { asc }) => asc(users.id),
    limit: pageSize,
    offset: (page - 1) * pageSize,
  });
};
await getUsers();
```

```
const getUsers = async (page = 1, pageSize = 10) => {
   const sq = db
    .select({ id: users.id })
    .from(users)
    .orderBy(users.id)
    .limit(pageSize)
    .offset((page - 1) * pageSize)
    .as('subquery');
   await db.select().from(users).innerJoin(sq, eq(users.id, sq.id)).orderBy(users.id);
};
```

```
const nextUserPage = async (cursor?: number, pageSize = 3) => {
  await db
    .select()
    .from(users)
    .where(cursor ? gt(users.id, cursor) : undefined) // if cursor is provided, get rows after it
    .limit(pageSize) // the number of rows to return
    .orderBy(asc(users.id)); // ordering
};
// pass the cursor of the last row of the previous page (id)
await nextUserPage(3);
```

### WITH clause[](#with-clause)

Using the `with` clause can help you simplify complex queries by splitting them into smaller subqueries called common table expressions (CTEs):

```
const sq = db.$with('sq').as(db.select().from(users).where(eq(users.id, 42)));

const result = await db.with(sq).select().from(sq);
```

```
with sq as (select "id", "name", "age" from "users" where "id" = 42)
select "id", "name", "age" from sq;
```

You can also provide `insert`, `update` and `delete` statements inside `with`

```
const sq = db.$with('sq').as(
    db.insert(users).values({ name: 'John' }).returning(),
);

const result = await db.with(sq).select().from(sq);
```

```
with "sq" as (insert into "users" ("id", "name") values (default, 'John') returning "id", "name") 
select "id", "name" from "sq"
```

```
const sq = db.$with('sq').as(
    db.update(users).set({ age: 25 }).where(eq(users.name, 'John')).returning(),
);
const result = await db.with(sq).select().from(sq);
```

```
with "sq" as (update "users" set "age" = 25 where "users"."name" = 'John' returning "id", "name", "age") 
select "id", "name", "age" from "sq"
```

```
const sq = db.$with('sq').as(
  db.delete(users).where(eq(users.name, 'John')).returning(),
);

const result = await db.with(sq).select().from(sq);
```

```
with "sq" as (delete from "users" where "users"."name" = $1 returning "id", "name", "age") 
select "id", "name", "age" from "sq"
```

To select arbitrary SQL values as fields in a CTE and reference them in other CTEs or in the main query, you need to add aliases to them:

```

const sq = db.$with('sq').as(db.select({ 
  name: sql<string>`upper(${users.name})`.as('name'),
})
.from(users));

const result = await db.with(sq).select({ name: sq.name }).from(sq);
```

If you don’t provide an alias, the field type will become `DrizzleTypeError` and you won’t be able to reference it in other queries. If you ignore the type error and still try to use the field, you will get a runtime error, since there’s no way to reference that field without an alias.

### Select from subquery[](#select-from-subquery)

Just like in SQL, you can embed queries into other queries by using the subquery API:

```
const sq = db.select().from(users).where(eq(users.id, 42)).as('sq');
const result = await db.select().from(sq);
```

```
select "id", "name", "age" from (select "id", "name", "age" from "users" where "id" = 42) "sq";
```

Subqueries can be used in any place where a table can be used, for example in joins:

```
const sq = db.select().from(users).where(eq(users.id, 42)).as('sq');
const result = await db.select().from(users).leftJoin(sq, eq(users.id, sq.id));
```

```
select "users"."id", "users"."name", "users"."age", "sq"."id", "sq"."name", "sq"."age" from "users"
  left join (select "id", "name", "age" from "users" where "id" = 42) "sq"
    on "users"."id" = "sq"."id";
```

### Aggregations[](#aggregations)

With Drizzle, you can do aggregations using functions like `sum`, `count`, `avg`, etc. by grouping and filtering with `.groupBy()` and `.having()` respectfully, same as you would do in raw SQL:

```
import { gt } from 'drizzle-orm';

await db.select({
  age: users.age,
  count: sql<number>`cast(count(${users.id}) as int)`,
})
  .from(users)
  .groupBy(users.age);

await db.select({
  age: users.age,
  count: sql<number>`cast(count(${users.id}) as int)`,
})
  .from(users)
  .groupBy(users.age)
  .having(({ count }) => gt(count, 1));
```

```
select "age", cast(count("id") as int)
  from "users"
  group by "age";

select "age", cast(count("id") as int)
  from "users"
  group by "age"
  having cast(count("id") as int) > 1;
```

`cast(... as int)` is necessary because `count()` returns `bigint` in PostgreSQL and `decimal` in MySQL, which are treated as string values instead of numbers. Alternatively, you can use [`.mapWith(Number)`](drizzle/docs/sql/index.md#sqlmapwith) to cast the value to a number at runtime.

If you need count aggregation - we recommend using our [`$count`](drizzle/docs/select/index.md#count) API

### Aggregations helpers[](#aggregations-helpers)

Drizzle has a set of wrapped `sql` functions, so you don’t need to write `sql` templates for common cases in your app

Remember, aggregation functions are often used with the GROUP BY clause of the SELECT statement. So if you are selecting using aggregating functions and other columns in one query, be sure to use the `.groupBy` clause

**count**

Returns the number of values in `expression`.

```
import { count } from 'drizzle-orm'

await db.select({ value: count() }).from(users);
await db.select({ value: count(users.id) }).from(users);
```

```
select count("*") from "users";
select count("id") from "users";
```

```
// It's equivalent to writing
await db.select({ 
  value: sql`count('*'))`.mapWith(Number) 
}).from(users);

await db.select({ 
  value: sql`count(${users.id})`.mapWith(Number) 
}).from(users);
```

**countDistinct**

Returns the number of non-duplicate values in `expression`.

```
import { countDistinct } from 'drizzle-orm'

await db.select({ value: countDistinct(users.id) }).from(users);
```

```
select count(distinct "id") from "users";
```

```
// It's equivalent to writing
await db.select({ 
  value: sql`count(${users.id})`.mapWith(Number) 
}).from(users);
```

**avg**

Returns the average (arithmetic mean) of all non-null values in `expression`.

```
import { avg } from 'drizzle-orm'

await db.select({ value: avg(users.id) }).from(users);
```

```
select avg("id") from "users";
```

```
// It's equivalent to writing
await db.select({ 
  value: sql`avg(${users.id})`.mapWith(String) 
}).from(users);
```

**avgDistinct**

Returns the average (arithmetic mean) of all non-null values in `expression`.

```
import { avgDistinct } from 'drizzle-orm'

await db.select({ value: avgDistinct(users.id) }).from(users);
```

```
select avg(distinct "id") from "users";
```

```
// It's equivalent to writing
await db.select({ 
  value: sql`avg(distinct ${users.id})`.mapWith(String) 
}).from(users);
```

**sum**

Returns the sum of all non-null values in `expression`.

```
import { sum } from 'drizzle-orm'

await db.select({ value: sum(users.id) }).from(users);
```

```
select sum("id") from "users";
```

```
// It's equivalent to writing
await db.select({ 
  value: sql`sum(${users.id})`.mapWith(String) 
}).from(users);
```

**sumDistinct**

Returns the sum of all non-null and non-duplicate values in `expression`.

```
import { sumDistinct } from 'drizzle-orm'

await db.select({ value: sumDistinct(users.id) }).from(users);
```

```
select sum(distinct "id") from "users";
```

```
// It's equivalent to writing
await db.select({ 
  value: sql`sum(distinct ${users.id})`.mapWith(String) 
}).from(users);
```

**max**

Returns the maximum value in `expression`.

```
import { max } from 'drizzle-orm'

await db.select({ value: max(users.id) }).from(users);
```

```
select max("id") from "users";
```

```
// It's equivalent to writing
await db.select({ 
  value: sql`max(${expression})`.mapWith(users.id) 
}).from(users);
```

**min**

Returns the minimum value in `expression`.

```
import { min } from 'drizzle-orm'

await db.select({ value: min(users.id) }).from(users);
```

```
select min("id") from "users";
```

```
// It's equivalent to writing
await db.select({ 
  value: sql`min(${users.id})`.mapWith(users.id) 
}).from(users);
```

A more advanced example:

```
const orders = sqliteTable('order', {
  id: integer('id').primaryKey(),
  orderDate: integer('order_date', { mode: 'timestamp' }).notNull(),
  requiredDate: integer('required_date', { mode: 'timestamp' }).notNull(),
  shippedDate: integer('shipped_date', { mode: 'timestamp' }),
  shipVia: integer('ship_via').notNull(),
  freight: numeric('freight').notNull(),
  shipName: text('ship_name').notNull(),
  shipCity: text('ship_city').notNull(),
  shipRegion: text('ship_region'),
  shipPostalCode: text('ship_postal_code'),
  shipCountry: text('ship_country').notNull(),
  customerId: text('customer_id').notNull(),
  employeeId: integer('employee_id').notNull(),
});

const details = sqliteTable('order_detail', {
  unitPrice: numeric('unit_price').notNull(),
  quantity: integer('quantity').notNull(),
  discount: numeric('discount').notNull(),
  orderId: integer('order_id').notNull(),
  productId: integer('product_id').notNull(),
});

db
  .select({
    id: orders.id,
    shippedDate: orders.shippedDate,
    shipName: orders.shipName,
    shipCity: orders.shipCity,
    shipCountry: orders.shipCountry,
    productsCount: sql<number>`cast(count(${details.productId}) as int)`,
    quantitySum: sql<number>`sum(${details.quantity})`,
    totalPrice: sql<number>`sum(${details.quantity} * ${details.unitPrice})`,
  })
  .from(orders)
  .leftJoin(details, eq(orders.id, details.orderId))
  .groupBy(orders.id)
  .orderBy(asc(orders.id))
  .all();
```

### $count[](#count)

`db.$count()` is a utility wrapper of `count(*)`, it is a very flexible operator which can be used as is or as a subquery, more details in our [GitHub discussion](https://github.com/drizzle-team/drizzle-orm/discussions/3119).

```
const count = await db.$count(users);
//    ^? number

const count = await db.$count(users, eq(users.name, "Dan")); // works with filters
```

```
select count(*) from "users";
select count(*) from "users" where "name" = 'Dan';
```

It is exceptionally useful in [subqueries](drizzle/docs/select/index.md#select-from-subquery):

```
const users = await db.select({
  ...users,
  postsCount: db.$count(posts, eq(posts.authorId, users.id)),
}).from(users);
```

usage example with [relational queries](drizzle/docs/rqb/index.md)

```
const users = await db.query.users.findMany({
  extras: {
    postsCount: db.$count(posts, eq(posts.authorId, users.id)),
  },
});
```

### Iterator[](#iterator)

MySQL

PostgreSQL\[WIP\]

SQLite\[WIP\]

SingleStore\[WIP\]

MSSQL

CockroachDB\[WIP\]

If you need to return a very large amount of rows from a query and you don’t want to load them all into memory, you can use `.iterator()` to convert the query into an async iterator:

```
const iterator = await db.select().from(users).iterator();

for await (const row of iterator) {
  console.log(row);
}
```

It also works with prepared statements:

```
const query = await db.select().from(users).prepare();
const iterator = await query.iterator();

for await (const row of iterator) {
  console.log(row);
}
```

### Use Index[](#use-index)

The `USE INDEX` hint suggests to the optimizer which indexes to consider when processing the query. The optimizer is not forced to use these indexes but will prioritize them if they are suitable.

MySQL

PostgreSQL

SQLite

SingleStore

MSSQL

CockroachDB

```
export const users = mysqlTable('users', {
	id: int('id').primaryKey(),
	name: varchar('name', { length: 100 }).notNull(),
}, () => [usersTableNameIndex]);

const usersTableNameIndex = index('users_name_index').on(users.name);

await db.select()
  .from(users, { useIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```

You can also use this option on any join you want

```
await db.select()
  .from(users)
  .leftJoin(posts, eq(posts.userId, users.id), { useIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```

### Ignore Index[](#ignore-index)

The `IGNORE INDEX` hint tells the optimizer to avoid using specific indexes for the query. MySQL will consider all other indexes (if any) or perform a full table scan if necessary.

MySQL

PostgreSQL

SQLite

SingleStore

MSSQL

CockroachDB

```
export const users = mysqlTable('users', {
	id: int('id').primaryKey(),
	name: varchar('name', { length: 100 }).notNull(),
}, () => [usersTableNameIndex]);

const usersTableNameIndex = index('users_name_index').on(users.name);

await db.select()
  .from(users, { ignoreIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```

You can also use this option on any join you want

```
await db.select()
  .from(users)
  .leftJoin(posts, eq(posts.userId, users.id), { useIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```

### Force Index[](#force-index)

The `FORCE INDEX` hint forces the optimizer to use the specified index(es) for the query. If the specified index cannot be used, MySQL will not fall back to other indexes; it might resort to a full table scan instead.

MySQL

PostgreSQL

SQLite

SingleStore

MSSQL

CockroachDB

```
export const users = mysqlTable('users', {
	id: int('id').primaryKey(),
	name: varchar('name', { length: 100 }).notNull(),
}, () => [usersTableNameIndex]);

const usersTableNameIndex = index('users_name_index').on(users.name);

await db.select()
  .from(users, { forceIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```

You can also use this option on any join you want

```
await db.select()
  .from(users)
  .leftJoin(posts, eq(posts.userId, users.id), { useIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```


