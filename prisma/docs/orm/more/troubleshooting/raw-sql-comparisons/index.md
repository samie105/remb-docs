---
title: "Raw SQL comparisons"
source: "https://www.prisma.io/docs/orm/more/troubleshooting/raw-sql-comparisons"
canonical_url: "https://www.prisma.io/docs/orm/more/troubleshooting/raw-sql-comparisons"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:37:53.835Z"
content_hash: "8b32e028cfc9d98904509b73538b77b517fa42e23225f6712a3d9f742ae7b52b"
menu_path: ["Raw SQL comparisons"]
section_path: []
content_language: "en"
---
Troubleshooting

## Raw SQL comparisons

Compare columns of the same table with raw queries in Prisma ORM

Comparing different columns from the same table is a common scenario. This page shows how to achieve this using raw queries for Prisma ORM versions prior to 4.3.0.

Example: retrieving posts that have more comments than likes.

```
model Post {
  id            Int      @id @default(autoincrement())
  createdAt     DateTime @default(now())
  updatedAt     DateTime @updatedAt
  title         String
  content       String?
  published     Boolean  @default(false)
  author        User     @relation(fields: [authorId], references: [id])
  authorId      Int
  likesCount    Int
  commentsCount Int
}
```

### [PostgreSQL / CockroachDB](#postgresql--cockroachdb)

```
const response =
  await prisma.$queryRaw`SELECT * FROM "public"."Post" WHERE "likesCount" < "commentsCount";`;
```

### [MySQL](#mysql)

```
const response =
  await prisma.$queryRaw`SELECT * FROM \`public\`.\`Post\` WHERE \`likesCount\` < \`commentsCount\`;`;
```

### [SQLite](#sqlite)

```
const response =
  await prisma.$queryRaw`SELECT * FROM "Post" WHERE "likesCount" < "commentsCount";`;
```

Example: get all projects completed after the due date.

```
model Project {
  id            Int      @id @default(autoincrement())
  title         String
  author        User     @relation(fields: [authorId], references: [id])
  authorId      Int
  dueDate       DateTime
  completedDate DateTime
  createdAt     DateTime @default(now())
}
```

### [PostgreSQL / CockroachDB](#postgresql--cockroachdb-1)

```
const response =
  await prisma.$queryRaw`SELECT * FROM "public"."Project" WHERE "completedDate" > "dueDate";`;
```

### [MySQL](#mysql-1)

```
const response =
  await prisma.$queryRaw`SELECT * FROM \`public\`.\`Project\` WHERE \`completedDate\` > \`dueDate\`;`;
```

### [SQLite](#sqlite-1)

```
const response =
  await prisma.$queryRaw`SELECT * FROM "Project" WHERE "completedDate" > "dueDate";`;
```
