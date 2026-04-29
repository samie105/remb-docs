---
title: "One-to-many relations"
source: "https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-many-relations"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-many-relations"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:44:47.260Z"
content_hash: "da87fa2b0c5e95f3108d298b2d5e36069682f8fad08e652fca9013b98e3a8f25"
menu_path: ["One-to-many relations"]
section_path: []
content_language: "en"
nav_prev: {"path": "../many-to-many-relations/index.md", "title": "Many-to-many relations"}
nav_next: {"path": "../one-to-one-relations/index.md", "title": "One-to-one relations"}
---

How to define and work with one-to-many relations in Prisma.

One-to-many (1-n) relations connect one record on one side to zero or more records on the other side:

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

This expresses:

-   A user can have zero or more posts
-   A post must always have an author

You can also reference a non-ID field with `@unique`:

```
model Post {
  id          Int    @id @default(autoincrement())
  authorEmail String
  author      User   @relation(fields: [authorEmail], references: [email])
}
```

```
model User {
  firstName String
  lastName  String
  post      Post[]
  @@id([firstName, lastName])
}

model Post {
  id              Int    @id @default(autoincrement())
  author          User   @relation(fields: [authorFirstName, authorLastName], references: [firstName, lastName])
  authorFirstName String
  authorLastName  String
}
```

The difference between 1-1 and 1-n is that in a 1-1 relation the foreign key must have a `UNIQUE` constraint. Without `UNIQUE`, multiple records can point to the same parent, making it 1-n.

The annotated relation field and relation scalar can be either optional or mandatory. The list side is always mandatory.

**Optional 1-n** (can create Post without User):

```
model User {
  id    Int    @id @default(autoincrement())
  posts Post[]
}

model Post {
  id       Int   @id @default(autoincrement())
  author   User? @relation(fields: [authorId], references: [id])
  authorId Int?
}
```

**Mandatory 1-n** (must assign User when creating Post):

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
