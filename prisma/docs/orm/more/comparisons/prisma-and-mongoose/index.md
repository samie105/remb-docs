---
title: "Mongoose"
source: "https://www.prisma.io/docs/orm/more/comparisons/prisma-and-mongoose"
canonical_url: "https://www.prisma.io/docs/orm/more/comparisons/prisma-and-mongoose"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:01.972Z"
content_hash: "43ee432bf03d141a564e7c787d29d2ba5ae6ecf2ede17cde23fe6cccbd37bb9f"
menu_path: ["Mongoose"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/more/comparisons/prisma-and-drizzle/index.md", "title": "Drizzle"}
nav_next: {"path": "prisma/docs/orm/more/comparisons/prisma-and-sequelize/index.md", "title": "Sequelize"}
---

Comparisons

Learn how Prisma ORM compares to Mongoose

This page compares the Prisma ORM and [Mongoose](https://mongoosejs.com/docs/guide.html) APIs. If you want to learn how to migrate from Mongoose to Prisma, check out this [guide](https://www.prisma.io/docs/guides/switch-to-prisma-orm/from-mongoose).

**Prisma ORM**

```
const user = await prisma.user.findUnique({
  where: {
    id: 1,
  },
});
```

**Mongoose**

```
const result = await User.findById(1);
```

**Prisma ORM**

```
const user = await prisma.user.findUnique({
  where: {
    id: 1,
  },
  select: {
    name: true,
  },
});
```

**Mongoose**

```
const user = await User.findById(1).select(["name"]);
```

**Prisma ORM**

**Mongoose**

```
const userWithPost = await User.findById(2).populate("post");
```

**Prisma ORM**

```
const posts = await prisma.post.findMany({
  where: {
    title: {
      contains: "Hello World",
    },
  },
});
```

**Mongoose**

```
const posts = await Post.find({
  title: "Hello World",
});
```

**Prisma ORM**

Prisma ORM generates many [additional filters](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting) that are commonly used in modern application development.

**Mongoose**

Mongoose exposes the [MongoDB query selectors](https://www.mongodb.com/docs/manual/reference/mql/query-predicates/logical/) as filter criteria.

**Prisma ORM**

Prisma ORM lets you filter a list based on a criteria that applies not only to the models of the list being retrieved, but to a _relation_ of that model.

For example, the following query returns users with one or more posts with "Hello" in the title:

```
const posts = await prisma.user.findMany({
  where: {
    Post: {
      some: {
        title: {
          contains: "Hello",
        },
      },
    },
  },
});
```

**Mongoose**

Mongoose doesn't offer a dedicated API for relation filters. You can get similar functionality by adding an additional step to filter the results returned by the query.

**Prisma ORM**

Cursor-style pagination:

```
const page = prisma.post.findMany({
  before: {
    id: 242,
  },
  last: 20,
});
```

Offset pagination:

```
const cc = prisma.post.findMany({
  skip: 200,
  first: 20,
});
```

**Mongoose**

```
const posts = await Post.find({
  skip: 200,
  limit: 20,
});
```

**Prisma ORM**

```
const user = await prisma.user.create({
  data: {
    name: "Alice",
    email: "alice@prisma.io",
  },
});
```

**Mongoose**

**Prisma ORM**

```
const user = await prisma.user.update({
  data: {
    name: "Alicia",
  },
  where: {
    id: 2,
  },
});
```

**Mongoose**

**Prisma ORM**

```
const user = prisma.user.delete({
  where: {
    id: 10,
  },
});
```

**Mongoose**

```
await User.deleteOne({ _id: 10 });
```

**Prisma ORM**

```
const users = await prisma.user.deleteMany({
  where: {
    id: {
      in: [1, 2, 6, 6, 22, 21, 25],
    },
  },
});
```

**Mongoose**

```
await User.deleteMany({ id: { $in: [1, 2, 6, 6, 22, 21, 25] } });
```

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/more/comparisons/prisma-and-mongoose.mdx)


