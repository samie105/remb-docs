---
title: "drizzle-kit up"
source: "https://orm.drizzle.team/docs/drizzle-kit-up"
canonical_url: "https://orm.drizzle.team/docs/drizzle-kit-up"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:14.345Z"
content_hash: "aedb0e00921cce807864d859f7fbc01f5597f80911f1c81929c9c9d609d71b63"
menu_path: ["drizzle-kit up"]
section_path: []
nav_prev: {"path": "drizzle/docs/drizzle-kit-check/index.md", "title": "drizzle-kit check"}
nav_next: {"path": "drizzle/docs/drizzle-kit-studio/index.md", "title": "drizzle-kit studio"}
---

`drizzle-kit up` command lets you upgrade drizzle schema snapshots to a newer version. It’s required whenever we introduce breaking changes to the json snapshots of the schema and upgrade the internal version.

  

* * *

`drizzle-kit up` command requires you to specify both `dialect` and database connection credentials, you can provide them either via [drizzle.config.ts](drizzle/docs/drizzle-config-file/index.md) config file or via CLI options

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
npx drizzle-kit up
```

```
npx drizzle-kit up --dialect=postgresql
```

### Multiple configuration files in one project[](#multiple-configuration-files-in-one-project)

You can have multiple config files in the project, it’s very useful when you have multiple database stages or multiple databases on the same project:

npm

yarn

pnpm

bun

```
npx drizzle-kit migrate --config=drizzle-dev.config.ts
npx drizzle-kit migrate --config=drizzle-prod.config.ts
```

```
yarn drizzle-kit migrate --config=drizzle-dev.config.ts
yarn drizzle-kit migrate --config=drizzle-prod.config.ts
```

```
pnpm drizzle-kit migrate --config=drizzle-dev.config.ts
pnpm drizzle-kit migrate --config=drizzle-prod.config.ts
```

```
bunx drizzle-kit migrate --config=drizzle-dev.config.ts
bunx drizzle-kit migrate --config=drizzle-prod.config.ts
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
npx drizzle-kit up --dialect=postgresql
npx drizzle-kit up --dialect=postgresql --out=./migrations-folder
```

```
yarn drizzle-kit up --dialect=postgresql
yarn drizzle-kit up --dialect=postgresql --out=./migrations-folder
```

```
pnpm drizzle-kit up --dialect=postgresql
pnpm drizzle-kit up --dialect=postgresql --out=./migrations-folder
```

```
bunx drizzle-kit up --dialect=postgresql
bunx drizzle-kit up --dialect=postgresql --out=./migrations-folder
```

![](https://orm.drizzle.team/_astro/up_mysql.FpcTUeNG_Zl2NXa.webp)
