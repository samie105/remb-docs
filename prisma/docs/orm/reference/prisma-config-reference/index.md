---
title: "Config API"
source: "https://www.prisma.io/docs/orm/reference/prisma-config-reference"
canonical_url: "https://www.prisma.io/docs/orm/reference/prisma-config-reference"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:35:36.287Z"
content_hash: "91d3a267e01c490d78544e0a25bebde9de92a115ee3473a3aa7c711f0990a366"
menu_path: ["Config API"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "../prisma-schema-reference/index.md", "title": "Schema API"}
nav_next: {"path": "../connection-urls/index.md", "title": "Connection URLs"}
---

# `migrations` and `schema.prisma` are on the same level
.
├── migrations
├── models
│   ├── posts.prisma
│   └── users.prisma
└── schema.prisma
```

Prisma CLI commands such as `prisma validate` or `prisma migrate` use `prisma.config.ts` (or `.config/prisma.ts`) to locate your Prisma schema and other resources.

**Key rules:**

-   Paths defined in the config file (e.g., `schema`, `migrations`) are always resolved **relative to the location of the config file**, not where you run the CLI command from.
-   The CLI must first **find the config file** itself, which depends on how Prisma is installed and the package manager used.

### [Behavior with `pnpm prisma`](#behavior-with-pnpm-prisma)

When Prisma is installed locally and run via `pnpm prisma`, the config file is detected automatically whether you run the command from the project root or a subdirectory.

Example project tree:

```
.
├── node_modules
├── package.json
├── prisma-custom
│   └── schema.prisma
├── prisma.config.ts
└── src
```

Example run from the project root:

```
pnpm prisma validate
# → Loaded Prisma config from ./prisma.config.ts
# → Prisma schema loaded from prisma-custom/schema.prisma
```

Example run from a subdirectory:

```
cd src
pnpm prisma validate
# → Still finds prisma.config.ts and resolves schema correctly
```

### [Behavior with `npx prisma` or `bunx --bun prisma`](#behavior-with-npx-prisma-or-bunx---bun-prisma)

When running via `npx prisma` or `bunx --bun prisma`, the CLI only detects the config file if the command is run from the **project root** (where `package.json` declares Prisma).

Example run from the project root:

Run from a subdirectory (fails):

To fix this, you can use the `--config` flag:

### [Global Prisma installations](#global-prisma-installations)

If Prisma is installed globally (`npm i -g prisma`), it may not find your `prisma.config.ts` or `prisma/config` module by default. To avoid issues:

-   Prefer local Prisma installations in your project.
-   Or use `prisma/config` locally and pass `--config` to point to your config file.

### [Monorepos](#monorepos)

-   If Prisma is installed in the **workspace root**, `pnpm prisma` will detect the config file from subdirectories.
-   If Prisma is installed in a **subpackage** (e.g., `./packages/db`), run commands from that package directory or deeper.

### [Custom config location](#custom-config-location)

You can specify a custom location for your config file when running Prisma CLI commands:

```
prisma validate --config ./path/to/myconfig.ts
```

To load environment variables, install the `dotenv` package and add `import 'dotenv/config'` at the top of your `prisma.config.ts` file.

To load environment variables in your Prisma application, you can use the `prisma.config.ts` file along with the `env` helper from `prisma/config`. This approach provides better type safety and configuration management.

1.  Install the `dotenv` package:
    
2.  Create a `.env` file in your project root (if it doesn't exist) and add your database connection string:
    
    ```
    DATABASE_URL="your_database_connection_string_here"
    ```
    
3.  Ensure your `prisma.config.ts` file imports `dotenv/config` at the top:
    
    prisma.config.ts
    
    ```
    import "dotenv/config"; 
    import { defineConfig, env } from "prisma/config";
    
    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
        seed: "tsx prisma/seed.ts",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
    ```
