---
title: "Drizzle <> PlanetScale MySQL"
source: "https://orm.drizzle.team/docs/connect-planetscale"
canonical_url: "https://orm.drizzle.team/docs/connect-planetscale"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:30.459Z"
content_hash: "3404f66339d290e14c5177bcda6e69d4b9f5b990a014ff23560d722e5ce9bc30"
menu_path: ["Drizzle <> PlanetScale MySQL"]
section_path: []
---
PlanetScale offers both MySQL (Vitess) and PostgreSQL databases. This page covers connecting to PlanetScale MySQL.

For PlanetScale Postgres, see the [PlanetScale Postgres connection guide](https://orm.drizzle.team/docs/connect-planetscale-postgres).

With Drizzle ORM you can access PlanetScale MySQL over http through their official **[`database-js`](https://github.com/planetscale/database-js)** driver from serverless and serverfull environments with our `drizzle-orm/planetscale-serverless` package.

You can also access PlanetScale MySQL through TCP with `mysql2` driver — **[see here.](https://orm.drizzle.team/docs/get-started-mysql)**

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

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

```
import { drizzle } from "drizzle-orm/planetscale-serverless";

const db = drizzle({ connection: {
  host: process.env["DATABASE_HOST"],
  username: process.env["DATABASE_USERNAME"],
  password: process.env["DATABASE_PASSWORD"],
}});

const response = await db.select().from(...)
```

If you need to provide your existing driver

```
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
