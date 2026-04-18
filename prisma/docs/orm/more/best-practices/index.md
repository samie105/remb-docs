---
title: "Best practices"
source: "https://www.prisma.io/docs/orm/more/best-practices"
canonical_url: "https://www.prisma.io/docs/orm/more/best-practices"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:53.917Z"
content_hash: "eb98809dfa9f4bea64ea14b752f08cc2f07562bb66f8d00ab54da935045adbfa"
menu_path: ["Best practices"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/reference/preview-features/cli-preview-features/index.md", "title": "Prisma CLI Preview features"}
nav_next: {"path": "prisma/docs/orm/more/releases/index.md", "title": "ORM releases and maturity levels"}
---

Learn production-ready patterns for schema design, query optimization, type safety, security, and deployment with Prisma ORM.

### [Naming conventions](#naming-conventions)

Use **PascalCase** for model names (singular) and **camelCase** for field names. Map to legacy database naming with `@map` and `@@map`:

```
model Comment {
  id      Int    @id @default(autoincrement())
  content String @map("comment_text")
  email   String @map("commenter_email")

  @@map("comments")
}
```

This keeps your Prisma schema readable while supporting any database naming convention.

### [Model relations explicitly](#model-relations-explicitly)

Always define both sides of a relation to keep your schema clear and maintainable:

```
model User {
  id    Int    @id @default(autoincrement())
  posts Post[]
}

model Post {
  id       Int  @id @default(autoincrement())
  author   User @relation(fields: [authorId], references: [id])
  authorId Int
}
```

### [Index strategy](#index-strategy)

Index fields used in `where`, `orderBy`, and relations. Without indexes, the database can be forced to scan entire tables to find matching rows, which becomes slower as tables grow.

```
model Comment {
  id      Int    @id @default(autoincrement())
  postId  Int
  status  String
  post    Post   @relation(fields: [postId], references: [id])

  @@index([postId])
  @@index([status])
}
```

### [Enum vs string fields](#enum-vs-string-fields)

Enums provide type-safe, finite sets of values. You can map enum values to match your database naming:

```
enum Role {
  USER  @map("user")
  ADMIN @map("admin")

  @@map("user_role")
}

model User {
  id   Int  @id @default(autoincrement())
  role Role @default(USER)
}
```

For values that change frequently or are user-generated, `String` avoids schema changes.

### [Multi-file schema organization](#multi-file-schema-organization)

For large projects, use multi-file Prisma schemas (available since v6.7.0):

```
prisma/
├── schema.prisma        # Main schema with generator and datasource
├── migrations/          # Migration files
├── user.prisma         # User-related models
├── product.prisma      # Product-related models
└── order.prisma        # Order-related models
```

The `schema.prisma` file (containing the `generator` block) and `migrations/` directory must be at the same level. You can also group additional schema files under a subdirectory such as `prisma/models/`.

### [Connection pooling](#connection-pooling)

Create one global `PrismaClient` instance and reuse it throughout your application. Creating multiple instances creates multiple connection pools, which can exhaust your database's connection limit and slow down queries.

```
import { PrismaClient } from '../generated/prisma/client'
import { PrismaPg } from '@prisma/adapter-pg'

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL
})

export const prisma = new PrismaClient({ adapter })
```

**Serverless environments:**

*   Instantiate `PrismaClient` **outside** the handler function to reuse connections across warm invocations
*   Consider [Prisma Postgres](https://www.prisma.io/docs/postgres) for built-in connection pooling or external poolers like PgBouncer

### [Preventing N+1 queries](#preventing-n1-queries)

The N+1 problem occurs when you run 1 query to fetch a list, then 1 additional query per item in that list. This creates many unnecessary round-trips to the database instead of a few efficient queries.

```
// ❌ Bad: N+1 queries (1 + N queries)
const users = await prisma.user.findMany()
for (const user of users) {
  const posts = await prisma.post.findMany({
    where: { authorId: user.id }
  })
}

// ✅ Good: Single query with include
const users = await prisma.user.findMany({
  include: { posts: true }
})

// ✅ Good: Batch with IN filter
const users = await prisma.user.findMany()
const posts = await prisma.post.findMany({
  where: { authorId: { in: users.map(u => u.id) } }
})
```

### [Select only needed fields](#select-only-needed-fields)

By default, Prisma ORM returns all scalar fields. Use `select` to whitelist specific fields you want returned:

```
const user = await prisma.user.findFirst({
  select: {
    id: true,
    email: true,
    role: true
  }
})
```

Use `omit` to blacklist fields you want excluded (useful for sensitive data):

```
import { PrismaClient } from '../generated/prisma/client'
import { PrismaPg } from '@prisma/adapter-pg'

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL
})

const prisma = new PrismaClient({
  adapter,
  omit: {
    user: { secretValue: true }
  }
})
```

You cannot combine `select` and `omit` in the same query.

Use **offset pagination** for small datasets where jumping to arbitrary pages is needed:

```
const posts = await prisma.post.findMany({
  skip: 40,
  take: 10,
  where: { email: { contains: 'prisma.io' } },
})
```

Use **cursor-based pagination** for large datasets or infinite scroll. Cursor-based pagination scales better because it uses indexed columns to find the starting position instead of traversing skipped rows:

```
const posts = await prisma.post.findMany({
  take: 10,
  skip: 1,
  cursor: {
    id: lastPost.id,
  },
  orderBy: {
    id: 'asc',
  },
})
```

### [Batch operations](#batch-operations)

Use bulk methods when operating on multiple records:

```
await prisma.user.createMany({
  data: [
    { email: 'alice@prisma.io' },
    { email: 'bob@prisma.io' }
  ]
})

await prisma.post.updateMany({
  where: { published: false },
  data: { published: true }
})
```

Bulk operations (`createMany`, `createManyAndReturn`, `updateMany`, `updateManyAndReturn`, and `deleteMany`) [automatically run as transactions](prisma/docs/orm/prisma-client/queries/transactions/index.md#batch-operations), so all writes either succeed together or are rolled back if something fails.

### [Raw queries](#raw-queries)

Prefer Prisma ORM's query API. Use raw SQL only when you need features not supported by Prisma ORM or heavily optimized queries:

```
const email = 'user@example.com'
const users = await prisma.$queryRaw`
  SELECT * FROM "User" WHERE email = ${email}
`
```

### [Leverage generated types](#leverage-generated-types)

Use Prisma ORM's generated types instead of duplicating interfaces:

```
import type { User } from '../generated/prisma/client'

async function getAdminEmails(): Promise<string[]> {
  const admins: User[] = await prisma.user.findMany({
    where: { role: 'ADMIN' }
  })

  return admins.map(a => a.email)
}
```

### [Input validation](#input-validation)

Always validate and sanitize user input before database operations:

```
import { z } from 'zod'

const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100)
})

async function createUser(input: unknown) {
  const data = createUserSchema.parse(input)
  return prisma.user.create({ data })
}
```

### [SQL injection prevention](#sql-injection-prevention)

Prisma ORM's API is safe by default. For raw queries, always use parameterized queries. String concatenation with untrusted input allows attackers to inject arbitrary SQL into your queries.

```
// ✅ Safe: tagged template
const result = await prisma.$queryRaw`
  SELECT * FROM "User" WHERE email = ${email}
`

// ✅ Safe: parameterized
const result = await prisma.$queryRawUnsafe(
  'SELECT * FROM "User" WHERE email = $1',
  email
)

// ❌ Unsafe: string concatenation
const query = `SELECT * FROM "User" WHERE email = '${email}'`
const result = await prisma.$queryRawUnsafe(query)
```

### [Sensitive data handling](#sensitive-data-handling)

Exclude sensitive fields from query results:

```
import { PrismaClient } from '../generated/prisma/client'
import { PrismaPg } from '@prisma/adapter-pg'

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL
})

// Global exclusion
const prisma = new PrismaClient({
  adapter,
  omit: {
    user: { secretValue: true }
  }
})

// Per-query exclusion
const user = await prisma.user.findUnique({
  where: { id: 1 },
  omit: { secretValue: true }
})
```

### [Database setup](#database-setup)

Use a dedicated test database that can be reset freely:

1.  Start test database (often in Docker)
2.  Apply schema via migrations
3.  Seed test data
4.  Run tests
5.  Clean up or reset database

### [Unit tests with mocking](#unit-tests-with-mocking)

Mock Prisma ORM using `jest-mock-extended`:

```
import { PrismaClient } from '../generated/prisma/client'
import { mockDeep } from 'jest-mock-extended'

const prismaMock = mockDeep<PrismaClient>()

test('finds user by email', async () => {
  prismaMock.user.findUnique.mockResolvedValue({
    id: 1,
    email: 'test@example.com',
    name: 'Test User'
  })

  const user = await prismaMock.user.findUnique({
    where: { email: 'test@example.com' }
  })

  expect(user).toBeDefined()
})
```

### [Integration tests with real database](#integration-tests-with-real-database)

Use a real database with Prisma Migrate:

```
import { PrismaClient } from '../generated/prisma/client'
import { PrismaPg } from '@prisma/adapter-pg'

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL
})

const prisma = new PrismaClient({ adapter })

beforeEach(async () => {
  await prisma.user.create({
    data: { email: 'test@example.com', name: 'Test' }
  })
})

afterEach(async () => {
  await prisma.user.deleteMany()
})

test('creates user', async () => {
  const user = await prisma.user.create({
    data: { email: 'new@example.com', name: 'New User' }
  })

  expect(user.email).toBe('new@example.com')
})
```

### [Migration strategies](#migration-strategies)

**Development:**

*   Use `prisma migrate dev` to create and apply migrations
*   Use `prisma db push` only for quick prototyping (may reset data)

**Production:**

*   Use **only** `prisma migrate deploy` with committed migrations
*   Never use `migrate dev` (can prompt to reset DB) or `db push` (can be destructive and locks you into a migrationless workflow)

`prisma migrate deploy` applies existing migrations in a non-interactive way, uses advisory locking to prevent concurrent runs, and is safe for production data.

Example CI/CD workflow:

```
- name: Apply migrations
  run: npx prisma migrate deploy
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

### [Serverless considerations](#serverless-considerations)

For AWS Lambda, Vercel, Cloudflare Workers, or similar platforms:

1.  Instantiate `PrismaClient` **outside** the handler function to reuse connections across warm invocations
2.  Do **not** call `$disconnect()` at the end of each invocation (the container may be reused)
3.  Consider external connection poolers (like PgBouncer) for high-concurrency workloads

```
import { PrismaClient } from '../generated/prisma/client'
import { PrismaPg } from '@prisma/adapter-pg'

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL
})

const prisma = new PrismaClient({ adapter })

export async function handler(event) {
  const users = await prisma.user.findMany()
  return {
    statusCode: 200,
    body: JSON.stringify(users)
  }
}
```

Creating a new client inside the handler on every invocation risks exhausting database connections. Each concurrent function creates its own connection pool, quickly multiplying connection counts.

*   [Query optimization](https://www.prisma.io/docs/query-insights)
*   [Raw queries](prisma/docs/orm/prisma-client/using-raw-sql/raw-queries/index.md)
*   [Prisma Migrate workflows](prisma/docs/orm/prisma-migrate/workflows/development-and-production/index.md)
