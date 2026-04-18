---
title: "Native database types"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/native-database-types"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/native-database-types"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:56.252Z"
content_hash: "b6928fc7c19a41f45b1365b636fd15de7e1b87f6a0abf38ca7fbb78bd74fad71"
menu_path: ["Native database types"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-migrate/workflows/native-database-functions/index.md", "title": "Native database functions"}
nav_next: {"path": "prisma/docs/orm/prisma-migrate/workflows/patching-and-hotfixing/index.md", "title": "Patching & hotfixing"}
---

Workflows

Native database types

Prisma Migrate translates the model defined in your [Prisma schema](prisma/docs/orm/prisma-schema/overview/index.md) into features in your database.

![A diagram that shows a Prisma schema on the left (labeled: Prisma schema, models) and a database on the right (labeled: Database, tables). Two parallel arrows connect the schema and the database, showing how '@unique' maps to 'UNIQUE' and '@id' maps to 'PRIMARY KEY'.](https://www.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/migrate-mapping.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Every¹ feature in your [data model](prisma/docs/orm/prisma-schema/data-model/models/index.md) maps to a corresponding feature in the underlying database. **If you can define a feature in the Prisma schema, it is supported by Prisma Migrate.**

For a complete list of Prisma schema features, refer to:

*   [Database features matrix](prisma/docs/orm/reference/database-features/index.md) for a list of database features and what they map to in the Prisma schema.
*   [Prisma schema reference](prisma/docs/orm/reference/prisma-schema-reference/index.md) for a list of all Prisma schema features, including field types, attributes, and functions.

Prisma Migrate also supports mapping each field to a [specific native type](#mapping-fields-to-a-specific-native-type), and there are ways to [include features without a Prisma schema equivalent in your database](#handling-unsupported-database-features).

Each Prisma ORM type maps to a default underlying database type - for example, the PostgreSQL connector maps `String` to `text` by default. [Native database type attributes](prisma/docs/orm/prisma-schema/data-model/models/index.md#native-types-mapping) determines which _specific_ native type should be created in the database.

In the following example, the `name` and `title` fields have a `@db.VarChar(X)` type attribute:

```
datasource db {
  provider = "postgresql"
}

model User {
  id    Int    @id @default(autoincrement())
  name  String @db.VarChar(200)
  posts Post[]
}

model Post {
  id        Int     @id @default(autoincrement())
  title     String  @db.VarChar(150)
  published Boolean @default(true)
  authorId  Int
  author    User    @relation(fields: [authorId], references: [id])
}
```

Prisma Migrate uses the specified types when it creates a migration:

```
  -- CreateTable
CREATE TABLE "User" (
    "id" SERIAL,
    "name" VARCHAR(200) NOT NULL,
    PRIMARY KEY ("id")
);
  -- CreateTable
CREATE TABLE "Post" (
    "id" SERIAL,
    "title" VARCHAR(150) NOT NULL,
    "published" BOOLEAN NOT NULL DEFAULT true,
    "authorId" INTEGER NOT NULL,
    PRIMARY KEY ("id")
);

  -- AddForeignKey
ALTER TABLE "Post" ADD FOREIGN KEY("authorId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

### [Mappings by Prisma ORM type](#mappings-by-prisma-orm-type)

For type mappings organized by Prisma ORM type, refer to the [Prisma schema reference](prisma/docs/orm/reference/prisma-schema-reference/index.md#model-field-scalar-types) documentation.

### [Mappings by database provider](#mappings-by-database-provider)

For type mappings organized by database provider, see:

*   [PostgreSQL mappings](prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md#prisma-to-postgresql)
*   [MySQL mappings](prisma/docs/orm/core-concepts/supported-databases/mysql/index.md#type-mapping-between-mysql-and-prisma-schema)
*   [Microsoft SQL Server mappings](prisma/docs/orm/core-concepts/supported-databases/sql-server/index.md#type-mappings)
*   [SQLite mappings](prisma/docs/orm/core-concepts/supported-databases/sqlite/index.md#type-mappings)

Prisma Migrate cannot automatically create database features that have no equivalent in Prisma Schema Language (PSL). For example, there is currently no way to define a stored procedure or a trigger in PSL. However, there are ways to add unsupported features to your database with Prisma Migrate:

*   [Handle unsupported field types](prisma/docs/orm/prisma-schema/data-model/unsupported-database-features/index.md#unsupported-field-types) (like `circle`)
*   [Handle unsupported features](prisma/docs/orm/prisma-schema/data-model/unsupported-database-features/index.md#unsupported-database-features), like stored procedures
*   [How to use native database functions](prisma/docs/orm/prisma-schema/data-model/unsupported-database-features/index.md#native-database-functions)

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-migrate/workflows/native-database-types.mdx)

