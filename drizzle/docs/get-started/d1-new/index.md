---
title: "Get Started with Drizzle and D1"
source: "https://orm.drizzle.team/docs/get-started/d1-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/d1-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:07.562Z"
content_hash: "0a972c77339d0265acbaca75eff28b7ccfd3b39a53bc5d2f2d4d5f17d24f2fe9"
menu_path: ["Get Started with Drizzle and D1"]
section_path: []
nav_prev: {"path": "drizzle/docs/get-started/d1-existing/index.md", "title": "Get Started with Drizzle and D1 in existing project"}
nav_next: {"path": "drizzle/docs/get-started/do-new/index.md", "title": "Get Started with Drizzle and SQLite Durable Objects"}
---

## Get Started with Drizzle and D1

This guide assumes familiarity with:

*   **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
*   **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
*   **Cloudflare D1** - Serverless SQL database to query from your Workers and Pages projects - [read here](https://developers.cloudflare.com/d1/)
*   **wrangler** - Cloudflare Developer Platform command-line interface - [read here](https://developers.cloudflare.com/workers/wrangler)

#### Basic file structure

This is the basic file structure of the project. In the `src/db` directory, we have table definition in `schema.ts`. In `drizzle` folder there are sql migration file and snapshots.

```
📦 <project root>
 ├ 📂 drizzle
 ├ 📂 src
 │   ├ 📂 db
 │   │  └ 📜 schema.ts
 │   └ 📜 index.ts
 ├ 📜 .env
 ├ 📜 drizzle.config.ts
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

#### Step 1 - Install required packages[](#step-1---install-required-packages)

npm

yarn

pnpm

bun

```
npm i drizzle-orm wrangler dotenv
npm i -D drizzle-kit tsx
```

```
yarn add drizzle-orm wrangler dotenv
yarn add -D drizzle-kit tsx
```

```
pnpm add drizzle-orm wrangler dotenv
pnpm add -D drizzle-kit tsx
```

```
bun add drizzle-orm wrangler dotenv
bun add -D drizzle-kit tsx
```

#### Step 2 - Setup wrangler.toml[](#step-2---setup-wranglertoml)

You would need to have a `wrangler.toml` file for D1 database and will look something like this:

```
name = "YOUR PROJECT NAME"
main = "src/index.ts"
compatibility_date = "2022-11-07"
node_compat = true

[[ d1_databases ]]
binding = "DB"
database_name = "YOUR DB NAME"
database_id = "YOUR DB ID"
migrations_dir = "drizzle"
```

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

```
import { drizzle } from 'drizzle-orm/d1';

export interface Env {
  <BINDING_NAME>: D1Database;
}
export default {
  async fetch(request: Request, env: Env) {
    const db = drizzle(env.<BINDING_NAME>);
  },
};
```

#### Step 4 - Generate wrangler types[](#step-4---generate-wrangler-types)

npm

yarn

pnpm

bun

```
npx wrangler types
```

```
yarn wrangler types
```

```
pnpm wrangler types
```

```
bunx wrangler types
```

The output of this command will be a `worker-configuration.d.ts` file.

#### Step 5 - Create a table[](#step-5---create-a-table)

Create a `schema.ts` file in the `src/db` directory and declare your table:

```
import { int, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const usersTable = sqliteTable("users_table", {
  id: int().primaryKey({ autoIncrement: true }),
  name: text().notNull(),
  age: int().notNull(),
  email: text().notNull().unique(),
});
```

#### Step 6 - Setup Drizzle config file[](#step-6---setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import 'dotenv/config';
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  out: './drizzle',
  schema: './src/db/schema.ts',
  dialect: 'sqlite',
  driver: 'd1-http',
  dbCredentials: {
    accountId: process.env.CLOUDFLARE_ACCOUNT_ID!,
    databaseId: process.env.CLOUDFLARE_DATABASE_ID!,
    token: process.env.CLOUDFLARE_D1_TOKEN!,
  },
});
```

tips

You can check [our tutorial](drizzle/docs/guides/d1-http-with-drizzle-kit/index.md) on how to get env variables from CloudFlare

#### Step 7 - Applying changes to the database[](#step-7---applying-changes-to-the-database)

You can directly apply changes to your database using the `drizzle-kit push` command. This is a convenient method for quickly testing new schema designs or modifications in a local development environment, allowing for rapid iterations without the need to manage migration files:

```
npx drizzle-kit push
```

Read more about the push command in [documentation](drizzle/docs/drizzle-kit-push/index.md).

Tips

Alternatively, you can generate migrations using the `drizzle-kit generate` command and then apply them using the `drizzle-kit migrate` command:

Generate migrations:

```
npx drizzle-kit generate
```

Apply migrations:

```
npx drizzle-kit migrate
```

Read more about migration process in [documentation](drizzle/docs/kit-overview/index.md).

#### Step 8 - Seed and Query the database[](#step-8---seed-and-query-the-database)

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

#### Step 9 - Run index.ts file[](#step-9---run-indexts-file)

To run any TypeScript files, you have several options, but let’s stick with one: using `tsx`

You’ve already installed `tsx`, so we can run our queries now

**Run `index.ts` script**

npm

yarn

pnpm

bun

```
npx tsx src/index.ts
```

```
yarn tsx src/index.ts
```

```
pnpm tsx src/index.ts
```

```
bunx tsx src/index.ts
```

tips

We suggest using `bun` to run TypeScript files. With `bun`, such scripts can be executed without issues or additional settings, regardless of whether your project is configured with CommonJS (CJS), ECMAScript Modules (ESM), or any other module format. To run a script with `bun`, use the following command:

```
bun src/index.ts
```

If you don’t have bun installed, check the [Bun installation docs](https://bun.sh/docs/installation#installing)

