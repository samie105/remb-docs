---
title: "SingleStore column types"
source: "https://orm.drizzle.team/docs/column-types/singlestore"
canonical_url: "https://orm.drizzle.team/docs/column-types/singlestore"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:25.445Z"
content_hash: "1e4c73767c4aaf282e14b494d302e8597fc42677b297eda6ef9ba75b9bdc2a4e"
menu_path: ["SingleStore column types"]
section_path: []
---
We have native support for all of them, yet if that’s not enough for you, feel free to create **[custom types](https://orm.drizzle.team/docs/custom-types)**.

important

All examples in this part of the documentation do not use database column name aliases, and column names are generated from TypeScript keys.

You can use database aliases in column names if you want, and you can also use the `casing` parameter to define a mapping strategy for Drizzle.

You can read more about it [here](https://orm.drizzle.team/docs/sql-schema-declaration#shape-your-data-schema)

### integer[](#integer)

A signed integer, stored in `0`, `1`, `2`, `3`, `4`, `6`, or `8` bytes depending on the magnitude of the value.

```
import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { tinyint, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { smallint, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { mediumint, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { bigint, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { real, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	real: real()
});
```

```
CREATE TABLE `table` (
	`real` real
);
```

```
import { real, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { decimal, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { decimal, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { double, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	double: double('double')
});
```

```
CREATE TABLE `table` (
	`double` double
);
```

```
import { double, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { float, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { serial, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	serial: serial()
});
```

```
CREATE TABLE `table` (
	`serial` serial AUTO_INCREMENT
);
```

### binary[](#binary)

```
import { binary, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	binary: binary()
});
```

```
CREATE TABLE `table` (
	`binary` binary
);
```

### varbinary[](#varbinary)

```
import { varbinary, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	varbinary: varbinary({ length: 2}),
});
```

```
CREATE TABLE `table` (
	`varbinary` varbinary(2)
);
```

### char[](#char)

```
import { char, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { varchar, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { text, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { boolean, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { boolean, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { datetime, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	datetime: datetime(),
});

datetime('...', { mode: 'date' | "string"}),
```

```
CREATE TABLE `table` (
	`datetime` datetime
);
```

### time[](#time)

```
import { time, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	time: time(),
});
```

```
CREATE TABLE `table` (
	`time` time
);
```

### year[](#year)

```
import { year, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { timestamp, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	timestamp: timestamp(),
});

timestamp('...', { mode: 'date' | "string"}),
```

```
CREATE TABLE `table` (
	`timestamp` timestamp
);
```

```
import { timestamp, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { json, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { singlestoreEnum, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	popularity: singlestoreEnum(['unknown', 'known', 'popular']),
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

const users = singlestoreTable('users', {
  id: int().$type<UserId>().primaryKey(),
  jsonField: json().$type<Data>(),
});
```

### Not null[](#not-null)

`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.

```
import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { varchar, singlestoreTable } from "drizzle-orm/singlestore-core";
import { createId } from '@paralleldrive/cuid2';

const table = singlestoreTable('table', {
	id: varchar({ length: 128 }).$defaultFn(() => createId()),
});
```

When using `$onUpdate()` or `$onUpdateFn()`, which are simply different aliases for the same function, you can generate defaults at runtime and use these values in all update queries.

Adds a dynamic update value to the column. The function will be called when the row is updated, and the returned value will be used as the column value if none is provided. If no default (or $defaultFn) value is provided, the function will be called when the row is inserted as well, and the returned value will be used as the column value.

Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```
import { text, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
    alwaysNull: text().$type<string | null>().$onUpdate(() => null),
});
```

### Primary key[](#primary-key)

```
import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
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
import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	int: int().autoincrement(),
});
```

```
CREATE TABLE `table` (
	`int` int AUTO_INCREMENT
);
```
