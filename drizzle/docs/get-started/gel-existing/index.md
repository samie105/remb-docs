---
title: "Get Started with Drizzle and Gel in existing project"
source: "https://orm.drizzle.team/docs/get-started/gel-existing"
canonical_url: "https://orm.drizzle.team/docs/get-started/gel-existing"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:09.903Z"
content_hash: "d32e45d73fabe1dffef46f4a5a907aa49839dbc99858a41b60919ca68c8f508f"
menu_path: ["Get Started with Drizzle and Gel in existing project"]
section_path: []
nav_prev: {"path": "drizzle/docs/get-started/effect-postgresql-new/index.md", "title": "Get Started with Drizzle and Effect PostgreSQL"}
nav_next: {"path": "drizzle/docs/get-started/mssql-existing/index.md", "title": "Get Started with Drizzle and MSSQL in existing project"}
---

## Get Started with Drizzle and Gel in existing project

This guide assumes familiarity with:

*   **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
*   **gel-js** - package for querying your Gel database - [read here](https://github.com/geldata/gel-js)

Drizzle has native support for Gel connections with the `gel` client.

This is the basic file structure of the project. In the `src` directory, we have table definition in `index.ts`. In `drizzle` folder there are generated Gel to Drizzle schema

```
📦 <project root>
 ├ 📂 drizzle
 ├ 📂 dbschema
 │ ├ 📂 migrations
 │ ├ 📜 default.esdl
 │ └ 📜 scoping.esdl
 ├ 📂 src
 │ └ 📜 index.ts
 ├ 📜 drizzle.config.ts
 ├ 📜 edgedb.toml
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

#### Step 1 - Install required packages[](#step-1---install-required-packages)

npm

yarn

pnpm

bun

```
npm i drizzle-orm gel
npm i -D drizzle-kit tsx
```

```
yarn add drizzle-orm gel
yarn add -D drizzle-kit tsx
```

```
pnpm add drizzle-orm gel
pnpm add -D drizzle-kit tsx
```

```
bun add drizzle-orm gel
bun add -D drizzle-kit tsx
```

#### Step 2 - Setup Drizzle config file[](#step-2---setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  dialect: 'gel',
});
```

#### Step 3 - Pull Gel types to Drizzle schema[](#step-3---pull-gel-types-to-drizzle-schema)

Pull your database schema:

npm

yarn

pnpm

bun

```
npx drizzle-kit pull
```

```
yarn drizzle-kit pull
```

```
pnpm drizzle-kit pull
```

```
bunx drizzle-kit pull
```

Here is an example of the generated schema.ts file:

```
import { gelTable, uniqueIndex, uuid, smallint, text } from "drizzle-orm/gel-core"
import { sql } from "drizzle-orm"

export const users = gelTable("users", {
	id: uuid().default(sql`uuid_generate_v4()`).primaryKey().notNull(),
	age: smallint(),
	email: text().notNull(),
	name: text(),
}, (table) => [
	uniqueIndex("a8c6061c-f37f-11ef-9249-0d78f6c1807b;schemaconstr").using("btree", table.id.asc().nullsLast().op("uuid_ops")),
]);
```

#### Step 4 - Connect Drizzle ORM to the database[](#step-4---connect-drizzle-orm-to-the-database)

Create a `index.ts` file in the `src` directory and initialize the connection:

```
import { drizzle } from "drizzle-orm/gel";
import { createClient } from "gel";

const gelClient = createClient();
const db = drizzle({ client: gelClient });
```

#### Step 5 - Query the database[](#step-5---query-the-database)

```
import { eq } from "drizzle-orm";
import { drizzle } from "drizzle-orm/gel";
import { createClient } from "gel";
import { users } from "../drizzle/schema";

const gelClient = createClient();
const db = drizzle({ client: gelClient });

async function main() {
  const user: typeof users.$inferInsert = {
    name: "John",
    age: 30,
    email: "john@example.com",
  };

  await db.insert(users).values(user);
  console.log("New user created!");

  const usersResponse = await db.select().from(users);
  console.log("Getting all users from the database: ", usersResponse);
  /*
  const users: {
    id: number;
    name: string;
    age: number;
    email: string;
  }[]
  */

  await db
    .update(users)
    .set({
      age: 31,
    })
    .where(eq(users.email, user.email));
  console.log("User info updated!");

  await db.delete(users).where(eq(users.email, user.email));
  console.log("User deleted!");
}

main();
```

#### Step 6 - Run index.ts file[](#step-6---run-indexts-file)

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

