---
title: "Use Supabase with Next.js"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/nextjs"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/nextjs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:16.934Z"
content_hash: "d1015bca7aa13be7e105753f67a6485be3ef4ed8971d6916011846f51b8e6401"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Next.js","Next.js"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Next.js","Next.js"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/kotlin/index.md", "title": "Use Supabase with Android Kotlin"}
nav_next: {"path": "supabase/docs/guides/getting-started/quickstarts/reactjs/index.md", "title": "Use Supabase with React"}
---

# 

Use Supabase with Next.js

## 

Learn how to create a Supabase project, add some sample data, and query from a Next.js app.

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

### Create a Next.js app

Use the `create-next-app` command and the `with-supabase` template, to create a Next.js app pre-configured with:

*   [Cookie-based Auth](/docs/guides/auth/server-side/creating-a-client?queryGroups=package-manager&package-manager=npm&queryGroups=framework&framework=nextjs&queryGroups=environment&environment=server)
    
*   [TypeScript](https://www.typescriptlang.org/)
    
*   [Tailwind CSS](https://tailwindcss.com/)
    
    ##### Explore drop-in UI components for your Supabase app.
    
    UI components built on shadcn/ui that connect to Supabase via a single command.
    
    [Explore Components](https://supabase.com/ui)
    

```
1npx create-next-app -e with-supabase
```

3

### Declare Supabase Environment Variables

Rename `.env.example` to `.env.local` and populate with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

```
1NEXT_PUBLIC_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>2NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nextjs).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nextjs).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nextjs), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

4

### Query Supabase data from Next.js

Create a new file at `app/instruments/page.tsx` and populate with the following.

This selects all the rows from the `instruments` table in Supabase and render them on the page.

```
1import { createClient } from "@/lib/supabase/server";2import { Suspense } from "react";34async function InstrumentsData() {5  const supabase = await createClient();6  const { data: instruments } = await supabase.from("instruments").select();78  return <pre>{JSON.stringify(instruments, null, 2)}</pre>;9}1011export default function Instruments() {12  return (13    <Suspense fallback={<div>Loading instruments...</div>}>14      <InstrumentsData />15    </Suspense>16  );17}
```

5

### Start the app

Run the development server, go to [http://localhost:3000/instruments](http://localhost:3000/instruments) in a browser and you should see the list of instruments.

```
1npm run dev
```

## Next steps[#](#next-steps)

*   Set up [Auth](/docs/guides/auth) for your app
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)


