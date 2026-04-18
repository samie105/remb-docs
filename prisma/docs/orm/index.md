---
title: "Prisma ORM"
source: "https://www.prisma.io/docs/orm"
canonical_url: "https://www.prisma.io/docs/orm"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:11.908Z"
content_hash: "96a35d5f7e31f1c1ad11cc362caa36a9eb93c84dbc33add3838e81aa8ce131da"
menu_path: ["Prisma ORM"]
section_path: []
nav_next: {"path": "prisma/docs/orm/core-concepts/data-modeling/index.md", "title": "Data modeling"}
---

Prisma ORM is a next-generation Node.js and TypeScript ORM that provides type-safe database access, migrations, and a visual data editor.

Prisma ORM is [open-source](https://github.com/prisma/prisma) and consists of:

*   [**Prisma Client**](prisma/docs/orm/prisma-client/setup-and-configuration/introduction/index.md): Auto-generated, type-safe **ORM interface**
*   [**Prisma Migrate**](prisma/docs/orm/prisma-migrate/index.md): Database migration system
*   [**Prisma Studio**](https://www.prisma.io/studio): GUI to view and edit your data

Prisma Client works with any Node.js or TypeScript backend, whether you're deploying to traditional servers, serverless functions, or microservices.

Traditional database tools force a tradeoff between **productivity** and **control**. Raw SQL gives full control but is error-prone and lacks type safety. Traditional ORMs improve productivity but abstract too much, leading to the [object-relational impedance mismatch](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch) and performance pitfalls like the n+1 problem.

Prisma takes a different approach:

*   **Type-safe queries** validated at compile time with full autocompletion
*   **Thinking in objects** without the complexity of mapping relational data
*   **Plain JavaScript objects** returned from queries, not complex model instances
*   **Single source of truth** in the Prisma schema for database and application models
*   **Healthy constraints** that prevent common pitfalls and anti-patterns

**Prisma is a good fit if you:**

*   Build server-side applications (REST, GraphQL, gRPC, serverless)
*   Value type safety and developer experience
*   Work in a team and want a clear, declarative schema
*   Need migrations, querying, and data modeling in one toolkit

**Consider alternatives if you:**

*   Need full control over every SQL query (use raw SQL drivers)
*   Want a no-code backend (use a BaaS like Supabase or Firebase)
*   Need an auto-generated CRUD GraphQL API (use Hasura or PostGraphile)

### [1\. Define your schema](#1-define-your-schema)

The [Prisma schema](prisma/docs/orm/prisma-schema/overview/index.md) defines your data models and database connection:

```
datasource db {
  provider = "postgresql"
}

generator client {
  provider = "prisma-client"
  output   = "./generated"
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}

model Post {
  id        Int     @id @default(autoincrement())
  title     String
  published Boolean @default(false)
  author    User?   @relation(fields: [authorId], references: [id])
  authorId  Int?
}
```

### [2\. Configure your connection](#2-configure-your-connection)

Create a `prisma.config.ts` file in your project root:

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

### [3\. Run migrations](#3-run-migrations)

Use [Prisma Migrate](prisma/docs/orm/prisma-migrate/index.md) to create and apply migrations:

Or [introspect](prisma/docs/orm/prisma-schema/introspection/index.md) an existing database:

### [4\. Query with Prisma Client](#4-query-with-prisma-client)

Generate and use the type-safe client:

```
import { PrismaClient } from "./generated/client";

const prisma = new PrismaClient();

// Find all users with their posts
const users = await prisma.user.findMany({
  include: { posts: true },
});

// Create a user with a post
const user = await prisma.user.create({
  data: {
    email: "alice@prisma.io",
    posts: {
      create: { title: "Hello World" },
    },
  },
});
```

*   [**Prisma schema**](prisma/docs/orm/prisma-schema/overview/index.md) - Learn the schema language
*   [**Prisma Client**](prisma/docs/orm/prisma-client/setup-and-configuration/introduction/index.md) - Explore the query API

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/index.mdx)


