---
title: "Schema location"
source: "https://www.prisma.io/docs/orm/prisma-schema/overview/location"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/overview/location"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:05.473Z"
content_hash: "0a28ddc0076b2649ebbc910a48f167990f506088f43cbb9392ce6d9afef53625"
menu_path: ["Schema location"]
section_path: []
---
Overview

Documentation regarding proper location of Prisma Schema including default naming and multiple files.

The default name for the Prisma Schema is a single file `schema.prisma` in your `prisma` folder. When your schema is named like this, the Prisma CLI will detect it automatically.

The Prisma CLI looks for the Prisma Schema in the following locations, in the following order:

1.  The location specified by the [`--schema` flag](https://www.prisma.io/docs/orm/reference/prisma-cli-reference), which is available when you `introspect`, `generate`, `migrate`, and `studio`:
    
    ```
    prisma generate --schema=./alternative/schema.prisma
    ```
    
2.  The location specified in the `prisma.config.ts` file:
    
    ```
    import { defineConfig } from "prisma/config";
    
    export default defineConfig({
      schema: "prisma/",
      ...
    });
    ```
    
3.  Default locations:
    
    *   `./prisma/schema.prisma`
    *   `./schema.prisma`

The Prisma CLI outputs the path of the schema that will be used. The following example shows the terminal output for `prisma db pull`:

```
Environment variables loaded from .env
Prisma Schema loaded from prisma/schema.prisma

Introspecting based on datasource defined in prisma/schema.prisma …

✔ Introspected 4 models and wrote them into prisma/schema.prisma in 239ms

Run prisma generate to generate Prisma Client.
```

If you prefer splitting your Prisma schema into multiple files, you can have a setup that looks as follows:

```
prisma/
├── migrations
├── models
│   ├── posts.prisma
│   ├── users.prisma
│   └── ... other `.prisma` files
└── schema.prisma
```

### [Usage](#usage)

When using a multi-file Prisma schema, you must always explicitly specify the location of the directory that contains your schema files (including the main `schema.prisma` file with your `generator` block).

You can do this in two ways:

*   pass the `--schema` option to your Prisma CLI command (e.g. `prisma migrate dev --schema ./prisma`)
    
*   set the `schema` property in [`prisma.config.ts`](https://www.prisma.io/docs/orm/reference/prisma-config-reference#schema) (for Prisma ORM v7):
    
    ```
    import { defineConfig, env } from "prisma/config";
    import "dotenv/config";
    
    export default defineConfig({
      schema: "prisma/",
      migrations: {
        path: "prisma/migrations",
        seed: "tsx prisma/seed.ts",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
    ```
    

You must also place the `migrations` directory at the same level as your `schema.prisma` file.

For example, assuming `schema.prisma` defines the `generator` block, here's the correct directory structure:

```
# All files must be inside the `prisma/` directory
# `migrations` and `schema.prisma` must be at the same level
prisma/
├── migrations
├── models
│   ├── posts.prisma
│   └── users.prisma
└── schema.prisma  # Contains generator block
```

### [Tips for multi-file Prisma Schema](#tips-for-multi-file-prisma-schema)

We've found that a few patterns work well with this feature and will help you get the most out of it:

*   Organize your files by domain: group related models into the same file. For example, keep all user-related models in `user.prisma` while post-related models go in `post.prisma`.
*   Use clear naming conventions: schema files should be named clearly and succinctly. Use names like `user.prisma` and `post.prisma` and not `myModels.prisma` or `CommentFeaturesSchema.prisma`.
*   Have an obvious "main" schema file: while you can now have as many schema files as you want, you'll still need a place where you define your `generator` block. We recommend having a single schema file that's obviously the "main" file so that this block is easy to find. `main.prisma`, `schema.prisma`, and `base.prisma` are a few we've seen that work well.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-schema/overview/location.mdx)
