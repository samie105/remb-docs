---
title: "Use Supabase with Vue"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/vue"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/vue"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:41.006Z"
content_hash: "0a45371d0934acda03945d7da9b33181af32620aa15d798898515a2904c2fa6b"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Vue","Vue"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Vue","Vue"]
---
# 

Use Supabase with Vue

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from a Vue app.

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

### Create a Vue app

*   Create a Vue app using the `npm init` command.
    
    ##### Explore drop-in UI components for your Supabase app.
    
    UI components built on shadcn/ui that connect to Supabase via a single command.
    
    [Explore Components](https://supabase.com/ui)
    

###### Terminal

```
1npm init vue@latest my-app
```

3

### Install the Supabase client library

The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a Vue app.

Navigate to the Vue app and install `supabase-js`.

###### Terminal

```
1cd my-app && npm install @supabase/supabase-js
```

4

### Declare Supabase Environment Variables

Create a `.env.local` file and populate with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

```
1VITE_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>2VITE_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=vue).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=vue).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=vue), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Create the Supabase client

Create a `/src/lib` directory in your Vue app, create a file called `supabaseClient.js` and add the following code to initialize the Supabase client:

###### src/lib/supabaseClient.js

```
1import { createClient } from '@supabase/supabase-js'23const supabaseUrl = import.meta.env.VITE_SUPABASE_URL4const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY56export const supabase = createClient(supabaseUrl, supabasePublishableKey)
```

6

### Query data from the app

Replace the existing content in your `App.vue` file with the following code.

###### src/App.vue

```
1<script setup>2import { ref, onMounted } from 'vue'3import { supabase } from './lib/supabaseClient'45const instruments = ref([])67async function getInstruments() {8  const { data } = await supabase.from('instruments').select()9  instruments.value = data10}1112onMounted(() => {13   getInstruments()14})15</script>1617<template>18  <ul>19    <li v-for="instrument in instruments" :key="instrument.id">{{ instrument.name }}</li>20  </ul>21</template>
```

7

### Start the app

Start the app and go to [http://localhost:5173](http://localhost:5173) in a browser and you should see the list of instruments.

###### Terminal

```
1npm run dev
```
