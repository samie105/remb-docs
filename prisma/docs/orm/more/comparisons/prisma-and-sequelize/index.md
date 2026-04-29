---
title: "Sequelize"
source: "https://www.prisma.io/docs/orm/more/comparisons/prisma-and-sequelize"
canonical_url: "https://www.prisma.io/docs/orm/more/comparisons/prisma-and-sequelize"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:37:13.810Z"
content_hash: "458582827947c87382aa78a582aab3315943783591af6649b68d077ff7bac32e"
menu_path: ["Sequelize"]
section_path: []
tab_variants: ["Using include","Fluent API","Using save","Using create","Using save","Using update","Manual","Automatic"]
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/more/comparisons/prisma-and-mongoose/index.md", "title": "Mongoose"}
nav_next: {"path": "prisma/docs/orm/more/comparisons/prisma-and-typeorm/index.md", "title": "TypeORM"}
---

Comparisons

Learn how Prisma ORM compares to Sequelize

This page compares the Prisma ORM and [Sequelize](https://sequelize.org/docs/v6/) APIs.

While Prisma ORM and Sequelize solve similar problems, they work in very different ways.

**Sequelize** is a traditional ORM which maps _tables_ to _model classes_. Instances of the model classes then provide an interface for CRUD queries to an application at runtime.

**Prisma ORM** is a new kind of ORM that mitigates many problems of traditional ORMs, such as bloated model instances, mixing business with storage logic, lack of type-safety or unpredictable queries caused e.g. by lazy loading.

It uses the [Prisma schema](../../../prisma-schema/overview/index.md) to define application models in a declarative way. Prisma Migrate then allows to generate SQL migrations from the Prisma schema and executes them against the database. CRUD queries are provided by Prisma Client, a lightweight and entirely type-safe database client for Node.js and TypeScript.

### [Fetching single objects](#fetching-single-objects)

**Prisma ORM**

```
const user = await prisma.user.findUnique({
  where: {
    id: 1,
  },
});
```

**Sequelize**

```
const user = await User.findByPk(id);
```

### [Fetching selected scalars of single objects](#fetching-selected-scalars-of-single-objects)

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

**Sequelize**

```
const user = await User.findByPk(1, { attributes: ["name"], raw: true });
```

### [Fetching relations](#fetching-relations)

**Prisma ORM**

> **Note**: `select` returns a `user` object that includes a `post` array, whereas the fluent API only returns a `post` array.

**Sequelize**

```
const user = await User.findByPk(id, {
  include: [
    {
      model: Post,
    },
  ],
});
```

### [Filtering for concrete values](#filtering-for-concrete-values)

**Prisma ORM**

```
const posts = await prisma.post.findMany({
  where: {
    title: {
      contains: "Hello",
    },
  },
});
```

**Sequelize**

```
const post = await Post.findAll({
  raw: true,
  where: {
    title: {
      [Op.like]: "%Hello%",
    },
  },
});
```

### [Other filter criteria](#other-filter-criteria)

**Prisma ORM**

Prisma ORM generates many [additional filters](https://www.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting) that are commonly used in modern application development.

**Sequelize**

Sequelize has an [extensive set of operators](https://sequelize.org/docs/v6/core-concepts/model-querying-basics/#operators).

### [Relation filters](#relation-filters)

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

**Sequelize**

Sequelize [doesn't offer a dedicated API for relation filters](https://github.com/sequelize/sequelize/issues/10943). You can get similar functionality by sending a raw SQL query to the database.

**Prisma ORM**

Cursor-style pagination:

```
const page = await prisma.post.findMany({
  before: {
    id: 242,
  },
  last: 20,
});
```

Offset pagination:

```
const cc = await prisma.post.findMany({
  skip: 200,
  first: 20,
});
```

**Sequelize**

Cursor pagination:

```
const posts = await Post.findAll({
  limit: 20,
  where: {
    id: {
      [Op.gt]: 242,
    },
  },
});
```

> **Note**: Sequelize use the [Sequelize operators](https://sequelize.org/docs/v6/core-concepts/model-querying-basics/#operators) to perform cursor pagination.

Offset pagination:

```
const posts = await Post.findAll({
  offset: 5,
  limit: 10,
});
```

### [Creating objects](#creating-objects)

**Prisma ORM**

```
const user = await prisma.user.create({
  data: {
    email: "alice@prisma.io",
  },
});
```

**Sequelize**

### [Updating objects](#updating-objects)

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

**Sequelize**

### [Deleting objects](#deleting-objects)

**Prisma ORM**

```
const user = await prisma.user.delete({
  where: {
    id: 10,
  },
});
```

**Sequelize**

```
await user.destroy();
```

### [Batch updates](#batch-updates)

**Prisma ORM**

```
const user = await prisma.user.updateMany({
  data: {
    name: "Published author!",
  },
  where: {
    email: {
      contains: "prisma.io",
    },
  },
});
```

**Sequelize**

```
const updatedUsers = await User.update({
  { role: "Admin" },
  where: {
    email: {
      [Op.like]: "%@prisma.io"
    }
  },
})
```

### [Batch deletes](#batch-deletes)

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

**Sequelize**

```
await User.destroy({
  where: {
    id: {
      [Op.in]: [id1, id2, id3],
    },
  },
});
```

### [Transactions](#transactions)

**Prisma ORM**

```
const user = await prisma.user.create({
  data: {
    email: "bob.rufus@prisma.io",
    name: "Bob Rufus",
    Post: {
      create: [{ title: "Working at Prisma" }, { title: "All about databases" }],
    },
  },
});
```

**Sequelize**
