---
title: "Migrations with Drizzle Kit"
source: "https://orm.drizzle.team/docs/kit-overview"
canonical_url: "https://orm.drizzle.team/docs/kit-overview"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:09:12.152Z"
content_hash: "b425acccd7bcfc24866390621f2ac9b8806b2d7aa4a645ae2a424a87ae23e3cf"
menu_path: ["Migrations with Drizzle Kit"]
section_path: []
nav_prev: {"path": "drizzle/docs/relations/index.md", "title": "Drizzle soft relations"}
nav_next: {"path": "drizzle/docs/drizzle-kit-generate/index.md", "title": "drizzle-kit generate"}
---

## Migrations with Drizzle Kit

This guide assumes familiarity with:

*   Get started with Drizzle and `drizzle-kit` - [read here](drizzle/docs/get-started/index.md)
*   Drizzle schema fundamentals - [read here](drizzle/docs/sql-schema-declaration/index.md)
*   Database connection basics - [read here](drizzle/docs/connect-overview/index.md)
*   Drizzle migrations fundamentals - [read here](drizzle/docs/migrations/index.md)

**Drizzle Kit** is a CLI tool for managing SQL database migrations with Drizzle.

npm

yarn

pnpm

bun

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

npm

yarn

pnpm

bun

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

[`drizzle-kit generate`](drizzle/docs/drizzle-kit-generate/index.md)

lets you generate SQL migration files based on your Drizzle schema either upon declaration or on subsequent changes, [see here](drizzle/docs/drizzle-kit-generate/index.md).

[`drizzle-kit migrate`](drizzle/docs/drizzle-kit-migrate/index.md)

lets you apply generated SQL migration files to your database, [see here](drizzle/docs/drizzle-kit-migrate/index.md).

[`drizzle-kit pull`](drizzle/docs/drizzle-kit-pull/index.md)

lets you pull(introspect) database schema, convert it to Drizzle schema and save it to your codebase, [see here](drizzle/docs/drizzle-kit-pull/index.md)

[`drizzle-kit push`](drizzle/docs/drizzle-kit-push/index.md)

lets you push your Drizzle schema to database either upon declaration or on subsequent schema changes, [see here](drizzle/docs/drizzle-kit-push/index.md)

[`drizzle-kit studio`](drizzle/docs/drizzle-kit-studio/index.md)

will connect to your database and spin up proxy server for Drizzle Studio which you can use for convenient database browsing, [see here](drizzle/docs/drizzle-kit-studio/index.md)

[`drizzle-kit check`](drizzle/docs/drizzle-kit-check/index.md)

will walk through all generate migrations and check for any race conditions(collisions) of generated migrations, [see here](drizzle/docs/drizzle-kit-check/index.md)

[`drizzle-kit up`](drizzle/docs/drizzle-kit-up/index.md)

used to upgrade snapshots of previously generated migrations, [see here](drizzle/docs/drizzle-kit-up/index.md)

Drizzle Kit is configured through [drizzle.config.ts](drizzle/docs/drizzle-config-file/index.md) configuration file or via CLI params.  
It’s required to at least provide SQL `dialect` and `schema` path for Drizzle Kit to know how to generate migrations.

```
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

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
});
```

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

  breakpoints: true,
  strict: true,
  verbose: true,
});
```

You can provide Drizzle Kit config path via CLI param, it’s very useful when you have multiple database stages or multiple databases or different databases on the same project:

npm

yarn

pnpm

bun

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
