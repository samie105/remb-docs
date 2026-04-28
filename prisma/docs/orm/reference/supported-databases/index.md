---
title: "Supported databases"
source: "https://www.prisma.io/docs/orm/reference/supported-databases"
canonical_url: "https://www.prisma.io/docs/orm/reference/supported-databases"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:36:10.270Z"
content_hash: "b739a3d03c4dea7d660c4bb0604486afb7fa275d70ccf422ce33eb9b6ba5f13e"
menu_path: ["Supported databases"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/reference/database-features/index.md", "title": "Database Features"}
nav_next: {"path": "prisma/docs/orm/reference/system-requirements/index.md", "title": "System requirements"}
---

This page lists all the databases and their versions that are supported by Prisma ORM

Prisma ORM currently supports the following databases.

> See also: [System requirements](prisma/docs/orm/reference/system-requirements/index.md).

An asterisk (\*) indicates that the version number is not relevant; either all versions are supported, there is not a public version number, etc.

| Database | Version |
| --- | --- |
| CockroachDB | 21.2.4+ |
| MariaDB | 10.0+ |
| MariaDB | 11.0+ |
| Microsoft SQL Server | 2017 |
| Microsoft SQL Server | 2019 |
| Microsoft SQL Server | 2022 |
| MongoDB | 4.2+ |
| MySQL | 5.6 |
| MySQL | 5.7 |
| MySQL | 8.0 |
| MySQL | 8.4 |
| PostgreSQL | 9.6 |
| PostgreSQL | 10 |
| PostgreSQL | 11 |
| PostgreSQL | 12 |
| PostgreSQL | 13 |
| PostgreSQL | 14 |
| PostgreSQL | 15 |
| PostgreSQL | 16 |
| PostgreSQL | 17 |
| PostgreSQL | 18 |
| SQLite | \* |

Note that a fixed version of SQLite is shipped with every Prisma ORM release.

| Database | Version |
| --- | --- |
| AWS Aurora | \* |
| AWS Aurora Serverless ¹ | \* |
| Azure SQL | \* |
| CockroachDB-as-a-Service | \* |
| MongoDB Atlas | \* |
| Neon Serverless Postgres | \* |
| PlanetScale | \* |
| Cloudflare D1 (Preview) | \* |
| Aiven (MySQL & Postgres) | \* |

¹ This does not include support for [Data API for Aurora Serverless](https://github.com/prisma/prisma/issues/1964).
