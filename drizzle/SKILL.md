# Drizzle ORM Skill File

## Overview

Drizzle ORM is a TypeScript-first ORM designed to offer a simple and powerful interface for building, querying, and migrating SQL databases. It supports a wide range of databases and provides "headless" operation (runtime codegen free), type safety, and flexible relation/query modeling.

---

## Key Concepts

- **TypeScript-first**: Schemas, queries, and migrations are first-class TypeScript citizens, ensuring end-to-end type safety.
- **Relational Modeling**: Supports advanced and composable relations between models/tables.
- **Flexible Query Builder**: Allows both simple and complex query composition, including joins, filters, and raw SQL.
- **Migrations & Schema Management**: Provides tools for managing database schema changes and code-first migrations.
- **Multi-Database Support**: Out-of-the-box adapters for PostgreSQL, MySQL, SQLite, MSSQL, and many clouds.
- **Drizzle Kit**: CLI and programmatic utilities for migration generation, pushing/pulling schemas, and more.
- **Serverless Support**: Designed for predictable performance in serverless environments.
- **Extensible**: Plugin-based approach, support for custom column types, extensions, and validation.

---

## Navigation Guide

- **Getting Started / Setup**: See `Get started` section and database-specific guides.
- **Schema Definition & Relations**: Use `Schema`, `Relations`, and `Schemas` for schema and table relationship concepts.
- **Database Connections**: Reference the `Database connection` section and the various cloud/on-prem adapter pages.
- **Query/Data Access**: Check `Query Data`, `Select`, `Insert`, `Update`, `Delete`, `Joins`, and query-related pages.
- **Migrations / Drizzle Kit**: Relevant migration commands and config live in the `drizzle-kit-*` pages and `drizzle.config.ts`.
- **Performance & Serverless**: See entries under `perf-*` for guidance on optimizing Drizzle in production/serverless.
- **Validation / Utils**: Integrations with schema validators (zod, valibot, etc.) and utility helpers.
- **Gotchas / Upgrades**: See `Gotchas` and `How to upgrade?` for common mistakes, breaking changes, or migration guides.
- **Release News**: Check `Latest releases`.

---

## Top 15 Most Important Pages

1. **[Overview](drizzle/docs/overview/index.md)**  
   Library introduction, philosophy, and feature summary.

2. **[Get started](drizzle/docs/get-started/index.md)**  
   First steps to using Drizzle, installation, and quickstart.

3. **[Schema](drizzle/docs/sql-schema-declaration/index.md)**  
   How to define your database schema in TypeScript.

4. **[Relations](drizzle/docs/relations-schema-declaration/index.md)**  
   Fundamentals of modeling relationships between tables.

5. **[Query Data](drizzle/docs/data-querying/index.md)**  
   Building and executing type-safe queries.

6. **[Select](drizzle/docs/select/index.md)**  
   Reading records—constructing SELECT queries.

7. **[Insert](drizzle/docs/insert/index.md)**  
   Creating records—usage and examples for INSERT.

8. **[Update](drizzle/docs/update/index.md)**  
   Modifying records—how to use UPDATE queries.

9. **[Delete](drizzle/docs/delete/index.md)**  
   Removing records from tables.

10. **[Migrations](drizzle/docs/migrations/index.md)**  
    Database schema evolution, migration workflows, and CLI.

11. **[drizzle.config.ts](drizzle/docs/drizzle-config-file/index.md)**  
    Drizzle configuration file structure and options.

12. **[Database connection](drizzle/docs/connect-overview/index.md)**  
    Comprehensive guide to connecting Drizzle to databases.

13. **[Gotchas](drizzle/docs/gotchas/index.md)**  
    Common pitfalls, edge cases, and best practice highlights.

14. **[Guides](drizzle/docs/guides/index.md)**  
    Multi-topic, in-depth walkthroughs and recipes.

15. **[How to upgrade?](drizzle/docs/upgrade-v1/index.md)**  
    Step-by-step advice for upgrading Drizzle versions.

---

## Notable Gotchas & Structure Quirks

- **Multiple Versions of Relations**: Both `relations-v1-v2` and `relations-v2` exist; always use the latest (`relations-v2`) unless maintaining legacy code.
- **Database Adapters Are Split**: Cloud and traditional DB guides are each in their own file under `connect-*` (e.g., `connect-vercel-postgres`, `connect-xata`, etc). Always check for a DB/hosting-specific page before generalizing solutions.
- **Migration Commands**: Migration details are split between `drizzle-kit-*` command guides (like push, pull, migrate, etc.) and the general `Migrations`/`Custom migrations` pages.
- **Validator Integration**: Pages for zod, valibot, typebox, etc., are under their own file in the root—useful when integrating validation layers.
- **[OLD] Documentation**: Pages prefixed with `[OLD]` (e.g., `[OLD] Query V1`) are for legacy code references—avoid unless working with pre-v1 apps.
- **Serverless/Performance**: See `perf-*` for performance/serverless tuning—these are not in "guides".
- **Upgrading and Breaking Features**: Always check `Gotchas` and `How to upgrade?` for API or migration issues before updating major versions.

---

## Additional Doc Path References for Frequent Tasks

- **Switching Database Targets**: Use the correct guide under `get-started-*` for local database drivers, or under `connect-*` for cloud/hosted adapters—for instance,  
  - [Get started with PostgreSQL](drizzle/docs/get-started-postgresql/index.md)  
  - [Drizzle <> Supabase](drizzle/docs/connect-supabase/index.md)
- **Defining Advanced Constraints/Indexes**: [Indexes & Constraints](drizzle/docs/indexes-constraints/index.md)
- **Batch & Transactions**: [Batch](drizzle/docs/batch-api/index.md), [Transactions](drizzle/docs/transactions/index.md)
- **Composing Dynamic Queries**: [Dynamic query building](drizzle/docs/dynamic-query-building/index.md)
- **Using Raw SQL**: [Magic sql`` operator](drizzle/docs/sql/index.md)
- **Validation**: [zod](drizzle/docs/zod/index.md), [valibot](drizzle/docs/valibot/index.md)
- **Extending Types**: [Custom types](drizzle/docs/custom-types/index.md)
- **Upgrading/Breaking Changes**: [Migrating to Relational Queries version 2](drizzle/docs/relations-v1-v2/index.md), [How to upgrade?](drizzle/docs/upgrade-v1/index.md)
- **Release Notes**: [Latest releases](drizzle/docs/latest-releases/index.md)

---

## See Also

Review the full table of contents for a comprehensive list and use the "Guides", "Tutorials", and database-specific "connect-*" sections for extended, scenario-driven help. The "Goodies" section also contains useful extensions and plugins for Drizzle.