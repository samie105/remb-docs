---
title: "ESLint Drizzle Plugin"
source: "https://orm.drizzle.team/docs/eslint-plugin"
canonical_url: "https://orm.drizzle.team/docs/eslint-plugin"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:38:07.110Z"
content_hash: "5ff03bd1f9d8d4bc93efb2e65fc26866b2cd4cf2a1b37805dcaf8e1a49ad34db"
menu_path: ["ESLint Drizzle Plugin"]
section_path: []
content_language: "en"
---
For cases where it’s impossible to perform type checks for specific scenarios, or where it’s possible but error messages would be challenging to understand, we’ve decided to create an ESLint package with recommended rules. This package aims to assist developers in handling crucial scenarios during development

## Install[](#install)

```
npm i eslint-plugin-drizzle
npm i @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

```
yarn add eslint-plugin-drizzle
yarn add @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

```
pnpm add eslint-plugin-drizzle
pnpm add @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

```
bun add eslint-plugin-drizzle
bun add @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

## Usage[](#usage)

**`.eslintrc.yml` example**

```yml
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

**All config**

This plugin exports an `all` that makes use of all rules (except for deprecated ones).

```yml
root: true
extends:
  - "plugin:drizzle/all"
parser: '@typescript-eslint/parser'
parserOptions:
  project: './tsconfig.json'
plugins:
  - drizzle
```

**Recommended config**

At the moment, `all` is equivalent to `recommended`

```yml
root: true
extends:
  - "plugin:drizzle/recommended"
parser: '@typescript-eslint/parser'
parserOptions:
  project: './tsconfig.json'
plugins:
  - drizzle
```

## Rules[](#rules)

### **enforce-delete-with-where**[](#enforce-delete-with-where)

Enforce using `delete` with the`.where()` clause in the `.delete()` statement. Most of the time, you don’t need to delete all rows in the table and require some kind of `WHERE` statements.

Optionally, you can define a `drizzleObjectName` in the plugin options that accept a `string` or `string[]`. This is useful when you have objects or classes with a delete method that’s not from Drizzle. Such a `delete` method will trigger the ESLint rule. To avoid that, you can define the name of the Drizzle object that you use in your codebase (like db) so that the rule would only trigger if the delete method comes from this object:

Example, config 1:

```yml
rules:
  'drizzle/enforce-delete-with-where': "error"
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

```yml
rules:
  'drizzle/enforce-delete-with-where':
    - "error"
    - "drizzleObjectName": 
      - "db"
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

### **enforce-update-with-where**:[](#enforce-update-with-where)

Enforce using `update` with the`.where()` clause in the `.update()` statement. Most of the time, you don’t need to update all rows in the table and require some kind of `WHERE` statements.

Optionally, you can define a `drizzleObjectName` in the plugin options that accept a `string` or `string[]`. This is useful when you have objects or classes with a delete method that’s not from Drizzle. Such as `update` method will trigger the ESLint rule. To avoid that, you can define the name of the Drizzle object that you use in your codebase (like db) so that the rule would only trigger if the delete method comes from this object:

Example, config 1:

```yml
rules:
  'drizzle/enforce-update-with-where': "error"
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

```yml
rules:
  'drizzle/enforce-update-with-where':
    - "error"
    - "drizzleObjectName": 
      - "db"
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
