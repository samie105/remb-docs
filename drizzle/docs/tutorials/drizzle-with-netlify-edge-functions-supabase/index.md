---
title: "Drizzle with Netlify Edge Functions and Supabase Database"
source: "https://orm.drizzle.team/docs/tutorials/drizzle-with-netlify-edge-functions-supabase"
canonical_url: "https://orm.drizzle.team/docs/tutorials/drizzle-with-netlify-edge-functions-supabase"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:23:27.499Z"
content_hash: "fc954875671fe1a3291bda95027646c3b80fc3f2ea94e2483f21b7bd8e3a9a9b"
menu_path: ["Drizzle with Netlify Edge Functions and Supabase Database"]
section_path: []
---
#### Create a new Supabase project[](#create-a-new-supabase-project)

You can create new Supabase project in the [dashboard](https://supabase.com/dashboard) or by following this [link](https://database.new/).

#### Setup connection string variable[](#setup-connection-string-variable)

You can find `Project connect details` by clicking **Connect** in the top bar of the dashboard and copy the URI from the `Transaction pooler` section. Remember to replace the password placeholder with your actual database password.

Add `DATABASE_URL` variable to your `.env` file.

```
DATABASE_URL=<YOUR_DATABASE_URL>
```

Read more about connecting to Supabase Database in the [documentation](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler).

#### Setup Netlify Edge Functions[](#setup-netlify-edge-functions)

Create `netlify/edge-functions` directory in the root of your project. This is where you’ll store your Edge Functions.

Create a function `user.ts` in the `netlify/edge-functions` directory.

```
import type { Context } from "@netlify/edge-functions";

export default async (request: Request, context: Context) => {
  return new Response("User data");
};
```

IMPORTANT

The types for the `Request` and `Response` objects are in the global scope.

#### Setup imports[](#setup-imports)

Create a `import_map.json` file in the root of your project and add the following content:

```
{
  "imports": {
    "drizzle-orm/": "https://esm.sh/drizzle-orm/",
    "postgres": "https://esm.sh/postgres"
  }
}
```

Read more about `import_map.json` in Netlify Edge Functions [here](https://docs.netlify.com/edge-functions/api/#import-maps).

#### Create a Netlify configuration file[](#create-a-netlify-configuration-file)

Create a `netlify.toml` file in the root of your project and add the following content:

```
[functions]
  deno_import_map = "./import_map.json"

[[edge_functions]]
  path = "/user"
  function = "user"
```

This configuration tells Netlify to use the `import_map.json` file for Deno imports and to route requests to the `/user` path to the `user.ts` function. Read more about `netlify.toml` [here](https://docs.netlify.com/configure-builds/file-based-configuration/).

#### Create a table[](#create-a-table)

Create a `schema.ts` file in the `netlify/edge-functions/common` directory and declare a table schema:

```
import { pgTable, serial, text, integer } from "drizzle-orm/pg-core";

export const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age').notNull(),
  email: text('email').notNull().unique(),
})
```

#### Setup Drizzle config file[](#setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](https://orm.drizzle.team/docs/kit-overview) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import 'dotenv/config'; // remove this line if you use Node.js v20.6.0 or later
import type { Config } from "drizzle-kit";

export default {
  schema: './netlify/edge-functions/common/schema.ts',
  out: './drizzle',
  dialect: 'postgresql',
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
} satisfies Config;
```

In this tutorial we will use Drizzle kit to push changes to the Neon database.

#### Apply changes to the database[](#apply-changes-to-the-database)

```
npx drizzle-kit push
```

IMPORTANT

Push command is good for situations where you need to quickly test new schema designs or changes in a local development environment, allowing for fast iterations without the overhead of managing migration files.

Alternatively, you can use migrations workflow. Read about it here: [Migrations](https://orm.drizzle.team/docs/migrations).

#### Connect Drizzle ORM to your database[](#connect-drizzle-orm-to-your-database)

Update your `netlify/edge-functions/user.ts` file and set up your database configuration:

```
import type { Context } from "@netlify/edge-functions";
import { usersTable } from "./common/schema.ts";
import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';

export default async (request: Request, context: Context) => {
  const queryClient = postgres(Netlify.env.get("DATABASE_URL")!);
  const db = drizzle({ client: queryClient });

  const users = await db.select().from(usersTable);

  return new Response(JSON.stringify(users));
};
```

IMPORTANT

You might see a red underline under the imports if you’re using VS Code. The Edge Function will still execute. To get rid of the red underline, you can configure VS Code to use Edge Functions in the next step.

#### Test your code locally[](#test-your-code-locally)

Run the following command to start the Netlify dev server:

```
netlify dev
```

When you first run the command it will suggest to configure VS Code to use Edge Functions. Click `Yes` to configure it. `settings.json` file will be created in the `.vscode` directory. If you still see red underlines, you can restart the Deno Language Server.

Open your browser and navigate to the route `/user`. You should see the user data returned from the Neon database:

```
[]
```

It could be an empty array if you haven’t added any data to the `users_table` table.

#### Initialize a new Netlify project[](#initialize-a-new-netlify-project)

Run the following command to initialize a new Netlify project:

```
netlify init
```

Answer the questions in the CLI to create a new Netlify project. In this tutorial, we will choose `Yes, create and deploy site manually` -> `<YOUR_TEAM>` -> `<SITE_NAME>`.

#### Setup Netlify environment variables[](#setup-netlify-environment-variables)

Run the following command to import your environment variables into Netlify:

```
netlify env:import .env
```

Read more about Netlify environment variables [here](https://docs.netlify.com/environment-variables/get-started/).

#### Deploy your project[](#deploy-your-project)

Run the following command to deploy your project:

```
netlify deploy
```

Follow the instructions in the CLI to deploy your project to Netlify. In this tutorial our publish directory is `'.'`.

It is a [draft deployment](https://docs.netlify.com/cli/get-started/#draft-deploys) by default. To do a production deployment, run the following command:

```
netlify deploy --prod
```

Finally, you can use URL of the deployed website and navigate to the route you created `(e.g. /user)` to access your edge function.
