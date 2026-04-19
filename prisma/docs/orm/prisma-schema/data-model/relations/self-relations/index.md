---
title: "Self-relations"
source: "https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/self-relations"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/self-relations"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:40.905Z"
content_hash: "8fcc6a4560fccfa83d59285cd3213ceaa5d0e2d75f5903162fbf4d5af2b35314"
menu_path: ["Self-relations"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-schema/data-model/relations/relation-mode/index.md", "title": "Relation mode"}
nav_next: {"path": "prisma/docs/orm/prisma-schema/data-model/relations/troubleshooting-relations/index.md", "title": "Troubleshooting relations"}
---

Data Model

Relations

How to define and work with self-relations in Prisma.

A relation field can reference its own model, called a _self-relation_. Self-relations can be 1-1, 1-n, or m-n.

```
model User {
  id          Int     @id @default(autoincrement())
  name        String?
  successorId Int?    @unique
  successor   User?   @relation("BlogOwnerHistory", fields: [successorId], references: [id])
  predecessor User?   @relation("BlogOwnerHistory")
}
```

This expresses:

*   A user can have zero or one predecessor
*   A user can have zero or one successor

**Key rules:**

*   Both sides must use the same `@relation` name
*   One side must be fully annotated with `fields` and `references`
*   The foreign key needs `@unique` for 1-1
*   Cannot be required on both sides (impossible to create first record)

```
model User {
  id        Int     @id @default(autoincrement())
  name      String?
  teacherId Int?
  teacher   User?   @relation("TeacherStudents", fields: [teacherId], references: [id])
  students  User[]  @relation("TeacherStudents")
}
```

This expresses:

*   A user has zero or one teacher
*   A user can have zero or more students

No `@unique` constraint on `teacherId` - multiple students can share the same teacher.

```
model User {
  id         Int     @id @default(autoincrement())
  name       String?
  followedBy User[]  @relation("UserFollows")
  following  User[]  @relation("UserFollows")
}
```

This expresses:

*   A user can be followed by zero or more users
*   A user can follow zero or more users

For relational databases, this is an implicit m-n (Prisma manages the relation table).

**Explicit version** (for storing additional fields):

```
model User {
  id         Int       @id @default(autoincrement())
  name       String?
  followedBy Follows[] @relation("followedBy")
  following  Follows[] @relation("following")
}

model Follows {
  followedBy   User @relation("followedBy", fields: [followedById], references: [id])
  followedById Int
  following    User @relation("following", fields: [followingId], references: [id])
  followingId  Int
  @@id([followingId, followedById])
}
```

You can combine multiple self-relations:

```
model User {
  id         Int     @id @default(autoincrement())
  name       String?
  teacherId  Int?
  teacher    User?   @relation("TeacherStudents", fields: [teacherId], references: [id])
  students   User[]  @relation("TeacherStudents")
  followedBy User[]  @relation("UserFollows")
  following  User[]  @relation("UserFollows")
}
```

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-schema/data-model/relations/self-relations.mdx)
