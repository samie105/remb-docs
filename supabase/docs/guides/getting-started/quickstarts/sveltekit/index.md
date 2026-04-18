---
title: "Use Supabase with SvelteKit"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/sveltekit"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/sveltekit"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:35.068Z"
content_hash: "059cdbda298078b6b09236bfa355eac84bb6804ef14684c5a73d3f7201cacc0d"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","SvelteKit","SvelteKit"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","SvelteKit","SvelteKit"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/solidjs/index.md", "title": "Use Supabase with SolidJS"}
nav_next: {"path": "supabase/docs/guides/getting-started/quickstarts/tanstack/index.md", "title": "Use Supabase with TanStack Start"}
---

# 

Use Supabase with SvelteKit

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from a SvelteKit app.

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

### Create a SvelteKit app

Create a SvelteKit app using the `npm create` command.

###### Terminal

```
1npx sv create my-app
```

3

### Install the Supabase client library

The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a SvelteKit app.

Navigate to the SvelteKit app and install `supabase-js`.

###### Terminal

```
1cd my-app && npm install @supabase/supabase-js
```

4

### Declare Supabase Environment Variables

Create a `.env` file at the root of your project and populate with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

```
1PUBLIC_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>2PUBLIC_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=sveltekit).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=sveltekit).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=sveltekit), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Create the Supabase client

Create a `src/lib` directory in your SvelteKit app, create a file called `supabaseClient.js` and add the following code to initialize the Supabase client:

```
1import { createClient } from '@supabase/supabase-js';2import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY } from '$env/static/public';34export const supabase = createClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY)
```

6

### Query data from the app

Use `load` method to fetch the data server-side and display the query results as a simple list.

Create `+page.server.js` file in the `src/routes` directory with the following code.

```
1import { supabase } from "$lib/supabaseClient";23  export async function load() {4    const { data } = await supabase.from("instruments").select();5    return {6      instruments: data ?? [],7    };8  }
```

Replace the existing content in your `+page.svelte` file in the `src/routes` directory with the following code.

###### src/routes/+page.svelte

```
1<script>2  let { data } = $props();3</script>45<ul>6  {#each data.instruments as instrument}7    <li>{instrument.name}</li>8  {/each}9</ul>
```

7

### Start the app

Start the app and go to [http://localhost:5173](http://localhost:5173) in a browser and you should see the list of instruments.

###### Terminal

```
1npm run dev
```

## Next steps[#](#next-steps)

*   Set up [Auth](/docs/guides/auth) for your app
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)

