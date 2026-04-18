---
title: "Drizzle with Vercel Edge Functions"
source: "https://orm.drizzle.team/docs/tutorials/drizzle-with-vercel-edge-functions"
canonical_url: "https://orm.drizzle.team/docs/tutorials/drizzle-with-vercel-edge-functions"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:24:39.664Z"
content_hash: "074d5704f61620ac6d7694aac2be4179ab251a9d6b259dbd067ea3c8b5642096"
menu_path: ["Drizzle with Vercel Edge Functions"]
section_path: []
nav_prev: {"path": "drizzle/docs/tutorials/drizzle-with-vercel/index.md", "title": "Drizzle with Vercel Postgres"}
nav_next: {"path": "drizzle/docs/tutorials/drizzle-with-xata/index.md", "title": "Drizzle with Xata"}
---

This tutorial demonstrates how to use Drizzle ORM with [Vercel Functions](https://vercel.com/docs/functions) in [Edge runtime](https://vercel.com/docs/functions/runtimes/edge-runtime).

This guide assumes familiarity with:

*   You should have the latest version of [Vercel CLI](https://vercel.com/docs/cli#) installed.

npm

yarn

pnpm

bun

```
npm i -g vercel
```

```
yarn add -g vercel
```

```
pnpm add -g vercel
```

```
bun add -g vercel
```

*   You should have an existing Next.js project or create a new one using the following command:

```
npx create-next-app@latest --typescript
```

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

IMPORTANT

In case you face the issue with resolving dependencies during installation:

If you’re not using React Native, forcing the installation with `--force` or `--legacy-peer-deps` should resolve the issue. If you are using React Native, then you need to use the exact version of React which is compatible with your React Native version.

## Edge-compatible driver[](#edge-compatible-driver)

When using Drizzle ORM with Vercel Edge functions you have to use edge-compatible drivers because the functions run in [Edge runtime](https://vercel.com/docs/functions/runtimes/edge-runtime) not in Node.js runtime, so there are some limitations of standard Node.js APIs.

You can choose one of these drivers according to your database dialect:

*   [Neon serverless driver](drizzle/docs/get-started-postgresql/index.md#neon) allows you to query your Neon Postgres databases from serverless and edge environments over HTTP or WebSockets in place of TCP. We recommend using this driver for connecting to `Neon Postgres`.
*   [Vercel Postgres driver](drizzle/docs/get-started-postgresql/index.md#vercel-postgres) is built on top of the `Neon serverless driver`. We recommend using this driver for connecting to `Vercel Postgres`.
*   [PlanetScale serverless driver](drizzle/docs/get-started-mysql/index.md#planetscale) allows you access any `MySQL` client and execute queries over an HTTP connection, which is generally not blocked by cloud providers.
*   [libSQL client](drizzle/docs/get-started-sqlite/index.md#turso) allows you to access [Turso](https://docs.turso.tech/introduction) database.

*   Navigate directly to the [Neon Postgres](drizzle/docs/tutorials/drizzle-with-vercel-edge-functions/index.md#neon-postgres) section.
*   Navigate directly to the [Vercel Postgres](drizzle/docs/tutorials/drizzle-with-vercel-edge-functions/index.md#vercel-postgres) section.
*   Navigate directly to the [PlanetScale](drizzle/docs/tutorials/drizzle-with-vercel-edge-functions/index.md#planetscale) section.
*   Navigate directly to the [Turso](drizzle/docs/tutorials/drizzle-with-vercel-edge-functions/index.md#turso) section.

### Neon Postgres[](#neon-postgres)

#### Install the `@neondatabase/serverless` driver[](#install-the-neondatabaseserverless-driver)

Install the `@neondatabase/serverless` driver:

npm

yarn

pnpm

bun

```
npm i @neondatabase/serverless
```

```
yarn add @neondatabase/serverless
```

```
pnpm add @neondatabase/serverless
```

```
bun add @neondatabase/serverless
```

#### Create a table[](#create-a-table)

Create a `schema.ts` file in the `src/db` directory and declare a table schema:

```
import { pgTable, serial, text } from "drizzle-orm/pg-core";

export const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: text('age').notNull(),
  email: text('email').notNull().unique(),
})
```

#### Setup Drizzle config file[](#setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/db/schema.ts",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.POSTGRES_URL!,
  },
});
```

Configure your database connection string in the `.env` file:

```
POSTGRES_URL="postgres://[user]:[password]@[host]-[region].aws.neon.tech:5432/[db-name]?sslmode=[ssl-mode]"
```

#### Applying changes to the database[](#applying-changes-to-the-database)

You can generate migrations using `drizzle-kit generate` command and then run them using the `drizzle-kit migrate` command.

Generate migrations:

```
npx drizzle-kit generate
```

These migrations are stored in the `drizzle` directory, as specified in your `drizzle.config.ts`. This directory will contain the SQL files necessary to update your database schema and a `meta` folder for storing snapshots of the schema at different migration stages.

Example of a generated migration:

```
CREATE TABLE IF NOT EXISTS "users_table" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" text NOT NULL,
	"age" text NOT NULL,
	"email" text NOT NULL,
	CONSTRAINT "users_table_email_unique" UNIQUE("email")
);
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

#### Connect Drizzle ORM to your database[](#connect-drizzle-orm-to-your-database)

Create a `index.ts` file in the `src/db` directory and set up your database configuration:

```
import { drizzle } from 'drizzle-orm/neon-serverless';

export const db = drizzle(process.env.POSTGRES_URL!)
```

#### Create an API route[](#create-an-api-route)

Create `route.ts` file in `src/app/api/hello` directory. To learn more about how to write a function, see the [Functions API Reference](https://vercel.com/docs/functions/functions-api-reference) and [Vercel Functions Quickstart](https://vercel.com/docs/functions/quickstart).

```
import { db } from "@/db";
import { usersTable } from "@/db/schema";
import { NextResponse } from "next/server";

export const dynamic = 'force-dynamic'; // static by default, unless reading the request
export const runtime = 'edge' // specify the runtime to be edge

export async function GET(request: Request) {
  const users = await db.select().from(usersTable)

  return NextResponse.json({ users, message: 'success' });
}
```

#### Test your code locally[](#test-your-code-locally)

Run the `next dev` command to start your local development server:

```
npx next dev
```

Navigate to the route you created `(e.g. /api/hello)` in your browser:

```
{
  "users": [],
  "message": "success"
}
```

#### Deploy your project[](#deploy-your-project)

Create a new project in the [dashboard](https://vercel.com/new) or run the `vercel` command to deploy your project:

```
vercel
```

Add `POSTGRES_URL` environment variable:

```
vercel env add POSTGRES_URL
```

Redeploy your project to update your environment variables:

```
vercel
```

Finally, you can use URL of the deployed project and navigate to the route you created `(e.g. /api/hello)` to access your edge function.

### Vercel Postgres[](#vercel-postgres)

You can check quickstart guide for Drizzle with Vercel Postgres client in the [documentation](drizzle/docs/get-started-postgresql/index.md#vercel-postgres).

#### Install the `@vercel/postgres` driver[](#install-the-vercelpostgres-driver)

Install the `@vercel/postgres` driver:

npm

yarn

pnpm

bun

```
npm i @vercel/postgres
```

```
yarn add @vercel/postgres
```

```
pnpm add @vercel/postgres
```

```
bun add @vercel/postgres
```

#### Create a table[](#create-a-table-1)

Create a `schema.ts` file in the `src/db` directory and declare a table schema:

```
import { pgTable, serial, text } from "drizzle-orm/pg-core";

export const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: text('age').notNull(),
  email: text('email').notNull().unique(),
})
```

#### Setup Drizzle config file[](#setup-drizzle-config-file-1)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/db/schema.ts",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.POSTGRES_URL!,
  },
});
```

Configure your database connection string in the `.env` file:

```
POSTGRES_URL="postgres://[user]:[password]@[host]-[region].aws.neon.tech:5432/[db-name]?sslmode=[ssl-mode]"
```

#### Applying changes to the database[](#applying-changes-to-the-database-1)

You can generate migrations using `drizzle-kit generate` command and then run them using the `drizzle-kit migrate` command.

Generate migrations:

```
npx drizzle-kit generate
```

These migrations are stored in the `drizzle` directory, as specified in your `drizzle.config.ts`. This directory will contain the SQL files necessary to update your database schema and a `meta` folder for storing snapshots of the schema at different migration stages.

Example of a generated migration:

```
CREATE TABLE IF NOT EXISTS "users_table" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" text NOT NULL,
	"age" text NOT NULL,
	"email" text NOT NULL,
	CONSTRAINT "users_table_email_unique" UNIQUE("email")
);
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

#### Connect Drizzle ORM to your database[](#connect-drizzle-orm-to-your-database-1)

Create a `index.ts` file in the `src/db` directory and set up your database configuration:

```
import { drizzle } from 'drizzle-orm/vercel-postgres';

export const db = drizzle()
```

#### Create an API route[](#create-an-api-route-1)

Create `route.ts` in `src/app/api/hello` directory. To learn more about how to write a function, see the [Functions API Reference](https://vercel.com/docs/functions/functions-api-reference) and [Vercel Functions Quickstart](https://vercel.com/docs/functions/quickstart).

```

import { db } from "@/db";
import { usersTable } from "@/db/schema";
import { NextResponse } from "next/server";

export const dynamic = 'force-dynamic'; // static by default, unless reading the request
export const runtime = 'edge' // specify the runtime to be edge

export async function GET(request: Request) {
  const users = await db.select().from(usersTable)

  return NextResponse.json({ users, message: 'success' });
}
```

#### Test your code locally[](#test-your-code-locally-1)

Run the `next dev` command to start your local development server:

```
npx next dev
```

Navigate to the route you created `(e.g. /api/hello)` in your browser:

```
{
  "users": [],
  "message": "success"
}
```

#### Deploy your project[](#deploy-your-project-1)

Create a new project in the [dashboard](https://vercel.com/new) or run the `vercel` command to deploy your project:

```
vercel
```

Add `POSTGRES_URL` environment variable:

```
vercel env add POSTGRES_URL
```

Redeploy your project to update your environment variables:

```
vercel
```

Finally, you can use URL of the deployed project and navigate to the route you created `(e.g. /api/hello)` to access your edge function.

### PlanetScale[](#planetscale)

In this tutorial we use [PlanetScale MySQL](https://planetscale.com/).

#### Install the `@planetscale/database` driver[](#install-the-planetscaledatabase-driver)

Install the `@planetscale/database` driver:

npm

yarn

pnpm

bun

```
npm i @planetscale/database
```

```
yarn add @planetscale/database
```

```
pnpm add @planetscale/database
```

```
bun add @planetscale/database
```

#### Create a table[](#create-a-table-2)

Create a `schema.ts` file in the `src/db` directory and declare a table schema:

```
import { mysqlTable, serial, text } from "drizzle-orm/mysql-core";

export const usersTable = mysqlTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: text('age').notNull(),
  email: text('email').notNull().unique(),
})
```

#### Setup Drizzle config file[](#setup-drizzle-config-file-2)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/db/schema.ts",
  dialect: "mysql",
  dbCredentials: {
    url: process.env.MYSQL_URL!,
  },
});
```

Configure your database connection string in the `.env` file:

```
MYSQL_URL="mysql://[user]:[password]@[host].[region].psdb.cloud/[db-name]?ssl={'rejectUnauthorized':[ssl-rejectUnauthorized]}"
```

#### Applying changes to the database[](#applying-changes-to-the-database-2)

You can generate migrations using `drizzle-kit generate` command and then run them using the `drizzle-kit migrate` command.

Generate migrations:

```
npx drizzle-kit generate
```

These migrations are stored in the `drizzle` directory, as specified in your `drizzle.config.ts`. This directory will contain the SQL files necessary to update your database schema and a `meta` folder for storing snapshots of the schema at different migration stages.

Example of a generated migration:

```
CREATE TABLE `users_table` (
	`id` serial AUTO_INCREMENT NOT NULL,
	`name` text NOT NULL,
	`age` text NOT NULL,
	`email` text NOT NULL,
	CONSTRAINT `users_table_id` PRIMARY KEY(`id`),
	CONSTRAINT `users_table_email_unique` UNIQUE(`email`)
);
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

#### Connect Drizzle ORM to your database[](#connect-drizzle-orm-to-your-database-2)

Create a `index.ts` file in the `src/db` directory and set up your database configuration:

```
import { drizzle } from "drizzle-orm/planetscale-serverless";

export const db = drizzle(process.env.MYSQL_URL!)
```

#### Create an API route[](#create-an-api-route-2)

Create `route.ts` in `src/app/api/hello` directory. To learn more about how to write a function, see the [Functions API Reference](https://vercel.com/docs/functions/functions-api-reference) and [Vercel Functions Quickstart](https://vercel.com/docs/functions/quickstart).

```
import { db } from "@/app/db/db";
import { usersTable } from "@/app/db/schema";
import { NextResponse } from "next/server";

export const dynamic = 'force-dynamic'; // static by default, unless reading the request
export const runtime = 'edge' // specify the runtime to be edge

export async function GET(request: Request) {
  const users = await db.select().from(usersTable)

  return NextResponse.json({ users, message: 'success' });
}
```

#### Test your code locally[](#test-your-code-locally-2)

Run the `next dev` command to start your local development server:

```
npx next dev
```

Navigate to the route you created `(e.g. /api/hello)` in your browser:

```
{
  "users": [],
  "message": "success"
}
```

#### Deploy your project[](#deploy-your-project-2)

Create a new project in the [dashboard](https://vercel.com/new) or run the `vercel` command to deploy your project:

```
vercel
```

Add `MYSQL_URL` environment variable:

```
vercel env add MYSQL_URL
```

Redeploy your project to update your environment variables:

```
vercel
```

Finally, you can use URL of the deployed project and navigate to the route you created `(e.g. /api/hello)` to access your edge function.

### Turso[](#turso)

You can check [quickstart guide](drizzle/docs/get-started-sqlite/index.md#turso) or [tutorial](drizzle/docs/tutorials/drizzle-with-turso/index.md) for Drizzle with Turso in the documentation.

#### Install the `@libsql/client` driver[](#install-the-libsqlclient-driver)

Install the `@libsql/client` driver:

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

#### Create a table[](#create-a-table-3)

Create a `schema.ts` file in the `src/db` directory and declare a table schema:

```
import { integer, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const usersTable = sqliteTable('users_table', {
  id: integer('id').primaryKey(),
  name: text('name').notNull(),
  age: text('age').notNull(),
  email: text('email').notNull().unique(),
})
```

#### Setup Drizzle config file[](#setup-drizzle-config-file-3)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/db/schema.ts",
  dialect: "turso",
  dbCredentials: {
    url: process.env.TURSO_CONNECTION_URL!,
    authToken: process.env.TURSO_AUTH_TOKEN!,
  },
});
```

Configure your database connection string and auth token in the `.env` file:

```
TURSO_CONNECTION_URL="libsql://[db-name].turso.io"
TURSO_AUTH_TOKEN="[auth-token]"
```

#### Applying changes to the database[](#applying-changes-to-the-database-3)

You can generate migrations using `drizzle-kit generate` command and then run them using the `drizzle-kit migrate` command.

Generate migrations:

```
npx drizzle-kit generate
```

These migrations are stored in the `drizzle` directory, as specified in your `drizzle.config.ts`. This directory will contain the SQL files necessary to update your database schema and a `meta` folder for storing snapshots of the schema at different migration stages.

Example of a generated migration:

```
CREATE TABLE `users_table` (
	`id` integer PRIMARY KEY NOT NULL,
	`name` text NOT NULL,
	`age` text NOT NULL,
	`email` text NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `users_table_email_unique` ON `users_table` (`email`);
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

#### Connect Drizzle ORM to your database[](#connect-drizzle-orm-to-your-database-3)

Create a `index.ts` file in the `src/db` directory and set up your database configuration:

```
import { drizzle } from 'drizzle-orm/libsql';

export const db = drizzle({ connection: {
  url: process.env.TURSO_CONNECTION_URL!,
  authToken: process.env.TURSO_AUTH_TOKEN!,
}})
```

#### Create an API route[](#create-an-api-route-3)

Create `route.ts` in `src/app/api/hello` directory. To learn more about how to write a function, see the [Functions API Reference](https://vercel.com/docs/functions/functions-api-reference) and [Vercel Functions Quickstart](https://vercel.com/docs/functions/quickstart).

```
import { db } from "@/app/db/db";
import { usersTable } from "@/app/db/schema";
import { NextResponse } from "next/server";

export const dynamic = 'force-dynamic'; // static by default, unless reading the request
export const runtime = 'edge' // specify the runtime to be edge

export async function GET(request: Request) {
  const users = await db.select().from(usersTable)

  return NextResponse.json({ users, message: 'success' });
}
```

#### Test your code locally[](#test-your-code-locally-3)

Run the `next dev` command to start your local development server:

```
npx next dev
```

Navigate to the route you created `(e.g. /api/hello)` in your browser:

```
{
  "users": [],
  "message": "success"
}
```

#### Deploy your project[](#deploy-your-project-3)

Create a new project in the [dashboard](https://vercel.com/new) or run the `vercel` command to deploy your project:

```
vercel
```

Add `TURSO_CONNECTION_URL` environment variable:

```
vercel env add TURSO_CONNECTION_URL
```

Add `TURSO_AUTH_TOKEN` environment variable:

```
vercel env add TURSO_AUTH_TOKEN
```

Redeploy your project to update your environment variables:

```
vercel
```

Finally, you can use URL of the deployed project and navigate to the route you created `(e.g. /api/hello)` to access your edge function.
