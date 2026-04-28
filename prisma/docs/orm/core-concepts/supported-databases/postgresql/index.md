---
title: "PostgreSQL"
source: "https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql"
canonical_url: "https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:36:52.381Z"
content_hash: "3b9c3ef5cfcbc21c4098e7f1bef10d56853edb4236cc1151187f922fd9ee60a7"
menu_path: ["PostgreSQL"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/core-concepts/supported-databases/mysql/index.md", "title": "MySQL"}
nav_next: {"path": "prisma/docs/orm/core-concepts/supported-databases/sql-server/index.md", "title": "SQL Server"}
---

Supported databases

Use Prisma ORM with PostgreSQL databases including self-hosted, serverless (Neon, Supabase), and CockroachDB

Prisma ORM supports PostgreSQL and PostgreSQL-compatible databases including self-hosted PostgreSQL, serverless providers (Neon, Supabase), and CockroachDB.

Configure the provider in your Prisma schema:

schema.prisma

```
datasource db {
  provider = "postgresql" // or "cockroachdb" for CockroachDB
}
```

**Self-hosted PostgreSQL:**

prisma.config.ts

```
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DATABASE_URL"), // postgres://user:pass@host:5432/db
  },
});
```

**Serverless (Neon/Supabase):**

Use separate URLs for CLI (direct) and runtime (pooled):

.env

```
DATABASE_URL="postgres://user:pass@host-pooler:6543/db?pgbouncer=true"
DIRECT_URL="postgres://user:pass@host:5432/db"
```

prisma.config.ts

```
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DIRECT_URL"), // CLI uses direct connection
  },
});
```

Use JavaScript database drivers via [driver adapters](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md#driver-adapters):

**Standard PostgreSQL with `pg`:**

```
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "./generated/prisma";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
const prisma = new PrismaClient({ adapter });
```

**Neon serverless:**

```
import { PrismaNeon } from "@prisma/adapter-neon";
import { PrismaClient } from "./generated/prisma";

const adapter = new PrismaNeon({ connectionString: process.env.DATABASE_URL });
const prisma = new PrismaClient({ adapter });
```

### [Self-hosted PostgreSQL](#self-hosted-postgresql)

Standard PostgreSQL server (9.6+).

-   Connection URL: `postgresql://user:pass@host:5432/database`
-   Full Prisma Migrate support
-   Use `prisma migrate dev` for development
-   TLS/SSL configuration via connection string parameters

**Connection string arguments:**

| Argument | Default | Description |
| --- | --- | --- |
| `schema` | `public` | PostgreSQL schema to use |
| `connect_timeout` | `5` | Seconds to wait for connection (0 = no timeout) |
| `sslmode` | `prefer` | TLS mode: `prefer`, `disable`, `require` |
| `sslcert` |  | Path to server certificate |
| `sslidentity` |  | Path to PKCS12 certificate |

### [Neon](#neon)

Serverless PostgreSQL with automatic scaling and branching.

-   Connection URL: `postgres://user:pass@host-pooler.region.aws.neon.tech:5432/db`
-   Add `-pooler` to hostname for connection pooling (PgBouncer, 10k connections)
-   Compute scales to zero after 5 minutes inactivity
-   Cold start: 500ms - few seconds
-   Database branching for development workflows

**Timeout configuration:** Configure connection and pool timeouts via your [driver adapter](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool/index.md) (e.g. `connectionTimeoutMillis` for `pg`).

**Resources:** [Neon docs](https://neon.tech/docs) • [Connection pooling](https://neon.tech/docs/connect/connection-pooling)

### [Supabase](#supabase)

PostgreSQL hosting with built-in auth, storage, and real-time features.

**Connection types:**

-   **Direct:** `db.[project-ref].supabase.co:5432`
-   **Transaction pooler:** Port `6543` with `?pgbouncer=true`
-   **Session pooler:** Port `5432` on pooler host

**Key features:**

-   Supavisor connection pooling
-   Built-in PostgreSQL extensions
-   Integrated with Supabase ecosystem
-   Automated backups

**Resources:** [Supabase docs](https://supabase.com/docs) • [Prisma integration](https://supabase.com/partners/integrations/prisma)

### [CockroachDB](#cockroachdb)

Distributed, PostgreSQL-compatible database designed for scalability and high availability.

-   Use `provider = "cockroachdb"` in schema
-   Connection URL: `postgresql://user:pass@host:26257/database`
-   Built-in replication and automated failover
-   Horizontal scaling with no single point of failure

**Key differences:**

| Feature | PostgreSQL | CockroachDB |
| --- | --- | --- |
| Native types | `VARCHAR(n)` | `STRING(n)` |
| ID generation | `autoincrement()` | Uses `unique_rowid()` |
| Sequential IDs | Recommended | Avoid (use `autoincrement()` instead) |

**ID generation example:**

```
model User {
  id   BigInt @id @default(autoincrement()) // Uses unique_rowid()
  name String
}
```

For compatibility with existing databases, use `sequence()`:

```
model User {
  id   Int    @id @default(sequence())
  name String
}
```

**Resources:** [CockroachDB docs](https://www.cockroachlabs.com/docs/) • [Primary key best practices](https://www.cockroachlabs.com/docs/stable/schema-design-table#primary-key-best-practices)

### [Prisma to PostgreSQL](#prisma-to-postgresql)

| Prisma | PostgreSQL | CockroachDB |
| --- | --- | --- |
| `String` | `text` | `STRING` |
| `Boolean` | `boolean` | `BOOL` |
| `Int` | `integer` | `INT4` |
| `BigInt` | `bigint` | `INT8` |
| `Float` | `double precision` | `FLOAT8` |
| `Decimal` | `decimal(65,30)` | `DECIMAL` |
| `DateTime` | `timestamp(3)` | `TIMESTAMP` |
| `Json` | `jsonb` | `JSONB` |
| `Bytes` | `bytea` | `BYTES` |

See [full type mapping reference](prisma/docs/orm/reference/prisma-schema-reference/index.md#model-field-scalar-types) for complete details.

**SSL connections:**

```
DATABASE_URL="postgresql://user:pass@host:5432/db?sslmode=require&sslcert=./cert.pem"
```

-   `sslmode=prefer` (default) - Use TLS if available
-   `sslmode=require` - Require TLS or fail
-   `sslmode=disable` - No TLS

**Socket connections:**

```
DATABASE_URL="postgresql://user:pass@localhost/db?host=/var/run/postgresql/"
```

**Specifying schema with driver adapters:**

```
const adapter = new PrismaPg(
  { connectionString: process.env.DATABASE_URL },
  { schema: "mySchema" }
);
```

**Connection pool defaults (Prisma ORM v7):**

Driver adapters use `pg` defaults which differ from v6:

-   **Connection timeout:** `0` (no timeout) vs v6's `5s`
-   **Idle timeout:** `10s` vs v6's `300s`

See [connection pool guide](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool/index.md#postgresql-using-the-pg-driver-adapter) for configuration.
