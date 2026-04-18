---
title: "Working with scalar lists"
source: "https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-scalar-lists-arrays"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-scalar-lists-arrays"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:27.885Z"
content_hash: "fffc6f2322586017758430a547e36cd0ead904656928deea7c4fdee9ae7fe7a9"
menu_path: ["Working with scalar lists"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/special-fields-and-types/working-with-composite-ids-and-constraints/index.md", "title": "Working with compound IDs and unique constraints"}
nav_next: {"path": "prisma/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields/index.md", "title": "Working with Json fields"}
---

Special Fields and Types

How to read, write, and filter by scalar lists / arrays

[Scalar lists](prisma/docs/orm/reference/prisma-schema-reference/index.md#-modifier) are represented by the `[]` modifier and are only available if the underlying database supports scalar lists. The following example has one scalar `String` list named `pets`:

Example field value:

```
["Fido", "Snoopy", "Brian"]
```

The following example demonstrates how to [`set`](prisma/docs/orm/reference/prisma-client-reference/index.md) the value of a scalar list (`coinflips`) when you create a model:

```
const createdUser = await prisma.user.create({
  data: {
    email: "eloise@prisma.io",
    coinflips: [true, true, true, false, true],
  },
});
```

The following example demonstrates how to [`unset`](prisma/docs/orm/reference/prisma-client-reference/index.md#unset) the value of a scalar list (`coinflips`):

```
const createdUser = await prisma.user.create({
  data: {
    email: "eloise@prisma.io",
    coinflips: {
      unset: true,
    },
  },
});
```

Unlike `set: null`, `unset` removes the list entirely.

Use the [`push`](prisma/docs/orm/reference/prisma-client-reference/index.md#push) method to add a single value to a scalar list:

```
const userUpdate = await prisma.user.update({
  where: {
    id: 9,
  },
  data: {
    coinflips: {
      push: true,
    },
  },
});
```

In earlier versions, you have to overwrite the entire value. The following example retrieves user, uses `push()` to add three new coin flips, and overwrites the `coinflips` field in an `update`:

```
const user = await prisma.user.findUnique({
  where: {
    email: "eloise@prisma.io",
  },
});

if (user) {
  console.log(user.coinflips);

  user.coinflips.push(true, true, false);

  const updatedUser = await prisma.user.update({
    where: {
      email: "eloise@prisma.io",
    },
    data: {
      coinflips: user.coinflips,
    },
  });

  console.log(updatedUser.coinflips);
}
```

Use [scalar list filters](prisma/docs/orm/reference/prisma-client-reference/index.md#scalar-list-filters) to filter for records with scalar lists that match a specific condition. The following example returns all posts where the tags list includes `databases` _and_ `typescript`:

```
const posts = await prisma.post.findMany({
  where: {
    tags: {
      hasEvery: ["databases", "typescript"],
    },
  },
});
```

### [`NULL` values in arrays](#null-values-in-arrays)

When using scalar list filters with a relational database connector, array fields with a `NULL` value are not considered by the following conditions:

*   `NOT` (array does not contain X)
*   `isEmpty` (array is empty)

This means that records you might expect to see are not returned. Consider the following examples:

*   The following query returns all posts where the `tags` **do not** include `databases`:
    
    ```
    const posts = await prisma.post.findMany({
      where: {
        NOT: {
          tags: {
            has: "databases",
          },
        },
      },
    });
    ```
    
    *   ✔ Arrays that do not contain `"databases"`, such as `{"typescript", "graphql"}`
    *   ✔ Empty arrays, such as `[]`
    
    The query does not return:
    
    *   ✘ `NULL` arrays, even though they do not contain `"databases"`

The following query returns all posts where `tags` is empty:

```
const posts = await prisma.post.findMany({
  where: {
    tags: {
      isEmpty: true,
    },
  },
});
```

The query returns:

*   ✔ Empty arrays, such as `[]`

The query does not return:

*   ✘ `NULL` arrays, even though they could be considered empty

To work around this issue, you can set the default value of array fields to `[]`.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/special-fields-and-types/working-with-scalar-lists-arrays.mdx)

