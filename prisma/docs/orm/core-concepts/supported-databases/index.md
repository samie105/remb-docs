---
title: "Overview"
source: "https://www.prisma.io/docs/orm/core-concepts/supported-databases"
canonical_url: "https://www.prisma.io/docs/orm/core-concepts/supported-databases"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:36:32.196Z"
content_hash: "3a50de62db755f2d78d7a2466a5989543ae6a81f3825d46605a25e78cbacd9b4"
menu_path: ["Overview"]
section_path: []
content_language: "en"
---
Supported databases

## Overview

Prisma ORM supports PostgreSQL, MySQL, SQLite, MongoDB, SQL Server, CockroachDB, and serverless databases

### [Self-hosted](#self-hosted)

### [Managed/Serverless](#managedserverless)

| Database | Notes |
| --- | --- |
| Neon | Serverless Postgres |
| Supabase | Postgres |
| PlanetScale | MySQL |
| Turso | libSQL (SQLite) |
| Cloudflare D1 (Preview) | SQLite |
| AWS Aurora | MySQL/Postgres |
| MongoDB Atlas | MongoDB |

### [Constraints](#constraints)

| Feature | PostgreSQL | MySQL | SQLite | SQL Server | MongoDB |
| --- | --- | --- | --- | --- | --- |
| PRIMARY KEY | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| FOREIGN KEY | ✔️ | ✔️ | ✔️ | ✔️ | — |
| UNIQUE | ✔️ | ✔️ | ✔️ | ✔️\* | ✔️ |
| NOT NULL | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| DEFAULT | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |

\*SQL Server has [limitations with UNIQUE constraints](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sql-server#common-considerations)

### [Data types](#data-types)

| Feature | PostgreSQL | MySQL | SQLite | SQL Server | MongoDB |
| --- | --- | --- | --- | --- | --- |
| Arrays | ✔️ | — | — | — | ✔️ |
| JSON | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| Enums | ✔️ | ✔️ | ✔️ | — | ✔️ |

-   [PostgreSQL](https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql) — Self-hosted, Neon, Supabase, and CockroachDB
-   [MySQL/MariaDB](https://www.prisma.io/docs/orm/core-concepts/supported-databases/mysql) — Self-hosted and PlanetScale
-   [SQLite](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sqlite) — Local, Turso, and Cloudflare D1
-   [SQL Server](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sql-server)
-   [MongoDB](https://www.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)

### [Driver adapters](#driver-adapters)

For custom database drivers, see [Driver adapters](https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers).
