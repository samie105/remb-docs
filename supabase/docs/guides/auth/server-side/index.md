---
title: "Server-Side Rendering"
source: "https://supabase.com/docs/guides/auth/server-side"
canonical_url: "https://supabase.com/docs/guides/auth/server-side"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:06.519Z"
content_hash: "400f1b0b96aac412eb1b3f06d6eec5b2aa888ed25fa2e2dd468220db725a88e9"
menu_path: ["Auth","Auth","More","More","More","Server-Side Rendering","Server-Side Rendering","Overview","Overview"]
section_path: ["Auth","Auth","More","More","More","Server-Side Rendering","Server-Side Rendering","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/auth/redirect-urls/index.md", "title": "Redirect URLs"}
nav_next: {"path": "supabase/docs/guides/auth/sessions/index.md", "title": "User sessions"}
---

# 

Server-Side Rendering

## 

How SSR works with Supabase Auth.

* * *

SSR frameworks move rendering and data fetches to the server, to reduce client bundle size and execution time.

Supabase Auth is fully compatible with SSR. You need to make a few changes to the configuration of your Supabase client, to store the user session in cookies instead of local storage. After setting up your Supabase client, follow the instructions for any flow in the How-To guides.

Make sure to use the PKCE flow instructions where those differ from the implicit flow instructions. If no difference is mentioned, don't worry about this.

## `@supabase/ssr`[#](#supabasessr)

We have developed an [`@supabase/ssr`](https://www.npmjs.com/package/@supabase/ssr) package to make setting up the Supabase client as simple as possible. This package is currently in beta. Adoption is recommended but be aware that the API is still unstable and may have breaking changes in the future.

## Framework quickstarts[#](#framework-quickstarts)

[

![Next.js](/docs/img/icons/nextjs-icon.svg)

Next.js

Automatically configure Supabase in Next.js to use cookies, making your user and their session available on the client and server.

](/docs/guides/auth/server-side/nextjs)[

![SvelteKit](/docs/img/icons/svelte-icon.svg)

SvelteKit

Automatically configure Supabase in SvelteKit to use cookies, making your user and their session available on the client and server.

](/docs/guides/auth/server-side/sveltekit)


