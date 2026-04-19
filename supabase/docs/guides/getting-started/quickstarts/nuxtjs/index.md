---
title: "Use Supabase with Nuxt"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/nuxtjs"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/nuxtjs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:20.782Z"
content_hash: "3d5544c32a7d33b31246743a5fad6db7b7f1d14acdfda31212383a03c0f07a83"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Nuxt","Nuxt"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Nuxt","Nuxt"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/nextjs/index.md", "title": "Use Supabase with Next.js"}
nav_next: {"path": "supabase/docs/guides/getting-started/quickstarts/reactjs/index.md", "title": "Use Supabase with React"}
---

# 

Use Supabase with Nuxt

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from a Nuxt app.

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

### Create a Nuxt app

*   Create a Nuxt app using the `npx nuxi` command.
    
    ##### Explore drop-in UI components for your Supabase app.
    
    UI components built on shadcn/ui that connect to Supabase via a single command.
    
    [Explore Components](https://supabase.com/ui)
    

###### Terminal

```
1npx nuxi@latest init my-app
```

3

### Install the Supabase client library

The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a Nuxt app.

Navigate to the Nuxt app and install `supabase-js`.

###### Terminal

```
1cd my-app && npm install @supabase/supabase-js
```

4

### Declare Supabase Environment Variables

Create a `.env` file and populate with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

```
1SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>2SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nuxt).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nuxt).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nuxt), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Query data from the app

In `app.vue`, create a Supabase client using your config values and replace the existing content with the following code.

###### app.vue

```
1<script setup>2import { createClient } from '@supabase/supabase-js'3const config = useRuntimeConfig()4const supabase = createClient(config.public.supabaseUrl, config.public.supabasePublishableKey)5const instruments = ref([])67async function getInstruments() {8  const { data } = await supabase.from('instruments').select()9  instruments.value = data10}1112onMounted(() => {13  getInstruments()14})15</script>1617<template>18  <ul>19    <li v-for="instrument in instruments" :key="instrument.id">{{ instrument.name }}</li>20  </ul>21</template>
```

6

### Start the app

Start the app, navigate to [http://localhost:3000](http://localhost:3000) in the browser, open the browser console, and you should see the list of instruments.

###### Terminal

```
1npm run dev
```

The community-maintained [@nuxtjs/supabase](https://supabase.nuxtjs.org/) module provides an alternate DX for working with Supabase in Nuxt.
