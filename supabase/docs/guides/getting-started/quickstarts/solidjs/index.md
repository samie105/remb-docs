---
title: "Use Supabase with SolidJS"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/solidjs"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/solidjs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:33.131Z"
content_hash: "5a2490c602488b4609fd38e592a00659505bc9c15cb34192ca54b31cce46058f"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","SolidJS","SolidJS"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","SolidJS","SolidJS"]
nav_prev: {"path": "../ruby-on-rails/index.md", "title": "Use Supabase with Ruby on Rails"}
nav_next: {"path": "../sveltekit/index.md", "title": "Use Supabase with SvelteKit"}
---

# 

Use Supabase with SolidJS

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from a SolidJS app.

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

### Create a SolidJS app

Create a SolidJS app using the `degit` command.

###### Terminal

```
1npx degit solidjs/templates/js my-app
```

3

### Install the Supabase client library

The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a SolidJS app.

Navigate to the SolidJS app and install `supabase-js`.

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

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=solidjs).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=solidjs).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=solidjs), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Query data from the app

In `App.jsx`, create a Supabase client to fetch the instruments data.

Add a `getInstruments` function to fetch the data and display the query result to the page.

###### src/App.jsx

```
1import { createClient } from "@supabase/supabase-js";2import { createResource, For } from "solid-js";34const supabase = createClient('https://<project>.supabase.co', '<sb_publishable_key>');56async function getInstruments() {7  const { data } = await supabase.from("instruments").select();8  return data;9}1011function App() {12  const [instruments] = createResource(getInstruments);1314  return (15    <ul>16      <For each={instruments()}>{(instrument) => <li>{instrument.name}</li>}</For>17    </ul>18  );19}2021export default App;
```

6

### Start the app

Start the app and go to [http://localhost:3000](http://localhost:3000) in a browser and you should see the list of instruments.

###### Terminal

```
1npm run dev
```
