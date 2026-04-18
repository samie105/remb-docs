---
title: "Models"
source: "https://www.prisma.io/docs/orm/prisma-schema/data-model/models"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/data-model/models"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:17.881Z"
content_hash: "75d39d25ef03837555987976c7e9d39f92787d8774c1bc41686502023b8bf931"
menu_path: ["Models"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-schema/data-model/multi-schema/index.md", "title": "Multi-schema"}
nav_next: {"path": "prisma/docs/orm/prisma-schema/data-model/unsupported-database-features/index.md", "title": "Unsupported database features (Prisma Schema)"}
---

Learn about the concepts for building your data model with Prisma: Models, scalar types, enums, attributes, functions, IDs, default values and more

The data model definition part of the [Prisma schema](prisma/docs/orm/prisma-schema/overview/index.md) defines your application models (also called **Prisma models**). Models:

*   Represent the **entities** of your application domain
*   Map to the **tables** (relational databases like PostgreSQL) or **collections** (MongoDB) in your database
*   Form the foundation of the **queries** available in the generated [Prisma Client API](prisma/docs/orm/prisma-client/setup-and-configuration/introduction/index.md)
*   When used with TypeScript, Prisma Client provides generated **type definitions** for your models and any [variations](prisma/docs/orm/prisma-client/type-safety/operating-against-partial-structures-of-model-types/index.md) of them to make database access entirely type safe.

The following schema describes a blogging platform - the data model definition is highlighted:

The data model definition is made up of:

*   [Models](#defining-models) ([`model`](prisma/docs/orm/reference/prisma-schema-reference/index.md#model) primitives) that define a number of fields, including [relations between models](#relation-fields)
*   [Enums](#defining-enums) ([`enum`](prisma/docs/orm/reference/prisma-schema-reference/index.md#enum) primitives) (if your connector supports Enums)
*   [Attributes](#defining-attributes) and [functions](#using-functions) that change the behavior of fields and models

The corresponding database looks like this:

![Sample database](https://www.prisma.io/docs/img/orm/sample-database.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

A model maps to the underlying structures of the data source.

*   In relational databases like PostgreSQL and MySQL, a `model` maps to a **table**
*   In MongoDB, a `model` maps to a **collection**

> **Note**: In the future there might be connectors for non-relational databases and other data sources. For example, for a REST API it would map to a _resource_.

The following query creates a `User` with nested `Post` and `Category` records:

```
const user = await prisma.user.create({
  data: {
    email: "ariadne@prisma.io",
    name: "Ariadne",
    posts: {
      create: [
        {
          title: "My first day at Prisma",
          categories: { create: { name: "Office" } },
        },
        {
          title: "How to connect to a SQLite database",
          categories: { create: [{ name: "Databases" }, { name: "Tutorials" }] },
        },
      ],
    },
  },
});
```

Your data model reflects _your_ application domain. For example:

*   In an **ecommerce** application you probably have models like `Customer`, `Order`, `Item` and `Invoice`.
*   In a **social media** application you probably have models like `User`, `Post`, `Photo` and `Message`.

There are two ways to define a data model:

*   **Write the data model manually and use Prisma Migrate**: You can write your data model manually and map it to your database using [Prisma Migrate](prisma/docs/orm/prisma-migrate/index.md). In this case, the data model is the single source of truth for the models of your application.
*   **Generate the data model via introspection**: When you have an existing database or prefer migrating your database schema with SQL, you generate the data model by [introspecting](prisma/docs/orm/prisma-schema/introspection/index.md) your database. In this case, the database schema is the single source of truth for the models of your application.

Models represent the entities of your application domain. Models are represented by [`model`](prisma/docs/orm/reference/prisma-schema-reference/index.md#model) blocks and define a number of [fields](prisma/docs/orm/reference/prisma-schema-reference/index.md#model-fields). In the example data model above, `User`, `Profile`, `Post` and `Category` are models.

A blogging platform can be extended with the following models:

```
model Comment {
  // Fields
}

model Tag {
  // Fields
}
```

### [Mapping model names to tables or collections](#mapping-model-names-to-tables-or-collections)

Prisma model [naming conventions (singular form, PascalCase)](prisma/docs/orm/reference/prisma-schema-reference/index.md#naming-conventions) do not always match table names in the database. A common approach for naming tables/collections in databases is to use plural form and [snake\_case](https://en.wikipedia.org/wiki/Snake_case) notation - for example: `comments`. When you introspect a database with a table named `comments`, the resulting Prisma model will look like this:

```
model comments {
  // Fields
}
```

However, you can still adhere to the naming convention without renaming the underlying `comments` table in the database by using the [`@@map`](prisma/docs/orm/reference/prisma-schema-reference/index.md) attribute:

```
model Comment {
  // Fields

  @@map("comments")
}
```

With this model definition, Prisma ORM automatically maps the `Comment` model to the `comments` table in the underlying database.

> **Note**: You can also [`@map`](prisma/docs/orm/reference/prisma-schema-reference/index.md#map) a column name or enum value, and `@@map` an enum name.

`@map` and `@@map` allow you to [tune the shape of your Prisma Client API](prisma/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names/index.md#using-map-and-map-to-rename-fields-and-models-in-the-prisma-client-api) by decoupling model and field names from table and column names in the underlying database.

The properties of a model are called _fields_, which consist of:

*   A **[field name](prisma/docs/orm/reference/prisma-schema-reference/index.md#model-fields)**
*   A **[field type](prisma/docs/orm/reference/prisma-schema-reference/index.md#model-fields)**
*   Optional **[type modifiers](#type-modifiers)**
*   Optional **[attributes](#defining-attributes)**, including [native database type attributes](#native-types-mapping)

A field's type determines its _structure_, and fits into one of two categories:

*   [Scalar types](#scalar-fields) (includes [enums](#defining-enums)) that map to columns (relational databases) or document fields (MongoDB) - for example, [`String`](prisma/docs/orm/reference/prisma-schema-reference/index.md#string) or [`Int`](prisma/docs/orm/reference/prisma-schema-reference/index.md#int)
*   Model types (the field is then called [relation field](prisma/docs/orm/prisma-schema/data-model/relations/index.md#relation-fields)) - for example `Post` or `Comment[]`

### [Scalar fields](#scalar-fields)

The following example extends the `Comment` and `Tag` models with several scalar types. Some fields include [attributes](#defining-attributes):

See [complete list of scalar field types](prisma/docs/orm/reference/prisma-schema-reference/index.md#model-field-scalar-types) .

### [Relation fields](#relation-fields)

A relation field's type is another model - for example, a post (`Post`) can have multiple comments (`Comment[]`):

Refer to the [relations documentation](prisma/docs/orm/prisma-schema/data-model/relations/index.md) for more examples and information about relationships between models.

### [Native types mapping](#native-types-mapping)

**Native database type attributes** describe the underlying database type:

```
model Post {
  id      Int    @id
  title   String @db.VarChar(200)
  content String
}
```

Type attributes are:

*   Specific to the underlying provider (e.g., PostgreSQL uses `@db.Boolean`, MySQL uses `@db.TinyInt(1)`)
*   Written in PascalCase and prefixed by `@db`
*   Only added during [introspection](prisma/docs/orm/prisma-schema/introspection/index.md) if the native type differs from the default

See [native database type attributes](prisma/docs/orm/reference/prisma-schema-reference/index.md#model-field-scalar-types) for the complete list.

### [Type modifiers](#type-modifiers)

The type of a field can be modified by appending either of two modifiers:

*   [`[]`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#-modifier) Make a field a list
*   [`?`](prisma/docs/orm/reference/prisma-schema-reference/index.md#-modifier-1) Make a field optional

> **Note**: You **cannot** combine type modifiers - optional lists are not supported.

#### [Lists](#lists)

The following example includes a scalar list and a list of related models:

```
model Post {
  id       Int       @id @default(autoincrement())
  comments Comment[] // A list of comments
  keywords String[]  // A scalar list
}
```

#### [Optional and mandatory fields](#optional-and-mandatory-fields)

```
model Comment {
  id      Int     @id @default(autoincrement())
  title   String       // Required field
  content String?      // Optional field (nullable)
}
```

Fields without `?` are required:

*   **Relational databases**: Represented via `NOT NULL` constraints
*   **Prisma Client**: TypeScript types enforce these fields at compile time

### [Unsupported types](#unsupported-types)

When you introspect a relational database, unsupported data types are added as [`Unsupported`](prisma/docs/orm/reference/prisma-schema-reference/index.md#unsupported):

```
location    Unsupported("POLYGON")?
```

Fields of type `Unsupported` don't appear in the generated Prisma Client API, but you can still use [raw database access](prisma/docs/orm/prisma-client/using-raw-sql/raw-queries/index.md) to query them.

Attributes modify the behavior of fields or model blocks. The following example includes three field attributes ([`@id`](prisma/docs/orm/reference/prisma-schema-reference/index.md#id) , [`@default`](prisma/docs/orm/reference/prisma-schema-reference/index.md#default) , and [`@unique`](prisma/docs/orm/reference/prisma-schema-reference/index.md#unique) ) and one block attribute ([`@@unique`](prisma/docs/orm/reference/prisma-schema-reference/index.md)):

Some attributes accept [arguments](prisma/docs/orm/reference/prisma-schema-reference/index.md#attribute-argument-types) - for example, `@default` accepts `true` or `false`:

```
isAdmin   Boolean @default(false) // short form of @default(value: false)
```

See [complete list of field and block attributes](prisma/docs/orm/reference/prisma-schema-reference/index.md#attributes)

### [Defining an ID field](#defining-an-id-field)

An ID uniquely identifies individual records of a model. A model can only have _one_ ID:

*   In **relational databases**, the ID can be a single field or based on multiple fields. If a model does not have an `@id` or an `@@id`, you must define a mandatory `@unique` field or `@@unique` block instead.
*   In **MongoDB**, an ID must be a single field that defines an `@id` attribute and a `@map("_id")` attribute.

#### [Defining IDs in relational databases](#defining-ids-in-relational-databases)

In relational databases, an ID can be defined by a single field using the [`@id`](prisma/docs/orm/reference/prisma-schema-reference/index.md#id) attribute, or multiple fields using the [`@@id`](prisma/docs/orm/reference/prisma-schema-reference/index.md) attribute.

##### [Single field IDs](#single-field-ids)

In the following example, the `User` ID is represented by the `id` integer field:

```
model User {
  id      Int      @id @default(autoincrement()) 
  email   String   @unique
  name    String?
  role    Role     @default(USER)
  posts   Post[]
  profile Profile?
}
```

##### [Composite IDs](#composite-ids)

In the following example, the `User` ID is represented by a combination of the `firstName` and `lastName` fields:

```
model User {
  firstName String
  lastName  String
  email     String  @unique
  isAdmin   Boolean @default(false)

  @@id([firstName, lastName]) 
}
```

By default, the name of this field in Prisma Client queries will be `firstName_lastName`.

You can also provide your own name for the composite ID using the [`@@id`](prisma/docs/orm/reference/prisma-schema-reference/index.md) attribute's `name` field:

```
model User {
  firstName String
  lastName  String
  email     String  @unique
  isAdmin   Boolean @default(false)

  @@id(name: "fullName", fields: [firstName, lastName]) 
}
```

The `firstName_lastName` field will now be named `fullName` instead.

##### [`@unique` fields as unique identifiers](#unique-fields-as-unique-identifiers)

In the following example, users are uniquely identified by a `@unique` field. Because the `email` field functions as a unique identifier for the model (which is required), it must be mandatory:

```
model User {
  email   String   @unique
  name    String?
  role    Role     @default(USER)
  posts   Post[]
  profile Profile?
}
```

#### [Defining IDs in MongoDB](#defining-ids-in-mongodb)

The MongoDB connector has [specific rules for defining an ID field](prisma/docs/orm/reference/prisma-schema-reference/index.md#mongodb) that differs from relational databases. An ID must be defined by a single field using the [`@id`](prisma/docs/orm/reference/prisma-schema-reference/index.md#id) attribute and must include `@map("_id")`.

In the following example, the `User` ID is represented by the `id` string field that accepts an auto-generated `ObjectId`:

```
model User {
  id      String   @id @default(auto()) @map("_id") @db.ObjectId
  email   String   @unique
  name    String?
  role    Role     @default(USER)
  posts   Post[]
  profile Profile?
}
```

In the following example, the `User` ID is represented by the `id` string field that accepts something other than an `ObjectId` - for example, a unique username:

```
model User {
  id      String   @id @map("_id") 
  email   String   @unique
  name    String?
  role    Role     @default(USER)
  posts   Post[]
  profile Profile?
}
```

### [Defining a default value](#defining-a-default-value)

You can define default values for scalar fields using the [`@default`](prisma/docs/orm/reference/prisma-schema-reference/index.md#default) attribute:

```
model Post {
  id         Int        @id @default(autoincrement())
  createdAt  DateTime   @default(now())
  title      String
  published  Boolean    @default(false)
  data       Json       @default("{ \"hello\": \"world\" }")
}
```

Default values can be:

*   **Static values**: `5` (`Int`), `"Hello"` (`String`), `false` (`Boolean`)
*   **Lists**: `[5, 6, 8]` (`Int[]`), `["Hello", "Goodbye"]` (`String[]`)
*   **Functions**: [`now()`](prisma/docs/orm/reference/prisma-schema-reference/index.md#now), [`uuid()`](prisma/docs/orm/reference/prisma-schema-reference/index.md#uuid), [`cuid()`](prisma/docs/orm/reference/prisma-schema-reference/index.md#cuid)
*   **JSON**: Use escaped strings, e.g., `@default("{ \"hello\": \"world\" }")`

See [attribute functions](prisma/docs/orm/reference/prisma-schema-reference/index.md#attribute-functions) for connector support details.

### [Defining a unique field](#defining-a-unique-field)

Unique attributes can be defined on a single field using [`@unique`](prisma/docs/orm/reference/prisma-schema-reference/index.md#unique), or on multiple fields using [`@@unique`](prisma/docs/orm/reference/prisma-schema-reference/index.md):

```
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique      // Single field unique
  name  String?
}

model Post {
  id       Int    @id @default(autoincrement())
  title    String
  authorId Int

  @@unique([authorId, title]) // Composite unique
}
```

You can customize the constraint name with the `name` field: `@@unique(name: "authorTitle", [authorId, title])`

See [working with composite unique identifiers](prisma/docs/orm/prisma-client/special-fields-and-types/working-with-composite-ids-and-constraints/index.md) for Prisma Client usage.

#### [Composite type unique constraints (MongoDB)](#composite-type-unique-constraints-mongodb)

For MongoDB composite types, you can define unique constraints on nested fields:

```
type Address {
  street String
  number Int
}

model User {
  id      Int     @id
  email   String
  address Address

  @@unique([email, address.number])
}
```

### [Defining an index](#defining-an-index)

Define indexes via [`@@index`](prisma/docs/orm/reference/prisma-schema-reference/index.md#index):

```
model Post {
  id      Int     @id @default(autoincrement())
  title   String
  content String?

  @@index([title, content])
}
```

For MongoDB composite types, use dot notation: `@@index([address.city.name])`

See [custom index names](prisma/docs/orm/prisma-schema/data-model/database-mapping/index.md#constraint-and-index-names) for naming customization.

Enums are defined via the [`enum`](prisma/docs/orm/reference/prisma-schema-reference/index.md#enum) block when [supported by your database](prisma/docs/orm/reference/database-features/index.md#misc):

```
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  role  Role    @default(USER)
}

enum Role {
  USER
  ADMIN
}
```

Composite types (embedded documents) allow embedding records inside other records:

```
model Product {
  id     String  @id @default(auto()) @map("_id") @db.ObjectId
  name   String
  photos Photo[]
}

type Photo {
  height Int
  width  Int
  url    String
}
```

**Supported attributes in composite types:** `@default`, `@map`, native types (`@db.ObjectId`)

**Not supported:** `@unique`, `@id`, `@relation`, `@ignore`, `@updatedAt`

The Prisma schema supports [functions](prisma/docs/orm/reference/prisma-schema-reference/index.md#attribute-functions) for default values:

```
model Post {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  uuid      String   @default(uuid())
}
```

Common functions: `now()`, `uuid()`, `cuid()`, `autoincrement()`, `auto()` (MongoDB ObjectId)

See [relations documentation](prisma/docs/orm/prisma-schema/data-model/relations/index.md) for relationship details.

### [Queries (CRUD)](#queries-crud)

Every model generates CRUD queries in the [Prisma Client API](prisma/docs/orm/prisma-client/setup-and-configuration/introduction/index.md):

`findMany()` | `findFirst()` | `findUnique()` | `create()` | `update()` | `upsert()` | `delete()` | `createMany()` | `updateMany()` | `deleteMany()`

Access via the lowercase model name property: `prisma.user.create({ ... })`

### [Type definitions](#type-definitions)

Prisma Client generates TypeScript types for your models:

```
export type User = {
  id: number;
  email: string;
  name: string | null;
};
```

These types ensure type-safe database queries.

Every Prisma model must have at least one unique identifier:

*   `@id` or `@@id` for primary key
*   `@unique` or `@@unique` for unique constraint

