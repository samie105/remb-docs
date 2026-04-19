---
title: "Drizzle <> Cloudflare D1"
source: "https://orm.drizzle.team/docs/connect-cloudflare-d1"
canonical_url: "https://orm.drizzle.team/docs/connect-cloudflare-d1"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:56.332Z"
content_hash: "5af2dae5ef5550187c5b3c79ca0fe80196906dc6e8903c104bf9726b3019229f"
menu_path: ["Drizzle <> Cloudflare D1"]
section_path: []
nav_prev: {"path": "drizzle/docs/connect-sqlite-cloud/index.md", "title": "Drizzle <> SQLite Cloud"}
nav_next: {"path": "drizzle/docs/connect-bun-sqlite/index.md", "title": "Drizzle <> Bun SQLite"}
---

According to the **[official website](https://developers.cloudflare.com/d1/)**, D1 is Cloudflare’s first queryable relational database.

Drizzle ORM fully supports the Cloudflare D1 database and Cloudflare Workers environment. We embrace SQL dialects and dialect specific drivers and syntax and mirror most popular SQLite-like `all`, `get`, `values` and `run` query methods syntax.

To setup project for your Cloudflare D1 please refer to **[official docs.](https://developers.cloudflare.com/d1/)**

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

```
npm i drizzle-orm
npm i -D drizzle-kit
```

```
yarn add drizzle-orm
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

You would need to have either a `wrangler.json` or a `wrangler.toml` file for D1 database and will look something like this:

wrangler.json

wrangler.toml

```
{
    "name": "YOUR_PROJECT_NAME",
    "main": "src/index.ts",
    "compatibility_date": "2024-09-26",
    "compatibility_flags": [
        "nodejs_compat"
    ],
    "d1_databases": [
        {
            "binding": "BINDING_NAME",
            "database_name": "YOUR_DB_NAME",
            "database_id": "YOUR_DB_ID",
            "migrations_dir": "drizzle/migrations"
        }
    ]
}
```

```
name = "YOUR_PROJECT_NAME"
main = "src/index.ts"
compatibility_date = "2022-11-07"
node_compat = true

[[ d1_databases ]]
binding = "BINDING_NAME"
database_name = "YOUR_DB_NAME"
database_id = "YOUR_DB_ID"
migrations_dir = "drizzle/migrations"
```

Make your first D1 query:

```
import { drizzle } from 'drizzle-orm/d1';

export interface Env {
  <BINDING_NAME>: D1Database;
}

export default {
  async fetch(request: Request, env: Env) {
    const db = drizzle(env.<BINDING_NAME>);
    const result = await db.select().from(users).all()
    return Response.json(result);
  },
};
```

#### What’s next?[](#whats-next)
