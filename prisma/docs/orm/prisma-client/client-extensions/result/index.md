---
title: "Add custom fields and methods to query results"
source: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/result"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/result"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:06.632Z"
content_hash: "288b11f220b0fd092a82cf707a89ba43cf6bea02c44b64426f323b79ffbe5c7e"
menu_path: ["Add custom fields and methods to query results"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/client-extensions/index.md", "title": "What are Client Extensions"}
nav_next: {"path": "prisma/docs/orm/prisma-client/client-extensions/type-utilities/index.md", "title": "Type utilities"}
---

You can use the `result` [Prisma Client extensions](prisma/docs/orm/prisma-client/client-extensions/index.md) component type to add custom fields and methods to query results.

Use the `$extends` [client-level method](prisma/docs/orm/reference/prisma-client-reference/index.md#client-methods) to create an _extended client_. An extended client is a variant of the standard Prisma Client that is wrapped by one or more extensions.

To add a custom [field](#add-a-custom-field-to-query-results) or [method](#add-a-custom-method-to-the-result-object) to query results, use the following structure. In this example, we add the custom field `myComputedField` to the result of a `user` model query.

```
const prisma = new PrismaClient().$extends({
  name?: 'name',
  result?: {
    user: {                   // in this case, we extend the `user` model
      myComputedField: {      // the name of the new computed field
        needs: { ... },
        compute() { ... }
      },
    },
  },
});
```

The parameters are as follows:

*   `name`: (optional) specifies a name for the extension that appears in error logs.
*   `result`: defines new fields and methods to the query results.
*   `needs`: an object which describes the dependencies of the result field.
*   `compute`: a method that defines how the virtual field is computed when it is accessed.

You can use the `result` extension component to add fields to query results. These fields are computed at runtime and are type-safe.

In the following example, we add a new virtual field called `fullName` to the `user` model.

```
const prisma = new PrismaClient().$extends({
  result: {
    user: {
      fullName: {
        // the dependencies
        needs: { firstName: true, lastName: true },
        compute(user) {
          // the computation logic
          return `${user.firstName} ${user.lastName}`;
        },
      },
    },
  },
});

const user = await prisma.user.findFirst();

// return the user's full name, such as "John Doe"
console.log(user.fullName);
```

In above example, the input `user` of `compute` is automatically typed according to the object defined in `needs`. `firstName` and `lastName` are of type `string`, because they are specified in `needs`. If they are not specified in `needs`, then they cannot be accessed.

The following example computes a user's title and full name in a type-safe way. `titleFullName` is a computed field that reuses the `fullName` computed field.

```
const prisma = new PrismaClient()
  .$extends({
    result: {
      user: {
        fullName: {
          needs: { firstName: true, lastName: true },
          compute(user) {
            return `${user.firstName} ${user.lastName}`;
          },
        },
      },
    },
  })
  .$extends({
    result: {
      user: {
        titleFullName: {
          needs: { title: true, fullName: true },
          compute(user) {
            return `${user.title} (${user.fullName})`;
          },
        },
      },
    },
  });
```

### [Considerations for fields](#considerations-for-fields)

*   For performance reasons, Prisma Client computes results on access, not on retrieval.
    
*   You can only create computed fields that are based on scalar fields.
    
*   You can only use computed fields with `select` and you cannot aggregate them. For example:
    
    ```
    const user = await prisma.user.findFirst({
      select: { email: true },
    });
    console.log(user.fullName); // undefined
    ```
    

You can use the `result` component to add methods to query results. The following example adds a new method, `save` to the result object.

```
const prisma = new PrismaClient().$extends({
  result: {
    user: {
      save: {
        needs: { id: true },
        compute(user) {
          return () => prisma.user.update({ where: { id: user.id }, data: user });
        },
      },
    },
  },
});

const user = await prisma.user.findUniqueOrThrow({ where: { id: someId } });
user.email = "mynewmail@mailservice.com";
await user.save();
```

You can use the [`omit` (Preview) option](prisma/docs/orm/reference/prisma-client-reference/index.md#omit) with [custom fields](#add-a-custom-field-to-query-results) and fields needed by custom fields.

### [`omit` fields needed by custom fields from query result](#omit-fields-needed-by-custom-fields-from-query-result)

If you `omit` a field that is a dependency of a custom field, it will still be read from the database even though it will not be included in the query result.

The following example omits the `password` field, which is a dependency of the custom field `sanitizedPassword`:

```
const xprisma = prisma.$extends({
  result: {
    user: {
      sanitizedPassword: {
        needs: { password: true },
        compute(user) {
          return sanitize(user.password);
        },
      },
    },
  },
});

const user = await xprisma.user.findFirstOrThrow({
  omit: {
    password: true,
  },
});
```

In this case, although `password` is omitted from the result, it will still be queried from the database because it is a dependency of the `sanitizedPassword` custom field.

### [`omit` custom field and dependencies from query result](#omit-custom-field-and-dependencies-from-query-result)

To ensure omitted fields are not queried from the database at all, you must omit both the custom field and its dependencies.

The following example omits both the custom field `sanitizedPassword` and the dependent `password` field:

```
const xprisma = prisma.$extends({
  result: {
    user: {
      sanitizedPassword: {
        needs: { password: true },
        compute(user) {
          return sanitize(user.password);
        },
      },
    },
  },
});

const user = await xprisma.user.findFirstOrThrow({
  omit: {
    sanitizedPassword: true,
    password: true,
  },
});
```

In this case, omitting both `password` and `sanitizedPassword` will exclude both from the result as well as prevent the `password` field from being read from the database.

As of now, Prisma Client's result extension component does not support relation fields. This means that you cannot create custom fields or methods based on related models or fields in a relational relationship (e.g., user.posts, post.author). The needs parameter can only reference scalar fields within the same model. Follow [issue #20091 on GitHub](https://github.com/prisma/prisma/issues/20091).

```
const prisma = new PrismaClient().$extends({
  result: {
    user: {
      postsCount: {
        needs: { posts: true }, // This will not work because posts is a relation field
        compute(user) {
          return user.posts.length; // Accessing a relation is not allowed
        },
      },
    },
  },
});
```

