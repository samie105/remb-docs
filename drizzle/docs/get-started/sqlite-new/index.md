---
title: "Get Started with Drizzle and SQLite"
source: "https://orm.drizzle.team/docs/get-started/sqlite-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/sqlite-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:11.910Z"
content_hash: "10ccb90a0d6b5c14f6d8da1c681f2c515557c39b75f0b409e37181a22fa59c91"
menu_path: ["Get Started with Drizzle and SQLite"]
section_path: []
nav_prev: {"path": "drizzle/docs/get-started/sqlite-existing/index.md", "title": "Get Started with Drizzle and SQLite in existing project"}
nav_next: {"path": "drizzle/docs/get-started/supabase-existing/index.md", "title": "Get Started with Drizzle and Supabase in existing project"}
---

## Get Started with Drizzle and SQLite

This guide assumes familiarity with:

*   **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
*   **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
*   **libsql** - a fork of SQLite optimized for low query latency, making it suitable for global applications - [read here](https://docs.turso.tech/libsql)

Drizzle has native support for SQLite connections with the `libsql` and `better-sqlite3` drivers.

We will use `libsql` for this get started example. But if you want to find more ways to connect to SQLite check our [SQLite Connection](drizzle/docs/get-started-sqlite/index.md) page

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
npm i drizzle-orm @libsql/client dotenv
npm i -D drizzle-kit tsx
```

```
yarn add drizzle-orm @libsql/client dotenv
yarn add -D drizzle-kit tsx
```

```
pnpm add drizzle-orm @libsql/client dotenv
pnpm add -D drizzle-kit tsx
```

```
bun add drizzle-orm @libsql/client dotenv
bun add -D drizzle-kit tsx
```

#### Step 2 - Setup connection variables[](#step-2---setup-connection-variables)

Create a `.env` file in the root of your project and add your database connection variable:

```
DB_FILE_NAME=
```

important

For example, if you want to create an SQLite database file in the root of your project for testing purposes, you need to use `file:` before the actual filename, as this is the format required by `LibSQL`, like this:

```
DB_FILE_NAME=file:local.db
```

You can check the **[LibSQL docs](https://docs.turso.tech/sdk/ts/reference#local-development)** for more info.

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

Create a `index.ts` file in the `src` directory and initialize the connection:

libsql

libsql with config

```
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/libsql';

const db = drizzle(process.env.DB_FILE_NAME!);
```

```
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/libsql';

// You can specify any property from the libsql connection options
const db = drizzle({ connection: { url: process.env.DB_FILE_NAME! }});
```

If you need to provide your existing driver:

```
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/libsql';
import { createClient } from '@libsql/client';

const client = createClient({ url: process.env.DB_FILE_NAME! });
const db = drizzle({ client });
```

#### Step 4 - Create a table[](#step-4---create-a-table)

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

#### Step 5 - Setup Drizzle config file[](#step-5---setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import 'dotenv/config';
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  out: './drizzle',
  schema: './src/db/schema.ts',
  dialect: 'sqlite',
  dbCredentials: {
    url: process.env.DB_FILE_NAME!,
  },
});
```

#### Step 6 - Applying changes to the database[](#step-6---applying-changes-to-the-database)

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

#### Step 7 - Seed and Query the database[](#step-7---seed-and-query-the-database)

Let’s **update** the `src/index.ts` file with queries to create, read, update, and delete users

```
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/libsql';
import { eq } from 'drizzle-orm';
import { usersTable } from './db/schema';
  
const db = drizzle(process.env.DB_FILE_NAME!);

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
