---
title: "Migrating to the SSR package from Auth Helpers"
source: "https://supabase.com/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers"
canonical_url: "https://supabase.com/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:52.972Z"
content_hash: "c84723eac9e3089b1f146ba65ac84f7d2d5bcecb81677ff81f6b8a06df6eb596"
menu_path: ["Auth","Auth","More","More","More","Server-Side Rendering","Server-Side Rendering","Migrating from Auth Helpers","Migrating from Auth Helpers"]
section_path: ["Auth","Auth","More","More","More","Server-Side Rendering","Server-Side Rendering","Migrating from Auth Helpers","Migrating from Auth Helpers"]
nav_prev: {"path": "supabase/docs/guides/auth/server-side/creating-a-client/index.md", "title": "Creating a Supabase client for SSR"}
nav_next: {"path": "supabase/docs/guides/auth/quickstarts/with-expo-react-native-social-auth/index.md", "title": "Build a Social Auth App with Expo React Native"}
---

# 

Migrating to the SSR package from Auth Helpers

* * *

The new `ssr` package takes the core concepts of the Auth Helpers and makes them available to any server language or framework. This page will guide you through migrating from the Auth Helpers package to `ssr`.

## Replacing Supabase packages[#](#replacing-supabase-packages)

```
1npm uninstall @supabase/auth-helpers-nextjs
```

```
1npm install @supabase/ssr
```

## Creating a client[#](#creating-a-client)

The new `ssr` package exports two functions for creating a Supabase client. The `createBrowserClient` function is used in the client, and the `createServerClient` function is used in the server.

Read the [Creating a client](/docs/guides/auth/server-side/creating-a-client) page for examples of creating a client in your framework [and our migration guide](/docs/guides/troubleshooting/how-to-migrate-from-supabase-auth-helpers-to-ssr-package-5NRunM).

## Next steps[#](#next-steps)

*   Implement [Authentication using Email and Password](/docs/guides/auth/passwords)
*   Implement [Authentication using OAuth](/docs/guides/auth/social-login)
*   [Learn more about SSR](/docs/guides/auth/server-side/advanced-guide)


