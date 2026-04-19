---
title: "SQLite column types"
source: "https://orm.drizzle.team/docs/column-types/sqlite"
canonical_url: "https://orm.drizzle.team/docs/column-types/sqlite"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:00.179Z"
content_hash: "c61cbe69a987e76fa2c14635767238e6d31eba9c38e7264d08caa09d1d26007f"
menu_path: ["SQLite column types"]
section_path: []
nav_prev: {"path": "drizzle/docs/column-types/singlestore/index.md", "title": "SingleStore column types"}
nav_next: {"path": "drizzle/docs/docs/drizzle-config-file/index.md", "title": "404"}
---

Based on the official **[SQLite docs](https://www.sqlite.org/datatype3.html)**, each value stored in an SQLite database (or manipulated by the database engine) has one of the following storage classes `NULL`, `INTEGER`, `REAL`, `TEXT` and `BLOB`.

We have native support for all of them, yet if that’s not enough for you, feel free to create **[custom types](drizzle/docs/custom-types/index.md)**.

important

All examples in this part of the documentation do not use database column name aliases, and column names are generated from TypeScript keys.

You can use database aliases in column names if you want, and you can also use the `casing` parameter to define a mapping strategy for Drizzle.

You can read more about it [here](drizzle/docs/sql-schema-declaration/index.md#shape-your-data-schema)

### Integer[](#integer)

A signed integer, stored in `0`, `1`, `2`, `3`, `4`, `6`, or `8` bytes depending on the magnitude of the value.

```
import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	id: integer()
});

// you can customize integer mode to be number, boolean, timestamp, timestamp_ms
integer({ mode: 'number' })
integer({ mode: 'boolean' })
integer({ mode: 'timestamp_ms' })
integer({ mode: 'timestamp' }) // Date
```

```
CREATE TABLE `table` (
	`id` integer
);
```

```
// to make integer primary key auto increment
integer({ mode: 'number' }).primaryKey({ autoIncrement: true })
```

```
CREATE TABLE `table` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL
);
```

### Real[](#real)

A floating point value, stored as an `8-byte IEEE` floating point number.

```
import { real, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	real: real()
});
```

```
CREATE TABLE `table` (
	`real` real
);
```

### Text[](#text)

A text string, stored using the database encoding (`UTF-8`, `UTF-16BE` or `UTF-16LE`).

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won’t** check runtime values.

```
import { text, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	text: text()
});

// will be inferred as text: "value1" | "value2" | null
text({ enum: ["value1", "value2"] })
text({ mode: 'json' })
text({ mode: 'json' }).$type<{ foo: string }>()
```

```
CREATE TABLE `table` (
	`text` text
);
```

### Blob[](#blob)

A blob of data, stored exactly as it was input.

It’s recommended to use `text('', { mode: 'json' })` instead of `blob('', { mode: 'json' })`, because it supports JSON functions:

All JSON functions currently throw an error if any of their arguments are BLOBs because BLOBs are reserved for a future enhancement in which BLOBs will store the binary encoding for JSON.

See **[https://www.sqlite.org/json1.html](https://www.sqlite.org/json1.html)**.

```
import { blob, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	blob: blob()
});

blob()
blob({ mode: 'buffer' })
blob({ mode: 'bigint' })

blob({ mode: 'json' })
blob({ mode: 'json' }).$type<{ foo: string }>()
```

```
CREATE TABLE `table` (
	`blob` blob
);
```

You can specify `.$type<..>()` for blob inference, it **won’t** check runtime values. It provides compile time protection for default values, insert and select schemas.

```
// will be inferred as { foo: string }
json: blob({ mode: 'json' }).$type<{ foo: string }>();

// will be inferred as string[]
json: blob({ mode: 'json' }).$type<string[]>();

// won't compile
json: blob({ mode: 'json' }).$type<string[]>().default({});
```

### Boolean[](#boolean)

SQLite does not have native `boolean` data type, yet you can specify `integer` column to be in a `boolean` mode. This allows you to operate boolean values in your code and Drizzle stores them as 0 and 1 integer values in the database.

```
import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	id: integer({ mode: 'boolean' })
});
```

```
CREATE TABLE `table` (
	`id` integer
);
```

### Bigint[](#bigint)

Since there is no `bigint` data type in SQLite, Drizzle offers a special `bigint` mode for `blob` columns. This mode allows you to work with BigInt instances in your code, and Drizzle stores them as blob values in the database.

```
import { blob, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	id: blob({ mode: 'bigint' })
});
```

```
CREATE TABLE `table` (
	`id` blob
);
```

### Numeric[](#numeric)

```
import { blob, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	numeric: numeric(),
	numericNum: numeric({ mode: 'number' }),
	numericBig: numeric({ mode: 'bigint' }),
});
```

```
CREATE TABLE `table` (
	`numeric` numeric,
	`numericNum` numeric,
	`numericBig` numeric
);
```

### Customizing data type[](#customizing-data-type)

Every column builder has a `.$type()` method, which allows you to customize the data type of the column. This is useful, for example, with unknown or branded types.

```
type UserId = number & { __brand: 'user_id' };
type Data = {
	foo: string;
	bar: number;
};

const users = sqliteTable('users', {
  id: integer().$type<UserId>().primaryKey(),
  jsonField: blob().$type<Data>(),
});
```

### Not null[](#not-null)

`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.

```
const table = sqliteTable('table', { 
	numInt: integer().notNull() 
});
```

```
CREATE TABLE table (
	`numInt` integer NOT NULL
);
```

### Default value[](#default-value)

The `DEFAULT` clause specifies a default value to use for the column if no value is explicitly provided by the user when doing an `INSERT`. If there is no explicit `DEFAULT` clause attached to a column definition, then the default value of the column is `NULL`.

An explicit `DEFAULT` clause may specify that the default value is `NULL`, a string constant, a blob constant, a signed-number, or any constant expression enclosed in parentheses.

```
import { sql } from "drizzle-orm";
import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	int1: integer().default(42),
	int2: integer().default(sql`(abs(42))`)
});
```

```
CREATE TABLE `table` (
	`int1` integer DEFAULT 42,
	`int2` integer DEFAULT (abs(42))
);
```

A default value may also be one of the special case-independent keywords `CURRENT_TIME`, `CURRENT_DATE` or `CURRENT_TIMESTAMP`.

```
import { sql } from "drizzle-orm";
import { text, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable("table", {
  time: text().default(sql`(CURRENT_TIME)`),
  date: text().default(sql`(CURRENT_DATE)`),
  timestamp: text().default(sql`(CURRENT_TIMESTAMP)`),
});
```

```
CREATE TABLE `table` (
	`time` text DEFAULT (CURRENT_TIME),
	`date` text DEFAULT (CURRENT_DATE),
	`timestamp` text DEFAULT (CURRENT_TIMESTAMP)
);
```

When using `$default()` or `$defaultFn()`, which are simply different aliases for the same function, you can generate defaults at runtime and use these values in all insert queries. These functions can assist you in utilizing various implementations such as `uuid`, `cuid`, `cuid2`, and many more.

Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```
import { text, sqliteTable } from "drizzle-orm/sqlite-core";
import { createId } from '@paralleldrive/cuid2';

const table = sqliteTable('table', {
	id: text().$defaultFn(() => createId()),
});
```

When using `$onUpdate()` or `$onUpdateFn()`, which are simply different aliases for the same function, you can generate defaults at runtime and use these values in all update queries.

Adds a dynamic update value to the column. The function will be called when the row is updated, and the returned value will be used as the column value if none is provided. If no default (or $defaultFn) value is provided, the function will be called when the row is inserted as well, and the returned value will be used as the column value.

Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```
import { text, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
    alwaysNull: text().$type<string | null>().$onUpdate(() => null),
});
```
