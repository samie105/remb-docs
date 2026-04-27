---
title: "Migrations with Drizzle Kit"
source: "https://orm.drizzle.team/docs/kit-overview"
canonical_url: "https://orm.drizzle.team/docs/kit-overview"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:06:31.374Z"
content_hash: "f1ce178180d75ce084bc7f9af4a3cbce9f69b93bec905e1ede1780b52707f887"
menu_path: ["Migrations with Drizzle Kit"]
section_path: []
content_language: "en"
---
## Migrations with Drizzle Kit

This guide assumes familiarity with:

-   Get started with Drizzle and `drizzle-kit` - [read here](https://orm.drizzle.team/docs/get-started)
-   Drizzle schema fundamentals - [read here](https://orm.drizzle.team/docs/sql-schema-declaration)
-   Database connection basics - [read here](https://orm.drizzle.team/docs/connect-overview)
-   Drizzle migrations fundamentals - [read here](https://orm.drizzle.team/docs/migrations)

**Drizzle Kit** is a CLI tool for managing SQL database migrations with Drizzle.

```
npm i -D drizzle-kit
```

```
yarn add -D drizzle-kit
```

```
pnpm add -D drizzle-kit
```

```
bun add -D drizzle-kit
```

IMPORTANT

Based on your schema, Drizzle Kit let’s you generate and run SQL migration files, push schema directly to the database, pull schema from database, spin up drizzle studio and has a couple of utility commands.

```
npx drizzle-kit generate
npx drizzle-kit migrate
npx drizzle-kit push
npx drizzle-kit pull
npx drizzle-kit check
npx drizzle-kit up
npx drizzle-kit studio
```

```
yarn drizzle-kit generate
yarn drizzle-kit migrate
yarn drizzle-kit push
yarn drizzle-kit pull
yarn drizzle-kit check
yarn drizzle-kit up
yarn drizzle-kit studio
```

```
pnpm drizzle-kit generate
pnpm drizzle-kit migrate
pnpm drizzle-kit push
pnpm drizzle-kit pull
pnpm drizzle-kit check
pnpm drizzle-kit up
pnpm drizzle-kit studio
```

```
bunx drizzle-kit generate
bunx drizzle-kit migrate
bunx drizzle-kit push
bunx drizzle-kit pull
bunx drizzle-kit check
bunx drizzle-kit up
bunx drizzle-kit studio
```

|  |  |
| --- | --- |
| [`drizzle-kit generate`](https://orm.drizzle.team/docs/drizzle-kit-generate) | lets you generate SQL migration files based on your Drizzle schema either upon declaration or on subsequent changes, [see here](https://orm.drizzle.team/docs/drizzle-kit-generate). |
| [`drizzle-kit migrate`](https://orm.drizzle.team/docs/drizzle-kit-migrate) | lets you apply generated SQL migration files to your database, [see here](https://orm.drizzle.team/docs/drizzle-kit-migrate). |
| [`drizzle-kit pull`](https://orm.drizzle.team/docs/drizzle-kit-pull) | lets you pull(introspect) database schema, convert it to Drizzle schema and save it to your codebase, [see here](https://orm.drizzle.team/docs/drizzle-kit-pull) |
| [`drizzle-kit push`](https://orm.drizzle.team/docs/drizzle-kit-push) | lets you push your Drizzle schema to database either upon declaration or on subsequent schema changes, [see here](https://orm.drizzle.team/docs/drizzle-kit-push) |
| [`drizzle-kit studio`](https://orm.drizzle.team/docs/drizzle-kit-studio) | will connect to your database and spin up proxy server for Drizzle Studio which you can use for convenient database browsing, [see here](https://orm.drizzle.team/docs/drizzle-kit-studio) |
| [`drizzle-kit check`](https://orm.drizzle.team/docs/drizzle-kit-check) | will walk through all generate migrations and check for any race conditions(collisions) of generated migrations, [see here](https://orm.drizzle.team/docs/drizzle-kit-check) |
| [`drizzle-kit up`](https://orm.drizzle.team/docs/drizzle-kit-up) | used to upgrade snapshots of previously generated migrations, [see here](https://orm.drizzle.team/docs/drizzle-kit-up) |

Drizzle Kit is configured through [drizzle.config.ts](https://orm.drizzle.team/docs/drizzle-config-file) configuration file or via CLI params.  
It’s required to at least provide SQL `dialect` and `schema` path for Drizzle Kit to know how to generate migrations.

```plaintext
📦 <project root>
 ├ 📂 drizzle
 ├ 📂 src
 ├ 📜 .env
 ├ 📜 drizzle.config.ts  <--- Drizzle config file
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

simple config

extended config

```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
});
```

```ts
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

  breakpoints: true,
  strict: true,
  verbose: true,
});
```

You can provide Drizzle Kit config path via CLI param, it’s very useful when you have multiple database stages or multiple databases or different databases on the same project:

```
npx drizzle-kit push --config=drizzle-dev.drizzle.config
npx drizzle-kit push --config=drizzle-prod.drizzle.config
```

```
yarn drizzle-kit push --config=drizzle-dev.drizzle.config
yarn drizzle-kit push --config=drizzle-prod.drizzle.config
```

```
pnpm drizzle-kit push --config=drizzle-dev.drizzle.config
pnpm drizzle-kit push --config=drizzle-prod.drizzle.config
```

```
bunx drizzle-kit push --config=drizzle-dev.drizzle.config
bunx drizzle-kit push --config=drizzle-prod.drizzle.config
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
