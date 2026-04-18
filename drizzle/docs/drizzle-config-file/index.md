---
title: "Drizzle Kit configuration file"
source: "https://orm.drizzle.team/docs/drizzle-config-file"
canonical_url: "https://orm.drizzle.team/docs/drizzle-config-file"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:45.474Z"
content_hash: "95e2edb4fffbe2eb04761309555b7d021409ca192728baa0651301fbd56b79ac"
menu_path: ["Drizzle Kit configuration file"]
section_path: []
nav_prev: {"path": "drizzle/docs/kit-web-mobile/index.md", "title": "Drizzle migrations in web and mobile environments"}
nav_next: {"path": "drizzle/docs/seed-overview/index.md", "title": "Drizzle Seed"}
---

## Drizzle Kit configuration file

Drizzle Kit lets you declare configuration options in `TypeScript` or `JavaScript` configuration files.

```
📦 <project root>
 ├ ...
 ├ 📂 drizzle
 ├ 📂 src
 ├ 📜 drizzle.config.ts
 └ 📜 package.json
```

drizzle.config.ts

drizzle.config.js

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  out: "./drizzle",
});
```

Example of an extended config file

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  out: "./drizzle",
  dialect: "postgresql",
  schema: "./src/schema.ts",

  driver: "pglite",
  dbCredentials: {
    url: "./database/",
  },

  extensionsFilters: ["postgis"],
  schemaFilter: "public",
  tablesFilter: "*",

  introspect: {
    casing: "camel",
  },

  migrations: {
    prefix: "timestamp",
    table: "__drizzle_migrations__",
    schema: "public",
  },

  entities: {
    roles: {
      provider: '',
      exclude: [],
      include: []
    }
  },

  breakpoints: true,
  strict: true,
  verbose: true,
});
```

Expand

### Multiple configuration files[](#multiple-configuration-files)

You can have multiple config files in the project, it’s very useful when you have multiple database stages or multiple databases or different databases on the same project:

npm

yarn

pnpm

bun

```
npx drizzle-kit generate --config=drizzle-dev.config.ts
npx drizzle-kit generate --config=drizzle-prod.config.ts
```

```
yarn drizzle-kit generate --config=drizzle-dev.config.ts
yarn drizzle-kit generate --config=drizzle-prod.config.ts
```

```
pnpm drizzle-kit generate --config=drizzle-dev.config.ts
pnpm drizzle-kit generate --config=drizzle-prod.config.ts
```

```
bunx drizzle-kit generate --config=drizzle-dev.config.ts
bunx drizzle-kit generate --config=drizzle-prod.config.ts
```

```
📦 <project root>
 ├ 📂 drizzle
 ├ 📂 src
 ├ 📜 .env
 ├ 📜 drizzle-dev.config.ts
 ├ 📜 drizzle-prod.config.ts
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

### Migrations folder[](#migrations-folder)

`out` param lets you define folder for your migrations, it’s optional and `drizzle` by default.  
It’s very useful since you can have many separate schemas for different databases in the same project and have different migration folders for them.

Migration folder contains folders with `.sql` migration files which is used by `drizzle-kit`

```
📦 <project root>
 ├ ...
 ├ 📂 drizzle
 │ ├ 📂 20242409125510_premium_mister_fear
 │ ├ 📜 user.ts 
 │ ├ 📜 post.ts 
 │ └ 📜 comment.ts 
 ├ 📂 src
 ├ 📜 drizzle.config.ts
 └ 📜 package.json
```

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql", // "mysql" | "sqlite" | "postgresql" | "turso" | "singlestore" | "mssql"
  schema: "./src/schema/*",
  out: "./drizzle",
});
```

### `dialect`[](#dialect)

Dialect of the database you’re using

type

`postgresql` `mysql` `sqlite` `turso` `singlestore` `mssql` `cockroachdb`

default

—

commands

`generate` `migrate` `push` `pull` `check` `up`

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "mysql", 
});
```

### `schema`[](#schema)

[`glob`](https://www.digitalocean.com/community/tools/glob?comments=true&glob=/**/*.js&matches=false&tests=//%20This%20will%20match%20as%20it%20ends%20with%20%27.js%27&tests=/hello/world.js&tests=//%20This%20won%27t%20match!&tests=/test/some/globs) based path to drizzle schema file(s) or folder(s) contaning schema files.

type

`string` `string[]`

default

—

commands

`generate` `push`

Example 1

Example 2

Example 3

Example 4

```
📦 <project root>
 ├ ...
 ├ 📂 drizzle
 ├ 📂 src
 │ ├ ...
 │ ├ 📜 index.ts
 │ └ 📜 schema.ts 
 ├ 📜 drizzle.config.ts
 └ 📜 package.json
```

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/schema.ts",
});
```

### `out`[](#out)

Defines output folder of your SQL migration files, json snapshots of your schema and `schema.ts` from `drizzle-kit pull` command.

type

`string` `string[]`

default

`drizzle`

commands

`generate` `migrate` `push` `pull` `check` `up`

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  out: "./drizzle", 
});
```

### `driver`[](#driver)

Drizzle Kit automatically picks available database driver from your current project based on the provided `dialect`, yet some vendor specific databases require a different subset of connection params.

`driver` option let’s you explicitely pick those exceptions drivers.

type

`aws-data-api` `d1-http` `pglight`

default

—

commands

`migrate` `push` `pull`

AWS Data API

PGLite

Cloudflare D1 HTTP

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  driver: "aws-data-api",
  dbCredentials: {
    database: "database",
    resourceArn: "resourceArn",
    secretArn: "secretArn",
  },
});
```

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  driver: "pglite",
  dbCredentials: {
    // inmemory
    url: ":memory:"
    
    // or database folder
    url: "./database/"
  },
});
```

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "sqlite",
  schema: "./src/schema.ts",
  driver: "d1-http",
  dbCredentials: {
    accountId: "accountId",
    databaseId: "databaseId",
    token: "token",
  },
});
```

### `dbCredentials`[](#dbcredentials)

Database connection credentials in a form of `url`, `user:password@host:port/db` params or exceptions drivers(`aws-data-api` `d1-http` `pglight` ) specific connection options.

type

union of drivers connection options

default

—

commands

`migrate` `push` `pull`

PostgreSQL

MySQL

SQLite

Turso

Cloudflare D1

AWS Data API

PGLite

```
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: {
    url: "postgres://user:password@host:port/db",
  }
});
```

```
import { defineConfig } from 'drizzle-kit'

// via connection params
export default defineConfig({
  dialect: "postgresql",
  dbCredentials: {
    host: "host",
    port: 5432,
    user: "user",
    password: "password",
    database: "dbname",
    ssl: true, // can be boolean | "require" | "allow" | "prefer" | "verify-full" | options from node:tls
  }
});
```

```
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "sqlite",
  dbCredentials: {
    url: ":memory:", // inmemory database
    // or
    url: "sqlite.db", 
    // or
    url: "file:sqlite.db" // file: prefix is required by libsql
  }
});
```

```
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "turso",
  dbCredentials: {
    url: "libsql://acme.turso.io" // remote Turso database url
    authToken: "...",

    // or if you need local db

    url: ":memory:", // inmemory database
    // or
    url: "file:sqlite.db", // file: prefix is required by libsql
  }
});
```

```
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "sqlite",
  driver: "d1-http",
  dbCredentials: {
    accountId: "",
    databaseId: "",
    token: "",
  }
});
```

```
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "postgresql",
  driver: "aws-data-api",
  dbCredentials: {
    database: "database",
    resourceArn: "resourceArn",
    secretArn: "secretArn",
  },
});
```

```
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "postgresql",
  driver: "pglite",
  dbCredentials: {
    url: "./database/", // database folder path
  }
});
```

### `migrations`[](#migrations)

When running `drizzle-kit migrate` - drizzle will records about successfully applied migrations in your database in log table named `__drizzle_migrations` in `public` schema(PostgreSQL only).

`migrations` config options lets you change both migrations log `table` name and `schema`.

type

`{ table: string, schema: string }`

default

`{ table: "__drizzle_migrations", schema: "drizzle" }`

commands

`migrate`

```
export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  migrations: {
    table: 'my-migrations-table', // `__drizzle_migrations` by default
    schema: 'public', // used in PostgreSQL only, `drizzle` by default
  },
});
```

### `introspect`[](#introspect)

Configuration for `drizzle-kit pull` command.

`casing` is responsible for in-code column keys casing

type

`{ casing: "preserve" | "camel" }`

default

`{ casing: "camel" }`

commands

`pull`

camel

preserve

```
import * as p from "drizzle-orm/pg-core"

export const users = p.pgTable("users", {
  id: p.serial(),
  firstName: p.text("first-name"),
  lastName: p.text("LastName"),
  email: p.text(),
  phoneNumber: p.text("phone_number"),
});
```

```
SELECT a.attname AS column_name, format_type(a.atttypid, a.atttypmod) as data_type FROM pg_catalog.pg_attribute a;
```

```
 column_name   | data_type        
---------------+------------------------
 id            | serial
 first-name    | text
 LastName      | text
 email         | text
 phone_number  | text
```

### `tablesFilter`[](#tablesfilter)

If you want to run multiple projects with one database - check out [our guide](drizzle/docs/goodies/index.md#multi-project-schema).

`drizzle-kit push` and `drizzle-kit pull` will by default manage all tables in `public` schema. You can configure list of tables, schemas and extensions via `tablesFilters`, `schemaFilter` and `extensionFilters` options.

`tablesFilter` option lets you specify [`glob`](https://www.digitalocean.com/community/tools/glob?comments=true&glob=/**/*.js&matches=false&tests=//%20This%20will%20match%20as%20it%20ends%20with%20%27.js%27&tests=/hello/world.js&tests=//%20This%20won%27t%20match!&tests=/test/some/globs) based table names filter, e.g. `["users", "user_info"]` or `"user*"`

type

`string` `string[]`

default

—

commands

`generate` `push` `pull`

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  tablesFilter: ["users", "posts", "project1_*"],
});
```

### `schemaFilter`[](#schemafilter)

Was changed starting from `1.0.0-beta.1` version!

IMPORTANT

How it works in 0.x versions

`drizzle-kit push` and `drizzle-kit pull` will by default manage all tables in `public` schema. You can configure list of tables, schemas and extensions via `tablesFilters`, `schemaFilter` and `extensionFilters` options.

`schemaFilter` option lets you specify list of schemas for Drizzle Kit to manage

type

`string[]`

default

`["public"]`

commands

`push` `pull`

If you want to run multiple projects with one database - check out [our guide](drizzle/docs/goodies/index.md#multi-project-schema).

`drizzle-kit push` and `drizzle-kit pull` will by default manage all schemas.

`schemaFilter` option lets you specify [`glob`](https://www.digitalocean.com/community/tools/glob?comments=true&glob=/**/*.js&matches=false&tests=//%20This%20will%20match%20as%20it%20ends%20with%20%27.js%27&tests=/hello/world.js&tests=//%20This%20won%27t%20match!&tests=/test/some/globs) based schema names filter, e.g. `["public", "auth"]` or `"tenant_*"`

type

`string[]`

commands

`push` `pull`

```
export default defineConfig({
  dialect: "postgresql",
  schemaFilter: ["public", "schema1", "schema2"],
});
```

### `extensionsFilters`[](#extensionsfilters)

Some extensions like [`postgis`](https://postgis.net/), when installed on the database, create its own tables in public schema. Those tables have to be ignored by `drizzle-kit push` or `drizzle-kit pull`.

`extensionsFilters` option lets you declare list of installed extensions for drizzle kit to ignore their tables in the schema.

type

`["postgis"]`

default

`[]`

commands

`push` `pull`

```
export default defineConfig({
  dialect: "postgresql",
  extensionsFilters: ["postgis"],
});
```

### `entities`[](#entities)

This configuration is created to set up management settings for specific `entities` in the database.

For now, it only includes `roles`, but eventually all database entities will migrate here, such as `tables`, `schemas`, `extensions`, `functions`, `triggers`, etc

#### `roles`[](#roles)

If you are using Drizzle Kit to manage your schema and especially the defined roles, there may be situations where you have some roles that are not defined in the Drizzle schema. In such cases, you may want Drizzle Kit to skip those `roles` without the need to write each role in your Drizzle schema and mark it with `.existing()`.

The `roles` option lets you:

*   Enable or disable role management with Drizzle Kit.
*   Exclude specific roles from management by Drizzle Kit.
*   Include specific roles for management by Drizzle Kit.
*   Enable modes for providers like `Neon` and `Supabase`, which do not manage their specific roles.
*   Combine all the options above

type

`boolean | { provider: "neon" | "supabase", include: string[], exclude: string[]}`

default

`false`

commands

`push` `pull` `generate`

By default, `drizzle-kit` won’t manage roles for you, so you will need to enable that. in `drizzle.config.ts`

```
export default defineConfig({
  dialect: "postgresql",
  entities: {
    roles: true
  }
});
```

**You have a role `admin` and want to exclude it from the list of manageable roles**

```
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      exclude: ['admin']
    }
  }
});
```

**You have a role `admin` and want to include to the list of manageable roles**

```
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      include: ['admin']
    }
  }
});
```

**If you are using `Neon` and want to exclude roles defined by `Neon`, you can use the provider option**

```
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      provider: 'neon'
    }
  }
});
```

**If you are using `Supabase` and want to exclude roles defined by `Supabase`, you can use the provider option**

```
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      provider: 'supabase'
    }
  }
});
```

important

You may encounter situations where Drizzle is slightly outdated compared to new roles specified by database providers, so you may need to use both the `provider` option and `exclude` additional roles. You can easily do this with Drizzle:

```
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      provider: 'supabase',
      exclude: ['new_supabase_role']
    }
  }
});
```

### `strict`[](#strict)

Prompts confirmation to run printed SQL statements when running `drizzle-kit push` command.

type

`boolean`

default

`false`

commands

`push`

```
export default defineConfig({
  dialect: "postgresql",
  strict: false,
});
```

### `verbose`[](#verbose)

Print all SQL statements during `drizzle-kit push` command.

type

`boolean`

default

`true`

commands

`generate` `pull`

```
export default defineConfig({
  dialect: "postgresql",
  verbose: false,
});
```

### `breakpoints`[](#breakpoints)

Drizzle Kit will automatically embed `--> statement-breakpoint` into generated SQL migration files, that’s necessary for databases that do not support multiple DDL alternation statements in one transaction(MySQL and SQLite).

`breakpoints` option flag lets you switch it on and off

type

`boolean`

default

`true`

commands

`generate` `pull`

```
export default defineConfig({
  dialect: "postgresql",
  breakpoints: false,
});
```


