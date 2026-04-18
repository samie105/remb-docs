---
title: "SQL Server"
source: "https://www.prisma.io/docs/orm/core-concepts/supported-databases/sql-server"
canonical_url: "https://www.prisma.io/docs/orm/core-concepts/supported-databases/sql-server"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:27.552Z"
content_hash: "11c66367f58eacf92fd582f17b1fc9c37db1d54755952aa2d4454b87b6ff22e0"
menu_path: ["SQL Server"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/core-concepts/supported-databases/mongodb/index.md", "title": "MongoDB"}
nav_next: {"path": "prisma/docs/orm/core-concepts/supported-databases/sqlite/index.md", "title": "SQLite"}
---

Supported databases

Use Prisma ORM with Microsoft SQL Server databases

Prisma ORM supports Microsoft SQL Server (2017+) databases.

Configure the SQL Server provider in your Prisma schema:

```
datasource db {
  provider = "sqlserver"
}
```

Set the connection URL in `prisma.config.ts`:

```
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DATABASE_URL"), // sqlserver://host:1433;database=db;...
  },
});
```

Use the `node-mssql` JavaScript database driver via [driver adapters](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md#driver-adapters):

```
import { PrismaMssql } from "@prisma/adapter-mssql";
import { PrismaClient } from "./generated/prisma";

const config = {
  server: "localhost",
  port: 1433,
  database: "mydb",
  user: "sa",
  password: "mypassword",
  options: {
    encrypt: true,
    trustServerCertificate: true, // For self-signed certificates
  },
};

const adapter = new PrismaMssql(config);
const prisma = new PrismaClient({ adapter });
```

SQL Server uses JDBC-style connection strings:

```
sqlserver://HOST[:PORT];database=DATABASE;user=USER;password=PASSWORD;encrypt=true
```

**Escaping special characters:**

If your credentials contain `: \ = ; / [ ] { }`, wrap values in curly braces:

```
sqlserver://host:1433;user={MyServer/User};password={Pass:Word;};database=db
```

### [Connection string arguments](#connection-string-arguments)

Argument

Default

Description

`database` / `initial catalog`

`master`

Database name

`user` / `username` / `uid`

SQL Server login or Windows username (if using `integratedSecurity`)

`password` / `pwd`

Password for user

`encrypt`

`true`

Use TLS: `true` (always), `false` (login only)

`integratedSecurity`

Windows authentication: `true`, `false`, `yes`, `no`

`schema`

`dbo`

Schema prefix for all queries

`connectTimeout`

`5`

Seconds to wait for connection

`socketTimeout`

Seconds to wait for each query

`poolTimeout`

`10`

Seconds to wait for connection from pool

`trustServerCertificate`

`false`

Trust server certificate without validation

`trustServerCertificateCA`

Path to CA certificate file (`.pem`, `.crt`, `.der`)

`ApplicationName`

Application name for the connection

**Using current Windows user:**

```
sqlserver://localhost:1433;database=sample;integratedSecurity=true;trustServerCertificate=true;
```

**Using specific Active Directory user:**

```
sqlserver://localhost:1433;database=sample;integratedSecurity=true;username=prisma;password=aBcD1234;trustServerCertificate=true;
```

**Named instance:**

```
sqlserver://mycomputer\sql2019;database=sample;integratedSecurity=true;trustServerCertificate=true;
```

Prisma

SQL Server

`String`

`NVARCHAR(1000)`

`Boolean`

`BIT`

`Int`

`INT`

`BigInt`

`BIGINT`

`Float`

`FLOAT(53)`

`Decimal`

`DECIMAL(32,16)`

`DateTime`

`DATETIME2`

`Json`

Not supported

`Bytes`

`VARBINARY(MAX)`

See [full type mapping reference](prisma/docs/orm/reference/prisma-schema-reference/index.md#model-field-scalar-types) for complete details.

**UNIQUE constraints:**

SQL Server [allows only one `NULL` value per `UNIQUE` constraint](https://learn.microsoft.com/en-us/sql/relational-databases/tables/unique-constraints-and-check-constraints). Use filtered indexes to work around this, but note they cannot be used as foreign keys.

**Cyclic references:**

With circular model references, you must use [`NoAction` referential actions](prisma/docs/orm/prisma-schema/data-model/relations/referential-actions/index.md#special-rules-for-sql-server-and-mongodb) to avoid validation errors.

**Raw queries with `VARCHAR` columns:**

`String` parameters in raw queries are encoded as `NVARCHAR(4000)` or `NVARCHAR(MAX)`. When querying `VARCHAR(N)` columns, manually cast to avoid index performance issues:

```
// ❌ Causes implicit conversion
await prisma.$queryRaw`SELECT * FROM user WHERE name = ${"John"}`;

// ✅ Enables index seek
await prisma.$queryRaw`SELECT * FROM user WHERE name = CAST(${"John"} AS VARCHAR(40))`;
```

**Schema names:**

SQL Server doesn't have `SET search_path`. Ensure your connection URL schema parameter matches production (typically `dbo`):

```
sqlserver://host:1433;database=db;schema=dbo;...
```

**Destructive changes:**

Some operations require table recreation:

*   Adding/removing `autoincrement()`
*   Dropping all columns from a table

**Shared default values:**

Prisma doesn't support SQL Server's `sp_bindefault`. Use per-column defaults instead.

**Windows:**

1.  Install [SQL Server 2019 Developer](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
2.  Install [SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
3.  Enable TCP/IP in SQL Server Configuration Manager → **Protocols for MSSQLSERVER**
4.  (Optional) Enable SQL authentication: **Properties** → **Security** → **SQL Server and Windows Authentication Mode**

**Docker:**

```
docker pull mcr.microsoft.com/mssql/server:2019-latest

docker run --name sql_container \
  -e 'ACCEPT_EULA=Y' \
  -e 'SA_PASSWORD=myPassword' \
  -p 1433:1433 \
  -d mcr.microsoft.com/mssql/server:2019-latest
```

Connect with: Username `sa`, password `myPassword`, port `1433`

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/core-concepts/supported-databases/sql-server.mdx)
