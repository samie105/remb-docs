---
title: "One-to-one relations"
source: "https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-one-relations"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-one-relations"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:27.239Z"
content_hash: "dd38fd60672bdad49128ab45e2340a9ac60ae9df2cc9e79e4fafcd2ab8b316cd"
menu_path: ["One-to-one relations"]
section_path: []
---
Data Model

Relations

How to define and work with one-to-one relations in Prisma.

One-to-one (1-1) relations connect at most **one** record on each side. In this example, `User` and `Profile` have a 1-1 relation:

```
model User {
  id      Int      @id @default(autoincrement())
  profile Profile?
}

model Profile {
  id     Int  @id @default(autoincrement())
  user   User @relation(fields: [userId], references: [id])
  userId Int  @unique // Foreign key with unique constraint
}
```

This expresses:

*   A user can have zero or one profile
*   A profile must always be connected to exactly one user

You can also reference a non-ID field with `@unique`:

```
model Profile {
  id        Int    @id @default(autoincrement())
  user      User   @relation(fields: [userEmail], references: [email])
  userEmail String @unique
}
```

```
model User {
  firstName String
  lastName  String
  profile   Profile?
  @@id([firstName, lastName])
}

model Profile {
  id            Int    @id @default(autoincrement())
  user          User   @relation(fields: [userFirstName, userLastName], references: [firstName, lastName])
  userFirstName String
  userLastName  String
  @@unique([userFirstName, userLastName])
}
```

In SQL, a 1-1 relation requires a `UNIQUE` constraint on the foreign key. Without this, it becomes a 1-n relation.

For MongoDB, documents reference each other by ID:

```
// User
{ "_id": { "$oid": "60d58e130011041800d209e1" }, "name": "Bob" }
// Profile
{ "_id": "...", "bio": "I like drawing.", "userId": { "$oid": "60d58e130011041800d209e1" } }
```

The side _without_ a relation scalar must be optional:

```
model User {
  id      Int      @id @default(autoincrement())
  profile Profile? // No relation scalar - must be optional
}
```

The side _with_ a relation scalar can be required or optional:

**Mandatory 1-1** (cannot create User without Profile):

```
model User {
  id        Int     @id @default(autoincrement())
  profile   Profile @relation(fields: [profileId], references: [id])
  profileId Int     @unique
}
```

**Optional 1-1** (can create User without Profile):

```
model User {
  id        Int      @id @default(autoincrement())
  profile   Profile? @relation(fields: [profileId], references: [id])
  profileId Int?     @unique
}
```

In 1-1 relations, you can choose which side holds the `@relation` attribute and foreign key. Both approaches are valid:

**Option 1:** Foreign key on `Profile`

```
model User {
  id      Int      @id @default(autoincrement())
  profile Profile?
}

model Profile {
  id     Int  @id @default(autoincrement())
  user   User @relation(fields: [userId], references: [id])
  userId Int  @unique
}
```

**Option 2:** Foreign key on `User`

```
model User {
  id        Int      @id @default(autoincrement())
  profile   Profile? @relation(fields: [profileId], references: [id])
  profileId Int?     @unique
}

model Profile {
  id   Int   @id @default(autoincrement())
  user User?
}
```

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-schema/data-model/relations/one-to-one-relations.mdx)
