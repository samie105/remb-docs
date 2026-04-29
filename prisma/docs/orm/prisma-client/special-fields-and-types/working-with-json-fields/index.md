---
title: "Working with Json fields"
source: "https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:40:01.426Z"
content_hash: "d7601dd28bfe6ee5047f337c46c49347347dea75f1e344fd784a17193d238feb"
menu_path: ["Working with Json fields"]
section_path: []
tab_variants: ["PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","PostgreSQL","MySQL","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "../working-with-geometry-fields/index.md", "title": "Working with geometry fields"}
nav_next: {"path": "../working-with-scalar-lists-arrays/index.md", "title": "Working with scalar lists"}
---

Use the [`Json`](../../../reference/prisma-schema-reference/index.md#json) Prisma ORM field type to read, write, and perform basic filtering on JSON types in the underlying database. In the following example, the `User` model has an optional `Json` field named `extendedPetsData`:

```
model User {
  id               Int     @id @default(autoincrement())
  email            String  @unique
  name             String?
  posts            Post[]
  extendedPetsData Json?
}
```

Example field value:

```
{
  "pet1": {
    "petName": "Claudine",
    "petType": "House cat"
  },
  "pet2": {
    "petName": "Sunny",
    "petType": "Gerbil"
  }
}
```

The `Json` field supports a few additional types, such as `string` and `boolean`. These additional types exist to match the types supported by [`JSON.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse):

```
export type JsonValue = string | number | boolean | null | JsonObject | JsonArray;
```

Reasons to store data as JSON rather than representing data as related models include:

-   You need to store data that does not have a consistent structure
-   You are importing data from another system and do not want to map that data to Prisma models

You can use the `Prisma.JsonArray` and `Prisma.JsonObject` utility classes to work with the contents of a `Json` field:

```
const { PrismaClient, Prisma } = require("@prisma/client");

const user = await prisma.user.findFirst({
  where: {
    id: 9,
  },
});

// Example extendedPetsData data:
// [{ name: 'Bob the dog' }, { name: 'Claudine the cat' }]

if (
  user?.extendedPetsData &&
  typeof user?.extendedPetsData === "object" &&
  Array.isArray(user?.extendedPetsData)
) {
  const petsObject = user?.extendedPetsData as Prisma.JsonArray;

  const firstPet = petsObject[0];
}
```

See also: [Advanced example: Update a nested JSON key value](#advanced-example-update-a-nested-json-key-value)

The following example writes a JSON object to the `extendedPetsData` field:

```
var json = [{ name: "Bob the dog" }, { name: "Claudine the cat" }] as Prisma.JsonArray;

const createUser = await prisma.user.create({
  data: {
    email: "birgitte@prisma.io",
    extendedPetsData: json,
  },
});
```

> **Note**: JavaScript objects (for example, `{ extendedPetsData: "none"}`) are automatically converted to JSON.

See also: [Advanced example: Update a nested JSON key value](#advanced-example-update-a-nested-json-key-value)

You can filter rows of `Json` type.

### [Filter on exact field value](#filter-on-exact-field-value)

The following query returns all users where the value of `extendedPetsData` matches the `json` variable exactly:

```
var json = [{ name: "Bob the dog" }, { name: "Claudine the cat" }];

const getUsers = await prisma.user.findMany({
  where: {
    extendedPetsData: {
      equals: json,
    },
  },
});
```

The following query returns all users where the value of `extendedPetsData` does **not** match the `json` variable exactly:

```
var json = [{ name: "Bob the dog" }, { name: "Claudine the cat" }];

const getUsers = await prisma.user.findMany({
  where: {
    extendedPetsData: {
      not: json,
    },
  },
});
```

You can also filter rows by the data inside a `Json` field. We call this **advanced `Json` filtering**. This functionality is supported by [PostgreSQL](../../../core-concepts/supported-databases/postgresql/index.md) and [MySQL](../../../core-concepts/supported-databases/mysql/index.md) only with [different syntaxes for the `path` option](#path-syntax-depending-on-database).

### [`path` syntax depending on database](#path-syntax-depending-on-database)

The filters below use a `path` option to select specific parts of the `Json` value to filter on. The implementation of that filtering differs between connectors:

-   The [MySQL connector](../../../core-concepts/supported-databases/mysql/index.md) uses [MySQL's implementation of JSON path](https://dev.mysql.com/doc/refman/8.0/en/json.html#json-path-syntax)
-   The [PostgreSQL connector](../../../core-concepts/supported-databases/postgresql/index.md) uses the custom JSON functions and operators [supported in version 12 _and earlier_](https://www.postgresql.org/docs/11/functions-json.html)

For example, the following is a valid MySQL `path` value:

```
$petFeatures.petName
```

The following is a valid PostgreSQL `path` value:

```
["petFeatures", "petName"]
```

### [Filter on object property](#filter-on-object-property)

You can filter on a specific property inside a block of JSON. In the following examples, the value of `extendedPetsData` is a one-dimensional, unnested JSON object:

```
{
  "petName": "Claudine",
  "petType": "House cat"
}
```

The following query returns all users where the value of `petName` is `"Claudine"`:

The following query returns all users where the value of `petType` _contains_ `"cat"`:

The following string filters are available:

-   [`string_contains`](../../../reference/prisma-client-reference/index.md#string_contains)
-   [`string_starts_with`](../../../reference/prisma-client-reference/index.md#string_starts_with)
-   [`string_ends_with`](../../../reference/prisma-client-reference/index.md#string_ends_with) .

To use case insensitive filter with these, you can use the [`mode`](../../../reference/prisma-client-reference/index.md#mode) option:

### [Filter on nested object property](#filter-on-nested-object-property)

You can filter on nested JSON properties. In the following examples, the value of `extendedPetsData` is a JSON object with several levels of nesting.

```
{
  "pet1": {
    "petName": "Claudine",
    "petType": "House cat"
  },
  "pet2": {
    "petName": "Sunny",
    "petType": "Gerbil",
    "features": {
      "eyeColor": "Brown",
      "furColor": "White and black"
    }
  }
}
```

The following query returns all users where `"pet2"` → `"petName"` is `"Sunny"`:

The following query returns all users where:

-   `"pet2"` → `"petName"` is `"Sunny"`
-   `"pet2"` → `"features"` → `"furColor"` contains `"black"`

### [Filtering on an array value](#filtering-on-an-array-value)

You can filter on the presence of a specific value in a scalar array (strings, integers). In the following example, the value of `extendedPetsData` is an array of strings:

```
["Claudine", "Sunny"]
```

The following query returns all users with a pet named `"Claudine"`:

The following array filters are available:

-   [`array_contains`](../../../reference/prisma-client-reference/index.md#array_contains)
-   [`array_starts_with`](../../../reference/prisma-client-reference/index.md#array_starts_with)
-   [`array_ends_with`](../../../reference/prisma-client-reference/index.md#array_ends_with)

### [Filtering on nested array value](#filtering-on-nested-array-value)

You can filter on the presence of a specific value in a scalar array (strings, integers). In the following examples, the value of `extendedPetsData` includes nested scalar arrays of names:

```
{
  "cats": { "owned": ["Bob", "Sunny"], "fostering": ["Fido"] },
  "dogs": { "owned": ["Ella"], "fostering": ["Prince", "Empress"] }
}
```

#### [Scalar value arrays](#scalar-value-arrays)

The following query returns all users that foster a cat named `"Fido"`:

The following query returns all users that foster cats named `"Fido"` _and_ `"Bob"`:

#### [JSON object arrays](#json-object-arrays)

-   If you are using PostgreSQL, you must pass in an array of objects to match, even if that array only contains one object:
    
    ```
    [{ status: "expired", insuranceID: 92 }]
    // PostgreSQL
    ```
    
    If you are using MySQL, you must pass in a single object to match:
    
    ```
    { status: "expired", insuranceID: 92 }
    // MySQL
    ```
    
-   If your filter array contains multiple objects, PostgreSQL will only return results if _all_ objects are present - not if at least one object is present.
    
-   You must set `array_contains` to a JSON object, not a string. If you use a string, Prisma Client escapes the quotation marks and the query will not return results. For example:
    
    ```
    array_contains: '[{"status": "expired", "insuranceID": 92}]';
    ```
    
    is sent to the database as:
    
    ```
    [{\"status\": \"expired\", \"insuranceID\": 92}]
    ```
    

### [Targeting an array element by index](#targeting-an-array-element-by-index)

You can filter on the value of an element in a specific position.

```
{ "owned": ["Bob", "Sunny"], "fostering": ["Fido"] }
```

### [Filtering on object key value inside array](#filtering-on-object-key-value-inside-array)

Depending on your provider, you can filter on the key value of an object inside an array.

In the following example, the value of `extendedPetsData` is an array of objects with a nested `insurances` array, which contains two objects:

```
[
  {
    "petName": "Claudine",
    "petType": "House cat",
    "insurances": [
      { "insuranceID": 92, "status": "expired" },
      { "insuranceID": 12, "status": "active" }
    ]
  },
  {
    "petName": "Sunny",
    "petType": "Gerbil"
  },
  {
    "petName": "Gerald",
    "petType": "Corn snake"
  },
  {
    "petName": "Nanna",
    "petType": "Moose"
  }
]
```

The following query returns all users where at least one pet is a moose:

```
const getUsers = await prisma.user.findMany({
  where: {
    extendedPetsData: {
      path: "$[*].petType",
      array_contains: "Moose",
    },
  },
});
```

-   `$[*]` is the root array of pet objects
-   `petType` matches the `petType` key in any pet object

The following query returns all users where at least one pet has an expired insurance:

```
const getUsers = await prisma.user.findMany({
  where: {
    extendedPetsData: {
      path: "$[*].insurances[*].status",
      array_contains: "expired",
    },
  },
});
```

-   `$[*]` is the root array of pet objects
-   `insurances[*]` matches any `insurances` array inside any pet object
-   `status` matches any `status` key in any insurance object

The following example assumes that the value of `extendedPetsData` is some variation of the following:

```
{
  "petName": "Claudine",
  "petType": "House cat",
  "insurances": [
    { "insuranceID": 92, "status": "expired" },
    { "insuranceID": 12, "status": "active" }
  ]
}
```

The following example:

1.  Gets all users
2.  Change the `"status"` of each insurance object to `"expired"`
3.  Get all users that have an expired insurance where the ID is `92`

There are two types of `null` values possible for a `JSON` field in an SQL database.

-   Database `NULL`: The value in the database is a `NULL`.
-   JSON `null`: The value in the database contains a JSON value that is `null`.

To differentiate between these possibilities, we've introduced three _null enums_ you can use:

-   `JsonNull`: Represents the `null` value in JSON.
-   `DbNull`: Represents the `NULL` value in the database.
-   `AnyNull`: Represents both `null` JSON values and `NULL` database values. (Only when filtering)

For example:

```
model Log {
  id   Int  @id
  meta Json
}
```

Here is an example of using `AnyNull`:

```
import { Prisma } from "@prisma/client";

prisma.log.findMany({
  where: {
    data: {
      meta: {
        equals: Prisma.AnyNull,
      },
    },
  },
});
```

### [Inserting `null` Values](#inserting-null-values)

This also applies to `create`, `update` and `upsert`. To insert a `null` value into a `Json` field, you would write:

```
import { Prisma } from "@prisma/client";

prisma.log.create({
  data: {
    meta: Prisma.JsonNull,
  },
});
```

And to insert a database `NULL` into a `Json` field, you would write:

```
import { Prisma } from "@prisma/client";

prisma.log.create({
  data: {
    meta: Prisma.DbNull,
  },
});
```

### [Filtering by `null` Values](#filtering-by-null-values)

To filter by `JsonNull` or `DbNull`, you would write:

```
import { Prisma } from "@prisma/client";

prisma.log.findMany({
  where: {
    meta: {
      equals: Prisma.AnyNull,
    },
  },
});
```

Prisma's `Json` fields are untyped by default. To add strong typing, you can use the external package [prisma-json-types-generator](https://www.npmjs.com/package/prisma-json-types-generator).

1.  First, install the package and add the generator to your `schema.prisma`:
    
    schema.prisma
    
    ```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }
    
    generator json {
      provider = "prisma-json-types-generator"
    }
    ```
    
2.  Next, link a field to a TypeScript type using an [AST comment](../../../prisma-schema/overview/index.md#comments).
    
    schema.prisma
    
    ```
    model Log {
      id   Int @id
    
      /// [LogMetaType]
      meta Json
    }
    ```
    
3.  Then, define `LogMetaType` in a type declaration file (e.g., `types.ts`) that is included in your `tsconfig.json`.
    
    types.ts
    
    ```
    declare global {
      namespace PrismaJson {
        type LogMetaType = { timestamp: number; host: string };
      }
    }
    
    // This file must be a module.
    export {};
    ```
    

Now, `Log.meta` will be strongly typed as `{ timestamp: number; host: string }`.

### [Typing `String` Fields and Advanced Features](#typing-string-fields-and-advanced-features)

You can also apply these techniques to `String` fields. This is especially useful for creating string-based enums directly in your schema when your database does not support enum types.

```
model Post {
  id     Int    @id

  /// !['draft' | 'published']
  status String

  /// [LogMetaType]
  meta   Json[]
}
```

This results in `post.status` being strongly typed as `'draft' | 'published'` and `post.meta` as `LogMetaType[]`.

For a complete guide on configuration, monorepo setup, and other advanced features, please refer to the [official `prisma-json-types-generator` documentation](https://github.com/arthurfiorette/prisma-json-types-generator#readme).

### [Can you select a subset of JSON key/values to return?](#can-you-select-a-subset-of-json-keyvalues-to-return)

No - it is not yet possible to [select which JSON elements to return](https://github.com/prisma/prisma/issues/2431). Prisma Client returns the entire JSON object.

### [Can you filter on the presence of a specific key?](#can-you-filter-on-the-presence-of-a-specific-key)

No - it is not yet possible to filter on the presence of a specific key.

### [Is case insensitive filtering supported?](#is-case-insensitive-filtering-supported)

Yes - you can use the `mode: 'insensitive'` option with string filters like `string_contains`, `string_starts_with`, and `string_ends_with`. See [Filter on object property](#filter-on-object-property) for examples.

### [Can you sort an object property within a JSON value?](#can-you-sort-an-object-property-within-a-json-value)

No, [sorting object properties within a JSON value](https://github.com/prisma/prisma/issues/10346) (order-by-prop) is not currently supported.

### [How to set a default value for JSON fields?](#how-to-set-a-default-value-for-json-fields)

When you want to set a `@default` value the `Json` type, you need to enclose it with double-quotes inside the `@default` attribute (and potentially escape any "inner" double-quotes using a backslash), for example:

```
model User {
  id    Int  @id @default(autoincrement())
  json1 Json @default("[]")
  json2 Json @default("{ \"hello\": \"world\" }")
}
```
