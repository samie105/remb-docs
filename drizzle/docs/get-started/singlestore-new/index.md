---
title: "Get Started with Drizzle and SingleStore"
source: "https://orm.drizzle.team/docs/get-started/singlestore-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/singlestore-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:51:46.587Z"
content_hash: "b01b073183c500591654124ac1581c490813425c99d00c50e420569c2e869f61"
menu_path: ["Get Started with Drizzle and SingleStore"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/get-started/singlestore-existing/index.md", "title": "Get Started with Drizzle and SingleStore in existing project"}
nav_next: {"path": "drizzle/docs/get-started/sqlite-cloud-existing/index.md", "title": "Get Started with Drizzle and SQLite Cloud in existing project"}
---

## Get Started with Drizzle and SingleStore

This guide assumes familiarity with:

-   **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
-   **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
-   **mysql2** - package for querying your MySQL database - [read here](https://github.com/sidorares/node-mysql2)

To use Drizzle with a SingleStore database, you should use the `singlestore` driver

According to the **[official website](https://github.com/sidorares/node-mysql2)**, `mysql2` is a MySQL client for Node.js with focus on performance.

Drizzle ORM natively supports `mysql2` with `drizzle-orm/singlestore` package for SingleStore database.

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

#### Step 1 - Install **mysql2** package[](#step-1---install-mysql2-package)

```
npm i drizzle-orm mysql2 dotenv
npm i -D drizzle-kit tsx
```

```
yarn add drizzle-orm mysql2 dotenv
yarn add -D drizzle-kit tsx
```

```
pnpm add drizzle-orm mysql2 dotenv
pnpm add -D drizzle-kit tsx
```

```
bun add drizzle-orm mysql2 dotenv
bun add -D drizzle-kit tsx
```

#### Step 2 - Setup connection variables[](#step-2---setup-connection-variables)

Create a `.env` file in the root of your project and add your database connection variable:

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

Create a `index.ts` file in the `src/db` directory and initialize the connection:

mysql2

mysql2 with config

your mysql2 driver

```typescript
import 'dotenv/config';
import { drizzle } from "drizzle-orm/singlestore";

const db = drizzle(process.env.DATABASE_URL);
```

```typescript
import 'dotenv/config';
import { drizzle } from "drizzle-orm/singlestore";

// You can specify any property from the mysql2 connection options
const db = drizzle({ connection: { uri: process.env.DATABASE_URL }});
```

```ts
import 'dotenv/config';
import { drizzle } from "drizzle-orm/singlestore";
import mysql from "mysql2/promise";
  
const poolConnection = mysql.createPool({
  host: "host",
  user: "user",
  database: "database",
});
const db = drizzle({ client: poolConnection });

// or if you need client connection
async function main() {
  const connection = await mysql.createConnection({
    host: "host",
    user: "user",
    database: "database",
  });
  const db = drizzle({ client: connection });
}
main();
```

IMPORTANT

For the built in `migrate` function with DDL migrations we and drivers strongly encourage you to use single `client` connection.

For querying purposes feel free to use either `client` or `pool` based on your business demands.

#### Step 4 - Create a table[](#step-4---create-a-table)

Create a `schema.ts` file in the `src/db` directory and declare your table:

```typescript
import { int, singlestoreTable, varchar } from 'drizzle-orm/singlestore-core';

export const usersTable = singlestoreTable('users_table', {
  id: int().primaryKey(),
  name: varchar({ length: 255 }).notNull(),
  age: int().notNull(),
  email: varchar({ length: 255 }).notNull().unique(),
});
```

#### Step 5 - Setup Drizzle config file[](#step-5---setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```typescript
import 'dotenv/config';
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  out: './drizzle',
  schema: './src/db/schema.ts',
  dialect: 'singlestore',
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

Read more about the push command in [documentation](drizzle/docs/drizzle-kit-push/index.md).

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

Read more about migration process in [documentation](drizzle/docs/kit-overview/index.md).

#### Step 7 - Seed and Query the database[](#step-7---seed-and-query-the-database)

Let’s **update** the `src/index.ts` file with queries to create, read, update, and delete users

```typescript
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/singlestore';
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
