---
title: "MySQL column types"
source: "https://orm.drizzle.team/docs/column-types/mysql"
canonical_url: "https://orm.drizzle.team/docs/column-types/mysql"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:40.801Z"
content_hash: "24f0f8c0b169e1101ccaf8e21ec45fc022e9ffc66aa470f2b5b08bbd2be96edf"
menu_path: ["MySQL column types"]
section_path: []
nav_prev: {"path": "drizzle/docs/column-types/singlestore/index.md", "title": "SingleStore column types"}
nav_next: {"path": "drizzle/docs/column-types/sqlite/index.md", "title": "SQLite column types"}
---

We have native support for all of them, yet if that’s not enough for you, feel free to create **[custom types](drizzle/docs/custom-types/index.md)**.

important

All examples in this part of the documentation do not use database column name aliases, and column names are generated from TypeScript keys.

You can use database aliases in column names if you want, and you can also use the `casing` parameter to define a mapping strategy for Drizzle.

You can read more about it [here](drizzle/docs/sql-schema-declaration/index.md#shape-your-data-schema)

### integer[](#integer)

A signed integer, stored in `0`, `1`, `2`, `3`, `4`, `6`, or `8` bytes depending on the magnitude of the value.

```
import { int, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	int: int()
});
```

```
CREATE TABLE `table` (
	`int` int
);
```

### tinyint[](#tinyint)

```
import { tinyint, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	tinyint: tinyint()
});
```

```
CREATE TABLE `table` (
	`tinyint` tinyint
);
```

### smallint[](#smallint)

```
import { smallint, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	smallint: smallint()
});
```

```
CREATE TABLE `table` (
	`smallint` smallint
);
```

### mediumint[](#mediumint)

```
import { mediumint, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	mediumint: mediumint()
});
```

```
CREATE TABLE `table` (
	`mediumint` mediumint
);
```

### bigint[](#bigint)

```
import { bigint, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	bigint: bigint({ mode: 'number' })
	bigintUnsigned: bigint({ mode: 'number', unsigned: true })
});

bigint('...', { mode: 'number' | 'bigint' });

// You can also specify unsigned option for bigint
bigint('...', { mode: 'number' | 'bigint', unsigned: true })
```

```
CREATE TABLE `table` (
	`bigint` bigint,
	`bigintUnsigned` bigint unsigned
);
```

We’ve omitted config of `M` in `bigint(M)`, since it indicates the display width of the numeric type

### real[](#real)

```
import { real, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	real: real()
});
```

```
CREATE TABLE `table` (
	`real` real
);
```

```
import { real, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	realPrecision: real({ precision: 1,}),
	realPrecisionScale: real({ precision: 1, scale: 1,}),
});
```

```
CREATE TABLE `table` (
	`realPrecision` real(1),
	`realPrecisionScale` real(1, 1)
);
```

### decimal[](#decimal)

```
import { decimal, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	decimal: decimal(),
	decimalNum: decimal({ scale: 30, mode: 'number' }),
	decimalBig: decimal({ scale: 30, mode: 'bigint' }),
});
```

```
CREATE TABLE `table` (
	`decimal` decimal,
	`decimalNum` decimal(30),
	`decimalBig` decimal(30)
);
```

```
import { decimal, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	decimalPrecision: decimal({ precision: 1,}),
	decimalPrecisionScale: decimal({ precision: 1, scale: 1,}),
});
```

```
CREATE TABLE `table` (
	`decimalPrecision` decimal(1),
	`decimalPrecisionScale` decimal(1, 1)
);
```

### double[](#double)

```
import { double, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	double: double('double')
});
```

```
CREATE TABLE `table` (
	`double` double
);
```

```
import { double, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	doublePrecision: double({ precision: 1,}),
	doublePrecisionScale: double({ precision: 1, scale: 1,}),
});
```

```
CREATE TABLE `table` (
	`doublePrecision` double(1),
	`doublePrecisionScale` double(1, 1)
);
```

### float[](#float)

```
import { float, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	float: float()
});
```

```
CREATE TABLE `table` (
	`float` float
);
```

### serial[](#serial)

`SERIAL` is an alias for `BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE`.

```
import { serial, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	serial: serial()
});
```

```
CREATE TABLE `table` (
	`serial` serial AUTO_INCREMENT
);
```

### binary[](#binary)

`BINARY(M)` stores a fixed-length byte string of exactly M bytes.  
On insert, shorter values are right-padded with `0x00` bytes to reach M bytes; on retrieval, no padding is stripped. All bytes—including trailing `0x00`—are significant in comparisons, `ORDER BY`, and `DISTINCT`

```
import { binary, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	binary: binary()
});
```

```
CREATE TABLE `table` (
	`binary` binary
);
```

### varbinary[](#varbinary)

`VARBINARY(M)` stores a variable-length byte string of exactly M bytes.  
On insert, shorter values are right-padded with `0x00` bytes to reach M bytes; on retrieval, no padding is stripped. All bytes—including trailing `0x00`—are significant in comparisons, `ORDER BY`, and `DISTINCT`

```
import { varbinary, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	varbinary: varbinary({ length: 2}),
});
```

```
CREATE TABLE `table` (
	`varbinary` varbinary(2)
);
```

### blob[](#blob)

IMPORTANT

Available starting from `drizzle-orm@1.0.0-beta.2`

A `BLOB` is a binary large object that can hold a variable amount of data.

```
import { blob, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	blob: blob()
});
```

```
CREATE TABLE `table` (
	`blob` blob
);
```

### tinyblob[](#tinyblob)

IMPORTANT

Available starting from `drizzle-orm@1.0.0-beta.2`

A `TINYBLOB` is a binary large object that can hold a variable amount of data.

```
import { tinyblob, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	tinyblob: tinyblob()
});
```

```
CREATE TABLE `table` (
	`tinyblob` tinyblob
);
```

### mediumblob[](#mediumblob)

IMPORTANT

Available starting from `drizzle-orm@1.0.0-beta.2`

A `MEDIUMBLOB` is a binary large object that can hold a variable amount of data.

```
import { mediumblob, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	mediumblob: mediumblob()
});
```

```
CREATE TABLE `table` (
	`mediumblob` mediumblob
);
```

### longblob[](#longblob)

IMPORTANT

Available starting from `drizzle-orm@1.0.0-beta.2`

A `LONGBLOB` is a binary large object that can hold a variable amount of data.

```
import { longblob, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	longblob: longblob()
});
```

```
CREATE TABLE `table` (
	`longblob` longblob
);
```

### char[](#char)

```
import { char, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	char: char(),
});
```

```
CREATE TABLE `table` (
	`char` char
);
```

### varchar[](#varchar)

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won’t** check runtime values.

```
import { varchar, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	varchar: varchar({ length: 2 }),
});

// will be inferred as text: "value1" | "value2" | null
varchar: varchar({ length: 6, enum: ["value1", "value2"] })
```

```
CREATE TABLE `table` (
	`varchar` varchar(2)
);
```

### text[](#text)

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won’t** check runtime values.

```
import { text, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	text: text(),
});

// will be inferred as text: "value1" | "value2" | null
text: text({ enum: ["value1", "value2"] });
```

```
CREATE TABLE `table` (
	`text` text
);
```

### boolean[](#boolean)

```
import { boolean, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	boolean: boolean(),
});
```

```
CREATE TABLE `table` (
	`boolean` boolean
);
```

### date[](#date)

```
import { boolean, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	date: date(),
});
```

```
CREATE TABLE `table` (
	`date` date
);
```

### datetime[](#datetime)

```
import { datetime, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	datetime: datetime(),
});

datetime('...', { mode: 'date' | "string"}),
datetime('...', { fsp : 0..6}),
```

```
CREATE TABLE `table` (
	`datetime` datetime
);
```

```
import { datetime, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	datetime: datetime({ mode: 'date', fsp: 6 }),
});
```

```
CREATE TABLE `table` (
	`datetime` datetime(6)
);
```

### time[](#time)

```
import { time, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	time: time(),
	timefsp: time({ fsp: 6 }),
});
	
time('...', { fsp: 0..6 }),
```

```
CREATE TABLE `table` (
	`time` time,
	`timefsp` time(6)
);
```

### year[](#year)

```
import { year, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	year: year(),
});
```

```
CREATE TABLE `table` (
	`year` year
);
```

### timestamp[](#timestamp)

```
import { timestamp, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	timestamp: timestamp(),
});

timestamp('...', { mode: 'date' | "string"}),
timestamp('...', { fsp : 0..6}),
```

```
CREATE TABLE `table` (
	`timestamp` timestamp
);
```

```
import { timestamp, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	timestamp: timestamp({ mode: 'date', fsp: 6 }),
});
```

```
CREATE TABLE `table` (
	`timestamp` timestamp(6)
);
```

```
import { timestamp, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	timestamp: timestamp().defaultNow(),
});
```

```
CREATE TABLE `table` (
	`timestamp` timestamp DEFAULT (now())
);
```

### json[](#json)

```
import { json, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	json: json(),
});
```

```
CREATE TABLE `table` (
	`json` json
);
```

You can specify `.$type<..>()` for json object inference, it **won’t** check runtime values. It provides compile time protection for default values, insert and select schemas.

```
// will be inferred as { foo: string }
json: json().$type<{ foo: string }>();

// will be inferred as string[]
json: json().$type<string[]>();

// won't compile
json: json().$type<string[]>().default({});
```

### enum[](#enum)

```
import { mysqlEnum, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	popularity: mysqlEnum(['unknown', 'known', 'popular']),
});
```

```
CREATE TABLE `table` (
	`popularity` enum('unknown','known','popular')
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

const users = mysqlTable('users', {
  id: int().$type<UserId>().primaryKey(),
  jsonField: json().$type<Data>(),
});
```

### Not null[](#not-null)

`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.

```
import { int, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	int: int().notNull(),
});
```

```
CREATE TABLE `table` (
	`int` int NOT NULL
);
```

### Default value[](#default-value)

The `DEFAULT` clause specifies a default value to use for the column if no value is explicitly provided by the user when doing an `INSERT`. If there is no explicit `DEFAULT` clause attached to a column definition, then the default value of the column is `NULL`.

An explicit `DEFAULT` clause may specify that the default value is `NULL`, a string constant, a blob constant, a signed-number, or any constant expression enclosed in parentheses.

```
import { int, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	int: int().default(3),
});
```

```
CREATE TABLE `table` (
	`int` int DEFAULT 3
);
```

When using `$default()` or `$defaultFn()`, which are simply different aliases for the same function, you can generate defaults at runtime and use these values in all insert queries. These functions can assist you in utilizing various implementations such as `uuid`, `cuid`, `cuid2`, and many more.

Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```
import { varchar, mysqlTable } from "drizzle-orm/mysql-core";
import { createId } from '@paralleldrive/cuid2';

const table = mysqlTable('table', {
	id: varchar({ length: 128 }).$defaultFn(() => createId()),
});
```

When using `$onUpdate()` or `$onUpdateFn()`, which are simply different aliases for the same function, you can generate defaults at runtime and use these values in all update queries.

Adds a dynamic update value to the column. The function will be called when the row is updated, and the returned value will be used as the column value if none is provided. If no default (or $defaultFn) value is provided, the function will be called when the row is inserted as well, and the returned value will be used as the column value.

Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```
import { text, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
    alwaysNull: text().$type<string | null>().$onUpdate(() => null),
});
```

### Primary key[](#primary-key)

```
import { int, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	int: int().primaryKey(),
});
```

```
CREATE TABLE `table` (
	`int` int PRIMARY KEY NOT NULL
);
```

### Auto increment[](#auto-increment)

```
import { int, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	int: int().autoincrement(),
});
```

```
CREATE TABLE `table` (
	`int` int AUTO_INCREMENT
);
```
