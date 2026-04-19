# Prisma ORM Skill File

## Overview
Prisma ORM is a next-generation ORM for Node.js and TypeScript that enables type-safe database access, simplified schema migrations, and seamless integration with modern APIs. It abstracts database operations via an auto-generated client, manages schema evolution with migration tools, and supports declarative modeling for robust, maintainable applications.

---

## Key Concepts

- **Prisma Client**: Auto-generated, type-safe data access layer for querying and updating databases.
- **Prisma Schema**: Declarative configuration file describing models, relations, and database connectors.
- **Data Modeling**: Defines database structure with a simple, readable language distinct from raw SQL.
- **Migration**: Controlled, versioned updates to your database schema using Prisma Migrate.
- **Introspection**: Generates a Prisma schema from an existing database for seamless onboarding.
- **API Integration**: Designed to work with REST, GraphQL, and fullstack frameworks.
- **Preview Features**: Cutting-edge functionalities and experimental integrations.
- **Supported Databases**: Broad compatibility with PostgreSQL, MySQL, SQLite, and more.

---

## Navigation Guide

- **Setup & Getting Started**: See [Prisma ORM](prisma/docs/orm/index.md), [Data modeling](prisma/docs/orm/core-concepts/data-modeling/index.md), and [Getting started with Prisma Migrate](prisma/docs/orm/prisma-migrate/getting-started/index.md).
- **Data Modeling & Schema**: [Data modeling](prisma/docs/orm/core-concepts/data-modeling/index.md), [Schema API](prisma/docs/orm/reference/prisma-schema-reference/index.md).
- **API Usage**: [API patterns](prisma/docs/orm/core-concepts/api-patterns/index.md), [Prisma Client API](prisma/docs/orm/reference/prisma-client-reference/index.md).
- **Migrations**: [Overview of Prisma Migrate](prisma/docs/orm/prisma-migrate/index.md), [Understanding Migrations](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model/index.md).
- **Database Connection & Features**: [Connection URLs](prisma/docs/orm/reference/connection-urls/index.md), [Database Features](prisma/docs/orm/reference/database-features/index.md), [Supported databases](prisma/docs/orm/reference/supported-databases/index.md).
- **CLI & Configuration**: [Prisma CLI reference](prisma/docs/orm/reference/prisma-cli-reference/index.md), [Config API](prisma/docs/orm/reference/prisma-config-reference/index.md).
- **Error Handling**: [Error Reference](prisma/docs/orm/reference/error-reference/index.md), [Prisma Error Reference](prisma/docs/orm/reference/errors/index.md).
- **Best Practices & Releases**: [Best practices](prisma/docs/orm/more/best-practices/index.md), [ORM releases and maturity levels](prisma/docs/orm/more/releases/index.md).
- **Advanced & Postgres Extensions**: [PostgreSQL extensions](prisma/docs/orm/prisma-schema/postgresql-extensions/index.md).

---

## Top 15 Most Important Pages

- [Prisma ORM](prisma/docs/orm/index.md): Core introduction and conceptual overview.
- [Data modeling](prisma/docs/orm/core-concepts/data-modeling/index.md): How to define database schemas in Prisma.
- [API patterns](prisma/docs/orm/core-concepts/api-patterns/index.md): Patterns for integrating Prisma with REST, GraphQL, etc.
- [What is introspection?](prisma/docs/orm/prisma-schema/introspection/index.md): Importing an existing database structure.
- [PostgreSQL extensions](prisma/docs/orm/prisma-schema/postgresql-extensions/index.md): Managing and using PostgreSQL-specific features.
- [Overview of Prisma Migrate](prisma/docs/orm/prisma-migrate/index.md): Migration system concepts and benefits.
- [Getting started with Prisma Migrate](prisma/docs/orm/prisma-migrate/getting-started/index.md): Step-by-step migration setup.
- [Understanding Migrations](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model/index.md): Deep dive into migration internals.
- [Migration histories](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories/index.md): How Prisma tracks migration history.
- [About the shadow database](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database/index.md): Explains the testing database for migration validation.
- [Limitations and known issues](prisma/docs/orm/prisma-migrate/understanding-prisma-migrate/limitations-and-known-issues/index.md): Current technical limitations.
- [Prisma CLI reference](prisma/docs/orm/reference/prisma-cli-reference/index.md): Documentation for CLI commands.
- [Prisma Client API](prisma/docs/orm/reference/prisma-client-reference/index.md): Reference for generated client queries and mutations.
- [Schema API](prisma/docs/orm/reference/prisma-schema-reference/index.md): Formal schema definition details.
- [Connection URLs](prisma/docs/orm/reference/connection-urls/index.md): Syntax and options for connecting to databases.

---

## Notable Gotchas & Doc Structure Quirks

- **Migrate Details**: Migration process, shadow DB, and known issues are in deeply nested subdirectories (see `prisma-migrate/understanding-prisma-migrate/`).
- **Error Handling**: Separate error reference pages exist—use both [Error Reference](prisma/docs/orm/reference/error-reference/index.md) and [Prisma Error Reference](prisma/docs/orm/reference/errors/index.md) for full coverage.
- **Preview Features**: Feature flags and experimental APIs are found under `reference/preview-features`.
- **Prisma Schema API**: Schema docs reference data sources—sometimes you must cross-link with [Data modeling](prisma/docs/orm/core-concepts/data-modeling/index.md) for practical examples.
- **Postgres Extensions**: Dedicated documentation for PostgreSQL features is not always surfaced in main guides, check [PostgreSQL extensions](prisma/docs/orm/prisma-schema/postgresql-extensions/index.md).
- **Supported Databases & Features**: For compatibility and version support, check both [Supported databases](prisma/docs/orm/reference/supported-databases/index.md) and [Database Features](prisma/docs/orm/reference/database-features/index.md).

---