---
title: "Overview of Prisma Schema"
source: "https://www.prisma.io/docs/orm/prisma-schema/overview"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/overview"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:42:45.551Z"
content_hash: "663ee8a71be4c9a6964ad1ceed5f16b4b16417b12dfd17d6edb62cf3a3810b98"
menu_path: ["Overview of Prisma Schema"]
section_path: []
tab_variants: ["Relational Databases","MongoDB"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-schema/data-model/views/index.md", "title": "Views"}
nav_next: {"path": "prisma/docs/orm/prisma-schema/overview/data-sources/index.md", "title": "Data sources"}
---

Overview

## Overview of Prisma Schema

The Prisma schema is the main method of configuration when using Prisma. It is typically called schema.prisma and contains your database connection and data model

The Prisma Schema (or _schema_ for short) is the main method of configuration for your Prisma ORM setup. It consists of the following parts:

-   [**Data sources**](prisma/docs/orm/prisma-schema/overview/data-sources/index.md): Specify the details of the data sources Prisma ORM should connect to (e.g. a PostgreSQL database)
-   [**Generators**](prisma/docs/orm/prisma-schema/overview/generators/index.md): Specifies what clients should be generated based on the data model (e.g. Prisma Client)
-   [**Data model definition**](prisma/docs/orm/prisma-schema/data-model/models/index.md): Specifies your application [models](prisma/docs/orm/prisma-schema/data-model/models/index.md#defining-models) (the shape of the data per data source) and their [relations](prisma/docs/orm/prisma-schema/data-model/relations/index.md)

It is typically a single file called `schema.prisma` (or multiple files with `.prisma` file extension) that is stored in a defined but customizable [location](prisma/docs/orm/prisma-schema/overview/location/index.md). You can also [organize your Prisma schema in multiple files](prisma/docs/orm/prisma-schema/overview/location/index.md#multi-file-prisma-schema) if you prefer that.

See the [Prisma schema API reference](prisma/docs/orm/reference/prisma-schema-reference/index.md) for detailed information about each section of the schema.

Whenever a `prisma` command is invoked, the CLI typically reads some information from the schema, e.g.:

-   `prisma generate`: Reads _all_ above mentioned information from the Prisma schema to generate the correct data source client code (e.g. Prisma Client).
-   `prisma migrate dev`: Reads the data sources and data model definition to create a new migration.

You can also [use environment variables](#accessing-environment-variables-from-the-schema) inside the schema to provide configuration options when a CLI command is invoked.

The following is an example of a Prisma Schema that specifies:

-   A data source (PostgreSQL or MongoDB)
-   A generator (Prisma Client)
-   A data model definition with two models (with one relation) and one `enum`
-   Several [native data type attributes](prisma/docs/orm/prisma-schema/data-model/models/index.md#native-types-mapping) (`@db.VarChar(255)`, `@db.ObjectId`)

Prisma Schema files are written in Prisma Schema Language (PSL). See the [data sources](prisma/docs/orm/prisma-schema/overview/data-sources/index.md), [generators](prisma/docs/orm/prisma-schema/overview/generators/index.md), [data model definition](prisma/docs/orm/prisma-schema/data-model/models/index.md) and of course [Prisma Schema API reference](prisma/docs/orm/reference/prisma-schema-reference/index.md) pages for details and examples.

### [VS Code](#vs-code)

Syntax highlighting for PSL is available via a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=Prisma.prisma) (which also lets you auto-format the contents of your Prisma schema and indicates syntax errors with red squiggly lines). Learn more about [setting up Prisma ORM in your editor](prisma/docs/orm/more/dev-environment/editor-setup/index.md).

### [GitHub](#github)

PSL code snippets on GitHub can be rendered with syntax highlighting as well by using the `.prisma` file extension or annotating fenced code blocks in Markdown with `prisma`:

```
```prisma
model User {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  email     String   @unique
  name      String?
}
```
```

You can use environment variables to provide configuration options when a CLI command is invoked, or a Prisma Client query is run.

Hardcoding URLs directly in your schema is possible but is discouraged because it poses a security risk. Using environment variables in the schema allows you to **keep secrets out of the schema** which in turn **improves the portability of the schema** by allowing you to use it in different environments.

Environment variables can be accessed using the `env()` function:

```
datasource db {
  provider = "postgresql"
}
```

You can use the `env()` function in the following places:

-   A datasource url
-   Generator binary targets

See [Environment variables](prisma/docs/orm/more/dev-environment/environment-variables/index.md) for more information about how to use an `.env` file during development.

There are three types of comments that are supported in Prisma Schema Language:

-   `// comment`: This comment is for the reader's clarity and is not present in the abstract syntax tree (AST) of the schema.
-   `/// comment`: These comments will show up in the abstract syntax tree (AST) of the schema as descriptions to AST nodes. Tools can then use these comments to provide additional information. All comments are attached to the next available node - [free-floating comments](https://github.com/prisma/prisma/issues/3544) are not supported and are not included in the AST.
-   `/* block comment */`: These comments will show up in the abstract syntax tree, similarly to `///` comments.

Here are some different examples:

```
/// This comment will get attached to the `User` node in the AST
model User {
  /// This comment will get attached to the `id` node in the AST
  id     Int   @default(autoincrement())
  // This comment is just for you
  weight Float /// This comment gets attached to the `weight` node
}

// This comment is just for you. It will not
// show up in the AST.

/// This comment will get attached to the
/// Customer node.
model Customer {
  /**
   * ...and so will this comment
   */
}
```

Prisma ORM supports formatting `.prisma` files automatically. There are two ways to format `.prisma` files:

-   Run the [`prisma format`](prisma/docs/orm/reference/prisma-cli-reference/index.md#format) command.
-   Install the [Prisma VS Code extension](https://marketplace.visualstudio.com/items?itemName=Prisma.prisma) and invoke the [VS Code format action](https://code.visualstudio.com/docs/editor/codebasics#_formatting) - manually or on save.

There are no configuration options - [formatting rules](#formatting-rules) are fixed (similar to Golang's `gofmt` but unlike Javascript's `prettier`):

### [Formatting rules](#formatting-rules)

#### [Configuration blocks are aligned by their = sign](#configuration-blocks-are-aligned-by-theirsign)

```
block _ {
  key      = "value"
  key2     = 1
  long_key = true
}
```

#### [Field definitions are aligned into columns separated by 2 or more spaces](#field-definitions-are-aligned-into-columns-separated-by-2-or-more-spaces)

```
block _ {
  id          String       @id
  first_name  LongNumeric  @default
}
```

#### [Empty lines resets block alignment and formatting rules](#empty-lines-resets-block-alignment-and-formatting-rules)

```
block _ {
  key   = "value"
  key2  = 1
  key10 = true

  long_key   = true
  long_key_2 = true
}
```

```
block _ {
  id  String  @id
              @default

  first_name  LongNumeric  @default
}
```

#### [Multiline field attributes are properly aligned with the rest of the field attributes](#multiline-field-attributes-are-properly-aligned-with-the-rest-of-the-field-attributes)

```
block _ {
  id          String       @id
                           @default
  first_name  LongNumeric  @default
}
```

#### [Block attributes are sorted to the end of the block](#block-attributes-are-sorted-to-the-end-of-the-block)

```
block _ {
  key   = "value"

  @@attribute
}
```
