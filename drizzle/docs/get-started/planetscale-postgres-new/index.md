---
title: "Get Started with Drizzle and PlanetScale Postgres"
source: "https://orm.drizzle.team/docs/get-started/planetscale-postgres-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/planetscale-postgres-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:20.574Z"
content_hash: "2606fca3810aa70a96573b9c241c7d0ccff1c621dc12c92e0540796e0d0132ba"
menu_path: ["Get Started with Drizzle and PlanetScale Postgres"]
section_path: []
nav_prev: {"path": "drizzle/docs/get-started/planetscale-new/index.md", "title": "Get Started with Drizzle and PlanetScale"}
nav_next: {"path": "drizzle/docs/get-started/planetscale-postgres-existing/index.md", "title": "Get Started with Drizzle and PlanetScale Postgres in existing project"}
---

## Get Started with Drizzle and PlanetScale Postgres

This guide assumes familiarity with:

*   **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
*   **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
*   **PlanetScale Postgres** - PostgreSQL database platform - [read here](https://planetscale.com/docs/postgres)
*   **node-postgres** - package for querying your PostgreSQL database - [read here](https://node-postgres.com/)

PlanetScale also offers MySQL

PlanetScale offers both MySQL (Vitess) and PostgreSQL databases. This guide covers connecting to PlanetScale Postgres using the standard `node-postgres` driver.

For detailed instructions on creating a PlanetScale Postgres database and obtaining credentials, see the [PlanetScale Postgres documentation](https://planetscale.com/docs/postgres/tutorials/planetscale-postgres-drizzle).

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

#### Step 1 - Install **node-postgres** package[](#step-1---install-node-postgres-package)

npm

yarn

pnpm

bun

```
npm i drizzle-orm pg dotenv
npm i -D drizzle-kit tsx @types/pg
```

```
yarn add drizzle-orm pg dotenv
yarn add -D drizzle-kit tsx @types/pg
```

```
pnpm add drizzle-orm pg dotenv
pnpm add -D drizzle-kit tsx @types/pg
```

```
bun add drizzle-orm pg dotenv
bun add -D drizzle-kit tsx @types/pg
```

#### Step 2 - Setup connection variables[](#step-2---setup-connection-variables)

Create a `.env` file in the root of your project and add your database connection variable:

```
DATABASE_URL=postgresql://{username}:{password}@{host}:{port}/postgres?sslmode=verify-full
```

tips

You can obtain your connection credentials from the PlanetScale dashboard by navigating to your database, clicking **“Connect”**, and creating a **“Default role”**. See the [PlanetScale connection guide](https://planetscale.com/docs/postgres/tutorials/planetscale-postgres-drizzle#create-credentials-and-connect) for detailed steps.

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

Create a `index.ts` file in the `src` directory and initialize the connection:

node-postgres

node-postgres with config

your node-postgres driver

```
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/node-postgres';

const db = drizzle(process.env.DATABASE_URL!);
```

```
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/node-postgres';

// You can specify any property from the node-postgres connection options
const db = drizzle({ 
  connection: { 
    connectionString: process.env.DATABASE_URL!,
    ssl: true
  }
});
```

```
import 'dotenv/config';
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL!,
});
const db = drizzle({ client: pool });
```

Connection ports

PlanetScale Postgres supports two connection ports:

*   **Port 5432** — Direct connection to PostgreSQL. Total connections are limited by your cluster’s `max_connections` setting.
*   **Port 6432** — Connection via PgBouncer for connection pooling. Recommended when you have many simultaneous connections.

#### Step 4 - Create a table[](#step-4---create-a-table)

Create a `schema.ts` file in the `src/db` directory and declare your table:

```
import { integer, pgTable, varchar } from "drizzle-orm/pg-core";

export const usersTable = pgTable("users", {
  id: integer().primaryKey().generatedAlwaysAsIdentity(),
  name: varchar({ length: 255 }).notNull(),
  age: integer().notNull(),
  email: varchar({ length: 255 }).notNull().unique(),
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
  dialect: 'postgresql',
  dbCredentials: {
    url: process.env.DATABASE_URL!,
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
import { drizzle } from 'drizzle-orm/node-postgres';
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


