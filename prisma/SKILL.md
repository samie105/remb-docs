1. **Overview**
Prisma is a next-generation ORM for Node.js and TypeScript that provides type-safe database access, declarative schema modeling, and automated migrations. Agents need to know it because it is a standard tool in modern full-stack applications, with distinct patterns for driver adapters, connection management, and framework integration.

2. **Mental Model**
Prisma is built around a schema-first workflow: you define your data model in a Prisma schema file, configure database connections (including serverless and edge driver adapters), run migrations to evolve the database, and execute type-safe queries via Prisma Client. This architecture separates database-level modeling from application-level access. Canonical pages: [`prisma/docs/orm/index.md`](prisma/docs/orm/index.md), [`prisma/docs/orm/core-concepts/data-modeling/index.md`](prisma/docs/orm/core-concepts/data-modeling/index.md), [`prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md`](prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md).

3. **Learning Paths**
- **Getting Started:** `prisma/docs/orm/index.md` → `prisma/docs/orm/core-concepts/data-modeling/index.md` → `prisma/docs/orm/core-concepts/supported-databases/index.md`
- **Production Ready:** `prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md` → `prisma/docs/orm/more/best-practices/index.md` → `prisma/docs/orm/core-concepts/api-patterns/index.md`
- **Reference Deep-Dive:** `prisma/docs/orm/more/comparisons/prisma-and-drizzle/index.md` → `prisma/docs/orm/more/comparisons/prisma-and-typeorm/index.md` → `prisma/docs/orm/more/comparisons/prisma-and-sequelize/index.md`

4. **Concept Map**
- **Core Workflow**
  - Getting Started: `prisma/docs/orm/index.md`
  - Data Modeling: `prisma/docs/orm/core-concepts/data-modeling/index.md`
  - API Patterns: `prisma/docs/orm/core-concepts/api-patterns/index.md`
- **Database Support & Drivers**
  - Supported Databases Overview: `prisma/docs/orm/core-concepts/supported-databases/index.md`
  - Driver Adapters: `prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md`
  - PostgreSQL: `prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md`
  - MySQL / PlanetScale: `prisma/docs/orm/core-concepts/supported-databases/mysql/index.md`
  - SQLite / Turso / D1: `prisma/docs/orm/core-concepts/supported-databases/sqlite/index.md`
  - MongoDB: `prisma/docs/orm/core-concepts/supported-databases/mongodb/index.md`
  - SQL Server: `prisma/docs/orm/core-concepts/supported-databases/sql-server/index.md`
- **Best Practices**
  - Naming, Relations, Indexing: `prisma/docs/orm/more/best-practices/index.md`
- **Comparisons**
  - Drizzle (filtering, relations): `prisma/docs/orm/more/comparisons/prisma-and-drizzle/index.md`
  - Sequelize (fetching, filtering): `prisma/docs/orm/more/comparisons/prisma-and-sequelize/index.md`
  - TypeORM (filtering, relations): `prisma/docs/orm/more/comparisons/prisma-and-typeorm/index.md`
  - Mongoose: `prisma/docs/orm/more/comparisons/prisma-and-mongoose/index.md`

5. **If You Need To...**
| If you need to... | Read |
|---|---|
| Learn the core workflow (schema, connection, migrations, queries) | `prisma/docs/orm/index.md` |
| Model data on the database or application level | `prisma/docs/orm/core-concepts/data-modeling/index.md` |
| Configure driver adapters or edge-compatible drivers | `prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md` |
| Choose a database or understand constraints/data types | `prisma/docs/orm/core-concepts/supported-databases/index.md` |
| Integrate with a framework or build API routes | `prisma/docs/orm/core-concepts/api-patterns/index.md` |
| Apply naming conventions, explicit relations, or index strategy | `prisma/docs/orm/more/best-practices/index.md` |
| Work with PostgreSQL, Neon, Supabase, or CockroachDB | `prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md` |
| Work with MySQL or PlanetScale | `prisma/docs/orm/core-concepts/supported-databases/mysql/index.md` |
| Work with MongoDB and handle missing relations | `prisma/docs/orm/core-concepts/supported-databases/mongodb/index.md` |
| Compare Prisma with Drizzle on modeling and querying | `prisma/docs/orm/more/comparisons/prisma-and-drizzle/index.md` |
| Compare Prisma with TypeORM on filtering and relations | `prisma/docs/orm/more/comparisons/prisma-and-typeorm/index.md` |

6. **Top Must-Know Pages**
1. `prisma/docs/orm/index.md` — Entry point covering schema definition, connection configuration, migrations, and querying.
2. `prisma/docs/orm/core-concepts/data-modeling/index.md` — Explains database-level and application-level data modeling with Prisma.
3. `prisma/docs/orm/core-concepts/supported-databases/index.md` — Overview of self-hosted, managed, and serverless database constraints and data types.
4. `prisma/docs/orm/core-concepts/supported-databases/database-drivers/index.md` — Guide to database driver adapters, serverless adapters, and connection configuration.
5. `prisma/docs/orm/core-concepts/api-patterns/index.md` — Reference for supported frameworks, example routes, and tool integrations.
6. `prisma/docs/orm/more/best-practices/index.md` — Covers naming conventions, explicit relations, index strategy, and multi-file schema organization.
7. `prisma/docs/orm/core-concepts/supported-databases/postgresql/index.md` — PostgreSQL-specific guidance including Neon, Supabase, and CockroachDB.
8. `prisma/docs/orm/core-concepts/supported-databases/mongodb/index.md` — MongoDB-specific patterns for relations, null filtering, and data migration.
9. `prisma/docs/orm/more/comparisons/prisma-and-drizzle/index.md` — Side-by-side comparison of data modeling, migrations, querying, relations, and filtering.
10. `prisma/docs/orm/more/comparisons/prisma-and-typeorm/index.md` — Comparison focusing on filtering, relations, data modeling, and field selection.