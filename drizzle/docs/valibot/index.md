---
title: "valibot"
source: "https://orm.drizzle.team/docs/valibot"
canonical_url: "https://orm.drizzle.team/docs/valibot"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:26:11.416Z"
content_hash: "90815e1b5859f631aa41f4084e6fdf300643edb524d4d93a57dc10e137fe0b66"
menu_path: ["valibot"]
section_path: []
nav_prev: {"path": "drizzle/docs/zod/index.md", "title": "zod"}
nav_next: {"path": "drizzle/docs/typebox/index.md", "title": "typebox"}
---

WARNING

Starting from `drizzle-orm@1.0.0-beta.15`, `drizzle-valibot` has been deprecated in favor of first-class schema generation support within Drizzle ORM itself

You can still use `drizzle-valibot` package but all new update will be added to Drizzle ORM directly

### Install the dependencies[](#install-the-dependencies)

npm

yarn

pnpm

bun

```
npm i valibot
```

```
yarn add valibot
```

```
pnpm add valibot
```

```
bun add valibot
```

### Select schema[](#select-schema)

Defines the shape of data queried from the database - can be used to validate API responses.

```
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/valibot';
import { parse } from 'valibot';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userSelectSchema = createSelectSchema(users);

const rows = await db.select({ id: users.id, name: users.name }).from(users).limit(1);
const parsed: { id: number; name: string; age: number } = parse(userSelectSchema, rows[0]); // Error: `age` is not returned in the above query

const rows = await db.select().from(users).limit(1);
const parsed: { id: number; name: string; age: number } = parse(userSelectSchema, rows[0]); // Will parse successfully
```

Views and enums are also supported.

```
import { pgEnum } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/valibot';
import { parse } from 'valibot';

const roles = pgEnum('roles', ['admin', 'basic']);
const rolesSchema = createSelectSchema(roles);
const parsed: 'admin' | 'basic' = parse(rolesSchema, ...);

const usersView = pgView('users_view').as((qb) => qb.select().from(users).where(gt(users.age, 18)));
const usersViewSchema = createSelectSchema(usersView);
const parsed: { id: number; name: string; age: number } = parse(usersViewSchema, ...);
```

### Insert schema[](#insert-schema)

Defines the shape of data to be inserted into the database - can be used to validate API requests.

```
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createInsertSchema } from 'drizzle-orm/valibot';
import { parse } from 'valibot';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userInsertSchema = createInsertSchema(users);

const user = { name: 'John' };
const parsed: { name: string, age: number } = parse(userInsertSchema, user); // Error: `age` is not defined

const user = { name: 'Jane', age: 30 };
const parsed: { name: string, age: number } = parse(userInsertSchema, user); // Will parse successfully
await db.insert(users).values(parsed);
```

### Update schema[](#update-schema)

Defines the shape of data to be updated in the database - can be used to validate API requests.

```
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createUpdateSchema } from 'drizzle-orm/valibot';
import { parse } from 'valibot';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userUpdateSchema = createUpdateSchema(users);

const user = { id: 5, name: 'John' };
const parsed: { name?: string | undefined, age?: number | undefined } = parse(userUpdateSchema, user); // Error: `id` is a generated column, it can't be updated

const user = { age: 35 };
const parsed: { name?: string | undefined, age?: number | undefined } = parse(userUpdateSchema, user); // Will parse successfully
await db.update(users).set(parsed).where(eq(users.name, 'Jane'));
```

### Refinements[](#refinements)

Each create schema function accepts an additional optional parameter that you can used to extend, modify or completely overwite a field’s schema. Defining a callback function will extend or modify while providing a Valibot schema will overwrite it.

```
import { pgTable, text, integer, json } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/valibot';
import { parse, pipe, maxLength, object, string } from 'valibot';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  bio: text(),
  preferences: json()
});

const userSelectSchema = createSelectSchema(users, {
  name: (schema) => pipe(schema, maxLength(20)), // Extends schema
  bio: (schema) => pipe(schema, maxLength(1000)), // Extends schema before becoming nullable/optional
  preferences: object({ theme: string() }) // Overwrites the field, including its nullability
});

const parsed: {
  id: number;
  name: string,
  bio?: string | undefined;
  preferences: {
    theme: string;
  };
} = parse(userSelectSchema, ...);
```

### Data type reference[](#data-type-reference)

```
pg.boolean();

mysql.boolean();

sqlite.integer({ mode: 'boolean' });

// Schema
boolean();
```

```
pg.date({ mode: 'date' });
pg.timestamp({ mode: 'date' });

mysql.date({ mode: 'date' });
mysql.datetime({ mode: 'date' });
mysql.timestamp({ mode: 'date' });

sqlite.integer({ mode: 'timestamp' });
sqlite.integer({ mode: 'timestamp_ms' });

// Schema
date();
```

```
pg.date({ mode: 'string' });
pg.timestamp({ mode: 'string' });
pg.cidr();
pg.inet();
pg.interval();
pg.macaddr();
pg.macaddr8();
pg.numeric();
pg.text();
pg.sparsevec();
pg.time();

mysql.binary();
mysql.date({ mode: 'string' });
mysql.datetime({ mode: 'string' });
mysql.decimal();
mysql.time();
mysql.timestamp({ mode: 'string' });
mysql.varbinary();

sqlite.numeric();
sqlite.text({ mode: 'text' });

// Schema
string();
```

```
pg.bit({ dimensions: ... });

// Schema
pipe(string(), regex(/^[01]+$/), maxLength(dimensions));
```

```
pg.uuid();

// Schema
pipe(string(), uuid());
```

```
pg.char({ length: ... });

mysql.char({ length: ... });

// Schema
pipe(string(), length(length));
```

```
pg.varchar({ length: ... });

mysql.varchar({ length: ... });

sqlite.text({ mode: 'text', length: ... });

// Schema
pipe(string(), maxLength(length));
```

```
mysql.tinytext();

// Schema
pipe(string(), maxLength(255)); // unsigned 8-bit integer limit
```

```
mysql.text();

// Schema
pipe(string(), maxLength(65_535)); // unsigned 16-bit integer limit
```

```
mysql.mediumtext();

// Schema
pipe(string(), maxLength(16_777_215)); // unsigned 24-bit integer limit
```

```
mysql.longtext();

// Schema
pipe(string(), maxLength(4_294_967_295)); // unsigned 32-bit integer limit
```

```
pg.text({ enum: ... });
pg.char({ enum: ... });
pg.varchar({ enum: ... });

mysql.tinytext({ enum: ... });
mysql.mediumtext({ enum: ... });
mysql.text({ enum: ... });
mysql.longtext({ enum: ... });
mysql.char({ enum: ... });
mysql.varchar({ enum: ... });
mysql.mysqlEnum(..., ...);

sqlite.text({ mode: 'text', enum: ... });

// Schema
enum(enum);
```

```
mysql.tinyint();

// Schema
pipe(number(), minValue(-128), maxValue(127), integer()); // 8-bit integer lower and upper limit
```

```
mysql.tinyint({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(255), integer()); // unsigned 8-bit integer lower and upper limit
```

```
pg.smallint();
pg.smallserial();

mysql.smallint();

// Schema
pipe(number(), minValue(-32_768), maxValue(32_767), integer()); // 16-bit integer lower and upper limit
```

```
mysql.smallint({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(65_535), integer()); // unsigned 16-bit integer lower and upper limit
```

```
pg.real();

mysql.float();

// Schema
pipe(number(), minValue(-8_388_608), maxValue(8_388_607)); // 24-bit integer lower and upper limit
```

```
mysql.mediumint();

// Schema
pipe(number(), minValue(-8_388_608), maxValue(8_388_607), integer()); // 24-bit integer lower and upper limit
```

```
mysql.float({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(16_777_215)); // unsigned 24-bit integer lower and upper limit
```

```
mysql.mediumint({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(16_777_215), integer()); // unsigned 24-bit integer lower and upper limit
```

```
pg.integer();
pg.serial();

mysql.int();

// Schema
pipe(number(), minValue(-2_147_483_648), maxValue(2_147_483_647), integer()); // 32-bit integer lower and upper limit
```

```
mysql.int({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(4_294_967_295), integer()); // unsgined 32-bit integer lower and upper limit
```

```
pg.doublePrecision();

mysql.double();
mysql.real();

sqlite.real();

// Schema
pipe(number(), minValue(-140_737_488_355_328), maxValue(140_737_488_355_327)); // 48-bit integer lower and upper limit
```

```
mysql.double({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(281_474_976_710_655)); // unsigned 48-bit integer lower and upper limit
```

```
pg.bigint({ mode: 'number' });
pg.bigserial({ mode: 'number' });

mysql.bigint({ mode: 'number' });
mysql.bigserial({ mode: 'number' });

sqlite.integer({ mode: 'number' });

// Schema
pipe(number(), minValue(-9_007_199_254_740_991), maxValue(9_007_199_254_740_991), integer()); // Javascript min. and max. safe integers
```

```
mysql.serial();

// Schema
pipe(number(), minValue(0), maxValue(9_007_199_254_740_991), integer()); // Javascript max. safe integer
```

```
pg.bigint({ mode: 'bigint' });
pg.bigserial({ mode: 'bigint' });

mysql.bigint({ mode: 'bigint' });

sqlite.blob({ mode: 'bigint' });

// Schema
pipe(bigint(), minValue(-9_223_372_036_854_775_808n), maxValue(9_223_372_036_854_775_807n)); // 64-bit integer lower and upper limit
```

```
mysql.bigint({ mode: 'bigint', unsigned: true });

// Schema
pipe(bigint(), minValue(0n), maxValue(18_446_744_073_709_551_615n)); // unsigned 64-bit integer lower and upper limit
```

```
mysql.year();

// Schema
pipe(number(), minValue(1_901), maxValue(2_155), integer());
```

```
pg.geometry({ type: 'point', mode: 'tuple' });
pg.point({ mode: 'tuple' });

// Schema
tuple([number(), number()]);
```

```
pg.geometry({ type: 'point', mode: 'xy' });
pg.point({ mode: 'xy' });

// Schema
object({ x: number(), y: number() });
```

```
pg.halfvec({ dimensions: ... });
pg.vector({ dimensions: ... });

// Schema
pipe(array(number()), length(dimensions));
```

```
pg.line({ mode: 'abc' });

// Schema
object({ a: number(), b: number(), c: number() });
```

```
pg.line({ mode: 'tuple' });

// Schema
tuple([number(), number(), number()]);
```

```
pg.json();
pg.jsonb();

mysql.json();

sqlite.blob({ mode: 'json' });
sqlite.text({ mode: 'json' });

// Schema
union([union([string(), number(), boolean(), null_()]), array(any()), record(string(), any())]);
```

```
sqlite.blob({ mode: 'buffer' });

// Schema
custom<Buffer>((v) => v instanceof Buffer);
```

```
pg.dataType().array(...);

// Schema
pipe(array(baseDataTypeSchema), length(size));
```


