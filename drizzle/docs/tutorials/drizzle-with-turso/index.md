---
title: "Drizzle with Turso"
source: "https://orm.drizzle.team/docs/tutorials/drizzle-with-turso"
canonical_url: "https://orm.drizzle.team/docs/tutorials/drizzle-with-turso"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:24:26.223Z"
content_hash: "3b0970dcc35119bd31de98622397a0ef02afed5e7380cf1c03bf36ace0d3d6bc"
menu_path: ["Drizzle with Turso"]
section_path: []
nav_prev: {"path": "drizzle/docs/tutorials/drizzle-with-supabase/index.md", "title": "Drizzle with Supabase Database"}
nav_next: {"path": "drizzle/docs/tutorials/drizzle-with-vercel/index.md", "title": "Drizzle with Vercel Postgres"}
---

This tutorial demonstrates how to use Drizzle ORM with [Turso](https://docs.turso.tech/introduction).

This guide assumes familiarity with:

*   You should have installed Drizzle ORM and [Drizzle kit](drizzle/docs/kit-overview/index.md). You can do this by running the following command:

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

*   You should have installed `dotenv` package for managing environment variables. Read more about this package [here](https://www.npmjs.com/package/dotenv)

npm

yarn

pnpm

bun

```
npm i dotenv
```

```
yarn add dotenv
```

```
pnpm add dotenv
```

```
bun add dotenv
```

*   You should have installed `@libsql/client` package. Read more about this package [here](https://www.npmjs.com/package/@libsql/client).

npm

yarn

pnpm

bun

```
npm i @libsql/client
```

```
yarn add @libsql/client
```

```
pnpm add @libsql/client
```

```
bun add @libsql/client
```

*   You should have installed Turso CLI. Check [documentation](https://docs.turso.tech/cli/introduction) for more information

[Turso](https://docs.turso.tech/concepts) is a SQLite-compatible database built on [libSQL](https://docs.turso.tech/libsql), the Open Contribution fork of SQLite. It enables scaling to hundreds of thousands of databases per organization and supports replication to any location, including your own servers, for microsecond-latency access. You can read more about Turso’s concepts [here](https://docs.turso.tech/concepts).

Drizzle ORM natively supports libSQL driver. We embrace SQL dialects and dialect specific drivers and syntax and mirror most popular SQLite-like `all`, `get`, `values` and `run` query methods syntax.

Check [official documentation](https://docs.turso.tech/quickstart) to setup Turso database.

## Setup Turso and Drizzle ORM[](#setup-turso-and-drizzle-orm)

#### Signup or login to Turso[](#signup-or-login-to-turso)

Signup:

```
turso auth signup
```

Login:

```
turso auth login
```

#### Create new database[](#create-new-database)

Create new database by running the `turso db create <DATABASE_NAME>` command:

```
turso db create drizzle-turso-db
```

To see information about the database, run the following command:

```
turso db show drizzle-turso-db
```

#### Create an authentication token[](#create-an-authentication-token)

To create an authentication token for your database, run the following command:

```
turso db tokens create drizzle-turso-db
```

Learn more about this command and its options in the [documentation](https://docs.turso.tech/cli/db/tokens/create).

#### Update environment variables[](#update-environment-variables)

Update your `.env` or `.env.local` file with connection url and authentication token.

```
TURSO_CONNECTION_URL=
TURSO_AUTH_TOKEN=
```

#### Connect Drizzle ORM to your database[](#connect-drizzle-orm-to-your-database)

Create a `index.ts` file in the `src/db` directory and set up your database configuration:

```
import { config } from 'dotenv';
import { drizzle } from 'drizzle-orm/libsql';

config({ path: '.env' }); // or .env.local

export const db = drizzle({ connection: {
  url: process.env.TURSO_CONNECTION_URL!,
  authToken: process.env.TURSO_AUTH_TOKEN!,
}});
```

#### Create tables[](#create-tables)

Create a `schema.ts` file in the `src/db` directory and declare your tables:

```
import { sql } from 'drizzle-orm';
import { integer, sqliteTable, text } from 'drizzle-orm/sqlite-core';

export const usersTable = sqliteTable('users', {
  id: integer('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age').notNull(),
  email: text('email').unique().notNull(),
});

export const postsTable = sqliteTable('posts', {
  id: integer('id').primaryKey(),
  title: text('title').notNull(),
  content: text('content').notNull(),
  userId: integer('user_id')
    .notNull()
    .references(() => usersTable.id, { onDelete: 'cascade' }),
  createdAt: text('created_at')
    .default(sql`(CURRENT_TIMESTAMP)`)
    .notNull(),
  updatedAt: integer('updated_at', { mode: 'timestamp' }).$onUpdate(() => new Date()),
});

export type InsertUser = typeof usersTable.$inferInsert;
export type SelectUser = typeof usersTable.$inferSelect;

export type InsertPost = typeof postsTable.$inferInsert;
export type SelectPost = typeof postsTable.$inferSelect;
```

#### Setup Drizzle config file[](#setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import { config } from 'dotenv';
import { defineConfig } from 'drizzle-kit';

config({ path: '.env' });

export default defineConfig({
  schema: './src/db/schema.ts',
  out: './migrations',
  dialect: 'turso',
  dbCredentials: {
    url: process.env.TURSO_CONNECTION_URL!,
    authToken: process.env.TURSO_AUTH_TOKEN!,
  },
});
```

#### Applying changes to the database[](#applying-changes-to-the-database)

You can generate migrations using `drizzle-kit generate` command and then run them using the `drizzle-kit migrate` command.

Generate migrations:

```
npx drizzle-kit generate
```

These migrations are stored in the `migrations` directory, as specified in your `drizzle.config.ts`. This directory will contain the SQL files necessary to update your database schema and a `meta` folder for storing snapshots of the schema at different migration stages.

Example of a generated migration:

```
CREATE TABLE `posts` (
	`id` integer PRIMARY KEY NOT NULL,
	`title` text NOT NULL,
	`content` text NOT NULL,
	`user_id` integer NOT NULL,
	`created_at` text DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
	`updated_at` integer,
	FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON UPDATE no action ON DELETE cascade
);
--> statement-breakpoint
CREATE TABLE `users` (
	`id` integer PRIMARY KEY NOT NULL,
	`name` text NOT NULL,
	`age` integer NOT NULL,
	`email` text NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `users_email_unique` ON `users` (`email`);
```

Run migrations:

```
npx drizzle-kit migrate
```

Alternatively, you can push changes directly to the database using [Drizzle kit push command](drizzle/docs/kit-overview/index.md#prototyping-with-db-push):

```
npx drizzle-kit push
```

IMPORTANT

Push command is good for situations where you need to quickly test new schema designs or changes in a local development environment, allowing for fast iterations without the overhead of managing migration files.

### Basic file structure[](#basic-file-structure)

This is the basic file structure of the project. In the `src/db` directory, we have database-related files including connection in `index.ts` and schema definitions in `schema.ts`.

```
📦 <project root>
 ├ 📂 src
 │   ├ 📂 db
 │   │  ├ 📜 index.ts
 │   │  └ 📜 schema.ts
 ├ 📂 migrations
 │  ├ 📂 meta
 │  │  ├ 📜 _journal.json
 │  │  └ 📜 0000_snapshot.json
 │  └ 📜 0000_watery_spencer_smythe.sql
 ├ 📜 .env
 ├ 📜 drizzle.config.ts
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

## Query examples[](#query-examples)

For instance, we create `src/db/queries` folder and separate files for each operation: insert, select, update, delete.

#### Insert data[](#insert-data)

Read more about insert query in the [documentation](drizzle/docs/insert/index.md).

```
import { db } from '../index';
import { InsertPost, InsertUser, postsTable, usersTable } from '../schema';

export async function createUser(data: InsertUser) {
  await db.insert(usersTable).values(data);
}

export async function createPost(data: InsertPost) {
  await db.insert(postsTable).values(data);
}
```

#### Select data[](#select-data)

Read more about select query in the [documentation](drizzle/docs/select/index.md).

IMPORTANT

`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](drizzle/docs/upgrade-v1/index.md))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`

```
import { asc, count, eq, getColumns, gt, sql } from 'drizzle-orm';
import { db } from '../index';
import { SelectUser, postsTable, usersTable } from '../schema';

export async function getUserById(id: SelectUser['id']): Promise<
  Array<{
    id: number;
    name: string;
    age: number;
    email: string;
  }>
> {
  return db.select().from(usersTable).where(eq(usersTable.id, id));
}

export async function getUsersWithPostsCount(
  page = 1,
  pageSize = 5,
): Promise<
  Array<{
    postsCount: number;
    id: number;
    name: string;
    age: number;
    email: string;
  }>
> {
  return db
    .select({
      ...getColumns(usersTable),
      postsCount: count(postsTable.id),
    })
    .from(usersTable)
    .leftJoin(postsTable, eq(usersTable.id, postsTable.userId))
    .groupBy(usersTable.id)
    .orderBy(asc(usersTable.id))
    .limit(pageSize)
    .offset((page - 1) * pageSize);
}

export async function getPostsForLast24Hours(
  page = 1,
  pageSize = 5,
): Promise<
  Array<{
    id: number;
    title: string;
  }>
> {
  return db
    .select({
      id: postsTable.id,
      title: postsTable.title,
    })
    .from(postsTable)
    .where(gt(postsTable.createdAt, sql`(datetime('now','-24 hour'))`))
    .orderBy(asc(postsTable.title), asc(postsTable.id))
    .limit(pageSize)
    .offset((page - 1) * pageSize);
}
```

Alternatively, you can use [relational query syntax](drizzle/docs/rqb/index.md).

#### Update data[](#update-data)

Read more about update query in the [documentation](drizzle/docs/update/index.md).

```
import { eq } from 'drizzle-orm';
import { db } from '../index';
import { SelectPost, postsTable } from '../schema';

export async function updatePost(id: SelectPost['id'], data: Partial<Omit<SelectPost, 'id'>>) {
  await db.update(postsTable).set(data).where(eq(postsTable.id, id));
}
```

#### Delete data[](#delete-data)

Read more about delete query in the [documentation](drizzle/docs/delete/index.md).

```
import { eq } from 'drizzle-orm';
import { db } from '../index';
import { SelectUser, usersTable } from '../schema';

export async function deleteUser(id: SelectUser['id']) {
  await db.delete(usersTable).where(eq(usersTable.id, id));
}
```
