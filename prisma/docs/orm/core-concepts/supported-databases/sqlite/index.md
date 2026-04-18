---
title: "SQLite"
source: "https://www.prisma.io/docs/orm/core-concepts/supported-databases/sqlite"
canonical_url: "https://www.prisma.io/docs/orm/core-concepts/supported-databases/sqlite"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:44.580Z"
content_hash: "2bea168d9d2889db5a30043b70aa61f7ba66f8342f84b338823ac3cc2203f6a4"
menu_path: ["SQLite"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/core-concepts/supported-databases/sql-server/index.md", "title": "SQL Server"}
nav_next: {"path": "prisma/docs/orm/more/comparisons/prisma-and-drizzle/index.md", "title": "Drizzle"}
---

Supported databases

Use Prisma ORM with SQLite databases including local SQLite, Turso (libSQL), and Cloudflare D1

Prisma ORM supports SQLite and SQLite-compatible databases. This includes local SQLite files, Turso's distributed libSQL, and Cloudflare's serverless D1.

Configure the SQLite provider in your Prisma schema:

```
datasource db {
  provider = "sqlite"
}
```

Set the connection URL in `prisma.config.ts`:

```
import { defineConfig } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: "file:./dev.db", // or libsql:// for Turso
  },
});
```

Instead of Prisma's built-in driver, you can use JavaScript database drivers via [driver adapters](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md#driver-adapters):

**Local SQLite with `better-sqlite3`:**

```
import { PrismaBetterSqlite3 } from "@prisma/adapter-better-sqlite3";
import { PrismaClient } from "./generated/prisma";

const adapter = new PrismaBetterSqlite3({ url: "file:./prisma/dev.db" });
const prisma = new PrismaClient({ adapter });
```

**Turso with `@prisma/adapter-libsql`:**

```
import { PrismaLibSQL } from "@prisma/adapter-libsql";
import { PrismaClient } from "./generated/prisma";

const adapter = new PrismaLibSQL({
  url: process.env.TURSO_DATABASE_URL,
  authToken: process.env.TURSO_AUTH_TOKEN,
});
const prisma = new PrismaClient({ adapter });
```

**Cloudflare D1 with `@prisma/adapter-d1`:**

```
import { PrismaD1 } from "@prisma/adapter-d1";
import { PrismaClient } from "./generated/prisma";

const adapter = new PrismaD1(env.DB); // D1 binding in Workers
const prisma = new PrismaClient({ adapter });
```

### [Local SQLite](#local-sqlite)

Standard SQLite database files (`.db`). Connection URL format: `file:./path/to/database.db`

*   Use `prisma migrate dev` for schema changes
*   Store database file anywhere in your filesystem
*   Best for development and small applications

### [Turso (libSQL)](#turso-libsql)

Edge-hosted, distributed SQLite-compatible database.

*   Connection URL format: `libsql://[hostname]`
*   Requires authentication token
*   Supports embedded replicas for faster local reads
*   Use local SQLite file + Turso CLI for migrations (see [Turso docs](https://docs.turso.tech/))

**Key differences:**

*   Remote access over HTTP
*   Replication and automated backups
*   Schema changes via `prisma migrate diff` + Turso CLI

### [Cloudflare D1](#cloudflare-d1)

Serverless SQLite database for Cloudflare Workers.

*   Automatic read-replication across regions
*   Schema changes via Wrangler CLI + `prisma migrate diff`
*   Local (`.wrangler/state`) and remote versions available

**Key differences:**

*   No transaction support currently
*   Migrations via Wrangler: `wrangler d1 migrations apply`
*   Deploy with Cloudflare Workers

Prisma ORM

SQLite

`String`

`TEXT`

`Boolean`

`BOOLEAN`

`Int`

`INTEGER`

`BigInt`

`INTEGER`

`Float`

`REAL`

`Decimal`

`DECIMAL`

`DateTime`

`NUMERIC`

`Json`

`JSONB`

`Bytes`

`BLOB`

`Enum`

`TEXT`

**Timestamp format with driver adapters:**

Configure how `DateTime` values are stored:

```
const adapter = new PrismaBetterSqlite3(
  { url: "file:./dev.db" },
  { timestampFormat: "unixepoch-ms" } // For backward compatibility
);
```

*   **ISO 8601 (default)**: Best for new projects
*   **`unixepoch-ms`**: Required for migrating from Prisma's native driver

**Enum validation:**

SQLite doesn't enforce enum values at the database level. Invalid values will cause Prisma Client queries to fail at runtime.

**Integer overflow:**

Prisma ORM validates that numbers fit within integer boundaries. If a value exceeds limits, you'll get a P2023 error.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/core-concepts/supported-databases/sqlite.mdx)

