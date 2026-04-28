---
title: "Many-to-many relations"
source: "https://www.prisma.io/docs/orm/more/troubleshooting/many-to-many-relations"
canonical_url: "https://www.prisma.io/docs/orm/more/troubleshooting/many-to-many-relations"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:37:47.866Z"
content_hash: "8150e7d3e9964eb8156e0dc8dfc6c7dc42c9f31164aea7d82e4bb748232705fa"
menu_path: ["Many-to-many relations"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/more/troubleshooting/graphql-autocompletion/index.md", "title": "GraphQL autocompletion"}
nav_next: {"path": "prisma/docs/orm/more/troubleshooting/nextjs/index.md", "title": "Next.js"}
---

Troubleshooting

Learn how to model, query, and convert many-to-many relations with Prisma ORM

Modeling and querying many-to-many relations in relational databases can be challenging. This guide shows how to work with [implicit](prisma/docs/orm/prisma-schema/data-model/relations/many-to-many-relations/index.md#implicit-many-to-many-relations) and [explicit](prisma/docs/orm/prisma-schema/data-model/relations/many-to-many-relations/index.md#explicit-many-to-many-relations) many-to-many relations, and how to convert between them.

Implicit many-to-many relations let Prisma ORM handle the [relation table](prisma/docs/orm/prisma-schema/data-model/relations/many-to-many-relations/index.md#relation-table-conventions) internally:

```
model Post {
  id    Int    @id @default(autoincrement())
  title String
  tags  Tag[]
}

model Tag {
  id    Int    @id @default(autoincrement())
  name  String @unique
  posts Post[]
}
```

### [Creating records](#creating-records)

```
await prisma.post.create({
  data: {
    title: "Types of relations",
    tags: { create: [{ name: "dev" }, { name: "prisma" }] },
  },
});
```

### [Querying with relations](#querying-with-relations)

```
await prisma.post.findMany({
  include: { tags: true },
});
```

Result:

```
[
  {
    "id": 1,
    "title": "Types of relations",
    "tags": [
      { "id": 1, "name": "dev" },
      { "id": 2, "name": "prisma" }
    ]
  }
]
```

### [Connecting and creating tags simultaneously](#connecting-and-creating-tags-simultaneously)

```
await prisma.post.update({
  where: { id: 1 },
  data: {
    title: "Prisma is awesome!",
    tags: { set: [{ id: 1 }, { id: 2 }], create: { name: "typescript" } },
  },
});
```

Explicit relations are needed when you need to store extra fields in the relation table or when [introspecting](prisma/docs/orm/prisma-schema/introspection/index.md) an existing database:

```
model Post {
  id    Int        @id @default(autoincrement())
  title String
  tags  PostTags[]
}

model PostTags {
  id     Int   @id @default(autoincrement())
  post   Post? @relation(fields: [postId], references: [id])
  tag    Tag?  @relation(fields: [tagId], references: [id])
  postId Int?
  tagId  Int?

  @@index([postId, tagId])
}

model Tag {
  id    Int        @id @default(autoincrement())
  name  String     @unique
  posts PostTags[]
}
```

### [Creating records with explicit relations](#creating-records-with-explicit-relations)

```
await prisma.post.create({
  data: {
    title: "Types of relations",
    tags: {
      create: [{ tag: { create: { name: "dev" } } }, { tag: { create: { name: "prisma" } } }],
    },
  },
});
```

### [Querying with explicit relations](#querying-with-explicit-relations)

```
await prisma.post.findMany({
  include: { tags: { include: { tag: true } } },
});
```

### [Mapping the response](#mapping-the-response)

To get a cleaner response similar to implicit relations:

```
const result = posts.map((post) => {
  return { ...post, tags: post.tags.map((tag) => tag.tag) };
});
```

Sometimes you need to transition from implicit to explicit relations, for example to add metadata like timestamps to the relation.

### [Step 1: Add the explicit relation model](#step-1-add-the-explicit-relation-model)

Keep the implicit relation while adding the new model:

```
model User {
  id        Int        @id @default(autoincrement())
  name      String
  posts     Post[]
  userPosts UserPost[]
}

model Post {
  id        Int        @id @default(autoincrement())
  title     String
  authors   User[]
  userPosts UserPost[]
}

model UserPost {
  id        Int       @id @default(autoincrement())
  userId    Int
  postId    Int
  user      User      @relation(fields: [userId], references: [id])
  post      Post      @relation(fields: [postId], references: [id])
  createdAt DateTime  @default(now())

  @@unique([userId, postId])
}
```

Run the migration:

### [Step 2: Migrate existing data](#step-2-migrate-existing-data)

```
import { PrismaClient } from "../prisma/generated/client";

const prisma = new PrismaClient();

async function main() {
  const users = await prisma.user.findMany({
    include: { posts: true },
  });

  for (const user of users) {
    for (const post of user.posts) {
      await prisma.userPost.create({
        data: {
          userId: user.id,
          postId: post.id,
        },
      });
    }
  }

  console.log("Data migration completed.");
}

main()
  .catch((e) => {
    throw e;
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
```

### [Step 3: Remove implicit relation columns](#step-3-remove-implicit-relation-columns)

After migrating the data, remove the implicit relation columns:

```
model User {
  id        Int        @id @default(autoincrement())
  name      String
  userPosts UserPost[]
}

model Post {
  id        Int        @id @default(autoincrement())
  title     String
  userPosts UserPost[]
}
```

Run the migration:

This will drop the implicit table `_PostToUser`.
