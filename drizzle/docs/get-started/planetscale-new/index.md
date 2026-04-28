---
title: "Get Started with Drizzle and PlanetScale"
source: "https://orm.drizzle.team/docs/get-started/planetscale-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/planetscale-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:50:02.866Z"
content_hash: "4e0ccbd46bdf62449f99abf41ae93ba1347eb7c85d18d77dafb34d02d7b8092e"
menu_path: ["Get Started with Drizzle and PlanetScale"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/get-started/planetscale-existing/index.md", "title": "Get Started with Drizzle and PlanetScale in existing project"}
nav_next: {"path": "drizzle/docs/get-started/planetscale-postgres-existing/index.md", "title": "Get Started with Drizzle and PlanetScale Postgres in existing project"}
---

## Get Started with Drizzle and PlanetScale

This guide assumes familiarity with:

-   **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
-   **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
-   **PlanetScale** - MySQL database platform - [read here](https://planetscale.com/)
-   **database-js** - PlanetScale serverless driver - [read here](https://github.com/planetscale/database-js)

PlanetScale also offers Postgres

important

For this tutorial, we will use the `database-js` driver to make **HTTP** calls to the PlanetScale database. If you need to connect to PlanetScale through TCP, you can refer to our [MySQL Get Started](drizzle/docs/get-started/mysql-new/index.md) page

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

#### Step 1 - Install **@planetscale/database** package[](#step-1---install-planetscaledatabase-package)

```
npm i drizzle-orm @planetscale/database dotenv
npm i -D drizzle-kit tsx
```

```
yarn add drizzle-orm @planetscale/database dotenv
yarn add -D drizzle-kit tsx
```

```
pnpm add drizzle-orm @planetscale/database dotenv
pnpm add -D drizzle-kit tsx
```

```
bun add drizzle-orm @planetscale/database dotenv
bun add -D drizzle-kit tsx
```

#### Step 2 - Setup connection variables[](#step-2---setup-connection-variables)

Create a `.env` file in the root of your project and add your database connection variable:

```plaintext
DATABASE_HOST=
DATABASE_USERNAME=
DATABASE_PASSWORD=
```

tips

To get all the necessary environment variables to connect through the `database-js` driver, you can check the [PlanetScale docs](https://planetscale.com/docs/tutorials/planetscale-serverless-driver-node-example#use-the-sample-repository)

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

Create a `index.ts` file in the `src/db` directory and initialize the connection:

```typescript
import { drizzle } from "drizzle-orm/planetscale-serverless";

const db = drizzle({ connection: {
  host: process.env.DATABASE_HOST!,
  username: process.env.DATABASE_USERNAME!,
  password: process.env.DATABASE_PASSWORD!,
}});
```

If you need to provide your existing driver

```typescript
import { drizzle } from "drizzle-orm/planetscale-serverless";
import { Client } from "@planetscale/database";

const client = new Client({
  host: process.env.DATABASE_HOST!,
  username: process.env.DATABASE_USERNAME!,
  password: process.env.DATABASE_PASSWORD!,
});

const db = drizzle({ client: client });
```

#### Step 4 - Create a table[](#step-4---create-a-table)

Create a `schema.ts` file in the `src/db` directory and declare your table:

```typescript
import { int, mysqlTable, serial, varchar } from 'drizzle-orm/mysql-core';

export const usersTable = mysqlTable('users_table', {
  id: serial().primaryKey(),
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
  dialect: 'mysql',
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
import { eq } from 'drizzle-orm';
import { drizzle } from 'drizzle-orm/planetscale-serverless';
import { usersTable } from './db/schema';

const db = drizzle({ connection: {
  host: process.env.DATABASE_HOST!,
  username: process.env.DATABASE_USERNAME!,
  password: process.env.DATABASE_PASSWORD!,
}});

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
