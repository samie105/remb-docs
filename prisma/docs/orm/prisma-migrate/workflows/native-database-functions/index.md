---
title: "Native database functions"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:52.268Z"
content_hash: "87b866f213f51b76f011637d472326d8ea0724e01e5a7f7f2d7cfeecf1ed73ca"
menu_path: ["Native database functions"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-migrate/workflows/generating-down-migrations/index.md", "title": "Generating down migrations"}
nav_next: {"path": "prisma/docs/orm/prisma-migrate/workflows/native-database-types/index.md", "title": "Native database types"}
---

Workflows

How to enable PostgreSQL native database functions for projects that use Prisma Migrate.

In PostgreSQL, some [native database functions](prisma/docs/orm/prisma-schema/data-model/unsupported-database-features/index.md#native-database-functions) are part of optional extensions. For example, in PostgreSQL versions 12.13 and earlier the `gen_random_uuid()` function is part of the [`pgcrypto`](https://www.postgresql.org/docs/10/pgcrypto.html) extension.

To use a PostgreSQL extension, you must install it on the file system of your database server and then activate the extension. If you use Prisma Migrate, this must be done as part of a migration.

In Prisma ORM versions 4.5.0 and later, you can activate the extension by declaring it in your Prisma schema with the [`postgresqlExtensions` preview feature](prisma/docs/orm/prisma-schema/postgresql-extensions/index.md):

```
generator client {
  provider        = "prisma-client"
  output          = "./generated"
  previewFeatures = ["postgresqlExtensions"] 
}

datasource db {
  provider   = "postgresql"
  extensions = [pgcrypto] 
}
```

You can then apply these changes to your database with Prisma Migrate. See [How to migrate PostgreSQL extensions](prisma/docs/orm/prisma-schema/postgresql-extensions/index.md) for details.

In earlier versions of Prisma ORM, you must instead add a SQL command to your migration file to activate the extension. See [How to install a PostgreSQL extension as part of a migration](#how-to-install-a-postgresql-extension-as-part-of-a-migration).

## [How to install a PostgreSQL extension as part of a migration](#how-to-install-a-postgresql-extension-as-part-of-a-migration)

This section describes how to add a SQL command to a migration file to activate a PostgreSQL extension. If you manage PostgreSQL extensions in your Prisma Schema with the `postgresqlExtensions` preview feature instead, see [How to migrate PostgreSQL extensions](prisma/docs/orm/prisma-schema/postgresql-extensions/index.md).

The following example demonstrates how to install the `pgcrypto` extension as part of a migration:

*   Add the field with the native database function to your schema:

```
model User {
 id String @id @default(dbgenerated("gen_random_uuid()")) @db.Uuid
}
```

If you include a cast operator (such as `::TEXT`), you must surround the entire function with parentheses:

```
@default(dbgenerated("(gen_random_uuid()::TEXT)"))
```

*   Use the `--create-only` flag to generate a new migration without applying it:

*   Open the generated `migration.sql` file and enable the `pgcrypto` module:

```
CREATE EXTENSION IF NOT EXISTS pgcrypto;

ADD COLUMN "id" UUID NOT NULL DEFAULT gen_random_uuid(),
ADD PRIMARY KEY ("id");
```

*   Apply the migration:

Each time you reset the database or add a new member to your team, all required functions are part of the migration history.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-migrate/workflows/native-database-functions.mdx)


