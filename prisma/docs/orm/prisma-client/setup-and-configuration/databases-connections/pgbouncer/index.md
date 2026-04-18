---
title: "Configure Prisma Client with PgBouncer"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:11.145Z"
content_hash: "0cb12ba8a1e6ef83f7770745c458862cb221f11b39eba312f07fcdbc5e18426e"
menu_path: ["Configure Prisma Client with PgBouncer"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md", "title": "Database connections"}
nav_next: {"path": "prisma/docs/orm/prisma-schema/data-model/relations/index.md", "title": "Relations"}
---

# PgBouncer (pooled) connection string used by Prisma Client.
DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE?pgbouncer=true"

# Direct database connection string used by Prisma CLI. 
DIRECT_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE"
```

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DIRECT_URL"),
  },
});
```

```
import { PrismaClient } from "../prisma/generated/client";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
export const prisma = new PrismaClient({ adapter });
```

With this setup, PgBouncer stays in the path for runtime traffic, while Prisma CLI commands (`prisma migrate dev`, `prisma db push`, `prisma db pull`, and so on) always use the direct connection string defined in `prisma.config.ts`.

### [PgBouncer with different database providers](#pgbouncer-with-different-database-providers)

There are sometimes minor differences in how to connect directly to a Postgres database that depend on the provider hosting the database.

Below are links to information on how to set up these connections with providers who have setup steps not covered here in our documentation:

*   [Connecting directly to a PostgreSQL database hosted on Digital Ocean](https://github.com/prisma/prisma/issues/6157)
*   [Connecting directly to a PostgreSQL database hosted on ScaleGrid](https://github.com/prisma/prisma/issues/6701#issuecomment-824387959)

Supabase's Supavisor behaves similarly to [PgBouncer](#pgbouncer). You can add `?pgbouncer=true` to your connection pooled connection string available via your [Supabase database settings](https://supabase.com/dashboard/project/_/settings/database).

Although Prisma ORM does not have explicit support for other connection poolers, if the limitations are similar to the ones of [PgBouncer](#pgbouncer) you can usually also use `pgbouncer=true` in your connection string to put Prisma ORM in a mode that works with them as well.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer.mdx)

