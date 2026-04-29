---
title: "drizzle-kit check"
source: "https://orm.drizzle.team/docs/drizzle-kit-check"
canonical_url: "https://orm.drizzle.team/docs/drizzle-kit-check"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:35:18.397Z"
content_hash: "c90b7c9d33b2986b6f17b397391d4dcf0df5c4157e673064004e2f3ecfe8a9fc"
menu_path: ["drizzle-kit check"]
section_path: []
content_language: "en"
nav_prev: {"path": "../drizzle-kit-export/index.md", "title": "drizzle-kit export"}
nav_next: {"path": "../drizzle-kit-up/index.md", "title": "drizzle-kit up"}
---

`drizzle-kit check` command lets you check consistency of your generated SQL migrations history.

That’s extremely useful when you have multiple developers working on the project and altering database schema on different branches - read more about [migrations for teams](../kit-migrations-for-teams/index.md).

  

* * *

`drizzle-kit check` command requires you to specify both `dialect` and database connection credentials, you can provide them either via [drizzle.config.ts](../drizzle-config-file/index.md) config file or via CLI options

With config file

As CLI options

```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
});
```

```shell
npx drizzle-kit check
```

```shell
npx drizzle-kit check --dialect=postgresql
```

### Multiple configuration files in one project[](#multiple-configuration-files-in-one-project)

You can have multiple config files in the project, it’s very useful when you have multiple database stages or multiple databases on the same project:

```
npx drizzle-kit check --config=drizzle-dev.config.ts
npx drizzle-kit check --config=drizzle-prod.config.ts
```

```
yarn drizzle-kit check --config=drizzle-dev.config.ts
yarn drizzle-kit check --config=drizzle-prod.config.ts
```

```
pnpm drizzle-kit check --config=drizzle-dev.config.ts
pnpm drizzle-kit check --config=drizzle-prod.config.ts
```

```
bunx drizzle-kit check --config=drizzle-dev.config.ts
bunx drizzle-kit check --config=drizzle-prod.config.ts
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

### Extended list of configurations[](#extended-list-of-configurations)

We recommend configuring `drizzle-kit` through [drizzle.config.ts](../drizzle-config-file/index.md) file, yet you can provide all configuration options through CLI if necessary, e.g. in CI/CD pipelines, etc.

|  |  |  |
| --- | --- | --- |
| `dialect` | `required` | Database dialect you are using. Can be `postgresql`,`mysql` or `sqlite` |
| `out` |  | Migrations folder, default=`./drizzle` |
| `config` |  | Configuration file path, default=`drizzle.config.ts` |

  

```
npx drizzle-kit check --dialect=postgresql
npx drizzle-kit check --dialect=postgresql --out=./migrations-folder
```

```
yarn drizzle-kit check --dialect=postgresql
yarn drizzle-kit check --dialect=postgresql --out=./migrations-folder
```

```
pnpm drizzle-kit check --dialect=postgresql
pnpm drizzle-kit check --dialect=postgresql --out=./migrations-folder
```

```
bunx drizzle-kit check --dialect=postgresql
bunx drizzle-kit check --dialect=postgresql --out=./migrations-folder
```
