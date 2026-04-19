---
title: "drizzle-kit check"
source: "https://orm.drizzle.team/docs/drizzle-kit-check"
canonical_url: "https://orm.drizzle.team/docs/drizzle-kit-check"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:40.592Z"
content_hash: "f57d1ee4cca4c0959757ec83fbd2fdaf67105251cc510e1be60ebbb1af4f2a12"
menu_path: ["drizzle-kit check"]
section_path: []
nav_prev: {"path": "drizzle/docs/drizzle-kit-export/index.md", "title": "drizzle-kit export"}
nav_next: {"path": "drizzle/docs/drizzle-kit-up/index.md", "title": "drizzle-kit up"}
---

`drizzle-kit check` command lets you check consistency of your generated SQL migrations history.

That’s extremely useful when you have multiple developers working on the project and altering database schema on different branches - read more about [migrations for teams](drizzle/docs/kit-migrations-for-teams/index.md).

  

* * *

`drizzle-kit check` command requires you to specify both `dialect` and database connection credentials, you can provide them either via [drizzle.config.ts](drizzle/docs/drizzle-config-file/index.md) config file or via CLI options

With config file

As CLI options

```
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
});
```

```
npx drizzle-kit check
```

```
npx drizzle-kit check --dialect=postgresql
```

### Multiple configuration files in one project[](#multiple-configuration-files-in-one-project)

You can have multiple config files in the project, it’s very useful when you have multiple database stages or multiple databases on the same project:

npm

yarn

pnpm

bun

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

### Extended list of configurations[](#extended-list-of-configurations)

We recommend configuring `drizzle-kit` through [drizzle.config.ts](drizzle/docs/drizzle-config-file/index.md) file, yet you can provide all configuration options through CLI if necessary, e.g. in CI/CD pipelines, etc.

`dialect`

`required`

Database dialect you are using. Can be `postgresql`,`mysql` or `sqlite`

`out`

Migrations folder, default=`./drizzle`

`config`

Configuration file path, default=`drizzle.config.ts`

  

npm

yarn

pnpm

bun

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
