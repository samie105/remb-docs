---
title: "Config API"
source: "https://www.prisma.io/docs/orm/reference/prisma-config-reference"
canonical_url: "https://www.prisma.io/docs/orm/reference/prisma-config-reference"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:16.981Z"
content_hash: "6b428deb1f183b51077023337c7710b633ecf4cbae0e388e7570c9700946f64a"
menu_path: ["Config API"]
section_path: []
---
The Prisma Config file (`prisma.config.ts`) configures the Prisma CLI using TypeScript. It's automatically created when you run `prisma init`.

You can define your config using either the `defineConfig` helper or TypeScript's `satisfies` operator:

*   Using the `defineConfig` helper:
    
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
    
*   Using TypeScript's `satisfies` operator with the `PrismaConfig` type:
    
    ```
    import "dotenv/config";
    import type { PrismaConfig } from "prisma";
    import { env } from "prisma/config";
    
    export default {
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
        seed: "tsx prisma/seed.ts",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    } satisfies PrismaConfig;
    ```
    

Here is a simplified version of the `PrismaConfig` type:

```
export declare type PrismaConfig = {
  // Whether features with an unstable API are enabled.
  experimental: {
    externalTables: boolean;
  };

  // The path to the schema file, or path to a folder that shall be recursively searched for *.prisma files.
  schema?: string;

  // Configuration for Prisma migrations.
  migrations?: {
    path: string;
    seed: string;
    initShadowDb: string;
  };

  // Configuration for the database view entities.
  views?: {
    path: string;
  };

  // Configuration for the `typedSql` preview feature.
  typedSql?: {
    path: string;
  };

  // Database connection configuration
  datasource?: {
    url: string;
    shadowDatabaseUrl?: string;
  };
};
```

Prisma Config files can be named as `prisma.config.*` or `.config/prisma.*` with the extensions `js`, `ts`, `mjs`, `cjs`, `mts`, or `cts`. Other extensions are supported to ensure compatibility with different TypeScript compiler settings.

### [`schema`](#schema)

Configures how Prisma ORM locates and loads your schema file(s). Can be a file or folder path. Relative paths are resolved relative to the `prisma.config.ts` file location. See [here](https://www.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema) for more info about schema location options.

Property

Type

Required

Default

`schema`

`string`

No

`./prisma/schema.prisma` and `./schema.prisma`

### [`tables.external` and `enums.external`](#tablesexternal-and-enumsexternal)

These options declare tables and enums in your database that are **managed externally** (not by Prisma Migrate). You can still query them with Prisma Client, but they will be ignored by migrations.

Property

Type

Required

Default

`tables.external`

`string[]`

No

`[]`

`enums.external`

`string[]`

No

`[]`

**Example:**

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
  experimental: {
    externalTables: true,
  },
  tables: {
    external: ["public.users"],
  },
  enums: {
    external: ["public.role"],
  },
});
```

Learn more about the [`externalTables` feature here](https://www.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables).

### [`migrations.path`](#migrationspath)

The path to the directory where Prisma should store migration files, and look for them.

Property

Type

Required

Default

`migrations.path`

`string`

No

none

### [`migrations.seed`](#migrationsseed)

Defines the command to run when executing `npx prisma db seed`. Seeding is only triggered explicitly via this command.

Property

Type

Required

Default

`migrations.seed`

`string`

No

none

**Example:**

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
    seed: "tsx db/seed.ts",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

### [`migrations.initShadowDb`](#migrationsinitshadowdb)

This option allows you to define SQL statements that Prisma runs on the **shadow database** before creating migrations. It is useful when working with [external managed tables](https://www.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables), as Prisma needs to know about the structure of these tables to correctly generate migrations.

Property

Type

Required

Default

`migrations.initShadowDb`

`string`

No

none

**Example:**

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
    initShadowDb: `
      CREATE TABLE public.users (id SERIAL PRIMARY KEY);
    `,
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
  experimental: {
    externalTables: true,
  },
  tables: {
    external: ["public.users"],
  },
});
```

Learn more about the [`externalTables` feature here](https://www.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables).

### [`views.path`](#viewspath)

The path to the directory where Prisma should look for the SQL view definitions.

Property

Type

Required

Default

`views.path`

`string`

No

none

### [`typedSql.path`](#typedsqlpath)

The path to the directory where Prisma should look for the SQL files used for generating typings via [`typedSql`](https://www.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql).

Property

Type

Required

Default

`typedSql.path`

`string`

No

none

### [`experimental`](#experimental)

Enables specific experimental features in the Prisma CLI.

Property

Type

Required

Default

`externalTables`

`boolean`

No

`false`

Example:

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
  experimental: {
    externalTables: true,
  },
});
```

### [`datasource.url`](#datasourceurl)

Connection URL including authentication info. Uses [the syntax provided by the database](https://www.prisma.io/docs/orm/reference/connection-urls#format).

Property

Type

Required

Default

`datasource.url`

`string`

Yes

`''`

**Example:**

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

### [`datasource.shadowDatabaseUrl`](#datasourceshadowdatabaseurl)

Connection URL to the shadow database used by Prisma Migrate. Allows you to use a cloud-hosted database as the shadow database.

Property

Type

Required

Default

`datasource.shadowDatabaseUrl`

`string`

No

`''`

### [`datasource.directUrl` (Removed)](#datasourcedirecturl-removed)

For Prisma ORM v6.19 and earlier

Connection URL for direct connection to the database.

If you use a connection pooler URL in the `url` argument (for example, pgBouncer), Prisma CLI commands that require a direct connection to the database use the URL in the `directUrl` argument.

The `directUrl` property is supported by Prisma Studio from version 5.1.0 upwards. The `directUrl` property is not needed when using [Prisma Postgres](https://www.prisma.io/docs/postgres) database.

Property

Type

Required

Default

`datasource.directUrl`

`string`

No

`''`

### [`adapter` (Removed)](#adapter-removed)

For Prisma ORM v6.19 and earlier

A function that returns a Prisma driver adapter instance which is used by the Prisma CLI to run migrations. The function should return a `Promise` that resolves to a valid Prisma driver adapter.

Property

Type

Required

Default

`adapter`

`() => Promise<SqlMigrationAwareDriverAdapterFactory>`

No

none

Example using the Prisma ORM D1 driver adapter:

```
import path from "node:path";
import type { PrismaConfig } from "prisma";
import { PrismaD1 } from "@prisma/adapter-d1";

export default {
  experimental: {
    adapter: true,
  },
  engine: "js",
  schema: path.join("prisma", "schema.prisma"),
  async adapter() {
    return new PrismaD1({
      CLOUDFLARE_D1_TOKEN: process.env.CLOUDFLARE_D1_TOKEN,
      CLOUDFLARE_ACCOUNT_ID: process.env.CLOUDFLARE_ACCOUNT_ID,
      CLOUDFLARE_DATABASE_ID: process.env.CLOUDFLARE_DATABASE_ID,
    });
  },
} satisfies PrismaConfig;
```

### [`engine` (Removed)](#engine-removed)

For Prisma ORM v6.19 and earlier

Configure the schema engine your project should use.

Property

Type

Required

Default

`engine`

`classic` or `js`

No

`classic`

By default it is set to use the classic engine, which requires that `datasource` be set in your `prisma.config.ts`.

```
import "dotenv/config";
import path from "node:path";
import { defineConfig, env } from "prisma/config";
export default defineConfig({
  engine: "classic",
  datasource: {
    url: env("DATABASE_URL"),
  },
  schema: path.join("prisma", "schema.prisma"),
});
```

### [`studio` (Removed)](#studio-removed)

For Prisma ORM v6.19 and earlier

Configures how Prisma Studio connects to your database. See sub-options below for details.

Property

Type

Required

Default

`studio`

`object`

No

none

#### [`studio.adapter` (Removed)](#studioadapter-removed)

A function that returns a Prisma driver adapter instance. The function receives an `env` parameter containing environment variables and should return a `Promise` that resolves to a valid Prisma driver adapter.

Property

Type

Required

Default

`studio.adapter`

`(env: Env) => Promise<SqlMigrationAwareDriverAdapterFactory>`

No

none

Example using the Prisma ORM LibSQL driver adapter:

```
import type { PrismaConfig } from "prisma";

export default {
  experimental: {
    studio: true,
  },
  engine: "js",
  studio: {
    adapter: async (env: Env) => {
      const { PrismaLibSQL } = await import("@prisma/adapter-libsql");
      const { createClient } = await import("@libsql/client");

      const libsql = createClient({
        url: env.DOTENV_PRISMA_STUDIO_LIBSQL_DATABASE_URL,
      });
      return new PrismaLibSQL(libsql);
    },
  },
} satisfies PrismaConfig;
```

### [Setting up your project](#setting-up-your-project)

To get started with Prisma Config, create a `prisma.config.ts` file in your project root. You can use either of these approaches:

Using `defineConfig`:

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

Using TypeScript types:

```
import "dotenv/config";
import type { PrismaConfig } from "prisma";
import { env } from "prisma/config";

export default {
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
} satisfies PrismaConfig;
```

### [Using environment variables](#using-environment-variables)

Environment variables from `.env` files need to be loaded explicitly. The `prisma init` command generates a config that includes `import 'dotenv/config'` by default.

#### [Using dotenv (Recommended for Prisma ORM v7)](#using-dotenv-recommended-for-prisma-orm-v7)

1.  Install the `dotenv` package:

2.  Import `dotenv/config` at the top of your `prisma.config.ts` file:

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

#### [Using Node.js v20+ or tsx with --env-file flag](#using-nodejs-v20-or-tsx-with---env-file-flag)

If using Node.js v20+ or `tsx`, you can pass a `--env-file` flag to automatically load environment variables:

```
tsx --env-title=".env" src/index.ts
tsx watch --env-title=".env" --env-title=".local.env" src/index.ts
tsx --env-title=".env" ./prisma/seed.ts
```

#### [Using Bun](#using-bun)

For Bun, `.env` files are automatically loaded without additional configuration. The `import 'dotenv/config'` line that `prisma init` generates is not needed when using Bun and can be safely removed from your `prisma.config.ts` file.

#### [Type-safe environment variables](#type-safe-environment-variables)

Use the `env()` helper function to provide type-safe access to environment variables:

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

type Env = {
  DATABASE_URL: string;
};

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env<Env>("DATABASE_URL"),
  },
});
```

#### [Handling optional environment variables](#handling-optional-environment-variables)

The `env()` helper function from `prisma/config` **throws an error** if the specified environment variable is not defined. This is important to understand because:

*   Every Prisma CLI command loads the `prisma.config.ts` file
*   Only **some** commands actually need the `datasource.url` value (e.g., `prisma db *`, `prisma migrate *`, `prisma generate --sql`)
*   Commands like `prisma generate` don't need a database URL, but will still fail if `env()` throws an error when loading the config file

For example, if you run `prisma generate` without `DATABASE_URL` set, and your config uses `env('DATABASE_URL')`, you'll see:

```
Error: PrismaConfigEnvError: Missing required environment variable: DATABASE_URL
```

**Solution:** If your environment variable isn't guaranteed to exist (e.g., in CI/CD pipelines where you only run `prisma generate` for type-checking), don't use the `env()` helper. Instead, access the environment variable directly:

```
import "dotenv/config";
import { defineConfig } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: process.env.DATABASE_URL!, // Or use: process.env.DATABASE_URL ?? '' to provide a fallback value
  },
});
```

### [Using multi-file schemas](#using-multi-file-schemas)

If you want to split your Prisma schema into multiple files, you need to specify the path to your Prisma schema folder via the `schema` property:

```
import path from "node:path";
import type { PrismaConfig } from "prisma";

export default {
  schema: path.join("prisma", "schema"),
} satisfies PrismaConfig;
```

In that case, your `migrations` directory must be located next to the `.prisma` file that defines the `datasource` block.

For example, assuming `schema.prisma` defines the `datasource`, here's how how need to place the migrations folder:

```
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

*   Paths defined in the config file (e.g., `schema`, `migrations`) are always resolved **relative to the location of the config file**, not where you run the CLI command from.
*   The CLI must first **find the config file** itself, which depends on how Prisma is installed and the package manager used.

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

*   Prefer local Prisma installations in your project.
*   Or use `prisma/config` locally and pass `--config` to point to your config file.

### [Monorepos](#monorepos)

*   If Prisma is installed in the **workspace root**, `pnpm prisma` will detect the config file from subdirectories.
*   If Prisma is installed in a **subpackage** (e.g., `./packages/db`), run commands from that package directory or deeper.

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
