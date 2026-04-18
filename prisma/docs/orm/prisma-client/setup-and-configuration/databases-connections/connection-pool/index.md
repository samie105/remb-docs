---
title: "Connection pool"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:58.000Z"
content_hash: "fd14e1a8be1538abb79dbc14d038207ef5fb436ae2fe83a63ac8af49024e39e1"
menu_path: ["Connection pool"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/queries/advanced/query-optimization-performance/index.md", "title": "Query optimization"}
nav_next: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md", "title": "Database connections"}
---

Setup and Configuration

Database Connections

Prisma Client uses a connection pool (from the database driver or driver adapter) to store and manage database connections.

Prisma Client uses a **connection pool** of database connections (managed by the database driver when using [driver adapters](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md)). The pool is created when Prisma Client opens the _first_ connection to the database, which can happen in one of two ways:

*   By [explicitly calling `$connect()`](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management/index.md#connect) _or_
*   By running the first query, which calls `$connect()` under the hood

Relational database connectors use Prisma ORM's own connection pool, and the MongoDB connectors uses the [MongoDB driver connection pool](https://github.com/mongodb/specifications/blob/master/source/connection-monitoring-and-pooling/connection-monitoring-and-pooling.rst).

Questions answered in this page

*   How do I size Prisma's connection pool?
*   How do I set pool timeouts and limits?
*   When should I use PgBouncer with Prisma?

Starting with Prisma ORM v7, relational datasources instantiate Prisma Client with [driver adapters](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md) by default. Driver adapters rely on the Node.js driver you supply, so connection pooling defaults (and configuration) now come from the driver itself.

Use the tables below to translate Prisma ORM v6 connection URL parameters to the Prisma ORM v7 driver adapter fields alongside their defaults.

### [Prisma ORM v7 driver adapter defaults](#prisma-orm-v7-driver-adapter-defaults)

The following tables document the default connection pool settings for each driver adapter.

#### [PostgreSQL (using the `pg` driver adapter)](#postgresql-using-the-pg-driver-adapter)

Here are the default connection pool settings for the `pg` driver adapter:

Behavior

v6 URL parameter

v6 default

v7 `pg` config field

v7 default

Pool size

`connection_limit`

`num_cpus::get_physical() * 2 + 1`

`max`

`10`

Acquire timeout

`pool_timeout`

`10s`

`connectionTimeoutMillis`

`0` (no timeout)

Connection timeout

`connect_timeout`

`5s`

`connectionTimeoutMillis`

`0` (no timeout)

Idle timeout

`max_idle_connection_lifetime`

`300s`

`idleTimeoutMillis`

`10s`

Connection lifetime

`max_connection_lifetime`

`0` (no timeout)

`maxLifetimeSeconds`

`0` (no timeout)

Example: Matching Prisma ORM v6 defaults with the `pg` driver adapter

If you want to preserve the same timeout behavior you had in Prisma ORM v6, pass the following configuration when instantiating the driver adapter:

```
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL,
  // Match Prisma ORM v6 defaults:
  connectionTimeoutMillis: 5_000, // v6 connect_timeout was 5s
  idleTimeoutMillis: 300_000, // v6 max_idle_connection_lifetime was 300s
});
```

#### [MySQL or MariaDB (using the `mariadb` driver)](#mysql-or-mariadb-using-the-mariadb-driver)

Here are the default connection pool settings for the `mariadb` driver adapter:

Behavior

v6 URL parameter

v6 default

v7 `mariadb` config field

v7 default

Pool size

`connection_limit`

`num_cpus::get_physical() * 2 + 1`

`connectionLimit`

`10`

Acquire timeout

`pool_timeout`

`10s`

`acquireTimeout`

`10s`

Connection timeout

`connect_timeout`

`5s`

`connectTimeout`

`1s`

Idle timeout

`max_idle_connection_lifetime`

`300s`

`idleTimeout`

`1800s`

Example: Matching Prisma ORM v6 defaults with the `mariadb` driver adapter

If you want to preserve the same timeout behavior you had in Prisma ORM v6, pass the following configuration when instantiating the driver adapter:

```
import { PrismaMariaDb } from "@prisma/adapter-mariadb";

const adapter = new PrismaMariaDb({
  host: "localhost",
  port: 3306,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  // Match Prisma ORM v6 defaults:
  connectTimeout: 5_000, // v6 connect_timeout was 5s
  idleTimeout: 300, // v6 max_idle_connection_lifetime was 300s (note: in seconds, not ms)
});
```

#### [SQL Server (using the `mssql` driver)](#sql-server-using-the-mssql-driver)

Here are the default connection pool settings for the `mssql` driver adapter:

Behavior

v6 URL parameter

v6 default

v7 `mssql` config field

v7 default

Pool size

`connection_limit`

`num_cpus::get_physical() * 2 + 1`

`pool.max`

`10`

Connection timeout

`connect_timeout`

`5s`

`connectionTimeout`

`15s`

Idle timeout

`max_idle_connection_lifetime`

`300s`

`pool.idleTimeoutMillis`

`30s`

Example: Matching Prisma ORM v6 defaults with the `mssql` driver adapter

If you want to preserve the same timeout behavior you had in Prisma ORM v6, pass the following configuration when instantiating the driver adapter:

```
import { PrismaMssql } from "@prisma/adapter-mssql";

const adapter = new PrismaMssql({
  server: "localhost",
  port: 1433,
  database: "mydb",
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  // Match Prisma ORM v6 defaults:
  connectionTimeout: 5_000, // v6 connect_timeout was 5s
  pool: {
    idleTimeoutMillis: 300_000, // v6 max_idle_connection_lifetime was 300s
  },
});
```

The MongoDB connector does not use the Prisma ORM connection pool. The connection pool is managed internally by the MongoDB driver and [configured via connection string parameters](https://www.mongodb.com/docs/manual/reference/connection-string-options/#connection-pool-options).

The pool size cannot exceed what the underlying database can support. Configure pool size and timeouts via your [driver adapter](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool/index.md) (see the tables above). This is a particular challenge in serverless environments, where each function manages an instance of `PrismaClient` and its own connection pool.

Consider introducing [an external connection pooler like PgBouncer](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md#pgbouncer) to prevent your application or functions from exhausting the database connection limit.

When using Prisma Client with a driver adapter, database connections are managed by the driver and its pool. They are not exposed to the developer and it is not possible to manually access individual connections.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool.mdx)


