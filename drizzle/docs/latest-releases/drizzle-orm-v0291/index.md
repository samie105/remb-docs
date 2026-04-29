---
title: "Drizzle ORM - DrizzleORM v0.29.1 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0291"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0291"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:11:01.338Z"
content_hash: "c1b277633e25769534ee8223bdb6828bcea1fd813a6c52dec842d7b61bb471ae"
menu_path: ["Drizzle ORM - DrizzleORM v0.29.1 release"]
section_path: []
content_language: "en"
nav_prev: {"path": "../drizzle-orm-v0290/index.md", "title": "Drizzle ORM - DrizzleORM v0.29.0 release"}
nav_next: {"path": "../drizzle-orm-v0292/index.md", "title": "Drizzle ORM - DrizzleORM v0.29.2 release"}
---

DrizzleORM v0.29.1 release

Nov 29, 2023

## Fixes

-   Forward args correctly when using withReplica feature ([#1536](https://github.com/drizzle-team/drizzle-orm/pull/1536))
-   Fix selectDistinctOn not working with multiple columns ([#1466](https://github.com/drizzle-team/drizzle-orm/pull/1466))

## New Features/Helpers

### Detailed JSDoc for all query builders in all dialects

You can now access more information, hints, documentation links, etc. while developing and using JSDoc right in your IDE. Previously, we had them only for filter expressions, but now you can see them for all parts of the Drizzle query builder

### New helpers for aggregate functions in SQL

> Remember, aggregation functions are often used with the GROUP BY clause of the SELECT statement. So if you are selecting using aggregating functions and other columns in one query, be sure to use the `.groupBy` clause

Here is a list of functions and equivalent using `sql` template:

count

```ts
await db.select({ value: count() }).from(users);
await db.select({ value: count(users.id) }).from(users);

// It's equivalent to writing
await db.select({ 
  value: sql`count('*'))`.mapWith(Number) 
}).from(users);
await db.select({ 
  value: sql`count(${users.id})`.mapWith(Number) 
}).from(users);
```

countDistinct

```ts
await db.select({ value: countDistinct(users.id) }).from(users);

// It's equivalent to writing
await db.select({ 
  value: sql`count(${users.id})`.mapWith(Number) 
}).from(users);
```

avg

```ts
await db.select({ value: avg(users.id) }).from(users);

// It's equivalent to writing
await db.select({ 
  value: sql`avg(${users.id})`.mapWith(String) 
}).from(users);
```

avgDistinct

```ts
await db.select({ value: avgDistinct(users.id) }).from(users);

// It's equivalent to writing
await db.select({ 
  value: sql`avg(distinct ${users.id})`.mapWith(String) 
}).from(users);
```

sum

```ts
await db.select({ value: sum(users.id) }).from(users);

// It's equivalent to writing
await db.select({ 
  value: sql`sum(${users.id})`.mapWith(String) 
}).from(users);
```

sumDistinct

```ts
await db.select({ value: sumDistinct(users.id) }).from(users);

// It's equivalent to writing
await db.select({ 
  value: sql`sum(distinct ${users.id})`.mapWith(String) 
}).from(users);
```

max

```ts
await db.select({ value: max(users.id) }).from(users);

// It's equivalent to writing
await db.select({ 
  value: sql`max(${expression})`.mapWith(users.id) 
}).from(users);
```

min

```ts
await db.select({ value: min(users.id) }).from(users);

// It's equivalent to writing
await db.select({ 
  value: sql`min(${users.id})`.mapWith(users.id) 
}).from(users);
```

To find more information check docs: [aggregation helpers](../../select/index.md#aggregations-helpers)

## New Packages

### Drizzle ESLint Plugin

For cases where it’s impossible to perform type checks for specific scenarios, or where it’s possible but error messages would be challenging to understand, we’ve decided to create an ESLint package with recommended rules. This package aims to assist developers in handling crucial scenarios during development. For more information you can check [docs](../../eslint-plugin/index.md).

### Install

```
npm i eslint eslint-plugin-drizzle
```

```
yarn add eslint eslint-plugin-drizzle
```

```
pnpm add eslint eslint-plugin-drizzle
```

```
bun add eslint eslint-plugin-drizzle
```

You can install those packages for typescript support in your IDE

```
npm i @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

```
yarn add @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

```
pnpm add @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

```
bun add @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

### Usage

Create a `.eslintrc.yml` file, add `drizzle` to the `plugins`, and specify the rules you want to use. You can find a list of all existing rules below

```yaml
root: true
parser: '@typescript-eslint/parser'
parserOptions:
  project: './tsconfig.json'
plugins:
  - drizzle
rules:
  'drizzle/enforce-delete-with-where': "error"
  'drizzle/enforce-update-with-where': "error"
```

#### All config

This plugin exports an all config that makes use of all rules (except for deprecated ones).

```yaml
root: true
extends:
  - "plugin:drizzle/all"
parser: '@typescript-eslint/parser'
parserOptions:
  project: './tsconfig.json'
plugins:
  - drizzle
```

At the moment, `all` is equivalent to `recommended`

```yaml
root: true
extends:
  - "plugin:drizzle/recommended"
parser: '@typescript-eslint/parser'
parserOptions:
  project: './tsconfig.json'
plugins:
  - drizzle
```

### Rules

**enforce-delete-with-where**: Enforce using `delete` with `the.where()` clause in the `.delete()` statement. Most of the time, you don’t need to delete all rows in the table and require some kind of `WHERE` statements.

Error Message:

```plaintext
Without `.where(...)` you will delete all the rows in a table. If you didn't want to do it, please use `db.delete(...).where(...)` instead. Otherwise you can ignore this rule here
```

Optionally, you can define a `drizzleObjectName` in the plugin options that accept a `string` or `string[]`. This is useful when you have objects or classes with a delete method that’s not from Drizzle. Such a `delete` method will trigger the ESLint rule. To avoid that, you can define the name of the Drizzle object that you use in your codebase (like db) so that the rule would only trigger if the delete method comes from this object:

Example, config 1:

```json
"rules": {
  "drizzle/enforce-delete-with-where": ["error"]
}
```

```ts
class MyClass {
  public delete() {
    return {}
  }
}

const myClassObj = new MyClass();

// ---> Will be triggered by ESLint Rule
myClassObj.delete()

const db = drizzle(...)
// ---> Will be triggered by ESLint Rule
db.delete()
```

Example, config 2:

```json
"rules": {
  "drizzle/enforce-delete-with-where": ["error", { "drizzleObjectName": ["db"] }],
}
```

```ts
class MyClass {
  public delete() {
    return {}
  }
}

const myClassObj = new MyClass();

// ---> Will NOT be triggered by ESLint Rule
myClassObj.delete()

const db = drizzle(...)
// ---> Will be triggered by ESLint Rule
db.delete()
```

**enforce-update-with-where**: Enforce using `update` with `the.where()` clause in the `.update()` statement. Most of the time, you don’t need to update all rows in the table and require some kind of `WHERE` statements.

Error Message:

```plaintext
Without `.where(...)` you will update all the rows in a table. If you didn't want to do it, please use `db.update(...).set(...).where(...)` instead. Otherwise you can ignore this rule here
```

Optionally, you can define a `drizzleObjectName` in the plugin options that accept a `string` or `string[]`. This is useful when you have objects or classes with a delete method that’s not from Drizzle. Such as `update` method will trigger the ESLint rule. To avoid that, you can define the name of the Drizzle object that you use in your codebase (like db) so that the rule would only trigger if the delete method comes from this object:

Example, config 1:

```json
"rules": {
  "drizzle/enforce-update-with-where": ["error"]
}
```

```ts
class MyClass {
  public update() {
    return {}
  }
}

const myClassObj = new MyClass();

// ---> Will be triggered by ESLint Rule
myClassObj.update()

const db = drizzle(...)
// ---> Will be triggered by ESLint Rule
db.update()
```

Example, config 2:

```json
"rules": {
  "drizzle/enforce-update-with-where": ["error", { "drizzleObjectName": ["db"] }],
}
```

```ts
class MyClass {
  public update() {
    return {}
  }
}

const myClassObj = new MyClass();

// ---> Will NOT be triggered by ESLint Rule
myClassObj.update()

const db = drizzle(...)
// ---> Will be triggered by ESLint Rule
db.update()
```
