---
title: "Get Started with Drizzle and Bun:SQLite"
source: "https://orm.drizzle.team/docs/get-started/bun-sqlite-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/bun-sqlite-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:42:35.152Z"
content_hash: "a7c080dfd552e3bf5deab5e5c3b2c7bc63a012fe3511ee57ea784ee66c35e5ca"
menu_path: ["Get Started with Drizzle and Bun:SQLite"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/get-started/bun-sqlite-existing/index.md", "title": "Get Started with Drizzle and Bun:SQLite in existing project"}
nav_next: {"path": "drizzle/docs/get-started/cockroach-existing/index.md", "title": "Get Started with Drizzle and CockroachDB in existing project"}
---

## Get Started with Drizzle and Bun:SQLite

This guide assumes familiarity with:

-   **bun** - javaScript all-in-one toolkit - [read here](https://bun.sh/)
-   **bun:sqlite** - native implementation of a high-performance SQLite3 driver - [read here](https://bun.sh/docs/api/sqlite)

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

#### Step 1 - Install required packages[](#step-1---install-required-packages)

```
npm i drizzle-orm
npm i -D drizzle-kit @types/bun
```

```
yarn add drizzle-orm
yarn add -D drizzle-kit @types/bun
```

```
pnpm add drizzle-orm
pnpm add -D drizzle-kit @types/bun
```

```
bun add drizzle-orm
bun add -D drizzle-kit @types/bun
```

#### Step 2 - Setup connection variables[](#step-2---setup-connection-variables)

Create a `.env` file in the root of your project and add your database connection variable:

important

For example, if you want to create an SQLite database file in the root of your project for testing purposes, you can use this example:

```plaintext
DB_FILE_NAME=mydb.sqlite
```

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

Create a `index.ts` file in the `src` directory and initialize the connection:

bun:sqlite

bun:sqlite with config

```typescript
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/bun-sqlite';

const db = drizzle(process.env.DB_FILE_NAME!);
```

```typescript
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/bun-sqlite';

// You can specify any property from the bun:sql connection options
const db = drizzle({ connection: { source: process.env.DB_FILE_NAME! }});
```

If you need to provide your existing driver:

```typescript
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/bun-sqlite';
import { Database } from 'bun:sqlite';

const sqlite = new Database(process.env.DB_FILE_NAME!);
const db = drizzle({ client: sqlite });
```

#### Step 4 - Create a table[](#step-4---create-a-table)

Create a `schema.ts` file in the `src/db` directory and declare your table:

```typescript
import { int, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const usersTable = sqliteTable("users_table", {
  id: int().primaryKey({ autoIncrement: true }),
  name: text().notNull(),
  age: int().notNull(),
  email: text().notNull().unique(),
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
  dialect: 'sqlite',
  dbCredentials: {
    url: process.env.DB_FILE_NAME!,
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
import { drizzle } from 'drizzle-orm/bun-sqlite';
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

To run a script with `bun`, use the following command:

```bash
bun src/index.ts
```
