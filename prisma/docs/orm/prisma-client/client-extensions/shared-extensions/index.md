---
title: "Shared Prisma Client extensions"
source: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/shared-extensions"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/shared-extensions"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:28.380Z"
content_hash: "276de5ae44e51d7c60dabc163f21e1beb43a438d94186f0023e163f412b3f827"
menu_path: ["Shared Prisma Client extensions"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-schema/overview/location/index.md", "title": "Schema location"}
nav_next: {"path": "prisma/docs/orm/prisma-client/client-extensions/shared-extensions/permit-rbac/index.md", "title": "Fine-Grained Authorization (Permit)"}
---

You can share your [Prisma Client extensions](prisma/docs/orm/prisma-client/client-extensions/index.md) with other users, either as packages or as modules, and import extensions that other users create into your project.

If you would like to build a shareable extension, we also recommend using the [`prisma-client-extension-starter`](https://github.com/prisma/prisma-client-extension-starter) template.

To explore examples of Prisma's official Client extensions and those made by the community, visit [this](prisma/docs/orm/prisma-client/client-extensions/extension-examples/index.md) page.

In your project, you can install any Prisma Client extension that another user has published to `npm`. To do so, run the following command:

For example, if the package name for an available extension is `prisma-extension-find-or-create`, you could install it as follows:

To import the `find-or-create` extension from the example above, and wrap your client instance with it, you could use the following code. This example assumes that the extension name is `findOrCreate`.

```
import findOrCreate from "prisma-extension-find-or-create";
import { PrismaClient } from "../generated/prisma/client";
const prisma = new PrismaClient();
const xprisma = prisma.$extends(findOrCreate);
const user = await xprisma.user.findOrCreate();
```

When you call a method in an extension, use the constant name from your `$extends` statement, not `prisma`. In the above example, `xprisma.user.findOrCreate` works, but `prisma.user.findOrCreate` does not, because the original `prisma` is not modified.

When you want to create extensions other users can use, and that are not tailored just for your schema, Prisma ORM provides utilities to allow you to create shareable extensions.

To create a shareable extension:

1.  Define the extension as a module using `Prisma.defineExtension`
2.  Use one of the methods that begin with the `$all` prefix such as [`$allModels`](prisma/docs/orm/prisma-client/client-extensions/model/index.md#add-a-custom-method-to-all-models-in-your-schema) or [`$allOperations`](prisma/docs/orm/prisma-client/client-extensions/query/index.md#modify-all-prisma-client-operations)

### [Define an extension](#define-an-extension)

Use the `Prisma.defineExtension` method to make your extension shareable. You can use it to package the extension to either separate your extensions into a separate file or share it with other users as an npm package.

The benefit of `Prisma.defineExtension` is that it provides strict type checks and auto completion for authors of extension in development and users of shared extensions.

### [Use a generic method](#use-a-generic-method)

Extensions that contain methods under `$allModels` apply to every model instead of a specific one. Similarly, methods under `$allOperations` apply to a client instance as a whole and not to a named component, e.g. `result` or `query`.

You do not need to use the `$all` prefix with the [`client`](prisma/docs/orm/prisma-client/client-extensions/client/index.md) component, because the `client` component always applies to the client instance.

For example, a generic extension might take the following form:

```
export default Prisma.defineExtension({
  name: "prisma-extension-find-or-create", //Extension name
  model: {
    $allModels: {
      // new method
      findOrCreate(/* args */) {
        /* code for the new method */
        return query(args);
      },
    },
  },
});
```

Refer to the following pages to learn the different ways you can modify Prisma Client operations:

*   [Modify all Prisma Client operations](prisma/docs/orm/prisma-client/client-extensions/query/index.md#modify-all-prisma-client-operations)
*   [Modify a specific operation in all models of your schema](prisma/docs/orm/prisma-client/client-extensions/query/index.md#modify-a-specific-operation-in-all-models-of-your-schema)
*   [Modify all operations in all models of your schema](prisma/docs/orm/prisma-client/client-extensions/query/index.md#modify-all-operations-in-all-models-of-your-schema)

### [Publishing the shareable extension to npm](#publishing-the-shareable-extension-to-npm)

You can then share the extension on `npm`. When you choose a package name, we recommend that you use the `prisma-extension-<package-name>` convention, to make it easier to find and install.

### [Call a client-level method from your packaged extension](#call-a-client-level-method-from-your-packaged-extension)

In the following situations, you need to refer to a Prisma Client instance that your extension wraps:

*   When you want to use a [client-level method](prisma/docs/orm/reference/prisma-client-reference/index.md#client-methods), such as `$queryRaw`, in your packaged extension.
*   When you want to chain multiple `$extends` calls in your packaged extension.

However, when someone includes your packaged extension in their project, your code cannot know the details of the Prisma Client instance.

You can refer to this client instance as follows:

```
Prisma.defineExtension((client) => {
  // The Prisma Client instance that the extension user applies the extension to
  return client.$extends({
    name: "prisma-extension-<extension-name>",
  });
});
```

For example:

```
export default Prisma.defineExtension((client) => {
  return client.$extends({
    name: "prisma-extension-find-or-create",
    query: {
      $allModels: {
        async findOrCreate({ args, query, operation }) {
          return (await client.$transaction([query(args)]))[0];
        },
      },
    },
  });
});
```

### [Advanced type safety: type utilities for defining generic extensions](#advanced-type-safety-type-utilities-for-defining-generic-extensions)

You can improve the type-safety of your shared extensions using [type utilities](prisma/docs/orm/prisma-client/client-extensions/type-utilities/index.md).

