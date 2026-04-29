---
title: "Drizzle <> PlanetScale MySQL"
source: "https://orm.drizzle.team/docs/connect-planetscale"
canonical_url: "https://orm.drizzle.team/docs/connect-planetscale"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:30:50.008Z"
content_hash: "2b18d4dd11c489214a4762a1023917921679687b71220463ddbc45650105a600"
menu_path: ["Drizzle <> PlanetScale MySQL"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/connect-effect-postgres/index.md", "title": "Drizzle <> Effect Postgres"}
nav_next: {"path": "drizzle/docs/connect-tidb/index.md", "title": "Drizzle <> TiDB Serverless"}
---

PlanetScale offers both MySQL (Vitess) and PostgreSQL databases. This page covers connecting to PlanetScale MySQL.

For PlanetScale Postgres, see the [PlanetScale Postgres connection guide](../connect-planetscale-postgres/index.md).

With Drizzle ORM you can access PlanetScale MySQL over http through their official **[`database-js`](https://github.com/planetscale/database-js)** driver from serverless and serverfull environments with our `drizzle-orm/planetscale-serverless` package.

You can also access PlanetScale MySQL through TCP with `mysql2` driver — **[see here.](../get-started-mysql/index.md)**

#### Step 1 - Install packages[](#step-1---install-packages)

```
npm i drizzle-orm @planetscale/database -D drizzle-kit
```

```
yarn add drizzle-orm @planetscale/database -D drizzle-kit
```

```
pnpm add drizzle-orm @planetscale/database -D drizzle-kit
```

```
bun add drizzle-orm @planetscale/database -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

```typescript
import { drizzle } from "drizzle-orm/planetscale-serverless";

const db = drizzle({ connection: {
  host: process.env["DATABASE_HOST"],
  username: process.env["DATABASE_USERNAME"],
  password: process.env["DATABASE_PASSWORD"],
}});

const response = await db.select().from(...)
```

If you need to provide your existing driver

```typescript
import { drizzle } from "drizzle-orm/planetscale-serverless";
import { Client } from "@planetscale/database";

const client = new Client({
  host: process.env["DATABASE_HOST"],
  username: process.env["DATABASE_USERNAME"],
  password: process.env["DATABASE_PASSWORD"],
});

const db = drizzle({ client });
```

Make sure to checkout the PlanetScale official **[MySQL courses](https://planetscale.com/courses/mysql-for-developers)**, we think they’re outstanding 🙌

#### What’s next?[](#whats-next)
