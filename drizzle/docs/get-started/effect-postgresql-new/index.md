---
title: "Get Started with Drizzle and Effect PostgreSQL"
source: "https://orm.drizzle.team/docs/get-started/effect-postgresql-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/effect-postgresql-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:36.221Z"
content_hash: "142d2b9b05fdd889fd5b9d29215d49241b0d850f72727f9724762a8b5577dca4"
menu_path: ["Get Started with Drizzle and Effect PostgreSQL"]
section_path: []
nav_prev: {"path": "drizzle/docs/get-started/expo-new/index.md", "title": "Get Started with Drizzle and Expo"}
nav_next: {"path": "drizzle/docs/get-started/gel-existing/index.md", "title": "Get Started with Drizzle and Gel in existing project"}
---

## Get Started with Drizzle and Effect PostgreSQL

WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.13` and higher.

Effect is only available for PostgreSQL right now and soon be implemented for all other dialects

On how to upgrade (read more [here](drizzle/docs/upgrade-v1/index.md))

This guide assumes familiarity with:

*   **Effect** - Effect is a powerful TS library designed to help developers easily create complex, synchronous, and asynchronous programs. - [read more](https://effect.website/docs)
*   **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
*   **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
*   **@effect/sql-pg** - A PostgreSQL toolkit for Effect - [read here](https://effect-ts.github.io/effect/docs/sql-pg)

Drizzle has native support for Effect PostgreSQL connections with the `@effect/sql-pg` driver.

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
npm i drizzle-orm effect @effect/sql-pg pg dotenv
npm i -D drizzle-kit tsx @types/pg
```

```
yarn add drizzle-orm effect @effect/sql-pg pg dotenv
yarn add -D drizzle-kit tsx @types/pg
```

```
pnpm add drizzle-orm effect @effect/sql-pg pg dotenv
pnpm add -D drizzle-kit tsx @types/pg
```

```
bun add drizzle-orm effect @effect/sql-pg pg dotenv
bun add -D drizzle-kit tsx @types/pg
```

#### Step 2 - Setup connection variables[](#step-2---setup-connection-variables)

Create a `.env` file in the root of your project and add your database connection variable:

```
DATABASE_URL=
```

tips

If you don’t have a PostgreSQL database yet and want to create one for testing, you can use our guide on how to set up PostgreSQL in Docker.

The PostgreSQL in Docker guide is available [here](drizzle/docs/guides/postgresql-local-setup/index.md). Go set it up, generate a database URL (explained in the guide), and come back for the next steps

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

Create a `index.ts` file in the `src` directory and initialize the connection:

```
import 'dotenv/config';
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { PgClient } from '@effect/sql-pg';
import * as Effect from 'effect/Effect';
import * as Redacted from 'effect/Redacted';
import { types } from 'pg';

// Configure the PgClient layer with type parsers
const PgClientLive = PgClient.layer({
  url: Redacted.make(process.env.DATABASE_URL!),
  types: {
    getTypeParser: (typeId, format) => {
      // Return raw values for date/time types to let Drizzle handle parsing
      if ([1184, 1114, 1082, 1186, 1231, 1115, 1185, 1187, 1182].includes(typeId)) {
        return (val: any) => val;
      }
      return types.getTypeParser(typeId, format);
    },
  },
});

const program = Effect.gen(function*() {
  // Create the database with default services
  const db = yield* PgDrizzle.makeWithDefaults();

  // Your queries here...
});

// Run the program with the PgClient layer
Effect.runPromise(program.pipe(Effect.provide(PgClientLive)));
```

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
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { PgClient } from '@effect/sql-pg';
import * as Effect from 'effect/Effect';
import * as Redacted from 'effect/Redacted';
import { types } from 'pg';
import { eq } from 'drizzle-orm';
import { usersTable } from './db/schema';

const PgClientLive = PgClient.layer({
  url: Redacted.make(process.env.DATABASE_URL!),
  types: {
    getTypeParser: (typeId, format) => {
      if ([1184, 1114, 1082, 1186, 1231, 1115, 1185, 1187, 1182].includes(typeId)) {
        return (val: any) => val;
      }
      return types.getTypeParser(typeId, format);
    },
  },
});

const program = Effect.gen(function*() {
  const db = yield* PgDrizzle.makeWithDefaults();

  const user: typeof usersTable.$inferInsert = {
    name: 'John',
    age: 30,
    email: 'john@example.com',
  };

  yield* db.insert(usersTable).values(user);
  console.log('New user created!')

  const users = yield* db.select().from(usersTable);
  console.log('Getting all users from the database: ', users)
  /*
  const users: {
    id: number;
    name: string;
    age: number;
    email: string;
  }[]
  */

  yield* db
    .update(usersTable)
    .set({
      age: 31,
    })
    .where(eq(usersTable.email, user.email));
  console.log('User info updated!')

  yield* db.delete(usersTable).where(eq(usersTable.email, user.email));
  console.log('User deleted!')
});

Effect.runPromise(program.pipe(Effect.provide(PgClientLive)));
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


