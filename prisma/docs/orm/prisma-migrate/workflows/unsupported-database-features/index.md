---
title: "Unsupported database features (Prisma Migrate)"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/unsupported-database-features"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/unsupported-database-features"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:37.846Z"
content_hash: "367458529fcfc9b4310d39921b12983207237f98e806b044c14577789115dfb6"
menu_path: ["Unsupported database features (Prisma Migrate)"]
section_path: []
---
Workflows

How to include unsupported database features for projects that use Prisma Migrate

Prisma Migrate uses the Prisma schema to determine what features to create in the database. However, some database features [cannot be represented in the Prisma schema](https://www.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features) , including but not limited to:

*   Stored procedures
*   Triggers
*   Views

To add an unsupported feature to your database, you must [customize a migration](https://www.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations) to include that feature before you apply it.

To customize a migration to include an unsupported feature:

*   Use the `--create-only` flag to generate a new migration without applying it:

*   Open the generated `migration.sql` file and add the unsupported feature - for example, a trigger function:

```
CREATE OR REPLACE FUNCTION notify_on_insert()
RETURNS TRIGGER AS $$
BEGIN
  PERFORM pg_notify('new_record', NEW.id::text);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

*   Apply the migration:

*   Commit the modified migration to source control.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-migrate/workflows/unsupported-database-features.mdx)
