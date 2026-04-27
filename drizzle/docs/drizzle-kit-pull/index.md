---
title: "drizzle-kit pull"
source: "https://orm.drizzle.team/docs/drizzle-kit-pull"
canonical_url: "https://orm.drizzle.team/docs/drizzle-kit-pull"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:36:26.683Z"
content_hash: "3cad93c94d98bbed3f039cefe095162c18ed1d96174828fde8eef01518617b3e"
menu_path: ["drizzle-kit pull"]
section_path: []
content_language: "en"
---
`drizzle-kit pull` lets you literally pull(introspect) your existing database schema and generate `schema.ts` drizzle schema file, it is designed to cover [database first](https://orm.drizzle.team/docs/migrations) approach of Drizzle migrations.

How it works under the hood?

When you run Drizzle Kit `pull` command it will:

1.  Pull database schema(DDL) from your existing database
2.  Generate `schema.ts` drizzle schema file and save it to `out` folder

```plaintext
                                  ┌────────────────────────┐      ┌─────────────────────────┐ 
                                  │                        │ <---  CREATE TABLE "users" (
┌──────────────────────────┐      │                        │        "id" SERIAL PRIMARY KEY,
│ ~ drizzle-kit pull       │      │                        │        "name" TEXT,
└─┬────────────────────────┘      │        DATABASE        │        "email" TEXT UNIQUE
  │                               │                        │       );
  └ Pull datatabase schema -----> │                        │
  ┌ Generate Drizzle       <----- │                        │
  │ schema TypeScript file        └────────────────────────┘
  │
  v
```

```typescript
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(), 
};
```

It is a great approach if you need to manage database schema outside of your TypeScript project or you’re using database, which is managed by somebody else.

  

* * *

`drizzle-kit pull` requires you to specify `dialect` and either database connection `url` or `user:password@host:port/db` params, you can provide them either via [drizzle.config.ts](https://orm.drizzle.team/docs/drizzle-config-file) config file or via CLI options:

With config file

With CLI options

```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname",
  },
});
```

```shell
npx drizzle-kit pull
```

```shell
npx drizzle-kit pull --dialect=postgresql --url=postgresql://user:password@host:port/dbname
```

### Multiple configuration files in one project[](#multiple-configuration-files-in-one-project)

You can have multiple config files in the project, it’s very useful when you have multiple database stages or multiple databases or different databases on the same project:

```
npx drizzle-kit pull --config=drizzle-dev.config.ts
npx drizzle-kit pull --config=drizzle-prod.config.ts
```

```
yarn drizzle-kit pull --config=drizzle-dev.config.ts
yarn drizzle-kit pull --config=drizzle-prod.config.ts
```

```
pnpm drizzle-kit pull --config=drizzle-dev.config.ts
pnpm drizzle-kit pull --config=drizzle-prod.config.ts
```

```
bunx drizzle-kit pull --config=drizzle-dev.config.ts
bunx drizzle-kit pull --config=drizzle-prod.config.ts
```

```plaintext
📦 <project root>
 ├ 📂 drizzle
 ├ 📂 src
 ├ 📜 .env
 ├ 📜 drizzle-dev.config.ts
 ├ 📜 drizzle-prod.config.ts
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

### Specifying database driver[](#specifying-database-driver)

IMPORTANT

**Expo SQLite** and **OP SQLite** are on-device(per-user) databases, there’s no way to `pull` database schema from there.  
For embedded databases Drizzle provides **embedded migrations** - check out our [get started](https://orm.drizzle.team/docs/get-started/expo-new) guide.

Drizzle Kit does not come with a pre-bundled database driver, it will automatically pick available database driver from your current project based on the `dialect` - [see discussion](https://github.com/drizzle-team/drizzle-orm/discussions/2203).

Mostly all drivers of the same dialect share the same set of connection params, as for exceptions like `aws-data-api`, `pglight` and `d1-http` - you will have to explicitely specify `driver` param.

AWS Data API

PGLite

Cloudflare D1 HTTP

```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  driver: "aws-data-api",
  dbCredentials: {
    database: "database",
    resourceArn: "resourceArn",
    secretArn: "secretArn",
  },
};
```

```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  driver: "pglite",
  dbCredentials: {
    // inmemory
    url: ":memory:"
    
    // or database folder
    url: "./database/"
  },
};
```

```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "sqlite",
  driver: "d1-http",
  dbCredentials: {
    accountId: "accountId",
    databaseId: "databaseId",
    token: "token",
  },
};
```

### Initial pull[](#initial-pull)

WARNING

This feature is available on `1.0.0-beta.2` and higher.

```
npm i drizzle-orm@beta
npm i drizzle-kit@beta -D
```

```
yarn add drizzle-orm@beta
yarn add drizzle-kit@beta -D
```

```
pnpm add drizzle-orm@beta
pnpm add drizzle-kit@beta -D
```

```
bun add drizzle-orm@beta
bun add drizzle-kit@beta -D
```

You can use the `--init` flag to mark the pulled schema as an applied migration in your database, so that all subsequent migrations are diffed against the initial one

```shell
npx drizzle-kit push --init
```

### Including tables, schemas and extensions[](#including-tables-schemas-and-extensions)

`drizzle-kit push` will by default manage all tables in `public` schema. You can configure list of tables, schemas and extensions via `tablesFilters`, `schemaFilter` and `extensionFilters` options.

|  |  |
| --- | --- |
| `tablesFilter` | `glob` based table names filter, e.g. `["users", "user_info"]` or `"user*"`. Default is `"*"` |
| `schemaFilter` | `glob` based schema names filter, e.g. `["public", "drizzle"]` or `"drizzle*"`. Default is `"*"` |
| `extensionsFilters` | List of installed database extensions, e.g. `["postgis"]`. Default is `[]` |

Let’s configure drizzle-kit to only operate with **all tables** in **public** schema and let drizzle-kit know that there’s a **postgis** extension installed, which creates it’s own tables in public schema, so drizzle can ignore them.

```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname",
  },
  extensionsFilters: ["postgis"],
  schemaFilter: ["public"],
  tablesFilter: ["*"],
});
```

```shell
npx drizzle-kit push
```

### Extended list of configurations[](#extended-list-of-configurations)

We recommend configuring `drizzle-kit` through [drizzle.config.ts](https://orm.drizzle.team/docs/drizzle-config-file) file, yet you can provide all configuration options through CLI if necessary, e.g. in CI/CD pipelines, etc.

|  |  |  |
| --- | --- | --- |
| `dialect` | `required` | Database dialect, one of `postgresql` `mysql` `sqlite` `turso` `singlestore` `mssql` `cockroachdb` |
| `driver` |  | Drivers exceptions `aws-data-api` `d1-http` `pglight` |
| `out` |  | Migrations output folder path, default is `./drizzle` |
| `url` |  | Database connection string |
| `user` |  | Database user |
| `password` |  | Database password |
| `host` |  | Host |
| `port` |  | Port |
| `database` |  | Database name |
| `config` |  | Configuration file path, default is `drizzle.config.ts` |
| `introspect-casing` |  | Strategy for JS keys creation in columns, tables, etc. `preserve` `camel` |
| `tablesFilter` |  | Table name filter |
| `schemaFilter` |  | Schema name filter. Default: `["public"]` |
| `extensionsFilters` |  | Database extensions internal database filters |

```
npx drizzle-kit pull --dialect=postgresql --url=postgresql://user:password@host:port/dbname
npx drizzle-kit pull --dialect=postgresql --driver=pglite url=database/
npx drizzle-kit pull --dialect=postgresql --tablesFilter=‘user*’ --extensionsFilters=postgis url=postgresql://user:password@host:port/dbname
```

```
yarn drizzle-kit pull --dialect=postgresql --url=postgresql://user:password@host:port/dbname
yarn drizzle-kit pull --dialect=postgresql --driver=pglite url=database/
yarn drizzle-kit pull --dialect=postgresql --tablesFilter=‘user*’ --extensionsFilters=postgis url=postgresql://user:password@host:port/dbname
```

```
pnpm drizzle-kit pull --dialect=postgresql --url=postgresql://user:password@host:port/dbname
pnpm drizzle-kit pull --dialect=postgresql --driver=pglite url=database/
pnpm drizzle-kit pull --dialect=postgresql --tablesFilter=‘user*’ --extensionsFilters=postgis url=postgresql://user:password@host:port/dbname
```

```
bunx drizzle-kit pull --dialect=postgresql --url=postgresql://user:password@host:port/dbname
bunx drizzle-kit pull --dialect=postgresql --driver=pglite url=database/
bunx drizzle-kit pull --dialect=postgresql --tablesFilter=‘user*’ --extensionsFilters=postgis url=postgresql://user:password@host:port/dbname
```

![](https://orm.drizzle.team/_astro/introspect_mysql.Hk8acObY_Z20dDww.webp)
