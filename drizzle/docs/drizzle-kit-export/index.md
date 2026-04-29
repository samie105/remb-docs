---
title: "drizzle-kit export"
source: "https://orm.drizzle.team/docs/drizzle-kit-export"
canonical_url: "https://orm.drizzle.team/docs/drizzle-kit-export"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:35:20.456Z"
content_hash: "5befb26bf38e333a119f11d579ab2acd495e74385d095c68fa73d85ff80d6175"
menu_path: ["drizzle-kit export"]
section_path: []
content_language: "en"
nav_prev: {"path": "../drizzle-kit-pull/index.md", "title": "drizzle-kit pull"}
nav_next: {"path": "../drizzle-kit-check/index.md", "title": "drizzle-kit check"}
---

`drizzle-kit export` lets you export SQL representation of Drizzle schema and print in console SQL DDL representation on it.

How it works under the hood?

Drizzle Kit `export` command triggers a sequence of events:

1.  It will read through your Drizzle schema file(s) and compose a json snapshot of your schema
2.  Based on json differences it will generate SQL DDL statements
3.  Output SQL DDL statements to console

It’s designed to cover [codebase first](../migrations/index.md) approach of managing Drizzle migrations. You can export the SQL representation of the Drizzle schema, allowing external tools like Atlas to handle all the migrations for you

`drizzle-kit export` command requires you to provide both `dialect` and `schema` path options, you can set them either via [drizzle.config.ts](../drizzle-config-file/index.md) config file or via CLI options

With config file

As CLI options

```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
});
```

```shell
npx drizzle-kit export
```

```shell
npx drizzle-kit export --dialect=postgresql --schema=./src/schema.ts
```

### Schema files path[](#schema-files-path)

You can have a single `schema.ts` file or as many schema files as you want spread out across the project. Drizzle Kit requires you to specify path(s) to them as a [glob](https://www.digitalocean.com/community/tools/glob?comments=true&glob=/**/*.js&matches=false&tests=//%20This%20will%20match%20as%20it%20ends%20with%20%27.js%27&tests=/hello/world.js&tests=//%20This%20won%27t%20match!&tests=/test/some/globs) via `schema` configuration option.

Example 1

Example 2

Example 3

Example 4

```plaintext
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

```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/schema.ts",
});
```

### Multiple configuration files in one project[](#multiple-configuration-files-in-one-project)

You can have multiple config files in the project, it’s very useful when you have multiple database stages or multiple databases or different databases on the same project:

```
npx drizzle-kit export --config=drizzle-dev.config.ts
npx drizzle-kit export --config=drizzle-prod.config.ts
```

```
yarn drizzle-kit export --config=drizzle-dev.config.ts
yarn drizzle-kit export --config=drizzle-prod.config.ts
```

```
pnpm drizzle-kit export --config=drizzle-dev.config.ts
pnpm drizzle-kit export --config=drizzle-prod.config.ts
```

```
bunx drizzle-kit export --config=drizzle-dev.config.ts
bunx drizzle-kit export --config=drizzle-prod.config.ts
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

### Extended list of available configurations[](#extended-list-of-available-configurations)

`drizzle-kit export` has a list of cli-only options

|  |  |
| --- | --- |
| `--sql` | generating SQL representation of Drizzle Schema |

By default, Drizzle Kit outputs SQL files, but in the future, we want to support different formats

```
npx drizzle-kit push --name=init
npx drizzle-kit push --name=seed_users --custom
```

```
yarn drizzle-kit push --name=init
yarn drizzle-kit push --name=seed_users --custom
```

```
pnpm drizzle-kit push --name=init
pnpm drizzle-kit push --name=seed_users --custom
```

```
bunx drizzle-kit push --name=init
bunx drizzle-kit push --name=seed_users --custom
```

  

* * *

We recommend configuring `drizzle-kit` through [drizzle.config.ts](../drizzle-config-file/index.md) file, yet you can provide all configuration options through CLI if necessary, e.g. in CI/CD pipelines, etc.

|  |  |  |
| --- | --- | --- |
| `dialect` | `required` | Database dialect, one of `postgresql` `mysql` `sqlite` `turso` `singlestore` `mssql` `cockroachdb` |
| `schema` | `required` | Path to typescript schema file(s) or folder(s) with multiple schema files |
| `config` |  | Configuration file path, default is `drizzle.config.ts` |

### Example[](#example)

Example of how to export drizzle schema to console with Drizzle schema located in `./src/schema.ts`

We will also place drizzle config file in the `configs` folder.

Let’s create config file:

```plaintext
📦 <project root>
 ├ 📂 configs
 │ └ 📜 drizzle.config.ts
 ├ 📂 src
 │ └ 📜 schema.ts
 └ …
```

```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
});
```

```ts
import { pgTable, serial, text } from 'drizzle-orm/pg-core'

export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	email: text('email').notNull(),
	name: text('name')
});
```

Now let’s run

```shell
npx drizzle-kit export --config=./configs/drizzle.config.ts
```

And it will successfully output SQL representation of drizzle schema

```bash
CREATE TABLE "users" (
        "id" serial PRIMARY KEY NOT NULL,
        "email" text NOT NULL,
        "name" text
);
```
