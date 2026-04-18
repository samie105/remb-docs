---
title: "Drizzle with Supabase Edge Functions"
source: "https://orm.drizzle.team/docs/tutorials/drizzle-with-supabase-edge-functions"
canonical_url: "https://orm.drizzle.team/docs/tutorials/drizzle-with-supabase-edge-functions"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:24:02.432Z"
content_hash: "54cbfbc3a564f5a2ce51eec6862e2fa090ae0b21e4f9d354320b1a3b7d1e2c8b"
menu_path: ["Drizzle with Supabase Edge Functions"]
section_path: []
---
To learn how to create a basic Edge Function on your local machine and then deploy it, see the [Edge Functions Quickstart](https://supabase.com/docs/guides/functions/quickstart).

#### Create a table[](#create-a-table)

Create a `schema.ts` file in your `src` directory and declare a table schema:

```
import { pgTable, serial, text, integer } from "drizzle-orm/pg-core";

export const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age').notNull()
})
```

This file will be used to generate migrations for your database.

#### Setup Drizzle config file[](#setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](https://orm.drizzle.team/kit-docs/overview) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/schema.ts",
  out: "./supabase/migrations",
  dialect: "postgresql",
});
```

In this tutorial we will use Drizzle kit to generate migrations for our schema.

#### Initialize a new Supabase project[](#initialize-a-new-supabase-project)

Create a new Supabase project in a folder on your local machine:

```
supabase init
```

It will create `supabase` folder with `config.toml` file:

```
└── supabase
    └── config.toml
```

If you are using Visual Studio Code, follow the [Supabase documentation](https://supabase.com/docs/guides/functions/local-development#deno-with-visual-studio-code) to setup settings for Deno.

#### Generate migrations[](#generate-migrations)

Run the `drizzle-kit generate` command to generate migrations:

```
npx drizzle-kit generate
```

It will create a new migration file in the `supabase/migrations` directory:

#### Apply migrations[](#apply-migrations)

To start the Supabase local development stack, run the following command:

```
supabase start
```

To apply migrations, run the following command:

```
supabase migration up
```

You can read more about Supabase migrations in the [documentation](https://supabase.com/docs/guides/deployment/database-migrations).

IMPORTANT

Don’t forget to run Docker

Alternatively, you can apply migrations using the `drizzle-kit migrate` command. Learn more about this migration process in the [documentation](https://orm.drizzle.team/docs/migrations).

#### Create a new Edge Function[](#create-a-new-edge-function)

Run the `supabase functions new [FUNCTION_NAME]` command to create a new Edge Function:

```
supabase functions new drizzle-tutorial
```

It will create a new folder with the function name in the `supabase/functions` directory:

```
└── supabase
    └── functions
    │   └── drizzle-tutorial
    │   │   ├── .npmrc ## Function-specific npm configuration (if needed)
    │   │   ├── deno.json ## Function-specific Deno configuration
    │   │   └── index.ts ## Your function code
```

When you create a new Edge Function, it will use TypeScript by default. However, it is possible write Edge Function in JavaScript. Learn more about it in the [documentation](https://supabase.com/docs/guides/functions/quickstart#not-using-typescript).

#### Setup imports[](#setup-imports)

Add the following imports to the `deno.json` file in the `supabase/functions/drizzle-tutorial` directory:

```
{
  "imports": {
    "drizzle-orm/": "npm:/drizzle-orm/",
    "postgres": "npm:postgres"
  }
}
```

You can read more about managing dependencies [here](https://supabase.com/docs/guides/functions/dependencies#managing-dependencies).

#### Copy your schema to the functions directory[](#copy-your-schema-to-the-functions-directory)

Copy the code that you will use in your edge function from `src/schema.ts` file to the `supabase/functions/drizzle-tutorial/index.ts` file:

```
// Setup type definitions for built-in Supabase Runtime APIs
import "jsr:@supabase/functions-js/edge-runtime.d.ts"
import { pgTable, serial, text, integer } from "drizzle-orm/pg-core";

const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age').notNull()
})

Deno.serve(async (req) => {
  const { name } = await req.json()
  const data = {
    message: `Hello ${name}!`,
  }

  return new Response(
    JSON.stringify(data),
    { headers: { "Content-Type": "application/json" } },
  )
})  
```

IMPORTANT

In the Deno ecosystem, each function should be treated as an independent project with its own set of dependencies and configurations. For these reasons, Supabase recommend maintaining separate configuration files (`deno.json`, `.npmrc`, or `import_map.json`) within each function’s directory, even if it means duplicating some configurations. Read more [here](https://supabase.com/docs/guides/functions/dependencies#managing-dependencies).

#### Connect Drizzle ORM to your database[](#connect-drizzle-orm-to-your-database)

Update your edge function code with your database configuration:

```
// Setup type definitions for built-in Supabase Runtime APIs
import { integer, pgTable, serial, text } from "drizzle-orm/pg-core";
import { drizzle } from "drizzle-orm/postgres-js";
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import postgres from "postgres";

const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age').notNull()
})

Deno.serve(async () => {
  const connectionString = Deno.env.get("SUPABASE_DB_URL")!;

  // Disable prefetch as it is not supported for "Transaction" pool mode
  const client = postgres(connectionString, { prepare: false });
  const db = drizzle({ client });

  await db.insert(usersTable).values({
    name: "Alice",
    age: 25
  })
  const data = await db.select().from(usersTable);

  return new Response(
    JSON.stringify(data)
  )
})
```

`SUPABASE_DB_URL` is default environment variable for the direct database connection. Learn more about managing environment variables in Supabase Edge Functions in the [documentation](https://supabase.com/docs/guides/functions/secrets).

#### Test your code locally[](#test-your-code-locally)

Run the following command to test your function locally:

```
supabase functions serve --no-verify-jwt
```

Navigate to the route `(e.g. /drizzle-tutorial)` in your browser:

```
[
  {
    "id": 1,
    "name": "Alice",
    "age": 25
  }
]
```

#### Link your local project to a hosted Supabase project[](#link-your-local-project-to-a-hosted-supabase-project)

You can create new Supabase project in the [dashboard](https://supabase.com/dashboard) or by following this [link](https://database.new/).

Copy the `Reference ID` from project settings and use it to link your local development project to a hosted Supabase project by running the following command:

```
supabase link --project-ref=<REFERENCE_ID>
```

Push your schema changes to the hosted Supabase project by running the following command:

```
supabase db push
```

#### Setup environment variables[](#setup-environment-variables)

You can find `Project connect details` by clicking **Connect** in the top bar of the dashboard and copy the URI from the `Transaction pooler` section. Remember to replace the password placeholder with your actual database password.

Read more about Connection Pooler in the [documentation](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler).

Update your edge function code to use the `DATABASE_URL` environment variable instead of `SUPABASE_DB_URL`:

```
// imports

// const connectionString = Deno.env.get("SUPABASE_DB_URL")!;
const connectionString = Deno.env.get("DATABASE_URL")!;

// code
```

Run the following command to set the environment variable:

```
supabase secrets set DATABASE_URL=<CONNECTION_STRING>
```

Learn more about managing environment variables in Supabase Edge Functions in the [documentation](https://supabase.com/docs/guides/functions/secrets).

#### Deploy your function[](#deploy-your-function)

Deploy your function by running the following command:

```
supabase functions deploy drizzle-tutorial --no-verify-jwt
```

Finally, you can use URL of the deployed project and navigate to the route you created `(e.g. /drizzle-tutorial)` to access your edge function.
