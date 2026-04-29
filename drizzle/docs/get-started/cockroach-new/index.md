---
title: "Get Started with Drizzle and CockroachDB"
source: "https://orm.drizzle.team/docs/get-started/cockroach-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/cockroach-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:43:09.241Z"
content_hash: "45b762db3146c9ec7e24a9963871f9e5291c4f443d45b5c23580a8ca222a6dae"
menu_path: ["Get Started with Drizzle and CockroachDB"]
section_path: []
content_language: "en"
nav_prev: {"path": "../cockroach-existing/index.md", "title": "Get Started with Drizzle and CockroachDB in existing project"}
nav_next: {"path": "../d1-existing/index.md", "title": "Get Started with Drizzle and D1 in existing project"}
---

## Get Started with Drizzle and CockroachDB

WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.2` and higher.

  

This guide assumes familiarity with:

-   **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
-   **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
-   **node-postgres** - package for querying your PostgreSQL database - [read here](https://node-postgres.com/)

Drizzle has native support for CockroachDB connections with the `node-postgres` and `postgres.js` drivers.

We will use `node-postgres` for this get started example. But if you want to find more ways to connect to postgresql check our [CockroachDB Connection](../../get-started-cockroach/index.md) page

#### Basic file structure

This is the basic file structure of the project. In the `src/db` directory, we have table definition in `schema.ts`. In `drizzle` folder there are sql migration file and snapshots.

```plaintext
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

#### Step 1 - Install **node-postgres** package[](#step-1---install-node-postgres-package)

```
npm i drizzle-orm@beta pg dotenv
npm i -D drizzle-kit@beta tsx @types/pg
```

```
yarn add drizzle-orm@beta pg dotenv
yarn add -D drizzle-kit@beta tsx @types/pg
```

```
pnpm add drizzle-orm@beta pg dotenv
pnpm add -D drizzle-kit@beta tsx @types/pg
```

```
bun add drizzle-orm@beta pg dotenv
bun add -D drizzle-kit@beta tsx @types/pg
```

#### Step 2 - Setup connection variables[](#step-2---setup-connection-variables)

Create a `.env` file in the root of your project and add your database connection variable:

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

Create a `index.ts` file in the `src/db` directory and initialize the connection:

node-postgres

node-postgres with config

your node-postgres driver

```typescript
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/cockroach';

const db = drizzle(process.env.DATABASE_URL!);
```

```typescript
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/cockroach';

// You can specify any property from the node-postgres connection options
const db = drizzle({ 
  connection: { 
    connectionString: process.env.DATABASE_URL!,
    ssl: true
  }
});
```

```typescript
import 'dotenv/config';
import { drizzle } from "drizzle-orm/cockroach";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL!,
});
const db = drizzle({ client: pool });
```

#### Step 4 - Create a table[](#step-4---create-a-table)

Create a `schema.ts` file in the `src/db` directory and declare your table:

```typescript
import { int4, cockroachTable, varchar } from "drizzle-orm/cockroach-core";

export const usersTable = cockroachTable("users", {
  id: int4().primaryKey().generatedAlwaysAsIdentity(),
  name: varchar({ length: 255 }).notNull(),
  age: int4().notNull(),
  email: varchar({ length: 255 }).notNull().unique(),
});
```

#### Step 5 - Setup Drizzle config file[](#step-5---setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](../../kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```typescript
import 'dotenv/config';
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  out: './drizzle',
  schema: './src/db/schema.ts',
  dialect: 'cockroach',
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
});
```

#### Step 6 - Applying changes to the database[](#step-6---applying-changes-to-the-database)

You can directly apply changes to your database using the `drizzle-kit push` command. This is a convenient method for quickly testing new schema designs or modifications in a local development environment, allowing for rapid iterations without the need to manage migration files:

```bash
npx drizzle-kit push
```

Read more about the push command in [documentation](../../drizzle-kit-push/index.md).

Tips

Alternatively, you can generate migrations using the `drizzle-kit generate` command and then apply them using the `drizzle-kit migrate` command:

Generate migrations:

```bash
npx drizzle-kit generate
```

Apply migrations:

```bash
npx drizzle-kit migrate
```

Read more about migration process in [documentation](../../kit-overview/index.md).

#### Step 7 - Seed and Query the database[](#step-7---seed-and-query-the-database)

Let’s **update** the `src/index.ts` file with queries to create, read, update, and delete users

```typescript
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/cockroach';
import { eq } from 'drizzle-orm';
import { usersTable } from './db/schema';
  
const db = drizzle(process.env.DATABASE_URL!);

async function main() {
  const user: typeof usersTable.$inferInsert = {
    name: 'John',
    age: 30,
    email: 'john@example.com',
  };

  await db.insert(usersTable).values(user);
  console.log('New user created!')

  const users = await db.select().from(usersTable);
  console.log('Getting all users from the database: ', users)
  /*
  const users: {
    id: number;
    name: string;
    age: number;
    email: string;
  }[]
  */

  await db
    .update(usersTable)
    .set({
      age: 31,
    })
    .where(eq(usersTable.email, user.email));
  console.log('User info updated!')

  await db.delete(usersTable).where(eq(usersTable.email, user.email));
  console.log('User deleted!')
}

main();
```

#### Step 8 - Run index.ts file[](#step-8---run-indexts-file)

To run any TypeScript files, you have several options, but let’s stick with one: using `tsx`

You’ve already installed `tsx`, so we can run our queries now

**Run `index.ts` script**

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

```bash
bun src/index.ts
```

If you don’t have bun installed, check the [Bun installation docs](https://bun.sh/docs/installation#installing)
