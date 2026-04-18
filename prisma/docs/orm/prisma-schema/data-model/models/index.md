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
---
Learn about the concepts for building your data model with Prisma: Models, scalar types, enums, attributes, functions, IDs, default values and more

The data model definition part of the [Prisma schema](https://www.prisma.io/docs/orm/prisma-schema/overview) defines your application models (also called **Prisma models**). Models:

*   Represent the **entities** of your application domain
*   Map to the **tables** (relational databases like PostgreSQL) or **collections** (MongoDB) in your database
*   Form the foundation of the **queries** available in the generated [Prisma Client API](https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction)
*   When used with TypeScript, Prisma Client provides generated **type definitions** for your models and any [variations](https://www.prisma.io/docs/orm/prisma-client/type-safety/operating-against-partial-structures-of-model-types) of them to make database access entirely type safe.

The following schema describes a blogging platform - the data model definition is highlighted:

The data model definition is made up of:

*   [Models](#defining-models) ([`model`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#model) primitives) that define a number of fields, including [relations between models](#relation-fields)
*   [Enums](#defining-enums) ([`enum`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#enum) primitives) (if your connector supports Enums)
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

*   **Write the data model manually and use Prisma Migrate**: You can write your data model manually and map it to your database using [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate). In this case, the data model is the single source of truth for the models of your application.
*   **Generate the data model via introspection**: When you have an existing database or prefer migrating your database schema with SQL, you generate the data model by [introspecting](https://www.prisma.io/docs/orm/prisma-schema/introspection) your database. In this case, the database schema is the single source of truth for the models of your application.

Models represent the entities of your application domain. Models are represented by [`model`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#model) blocks and define a number of [fields](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#model-fields). In the example data model above, `User`, `Profile`, `Post` and `Category` are models.

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

Prisma model [naming conventions (singular form, PascalCase)](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#naming-conventions) do not always match table names in the database. A common approach for naming tables/collections in databases is to use plural form and [snake\_case](https://en.wikipedia.org/wiki/Snake_case) notation - for example: `comments`. When you introspect a database with a table named `comments`, the resulting Prisma model will look like this:

```
model comments {
  // Fields
}
```

However, you can still adhere to the naming convention without renaming the underlying `comments` table in the database by using the [`@@map`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference) attribute:

```
model Comment {
  // Fields

  @@map("comments")
}
```

With this model definition, Prisma ORM automatically maps the `Comment` model to the `comments` table in the underlying database.

> **Note**: You can also [`@map`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#map) a column name or enum value, and `@@map` an enum name.

`@map` and `@@map` allow you to [tune the shape of your Prisma Client API](https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names#using-map-and-map-to-rename-fields-and-models-in-the-prisma-client-api) by decoupling model and field names from table and column names in the underlying database.

The properties of a model are called _fields_, which consist of:

*   A **[field name](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#model-fields)**
*   A **[field type](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#model-fields)**
*   Optional **[type modifiers](#type-modifiers)**
*   Optional **[attributes](#defining-attributes)**, including [native database type attributes](#native-types-mapping)

A field's type determines its _structure_, and fits into one of two categories:

*   [Scalar types](#scalar-fields) (includes [enums](#defining-enums)) that map to columns (relational databases) or document fields (MongoDB) - for example, [`String`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#string) or [`Int`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#int)
*   Model types (the field is then called [relation field](https://www.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields)) - for example `Post` or `Comment[]`

### [Scalar fields](#scalar-fields)

The following example extends the `Comment` and `Tag` models with several scalar types. Some fields include [attributes](#defining-attributes):

See [complete list of scalar field types](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types) .

### [Relation fields](#relation-fields)

A relation field's type is another model - for example, a post (`Post`) can have multiple comments (`Comment[]`):

Refer to the [relations documentation](https://www.prisma.io/docs/orm/prisma-schema/data-model/relations) for more examples and information about relationships between models.

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
*   Only added during [introspection](https://www.prisma.io/docs/orm/prisma-schema/introspection) if the native type differs from the default

See [native database type attributes](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types) for the complete list.

### [Type modifiers](#type-modifiers)

The type of a field can be modified by appending either of two modifiers:

*   [`[]`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#-modifier) Make a field a list
*   [`?`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#-modifier-1) Make a field optional

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

When you introspect a relational database, unsupported data types are added as [`Unsupported`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#unsupported):

```
location    Unsupported("POLYGON")?
```

Fields of type `Unsupported` don't appear in the generated Prisma Client API, but you can still use [raw database access](https://www.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries) to query them.

Attributes modify the behavior of fields or model blocks. The following example includes three field attributes ([`@id`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#id) , [`@default`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#default) , and [`@unique`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#unique) ) and one block attribute ([`@@unique`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference)):

Some attributes accept [arguments](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-argument-types) - for example, `@default` accepts `true` or `false`:

```
isAdmin   Boolean @default(false) // short form of @default(value: false)
```

See [complete list of field and block attributes](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#attributes)

### [Defining an ID field](#defining-an-id-field)

An ID uniquely identifies individual records of a model. A model can only have _one_ ID:

*   In **relational databases**, the ID can be a single field or based on multiple fields. If a model does not have an `@id` or an `@@id`, you must define a mandatory `@unique` field or `@@unique` block instead.
*   In **MongoDB**, an ID must be a single field that defines an `@id` attribute and a `@map("_id")` attribute.

#### [Defining IDs in relational databases](#defining-ids-in-relational-databases)

In relational databases, an ID can be defined by a single field using the [`@id`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#id) attribute, or multiple fields using the [`@@id`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference) attribute.

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

You can also provide your own name for the composite ID using the [`@@id`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference) attribute's `name` field:

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

The MongoDB connector has [specific rules for defining an ID field](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#mongodb) that differs from relational databases. An ID must be defined by a single field using the [`@id`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#id) attribute and must include `@map("_id")`.

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

You can define default values for scalar fields using the [`@default`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#default) attribute:

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
*   **Functions**: [`now()`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#now), [`uuid()`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#uuid), [`cuid()`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#cuid)
*   **JSON**: Use escaped strings, e.g., `@default("{ \"hello\": \"world\" }")`

See [attribute functions](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions) for connector support details.

### [Defining a unique field](#defining-a-unique-field)

Unique attributes can be defined on a single field using [`@unique`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#unique), or on multiple fields using [`@@unique`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference):

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

See [working with composite unique identifiers](https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-composite-ids-and-constraints) for Prisma Client usage.

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

Define indexes via [`@@index`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#index):

```
model Post {
  id      Int     @id @default(autoincrement())
  title   String
  content String?

  @@index([title, content])
}
```

For MongoDB composite types, use dot notation: `@@index([address.city.name])`

See [custom index names](https://www.prisma.io/docs/orm/prisma-schema/data-model/database-mapping#constraint-and-index-names) for naming customization.

Enums are defined via the [`enum`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#enum) block when [supported by your database](https://www.prisma.io/docs/orm/reference/database-features#misc):

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

The Prisma schema supports [functions](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions) for default values:

```
model Post {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  uuid      String   @default(uuid())
}
```

Common functions: `now()`, `uuid()`, `cuid()`, `autoincrement()`, `auto()` (MongoDB ObjectId)

See [relations documentation](https://www.prisma.io/docs/orm/prisma-schema/data-model/relations) for relationship details.

### [Queries (CRUD)](#queries-crud)

Every model generates CRUD queries in the [Prisma Client API](https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction):

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
