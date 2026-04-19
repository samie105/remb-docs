---
title: "Drizzle ORM - DrizzleORM v0.30.4 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0304"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0304"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:04.161Z"
content_hash: "fcc42de70b18d16c0add1679a315a54d5699d3a1b14b93744a11a609844ccfb2"
menu_path: ["Drizzle ORM - DrizzleORM v0.30.4 release"]
section_path: []
nav_prev: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0303/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.3 release"}
nav_next: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0305/index.md", "title": "Drizzle ORM - DrizzleORM v0.30.5 release"}
---

DrizzleORM v0.30.4 release

Mar 19, 2024

## New Features

### 🎉 xata-http driver support

According their **[official website](https://xata.io/)**, Xata is a Postgres data platform with a focus on reliability, scalability, and developer experience. The Xata Postgres service is currently in beta, please see the [Xata docs](https://xata.io/docs/postgres) on how to enable it in your account.

Drizzle ORM natively supports both the `xata` driver with `drizzle-orm/xata` package and the **`postgres`** or **`pg`** drivers for accessing a Xata Postgres database.

The following example use the Xata generated client, which you obtain by running the [xata init](https://xata.io/docs/getting-started/installation) CLI command.

npm

yarn

pnpm

bun

```
npm i drizzle-orm @xata.io/client
npm i -D drizzle-kit
```

```
yarn add drizzle-orm @xata.io/client
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm @xata.io/client
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm @xata.io/client
bun add -D drizzle-kit
```

```
import { drizzle } from 'drizzle-orm/xata-http';
import { getXataClient } from './xata'; // Generated client

const xata = getXataClient();
const db = drizzle(xata);

const result = await db.select().from(...);
```

You can also connect to Xata using `pg` or `postgres.js` drivers

To get started with Xata and Drizzle follow the [documentation](drizzle/docs/get-started-postgresql/index.md#xata).
