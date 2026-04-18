---
title: "CockroachDB column types"
source: "https://orm.drizzle.team/docs/column-types/cockroach"
canonical_url: "https://orm.drizzle.team/docs/column-types/cockroach"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:20.282Z"
content_hash: "1e148204d47a33ddb5a0c3e5f918815c8c7d2728bf4b8013e55ee866bdb20221"
menu_path: ["CockroachDB column types"]
section_path: []
nav_prev: {"path": "drizzle/docs/column-types/mssql/index.md", "title": "MSSQL column types"}
nav_next: {"path": "drizzle/docs/column-types/singlestore/index.md", "title": "SingleStore column types"}
---

WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.2` and higher.

npm

yarn

pnpm

bun

```
npm i drizzle-orm@beta
npm i drizzle-kit@beta -D
```

```
yarn add drizzle-orm@beta
yarn add drizzle-kit@beta -D
```

```
pnpm add drizzle-orm@beta
pnpm add drizzle-kit@beta -D
```

```
bun add drizzle-orm@beta
bun add drizzle-kit@beta -D
```

We have native support for all of them, yet if that’s not enough for you, feel free to create **[custom types](drizzle/docs/custom-types/index.md)**.

important

All examples in this part of the documentation do not use database column name aliases, and column names are generated from TypeScript keys.

You can use database aliases in column names if you want, and you can also use the `casing` parameter to define a mapping strategy for Drizzle.

You can read more about it [here](drizzle/docs/sql-schema-declaration/index.md#shape-your-data-schema)

### bigint[](#bigint)

`int` `int8` `int64` `integer`

Signed 8-byte integer

If you’re expecting values above 2^31 but below 2^53, you can utilize `mode: 'number'` and deal with javascript number as opposed to bigint.

```
import { bigint, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	bigint: bigint({ mode: 'number' })
});

// will be inferred as `number`
bigint: bigint({ mode: 'number' })

// will be inferred as `bigint`
bigint: bigint({ mode: 'bigint' })
```

```
CREATE TABLE "table" (
	"bigint" bigint
);
```

```
import { sql } from "drizzle-orm";
import { bigint, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	bigint1: bigint().default(10),
	bigint2: bigint().default(sql`'10'::bigint`)
});
```

```
CREATE TABLE "table" (
	"bigint1" bigint DEFAULT 10,
	"bigint2" bigint DEFAULT '10'::bigint
);
```

### smallint[](#smallint)

`smallint` `int2`  
Small-range signed 2-byte integer

```
import { smallint, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	smallint: smallint()
});
```

```
CREATE TABLE "table" (
	"smallint" smallint
);
```

```
import { sql } from "drizzle-orm";
import { smallint, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	smallint1: smallint().default(10),
	smallint2: smallint().default(sql`'10'::smallint`)
});
```

```
CREATE TABLE "table" (
	"smallint1" smallint DEFAULT 10,
	"smallint2" smallint DEFAULT '10'::smallint
);
```

### int4[](#int4)

Signed 4-byte integer

```
import { int4, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	int4: int4()
});
```

```
CREATE TABLE "table" (
	"int4" int4
);
```

```
import { sql } from "drizzle-orm";
import { int4, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	int1: int4().default(10),
	int2: int4().default(sql`'10'::int4`)
});
```

```
CREATE TABLE "table" (
	"int1" int4 DEFAULT 10,
	"int2" int4 DEFAULT '10'::int4
);
```

### int8[](#int8)

An alias of **[bigint.](#bigint)**

### int2[](#int2)

An alias of **[smallint.](#smallint)**

### \---[](#---)

### bool[](#bool)

Cockroach provides the standard SQL type bool.

For more info please refer to the official Cockroach **[docs.](https://www.cockroachlabs.com/docs/stable/bool)**

```
import { bool, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	boolean: bool()
});
```

```
CREATE TABLE "table" (
	"boolean" bool
);
```

### string[](#string)

`text` `varchar`, `char`

The `STRING` data type stores a string of Unicode characters.

For PostgreSQL compatibility, CockroachDB supports the following STRING-related types and their aliases:

`VARCHAR` (and alias `CHARACTER VARYING`) `CHAR` (and alias `CHARACTER`) `NAME`

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/string)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won’t** check runtime values.

```
import { string, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
  stringColumn: string(), // equivalent to `text` PostgreSQL type
  stringColumn1: string({ length: 256 }), // equivalent to `varchar(256)` PostgreSQL type
});

// will be inferred as text: "value1" | "value2" | null
stringColumn: string({ enum: ["value1", "value2"] })
```

```
CREATE TABLE "table" (
	"stringColumn" string,
    "stringColumn1" string(256),
);
```

### text[](#text)

CockroachDB alias for `STRING`:

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/string)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won’t** check runtime values.

```
import { text, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
  text: text()
});

// will be inferred as text: "value1" | "value2" | null
text: text({ enum: ["value1", "value2"] })
```

```
CREATE TABLE "table" (
	"text" text
);
```

### varchar[](#varchar)

`character varying(n)` `varchar(n)`

`STRING` alias used to stay compatible with PostgreSQL

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/string)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won’t** check runtime values.

The `length` parameter is optional according to PostgreSQL docs.

```
import { varchar, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
  varchar1: varchar(),
  varchar2: varchar({ length: 256 }),
});

// will be inferred as text: "value1" | "value2" | null
varchar: varchar({ enum: ["value1", "value2"] }),
```

```
CREATE TABLE "table" (
	"varchar1" varchar,
	"varchar2" varchar(256)
);
```

### char[](#char)

`character(n)` `char(n)`

`STRING` alias used to stay compatible with PostgreSQL

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/string)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won’t** check runtime values.

The `length` parameter is optional according to PostgreSQL docs.

```
import { char, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
  char1: char(),
  char2: char({ length: 256 }),
});

// will be inferred as text: "value1" | "value2" | null
char: char({ enum: ["value1", "value2"] }),
```

```
CREATE TABLE "table" (
	"char1" char,
	"char2" char(256)
);
```

[https://www.cockroachlabs.com/docs/stable/float](https://www.cockroachlabs.com/docs/stable/float)

### decimal[](#decimal)

`numeric` `decimal` `dec` The DECIMAL data type stores exact, fixed-point numbers. This type is used when it is important to preserve exact precision, for example, with monetary data.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/decimal)**

```
import { decimal, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
  decimal1: decimal(),
  decimal2: decimal({ precision: 100 }),
  decimal3: decimal({ precision: 100, scale: 20 }),
  decimalNum: decimal({ mode: 'number' }),
  decimalBig: decimal({ mode: 'bigint' }),
});
```

```
CREATE TABLE "table" (
	"decimal1" decimal,
	"decimal2" decimal(100),
	"decimal3" decimal(100, 20),
	"decimalNum" decimal,
	"decimalBig" decimal
);
```

### numeric[](#numeric)

An alias of **[decimal.](#decimal)**

### float[](#float)

`float` `float8` `double precision`

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/float)**

```
import { sql } from "drizzle-orm";
import { float, cockroachTable } from "drizzle-orm/cockroach-core";  

const table = cockroachTable('table', {
	float1: float(),
	float2: float().default(10.10),
	float3: float().default(sql`'10.10'::float`),
});
```

```
CREATE TABLE "table" (
	"float1" float,
	"float2" float default 10.10,
	"float3" float default '10.10'::float
);
```

### real[](#real)

`real` `float4`  
Single precision floating-point number (4 bytes)

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/float)**

```
import { sql } from "drizzle-orm";
import { real, cockroachTable } from "drizzle-orm/cockroach-core";  

const table = cockroachTable('table', {
	real1: real(),
	real2: real().default(10.10),
	real3: real().default(sql`'10.10'::real`),
});
```

```
CREATE TABLE "table" (
	"real1" real,
	"real2" real default 10.10,
	"real3" real default '10.10'::real
);
```

### double precision[](#double-precision)

An alias of **[float.](#float)**

### jsonb[](#jsonb)

`jsonb`

The JSONB data type stores JSON (JavaScript Object Notation) data as a binary representation of the JSONB value, which eliminates whitespace, duplicate keys, and key ordering

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/jsonb)**

```
import { jsonb, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
	jsonb1: jsonb(),
	jsonb2: jsonb().default({ foo: "bar" }),
	jsonb3: jsonb().default(sql`'{foo: "bar"}'::jsonb`),
});
```

```
CREATE TABLE "table" (
	"jsonb1" jsonb,
	"jsonb2" jsonb default '{"foo": "bar"}'::jsonb,
	"jsonb3" jsonb default '{"foo": "bar"}'::jsonb
);
```

You can specify `.$type<..>()` for json object inference, it **won’t** check runtime values. It provides compile time protection for default values, insert and select schemas.

```
// will be inferred as { foo: string }
jsonb: jsonb().$type<{ foo: string }>();

// will be inferred as string[]
jsonb: jsonb().$type<string[]>();

// won't compile
jsonb: jsonb().$type<string[]>().default({});
```

### bit[](#bit)

`bit`

The BIT data types store bit arrays. With BIT, the length is fixed.

**Size**

The number of bits in a BIT value is determined as follows:

Type declaration

Logical size

BIT

1 bit

BIT(N)

N bits

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/bit)**

```
import { sql } from "drizzle-orm";
import { cockroachTable, bit } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	bit1: bit(),
	bit2: bit({ length: 15 }),
	bit3: bit({ length: 15 }).default('10011'),
	bit4: bit({ length: 15 }).default(sql`'10011'`)
});
```

```
CREATE TABLE "table" (
	"bit1" bit,
	"bit2" bit(15),
	"bit3" bit(15) DEFAULT '10011',
	"bit4" bit(15) DEFAULT '10011'
);
```

### varbit[](#varbit)

`varbit`

The VARBIT data types store bit arrays. With VARBIT, the length can be variable.

**Size**

The number of bits in a VARBIT value is determined as follows:

Type declaration

Logical size

VARBIT

variable with no maximum

VARBIT(N)

variable with a maximum of N bits

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/bit)**

```
import { sql } from "drizzle-orm";
import { cockroachTable, bit } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	varbit1: varbit(),
	varbit2: varbit({ length: 15 }),
	varbit3: varbit({ length: 15 }).default('10011'),
	varbit4: varbit({ length: 15 }).default(sql`'10011'`)
});
```

```
CREATE TABLE "table" (
	"varbit1" varbit,
	"varbit2" varbit(15),
	"varbit3" varbit(15) DEFAULT '10011',
	"varbit4" varbit(15) DEFAULT '10011'
);
```

### uuid[](#uuid)

`uuid`

The UUID (Universally Unique Identifier) data type stores a 128-bit value that is unique across both space and time.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/uuid)**

```
import { uuid, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
  uuid1: uuid(),
  uuid2: uuid().defaultRandom(),
  uuid3: uuid().default('a0ee-bc99-9c0b-4ef8-bb6d-6bb9-bd38-0a11')
});
```

```
CREATE TABLE "table" (
	"uuid1" uuid,
	"uuid2" uuid default gen_random_uuid(),
	"uuid3" uuid default 'a0ee-bc99-9c0b-4ef8-bb6d-6bb9-bd38-0a11'
);
```

### time[](#time)

`time` `timetz` `time with timezone` `time without timezone`

The `TIME` data type stores the time of day in UTC. The `TIMETZ` data type stores a time of day with a time zone offset from UTC.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/time)**

```
import { time, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
  time1: time(),
  time2: time({ withTimezone: true }),
  time3: time({ precision: 6 }),
  time4: time({ precision: 6, withTimezone: true })
});
```

```
CREATE TABLE "table" (
	"time1" time,
	"time2" time with timezone,
	"time3" time(6),
	"time4" time(6) with timezone
);
```

### timestamp[](#timestamp)

`timestamp` `timestamptz` `timestamp with time zone` `timestamp without time zone`

The TIMESTAMP and TIMESTAMPTZ data types store a date and time pair in UTC.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/timestamp)**

```
import { sql } from "drizzle-orm";
import { timestamp, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
  timestamp1: timestamp(),
	timestamp2: timestamp({ precision: 6, withTimezone: true }),
	timestamp3: timestamp().defaultNow(),
	timestamp4: timestamp().default(sql`now()`),
});
```

```
CREATE TABLE "table" (
	"timestamp1" timestamp,
	"timestamp2" timestamp (6) with time zone,
	"timestamp3" timestamp default now(),
	"timestamp4" timestamp default now()
);
```

You can specify either `date` or `string` infer modes:

```
// will infer as date
timestamp: timestamp({ mode: "date" }),

// will infer as string
timestamp: timestamp({ mode: "string" }),
```

> The `string` mode does not perform any mappings for you. This mode was added to Drizzle ORM to provide developers with the possibility to handle dates and date mappings themselves, depending on their needs. Drizzle will pass raw dates as strings `to` and `from` the database, so the behavior should be as predictable as possible and aligned 100% with the database behavior

> The `date` mode is the regular way to work with dates. Drizzle will take care of all mappings between the database and the JS Date object

### date[](#date)

`date`

The DATE data type stores a year, month, and day.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/date)**

```
import { date, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
	date: date(),
});
```

```
CREATE TABLE "table" (
	"date" date
);
```

You can specify either `date` or `string` infer modes:

```
// will infer as date
date: date({ mode: "date" }),

// will infer as string
date: date({ mode: "string" }),
```

### interval[](#interval)

`interval`

Stores a value that represents a span of time.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/interval)**

```
import { interval, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
	interval1: interval(),
  interval2: interval({ fields: 'day' }),
  interval3: interval({ fields: 'month' , precision: 6 }),
});
```

```
CREATE TABLE "table" (
	"interval1" interval,
	"interval2" interval day,
	"interval3" interval(6) month
);
```

### enum[](#enum)

`enum` `enumerated types`  
Enumerated (enum) types are data types that comprise a static, ordered set of values. They are equivalent to the enum types supported in a number of programming languages. An example of an enum type might be the days of the week, or a set of status values for a piece of data.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/enum)**

```
import { cockroachEnum, cockroachTable } from "drizzle-orm/cockroach-core";

export const moodEnum = cockroachEnum('mood', ['sad', 'ok', 'happy']);

export const table = cockroachTable('table', {
  mood: moodEnum(),
});
```

```
CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');

CREATE TABLE "table" (
	"mood" mood
);
```

### Customizing data type[](#customizing-data-type)

Every column builder has a `.$type()` method, which allows you to customize the data type of the column.

This is useful, for example, with unknown or branded types:

```
type UserId = number & { __brand: 'user_id' };
type Data = {
	foo: string;
	bar: number;
};

const users = cockroachTable('users', {
  id: int().$type<UserId>().primaryKey(),
  jsonField: json().$type<Data>(),
});
```

### Identity Columns[](#identity-columns)

To use this feature you would need to have `drizzle-orm@0.32.0` or higher and `drizzle-kit@0.23.0` or higher

PostgreSQL and CockroachDB supports identity columns as a way to automatically generate unique integer values for a column. These values are generated using sequences and can be defined using the GENERATED AS IDENTITY clause.

**Types of Identity Columns**

*   `GENERATED ALWAYS AS IDENTITY`: The database always generates a value for the column. Manual insertion or updates to this column are not allowed unless the OVERRIDING SYSTEM VALUE clause is used.
*   `GENERATED BY DEFAULT AS IDENTITY`: The database generates a value by default, but manual values can also be inserted or updated. If a manual value is provided, it will be used instead of the system-generated value.

**Usage example**

```
import { pgTable, integer, text } from 'drizzle-orm/pg-core' 

export const ingredients = pgTable("ingredients", {
  id: integer().primaryKey().generatedAlwaysAsIdentity({ startWith: 1000 }),
  name: text().notNull(),
  description: text(),
});
```

You can specify all properties available for sequences in the `.generatedAlwaysAsIdentity()` function. Additionally, you can specify custom names for these sequences

PostgreSQL docs [reference](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-PARMS-GENERATED-IDENTITY).

### Default value[](#default-value)

The `DEFAULT` clause specifies a default value to use for the column if no value is explicitly provided by the user when doing an `INSERT`. If there is no explicit `DEFAULT` clause attached to a column definition, then the default value of the column is `NULL`.

An explicit `DEFAULT` clause may specify that the default value is `NULL`, a string constant, a blob constant, a signed-number, or any constant expression enclosed in parentheses.

```
import { sql } from "drizzle-orm";
import { integer, pgTable, uuid } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	integer1: integer().default(42),
	integer2: integer().default(sql`'42'::integer`),
	uuid1: uuid().defaultRandom(),
	uuid2: uuid().default(sql`gen_random_uuid()`),
});
```

```
CREATE TABLE IF NOT EXISTS "table" (
	"integer1" integer DEFAULT 42,
	"integer2" integer DEFAULT '42'::integer,
	"uuid1" uuid DEFAULT gen_random_uuid(),
	"uuid2" uuid DEFAULT gen_random_uuid()
);
```

When using `$default()` or `$defaultFn()`, which are simply different aliases for the same function, you can generate defaults at runtime and use these values in all insert queries.

These functions can assist you in utilizing various implementations such as `uuid`, `cuid`, `cuid2`, and many more.

Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```
import { text, pgTable } from "drizzle-orm/pg-core";
import { createId } from '@paralleldrive/cuid2';

const table = pgTable('table', {
	id: text().$defaultFn(() => createId()),
});
```

When using `$onUpdate()` or `$onUpdateFn()`, which are simply different aliases for the same function, you can generate defaults at runtime and use these values in all update queries.

Adds a dynamic update value to the column. The function will be called when the row is updated, and the returned value will be used as the column value if none is provided. If no default (or $defaultFn) value is provided, the function will be called when the row is inserted as well, and the returned value will be used as the column value.

Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`

```
import { integer, timestamp, text, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	updateCounter: integer().default(sql`1`).$onUpdateFn((): SQL => sql`${table.update_counter} + 1`),
	updatedAt: timestamp({ mode: 'date', precision: 3 }).$onUpdate(() => new Date()),
    	alwaysNull: text().$type<string | null>().$onUpdate(() => null),
});
```

### Not null[](#not-null)

`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.

```
import { integer, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	integer: integer().notNull(),
});
```

```
CREATE TABLE IF NOT EXISTS "table" (
	"integer" integer NOT NULL
);
```

### Primary key[](#primary-key)

A primary key constraint indicates that a column, or group of columns, can be used as a unique identifier for rows in the table. This requires that the values be both unique and not null.

```
import { serial, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	id: serial().primaryKey(),
});
```

```
CREATE TABLE IF NOT EXISTS "table" (
	"id" serial PRIMARY KEY NOT NULL
);
```
