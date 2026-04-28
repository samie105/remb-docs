---
title: "Add custom methods to your models"
source: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/model"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/model"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:38:09.802Z"
content_hash: "72f7c4e212504a3248c9d331e2a18b666aeb283cae7393cac1c065be23c5d4e0"
menu_path: ["Add custom methods to your models"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/client-extensions/extension-examples/index.md", "title": "Shared packages & examples"}
nav_next: {"path": "prisma/docs/orm/prisma-client/client-extensions/query/index.md", "title": "Create custom Prisma Client queries"}
---

Client Extensions

## Add custom methods to your models

Extend the functionality of Prisma Client, model component

You can use the `model` [Prisma Client extensions](prisma/docs/orm/prisma-client/client-extensions/index.md) component type to add custom methods to your models.

Possible uses for the `model` component include the following:

-   New operations to operate alongside existing Prisma Client operations, such as `findMany`
-   Encapsulated business logic
-   Repetitive operations
-   Model-specific utilities

Use the `$extends` [client-level method](prisma/docs/orm/reference/prisma-client-reference/index.md#client-methods) to create an _extended client_. An extended client is a variant of the standard Prisma Client that is wrapped by one or more extensions. Use the `model` extension component to add methods to models in your schema.

### [Add a custom method to a specific model](#add-a-custom-method-to-a-specific-model)

To extend a specific model in your schema, use the following structure. This example adds a method to the `user` model.

```
const prisma = new PrismaClient().$extends({
  name?: '<name>',  // (optional) names the extension for error logs
  model?: {
    user: { ... }   // in this case, we extend the `user` model
  },
});
```

#### [Example](#example)

The following example adds a method called `signUp` to the `user` model. This method creates a new user with the specified email address:

```
const prisma = new PrismaClient().$extends({
  model: {
    user: {
      async signUp(email: string) {
        await prisma.user.create({ data: { email } });
      },
    },
  },
});
```

You would call `signUp` in your application as follows:

```
const user = await prisma.user.signUp("john@prisma.io");
```

### [Add a custom method to all models in your schema](#add-a-custom-method-to-all-models-in-your-schema)

To extend _all_ models in your schema, use the following structure:

```
const prisma = new PrismaClient().$extends({
  name?: '<name>', // `name` is an optional field that you can use to name the extension for error logs
  model?: {
    $allModels: { ... }
  },
})
```

#### [Example](#example-1)

The following example adds an `exists` method to all models.

```
const prisma = new PrismaClient().$extends({
  model: {
    $allModels: {
      async exists<T>(this: T, where: Prisma.Args<T, "findFirst">["where"]): Promise<boolean> {
        // Get the current model at runtime
        const context = Prisma.getExtensionContext(this);

        const result = await (context as any).findFirst({ where });
        return result !== null;
      },
    },
  },
});
```

You would call `exists` in your application as follows:

```
// `exists` method available on all models
await prisma.user.exists({ name: "Alice" });
await prisma.post.exists({
  OR: [{ title: { contains: "Prisma" } }, { content: { contains: "Prisma" } }],
});
```

You can call a custom method from another custom method, if the two methods are declared on the same model. For example, you can call a custom method on the `user` model from another custom method on the `user` model. It does not matter if the two methods are declared in the same extension or in different extensions.

To do so, use `Prisma.getExtensionContext(this).methodName`. Note that you cannot use `prisma.user.methodName`. This is because `prisma` is not extended yet, and therefore does not contain the new method.

For example:

```
const prisma = new PrismaClient().$extends({
  model: {
    user: {
      firstMethod() {
        ...
      },
      secondMethod() {
          Prisma.getExtensionContext(this).firstMethod()
      }
    }
  }
})
```

You can get the name of the current model at runtime with `Prisma.getExtensionContext(this).$name`. You might use this to write out the model name to a log, to send the name to another service, or to branch your code based on the model.

For example:

```
// `context` refers to the current model
const context = Prisma.getExtensionContext(this);

// `context.$name` returns the name of the current model
console.log(context.$name);

// Usage
await (context as any).findFirst({ args });
```

Refer to [Add a custom method to all models in your schema](#example-1) for a concrete example for retrieving the current model name at runtime.

You can improve the type-safety of `model` components in your shared extensions with [type utilities](prisma/docs/orm/prisma-client/client-extensions/type-utilities/index.md).
