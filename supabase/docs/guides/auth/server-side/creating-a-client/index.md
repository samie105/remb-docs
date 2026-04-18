---
title: "Creating a Supabase client for SSR"
source: "https://supabase.com/docs/guides/auth/server-side/creating-a-client"
canonical_url: "https://supabase.com/docs/guides/auth/server-side/creating-a-client"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:51.965Z"
content_hash: "e4fba4afedd1962c4075f465f9bdb8ab0186a4ca2c854d69841a6535a8077c13"
menu_path: ["Auth","Auth","More","More","More","Server-Side Rendering","Server-Side Rendering","Creating a client","Creating a client"]
section_path: ["Auth","Auth","More","More","More","Server-Side Rendering","Server-Side Rendering","Creating a client","Creating a client"]
nav_prev: {"path": "supabase/docs/guides/auth/server-side/advanced-guide/index.md", "title": "Advanced guide"}
nav_next: {"path": "supabase/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers/index.md", "title": "Migrating to the SSR package from Auth Helpers"}
---

# 

Creating a Supabase client for SSR

## 

Configure your Supabase client to use cookies

* * *

To use Server-Side Rendering (SSR) with Supabase, you need to configure your Supabase client to use cookies. The `@supabase/ssr` package helps you do this for JavaScript/TypeScript applications.

## Install[#](#install)

Install the `@supabase/supabase-js` and `@supabase/ssr` helper packages:

```
1npm install @supabase/supabase-js @supabase/ssr
```

## Set environment variables[#](#set-environment-variables)

Create a `.env.local` file in the project root directory. In the file, set the project's Supabase URL and Key:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

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

```
1NEXT_PUBLIC_SUPABASE_URL=supabase_project_url2NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=supabase_publishable_key
```

## Create a client[#](#create-a-client)

You need setup code to configure a Supabase client to use cookies. Once you have the utility code, you can use the `createClient` utility functions to get a properly configured Supabase client.

Use the browser client in code that runs on the browser, and the server client in code that runs on the server.

### Write utility functions to create Supabase clients[#](#write-utility-functions-to-create-supabase-clients)

To access Supabase from a Next.js app, you need 2 types of Supabase clients:

1.  **Client Component client** - To access Supabase from Client Components, which run in the browser.
2.  **Server Component client** - To access Supabase from Server Components, Server Actions, and Route Handlers, which run only on the server.

Since Next.js Server Components can't write cookies, you need a [Proxy](https://nextjs.org/docs/app/getting-started/proxy) to refresh expired Auth tokens and store them.

The Proxy is responsible for:

1.  Refreshing the Auth token by calling `supabase.auth.getClaims()`.
2.  Passing the refreshed Auth token to Server Components, so they don't attempt to refresh the same token themselves. This is accomplished with `request.cookies.set`.
3.  Passing the refreshed Auth token to the browser, so it replaces the old token. This is accomplished with `response.cookies.set`.

Create a `lib/supabase` folder at the root of your project, or inside the `./src` folder if you are using one, with a file for each type of client. Then copy the lib utility functions for each client type.

```
1import { createBrowserClient } from '@supabase/ssr'23export function createClient() {4  return createBrowserClient(5    process.env.NEXT_PUBLIC_SUPABASE_URL!,6    process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!7  )8}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/auth/nextjs/lib/supabase/client.ts)

### Hook up proxy[#](#hook-up-proxy)

The code adds a [matcher](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher) so the Proxy doesn't run on routes that don't access Supabase.

Be careful when protecting pages. The server gets the user session from the cookies, which can be spoofed by anyone.

Always use `supabase.auth.getClaims()` to protect pages and user data.

_Never_ trust `supabase.auth.getSession()` inside server code such as Proxy. It isn't guaranteed to revalidate the Auth token.

It's safe to trust `getClaims()` because it validates the JWT signature against the project's published public keys every time.

```
1import { type NextRequest } from 'next/server'2import { updateSession } from '@/lib/supabase/proxy'34export async function proxy(request: NextRequest) {5  return await updateSession(request)6}78export const config = {9  matcher: [10    /*11     * Match all request paths except for the ones starting with:12     * - _next/static (static files)13     * - _next/image (image optimization files)14     * - favicon.ico (favicon file)15     * Feel free to modify this pattern to include more paths.16     */17    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',18  ],19}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/auth/nextjs/proxy.ts)

## Congratulations[#](#congratulations)

You're done! To recap, you've successfully:

*   Called Supabase from a Server Action.
*   Called Supabase from a Server Component.
*   Set up a Supabase client utility to call Supabase from a Client Component. You can use this if you need to call Supabase from a Client Component, for example to set up a realtime subscription.
*   Set up Proxy to automatically refresh the Supabase Auth session.

You can now use any Supabase features from your client or server code!

## Caching considerations[#](#caching-considerations)

If your app uses ISR (Incremental Static Regeneration) or is deployed behind a CDN, caching of HTTP responses can cause users to receive another user's session. When a session is refreshed, the new token is written to the response via `Set-Cookie`. If that response is cached and served to a different user, that user will be signed in as the wrong person.

See the [advanced Auth server-side rendering guide](/docs/guides/auth/server-side/advanced-guide#can-i-use-server-side-rendering-with-a-cdn-or-cache) for details and framework-specific examples.

## Next steps[#](#next-steps)

*   Implement [Authentication using Email and Password](/docs/guides/auth/passwords)
*   Implement [Authentication using OAuth](/docs/guides/auth/social-login)
*   [Learn more about SSR](/docs/guides/auth/server-side/advanced-guide)
