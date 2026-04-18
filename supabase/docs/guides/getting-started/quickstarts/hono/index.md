---
title: "Use Supabase with Hono"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/hono"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/hono"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:10.059Z"
content_hash: "d7c8e8ce83e03b43808a9116db272055141734d1b95c237da59b6caa498fcd0d"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Hono","Hono"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Hono","Hono"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/flutter/index.md", "title": "Use Supabase with Flutter"}
nav_next: {"path": "supabase/docs/guides/getting-started/quickstarts/ios-swiftui/index.md", "title": "Use Supabase with iOS and SwiftUI"}
---

# 

Use Supabase with Hono

## 

Learn how to create a Supabase project, add some sample data to your database, secure it with auth, and query the data from a Hono app.

* * *

1

### Create a Hono app

Bootstrap the Hono example app from the Supabase Samples using the CLI.

###### Terminal

```
1npx supabase@latest bootstrap hono
```

2

### Install the Supabase client library

The `package.json` file in the project includes the necessary dependencies, including `@supabase/supabase-js` and `@supabase/ssr` to help with server-side auth.

###### Terminal

```
1npm install
```

3

### Set up the required environment variables

Copy the `.env.example` file to `.env` and update the values with your Supabase project URL and publishable key.

Lastly, [enable anonymous sign-ins](/dashboard/project/_/auth/providers) in the Auth settings.

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

###### Terminal

```
1cp .env.example .env
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

4

### Start the app

Start the app, go to [http://localhost:5173](http://localhost:5173).

Learn how [server side auth](/docs/guides/auth/server-side/creating-a-client?queryGroups=framework&framework=hono) works with Hono.

###### Terminal

```
1npm run dev
```

## Next steps[#](#next-steps)

*   Learn how [server side auth](/docs/guides/auth/server-side/creating-a-client?queryGroups=framework&framework=hono) works with Hono.
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)

