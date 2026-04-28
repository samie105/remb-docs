## Overview

Drizzle is a TypeScript-first ORM and query builder that mirrors native SQL syntax while providing type-safe database access across PostgreSQL, MySQL, SQLite, and other engines. An agent needs to know it because it underpins data layers in modern full-stack and edge applications, requiring precise schema definitions, driver configuration, and query construction.

## Mental Model

Drizzle treats SQL as a first-class citizen: you define schemas in TypeScript that compile to native DDL, compose queries through a SQL-like DSL, and execute them via lightweight database-specific drivers. It is modular by design—schemas, drivers, and caching are swappable—so you treat the database as typed infrastructure rather than a black box. Canonical starting points are `drizzle/docs/basic-file-structure.md` for project layout, `drizzle/docs/query-examples.md` for the query DSL, and `drizzle/docs/data-type-reference.md` for per-engine type mappings.

## Learning Paths

**Getting Started**
1. `drizzle/docs/install-the-dependencies.md`
2. `drizzle/docs/basic-file-structure.md`
3. `drizzle/docs/query-examples.md`

**Production Ready**
1. `drizzle/docs/extended-example.md`
2. `drizzle/docs/extended-list-of-configurations.md`
3. `drizzle/docs/multiple-configuration-files-in-one-project.md`
4. `drizzle/docs/cache/index.md`
5. `drizzle/docs/limitations.md`

**Reference Deep-Dive**
1. `drizzle/docs/data-type-reference.md`
2. `drizzle/docs/column-types/pg/index.md`
3. `drizzle/docs/column-types/mysql/index.md`
4. `drizzle/docs/column-types/sqlite/index.md`
5. `drizzle/docs/batch-api/index.md`
6. `drizzle/docs/arktype/index.md`

## Concept Map

- **Schema & Validation**
  - Refinements → `drizzle/docs/arktype/index.md`
  - Select / Insert / Update schemas → `drizzle/docs/arktype/index.md`
- **Column Types**
  - PostgreSQL → `drizzle/docs/column-types/pg/index.md`
  - MySQL → `drizzle/docs/column-types/mysql/index.md`
  - SQLite → `drizzle/docs/column-types/sqlite/index.md`
  - MSSQL → `drizzle/docs/column-types/mssql/index.md`
  - CockroachDB → `drizzle/docs/column-types/cockroach/index.md`
  - SingleStore → `drizzle/docs/column-types/singlestore/index.md`
  - Data type reference → `drizzle/docs/data-type-reference.md`
- **Queries & API**
  - Query examples → `drizzle/docs/query-examples.md`
  - Batch API → `drizzle/docs/batch-api/index.md`
- **Configuration**
  - Basic file structure → `drizzle/docs/basic-file-structure.md`
  - Multiple configuration files → `drizzle/docs/multiple-configuration-files-in-one-project.md`
  - Extended list of configurations → `drizzle/docs/extended-list-of-configurations.md`
  - Extended example → `drizzle/docs/extended-example.md`
- **Platform Connections**
  - AWS Data API MySQL → `drizzle/docs/connect-aws-data-api-mysql/index.md`
  - AWS Data API Postgres → `drizzle/docs/connect-aws-data-api-pg/index.md`
  - Bun SQL → `drizzle/docs/connect-bun-sql/index.md`
  - Bun SQLite → `drizzle/docs/connect-bun-sqlite/index.md`
  - Cloudflare D1 → `drizzle/docs/connect-cloudflare-d1/index.md`
  - Cloudflare Durable Objects → `drizzle/docs/connect-cloudflare-do/index.md`
- **Performance**
  - Cache quickstart → `drizzle/docs/cache/index.md`
  - Upstash integration → `drizzle/docs/cache/index.md`
  - Custom cache → `drizzle/docs/cache/index.md`
- **Releases & Constraints**
  - New features → `drizzle/docs/new-features.md`
  - Fixes → `drizzle/docs/fixes.md`
  - Limitations → `drizzle/docs/limitations.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Install Drizzle and its drivers | `drizzle/docs/install-the-dependencies.md` |
| Scaffold a new project layout | `drizzle/docs/basic-file-structure.md` |
| Write type-safe SELECT/INSERT/UPDATE schemas | `drizzle/docs/arktype/index.md` |
| Map SQL column types for Postgres/MySQL/SQLite | `drizzle/docs/data-type-reference.md` |
| Run many queries in one batch | `drizzle/docs/batch-api/index.md` |
| Add query caching or Upstash | `drizzle/docs/cache/index.md` |
| Connect to Cloudflare D1 or Durable Objects | `drizzle/docs/connect-cloudflare-d1/index.md`, `drizzle/docs/connect-cloudflare-do/index.md` |
| Manage multiple config files in one repo | `drizzle/docs/multiple-configuration-files-in-one-project.md` |
| Review edge-case constraints or unsupported features | `drizzle/docs/limitations.md` |
| See complex real-world configuration | `drizzle/docs/extended-example.md` |

## Top Must-Know Pages

1. `drizzle/docs/basic-file-structure.md` — Defines the standard project layout and where to place schemas, migrations, and config.
2. `drizzle/docs/query-examples.md` — Shows the SQL-like query syntax for selects, inserts, updates, and deletes.
3. `drizzle/docs/data-type-reference.md` — Central reference for mapping TypeScript types to database column types across engines.
4. `drizzle/docs/arktype/index.md` — Covers schema validation, refinements, and type-safe select/insert/update patterns.
5. `drizzle/docs/column-types/pg/index.md` — PostgreSQL-specific column type definitions and usage.
6. `drizzle/docs/column-types/mysql/index.md` — MySQL-specific column type definitions and usage.
7. `drizzle/docs/batch-api/index.md` — Explains how to execute multiple statements in a single batch call.
8. `drizzle/docs/cache/index.md` — Documents query caching, Upstash integration, and custom cache implementations.
9. `drizzle/docs/multiple-configuration-files-in-one-project.md` — Describes how to run multiple Drizzle configs within a single codebase.
10. `drizzle/docs/limitations.md` — Lists known constraints, unsupported features, and engine-specific caveats.