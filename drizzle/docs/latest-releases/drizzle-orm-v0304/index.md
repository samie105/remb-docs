---
title: "Drizzle ORM - DrizzleORM v0.30.4 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0304"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0304"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:13:14.437Z"
content_hash: "4e0fbe113beaa7e4df41528deccec00e8d5b6ee61eea6addcd0af2adb6cb344b"
menu_path: ["Drizzle ORM - DrizzleORM v0.30.4 release"]
section_path: []
content_language: "en"
---
DrizzleORM v0.30.4 release

Mar 19, 2024

## New Features

### 🎉 xata-http driver support

According their **[official website](https://xata.io/)**, Xata is a Postgres data platform with a focus on reliability, scalability, and developer experience. The Xata Postgres service is currently in beta, please see the [Xata docs](https://xata.io/docs/postgres) on how to enable it in your account.

Drizzle ORM natively supports both the `xata` driver with `drizzle-orm/xata` package and the **`postgres`** or **`pg`** drivers for accessing a Xata Postgres database.

The following example use the Xata generated client, which you obtain by running the [xata init](https://xata.io/docs/getting-started/installation) CLI command.

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

```ts
import { drizzle } from 'drizzle-orm/xata-http';
import { getXataClient } from './xata'; // Generated client

const xata = getXataClient();
const db = drizzle(xata);

const result = await db.select().from(...);
```

You can also connect to Xata using `pg` or `postgres.js` drivers

To get started with Xata and Drizzle follow the [documentation](https://orm.drizzle.team/docs/get-started-postgresql#xata).
