---
title: "Use Supabase Auth with Next.js"
source: "https://supabase.com/docs/guides/auth/quickstarts/nextjs"
canonical_url: "https://supabase.com/docs/guides/auth/quickstarts/nextjs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:39.657Z"
content_hash: "7c04fc80503087845901066d8f89c24c599a5156c3ace59fa4da0e5462795604"
menu_path: ["Auth","Auth","Getting Started","Getting Started","Next.js","Next.js"]
section_path: ["Auth","Auth","Getting Started","Getting Started","Next.js","Next.js"]
nav_prev: {"path": "supabase/docs/guides/auth/oauth-server/oauth-flows/index.md", "title": "OAuth 2.1 Flows"}
nav_next: {"path": "supabase/docs/guides/auth/quickstarts/react-native/index.md", "title": "Use Supabase Auth with React Native"}
---

# 

Use Supabase Auth with Next.js

## 

Learn how to configure Supabase Auth for the Next.js App Router.

* * *

1

### Create a new Supabase project

Head over to [database.new](https://database.new) and create a new Supabase project.

Your new database has a table for storing your users. You can see that this table is currently empty by running some SQL in the [SQL Editor](/dashboard/project/_/sql/new).

###### SQL\_EDITOR

```
1select * from auth.users;
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
    

###### Terminal

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

###### .env.local

```
1NEXT_PUBLIC_SUPABASE_URL=your-project-url2NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_... key
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

### Start the app

Start the development server, go to [http://localhost:3000](http://localhost:3000) in a browser, and you should see the contents of `app/page.tsx`.

To sign up a new user, navigate to [http://localhost:3000/auth/sign-up](http://localhost:3000/auth/sign-up), and click `Sign up`.

###### Terminal

```
1npm run dev
```

## Learn more[#](#learn-more)

*   [Setting up Server-Side Auth for Next.js](/docs/guides/auth/server-side/nextjs) for a Next.js deep dive
*   [Supabase Auth docs](/docs/guides/auth#authentication) for more Supabase authentication methods
