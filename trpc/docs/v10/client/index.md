---
title: "Client Overview"
source: "https://trpc.io/docs/v10/client"
canonical_url: "https://trpc.io/docs/v10/client"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:31:59.304Z"
content_hash: "e1eedc8eba6a775fcfb08304d9f6f2185664200419681c27caaeb047e599d029"
menu_path: ["Client Overview"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/index.md", "title": "tRPC"}
nav_next: {"path": "trpc/docs/v10/client/cors/index.md", "title": "Send cookies cross-origin"}
---

While a tRPC API can be called using normal HTTP requests like any other REST API, you will need a **client** to benefit from tRPC's typesafety.

A client knows the procedures that are available in your API, and their inputs and outputs. It uses this information to give you autocomplete on your queries and mutations, correctly type the returned data, and show errors if you are writing requests that don't match the shape of your backend.

If you are using React, the best way to call a tRPC API is by using our [React Query Integration](react/index.md), which in addition to typesafe API calls also offers caching, invalidation, and management of loading and error state. If you are using Next.js with the `/pages` directory, you can use our [Next.js integration](nextjs/index.md), which adds helpers for Serverside Rendering and Static Generation in addition to the React Query Integration.

If you want to call a tRPC API from another server or from a frontend framework for which we don't have an integration, you can use the [Vanilla Client](vanilla/index.md).

In addition to the React and Next.js integrations and the Vanilla Client, there are a variety of [community-built integrations for a variety of other frameworks](../../community/awesome-trpc/index.md#frontend-frameworks). Please note that these are not maintained by the tRPC team.
