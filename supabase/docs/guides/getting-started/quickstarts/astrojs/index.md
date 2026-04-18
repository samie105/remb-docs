---
title: "Use Supabase with Astro"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/astrojs"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/astrojs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:02.535Z"
content_hash: "a13eafb8f0bf323cd799a0a32980abf1df62dab5656b6313d5ea85f4a473701e"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Astro","Astro"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Astro","Astro"]
nav_prev: {"path": "supabase/docs/guides/functions/examples/upstash-redis/index.md", "title": "Upstash Redis"}
nav_next: {"path": "supabase/docs/guides/functions/examples/stripe-webhooks/index.md", "title": "Handling Stripe Webhooks"}
---

# 

Use Supabase with Astro

## 

Learn how to create a Supabase project, add sample data, and query from an Astro app.

* * *

1

### Create a Supabase project

Go to [database.new](https://database.new) and create a new Supabase project.

Alternatively, you can create a project using the Management API:

```
1# First, get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"34# List your organizations to get the organization ID5curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \6  https://api.supabase.com/v1/organizations78# Create a new project (replace <org-id> with your organization ID)9curl -X POST https://api.supabase.com/v1/projects \10  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \11  -H "Content-Type: application/json" \12  -d '{13    "organization_id": "<org-id>",14    "name": "My Project",15    "region": "us-east-1",16    "db_pass": "<your-secure-password>"17  }'
```

When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create an `instruments` table with some sample data.

```
1-- Create the table2create table instruments (3  id bigint primary key generated always as identity,4  name text not null5);6-- Insert some sample data into the table7insert into instruments (name)8values9  ('violin'),10  ('viola'),11  ('cello');1213alter table instruments enable row level security;
```

Make the data in your table publicly readable by adding an RLS policy:

```
1create policy "public can read instruments"2on public.instruments3for select to anon4using (true);
```

2

### Create an Astro app

*   Create an Astro app using the `npm create` command.
    
    ##### Explore drop-in UI components for your Supabase app.
    
    UI components built on shadcn/ui that connect to Supabase via a single command.
    
    [Explore Components](https://supabase.com/ui)
    

###### Terminal

```
1npm create astro@latest my-app2cd my-app
```

3

### Install Supabase client library and Node adapter

Install the `supabase-js` client library and the `@astrojs/node` adapter to enable server-side rendering.

###### Terminal

```
1npm install @supabase/supabase-js @astrojs/node
```

4

### Configure Astro for SSR

Update your `astro.config.mjs`.

###### astro.config.mjs

```
1import { defineConfig } from "astro/config";2import node from "@astrojs/node";34export default defineConfig({5  output: "server",6  adapter: node({7    mode: "standalone",8  }),9});
```

5

### Declare Supabase Environment Variables

Create a `.env.local` file and populate with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

```
1PUBLIC_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>2PUBLIC_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=astro).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=astro).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=astro), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

6

### Create a Supabase client helper

Create a utility file to initialize the Supabase client:

###### src/lib/supabase.ts

```
1import { createClient } from "@supabase/supabase-js";23const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL4const supabasePublishableKey = import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY56export function createServerClient() {7  return createClient(8    supabaseUrl,9    supabasePublishableKey10  );11}
```

7

### Query Supabase data from Astro

Create a new file at `src/pages/instruments.astro` and populate with the following.

This queries all rows from the `instruments` table in Supabase and renders them on the page.

###### src/pages/instruments.astro

```
1---2import { createServerClient } from "../lib/supabase";34const supabase = createServerClient();5const { data: instruments } = await supabase.from("instruments").select();6---78<html>9  <head>10    <title>Instruments</title>11  </head>12  <body>13    <ul>14      {instruments?.map((instrument) => (15        <li>{instrument.name}</li>16      ))}17    </ul>18  </body>19</html>
```

8

### Start the app

Run the development server, go to [http://localhost:4321/instruments](http://localhost:4321/instruments) in your browser of choice to check the list of instruments.

###### Terminal

```
1npm run dev
```

## Next steps[#](#next-steps)

*   Set up [Auth](/docs/guides/auth) for your app
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)


