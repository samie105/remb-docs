---
title: "typebox-legacy"
source: "https://orm.drizzle.team/docs/typebox-legacy"
canonical_url: "https://orm.drizzle.team/docs/typebox-legacy"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:25:36.340Z"
content_hash: "1666f9c09951e067db095e8692f2271501c5198e9f25cad7a28a82eb8d72990f"
menu_path: ["typebox-legacy"]
section_path: []
nav_prev: {"path": "drizzle/docs/arktype/index.md", "title": "arktype"}
nav_next: {"path": "drizzle/docs/effect-schema/index.md", "title": "effect-schema"}
---

WARNING

Starting from `drizzle-orm@1.0.0-beta.15`, `drizzle-typebox` has been deprecated in favor of first-class schema generation support within Drizzle ORM itself

You can still use `drizzle-typebox` package but all new update will be added to Drizzle ORM directly

This version of `typebox` is legacy by using `@sinclair/typebox` package

### Install the dependencies[](#install-the-dependencies)

npm

yarn

pnpm

bun

```
npm i drizzle-orm @sinclair/typebox
```

```
yarn add drizzle-orm @sinclair/typebox
```

```
pnpm add drizzle-orm @sinclair/typebox
```

```
bun add drizzle-orm @sinclair/typebox
```

### Select schema[](#select-schema)

Defines the shape of data queried from the database - can be used to validate API responses.

```
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/typebox-legacy';
import { Value } from '@sinclair/typebox/value';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userSelectSchema = createSelectSchema(users);

const rows = await db.select({ id: users.id, name: users.name }).from(users).limit(1);
const parsed: { id: number; name: string; age: number } = Value.Parse(userSelectSchema, rows[0]); // Error: `age` is not returned in the above query

const rows = await db.select().from(users).limit(1);
const parsed: { id: number; name: string; age: number } = Value.Parse(userSelectSchema, rows[0]); // Will parse successfully
```

Views and enums are also supported.

```
import { pgEnum } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/typebox-legacy';
import { Value } from '@sinclair/typebox/value';

const roles = pgEnum('roles', ['admin', 'basic']);
const rolesSchema = createSelectSchema(roles);
const parsed: 'admin' | 'basic' = Value.Parse(rolesSchema, ...);

const usersView = pgView('users_view').as((qb) => qb.select().from(users).where(gt(users.age, 18)));
const usersViewSchema = createSelectSchema(usersView);
const parsed: { id: number; name: string; age: number } = Value.Parse(usersViewSchema, ...);
```

### Insert schema[](#insert-schema)

Defines the shape of data to be inserted into the database - can be used to validate API requests.

```
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createInsertSchema } from 'drizzle-orm/typebox-legacy';
import { Value } from '@sinclair/typebox/value';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userInsertSchema = createInsertSchema(users);

const user = { name: 'John' };
const parsed: { name: string, age: number } = Value.Parse(userInsertSchema, user); // Error: `age` is not defined

const user = { name: 'Jane', age: 30 };
const parsed: { name: string, age: number } = Value.Parse(userInsertSchema, user); // Will parse successfully
await db.insert(users).values(parsed);
```

### Update schema[](#update-schema)

Defines the shape of data to be updated in the database - can be used to validate API requests.

```
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createUpdateSchema } from 'drizzle-orm/typebox-legacy';
import { Value } from '@sinclair/typebox/value';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userUpdateSchema = createUpdateSchema(users);

const user = { id: 5, name: 'John' };
const parsed: { name?: string | undefined, age?: number | undefined } = Value.Parse(userUpdateSchema, user); // Error: `id` is a generated column, it can't be updated

const user = { age: 35 };
const parsed: { name?: string | undefined, age?: number | undefined } = Value.Parse(userUpdateSchema, user); // Will parse successfully
await db.update(users).set(parsed).where(eq(users.name, 'Jane'));
```

### Refinements[](#refinements)

Each create schema function accepts an additional optional parameter that you can used to extend, modify or completely overwite a field’s schema. Defining a callback function will extend or modify while providing a Typebox schema will overwrite it.

```
import { pgTable, text, integer, json } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/typebox-legacy';
import { Type } from '@sinclair/typebox';
import { Value } from '@sinclair/typebox/value';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  bio: text(),
  preferences: json()
});

const userSelectSchema = createSelectSchema(users, {
  name: (schema) => Type.String({ ...schema, maxLength: 20 }), // Extends schema
  bio: (schema) => Type.String({ ...schema, maxLength: 1000 }), // Extends schema before becoming nullable/optional
  preferences: Type.Object({ theme: Type.String() }) // Overwrites the field, including its nullability
});

const parsed: {
  id: number;
  name: string,
  bio?: string | undefined;
  preferences: {
    theme: string;
  };
} = Value.Parse(userSelectSchema, ...);
```

### Factory functions[](#factory-functions)

For more advanced use cases, you can use the `createSchemaFactory` function.

**Use case: Using an extended Typebox instance**

```
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createSchemaFactory } from 'drizzle-orm/typebox';
import { t } from 'elysia'; // Extended Typebox instance

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const { createInsertSchema } = createSchemaFactory({ typeboxInstance: t });

const userInsertSchema = createInsertSchema(users, {
  // We can now use the extended instance
  name: (schema) => t.Number({ ...schema }, { error: '`name` must be a string' })
});
```

### Data type reference[](#data-type-reference)

```
pg.boolean();

mysql.boolean();

sqlite.integer({ mode: 'boolean' });

// Schema
Type.Boolean();
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
Type.Date();
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
Type.String();
```

```
pg.bit({ dimensions: ... });

// Schema
t.RegExp(/^[01]+$/, { maxLength: dimensions });
```

```
pg.uuid();

// Schema
Type.String({ format: 'uuid' });
```

```
pg.char({ length: ... });

mysql.char({ length: ... });

// Schema
Type.String({ minLength: length, maxLength: length });
```

```
pg.varchar({ length: ... });

mysql.varchar({ length: ... });

sqlite.text({ mode: 'text', length: ... });

// Schema
Type.String({ maxLength: length });
```

```
mysql.tinytext();

// Schema
Type.String({ maxLength: 255 }); // unsigned 8-bit integer limit
```

```
mysql.text();

// Schema
Type.String({ maxLength: 65_535 }); // unsigned 16-bit integer limit
```

```
mysql.mediumtext();

// Schema
Type.String({ maxLength: 16_777_215 }); // unsigned 24-bit integer limit
```

```
mysql.longtext();

// Schema
Type.String({ maxLength: 4_294_967_295 }); // unsigned 32-bit integer limit
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
Type.Enum(enum);
```

```
mysql.tinyint();

// Schema
Type.Integer({ minimum: -128, maximum: 127 }); // 8-bit integer lower and upper limit
```

```
mysql.tinyint({ unsigned: true });

// Schema
Type.Integer({ minimum: 0, maximum: 255 }); // unsigned 8-bit integer lower and upper limit
```

```
pg.smallint();
pg.smallserial();

mysql.smallint();

// Schema
Type.Integer({ minimum: -32_768, maximum: 32_767 }); // 16-bit integer lower and upper limit
```

```
mysql.smallint({ unsigned: true });

// Schema
Type.Integer({ minimum: 0, maximum: 65_535 }); // unsigned 16-bit integer lower and upper limit
```

```
pg.real();

mysql.float();

// Schema
Type.Number().min(-8_388_608).max(8_388_607); // 24-bit integer lower and upper limit
```

```
mysql.mediumint();

// Schema
Type.Integer({ minimum: -8_388_608, maximum: 8_388_607 }); // 24-bit integer lower and upper limit
```

```
mysql.float({ unsigned: true });

// Schema
Type.Number({ minimum: 0, maximum: 16_777_215 }); // unsigned 24-bit integer lower and upper limit
```

```
mysql.mediumint({ unsigned: true });

// Schema
Type.Integer({ minimum: 0, maximum: 16_777_215 }); // unsigned 24-bit integer lower and upper limit
```

```
pg.integer();
pg.serial();

mysql.int();

// Schema
Type.Integer({ minimum: -2_147_483_648, maximum: 2_147_483_647 }); // 32-bit integer lower and upper limit
```

```
mysql.int({ unsigned: true });

// Schema
Type.Integer({ minimum: 0, maximum: 4_294_967_295 }); // unsgined 32-bit integer lower and upper limit
```

```
pg.doublePrecision();

mysql.double();
mysql.real();

sqlite.real();

// Schema
Type.Number({ minimum: -140_737_488_355_328, maximum: 140_737_488_355_327 }); // 48-bit integer lower and upper limit
```

```
mysql.double({ unsigned: true });

// Schema
Type.Numer({ minimum: 0, maximum: 281_474_976_710_655 }); // unsigned 48-bit integer lower and upper limit
```

```
pg.bigint({ mode: 'number' });
pg.bigserial({ mode: 'number' });

mysql.bigint({ mode: 'number' });
mysql.bigserial({ mode: 'number' });

sqlite.integer({ mode: 'number' });

// Schema
Type.Integer({ minimum: -9_007_199_254_740_991, maximum: 9_007_199_254_740_991 }); // Javascript min. and max. safe integers
```

```
mysql.serial();

Type.Integer({ minimum: 0, maximum: 9_007_199_254_740_991 }); // Javascript max. safe integer
```

```
pg.bigint({ mode: 'bigint' });
pg.bigserial({ mode: 'bigint' });

mysql.bigint({ mode: 'bigint' });

sqlite.blob({ mode: 'bigint' });

// Schema
Type.BigInt({ minimum: -9_223_372_036_854_775_808n, maximum: 9_223_372_036_854_775_807n }); // 64-bit integer lower and upper limit
```

```
mysql.bigint({ mode: 'bigint', unsigned: true });

// Schema
Type.BigInt({ minimum: 0, maximum: 18_446_744_073_709_551_615n }); // unsigned 64-bit integer lower and upper limit
```

```
mysql.year();

// Schema
Type.Integer({ minimum: 1_901, maximum: 2_155 });
```

```
pg.geometry({ type: 'point', mode: 'tuple' });
pg.point({ mode: 'tuple' });

// Schema
Type.Tuple([Type.Number(), Type.Number()]);
```

```
pg.geometry({ type: 'point', mode: 'xy' });
pg.point({ mode: 'xy' });

// Schema
Type.Object({ x: Type.Number(), y: Type.Number() });
```

```
pg.halfvec({ dimensions: ... });
pg.vector({ dimensions: ... });

// Schema
Type.Array(Type.Number(), { minItems: dimensions, maxItems: dimensions });
```

```
pg.line({ mode: 'abc' });

// Schema
Type.Object({ a: Type.Number(), b: Type.Number(), c: Type.Number() });
```

```
pg.line({ mode: 'tuple' });

// Schema
Type.Tuple([Type.Number(), Type.Number(), Type.Number()]);
```

```
pg.json();
pg.jsonb();

mysql.json();

sqlite.blob({ mode: 'json' });
sqlite.text({ mode: 'json' });

// Schema
Type.Recursive((self) => Type.Union([Type.Union([Type.String(), Type.Number(), Type.Boolean(), Type.Null()]), Type.Array(self), Type.Record(Type.String(), self)]));
```

```
sqlite.blob({ mode: 'buffer' });

// Schema
t.Union([t.Union([t.String(), t.Number(), t.Boolean(), t.Null()]), t.Array(t.Any()), t.Record(t.String(), t.Any())]);
```

```
pg.dataType().array(...);

// Schema
Type.Array(baseDataTypeSchema, { minItems: size, maxItems: size });
```

