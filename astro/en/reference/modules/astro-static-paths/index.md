---
title: "Static Paths API Reference"
source: "https://docs.astro.build/en/reference/modules/astro-static-paths/"
canonical_url: "https://docs.astro.build/en/reference/modules/astro-static-paths/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:47.221Z"
content_hash: "b370cd307042e457fee414beb945ce2344246be35e0e00f0903de9ec84486409"
menu_path: ["Static Paths API Reference"]
section_path: []
nav_prev: {"path": "astro/en/reference/modules/astro-middleware/index.md", "title": "Middleware API Reference"}
nav_next: {"path": "astro/en/reference/modules/astro-transitions/index.md", "title": "View Transitions Router API Reference"}
---

# Static Paths API Reference

**Added in:** `astro@6.0.0`

This module provides utilities to help adapters collect static paths from within their target runtime (e.g. `workerd`). This only provides a real implementation in the `prerender` Vite environment. In other environments, it returns a no-op implementation.

## Imports from `astro:static-paths`

[Section titled “Imports from astro:static-paths”](#imports-from-astrostatic-paths)

```
import {  StaticPaths,} from 'astro:static-paths';
```

### `StaticPaths`

[Section titled “StaticPaths”](#staticpaths)

Allows adapters to collect all paths that need to be prerendered from within their target runtime. This is useful when [implementing a custom prerenderer](/en/reference/adapter-reference/#custom-prerenderer) that runs in a non-Node environment:

The `StaticPaths` constructor accepts a required [SSR manifest](/en/reference/integrations-reference/#ssrmanifest) and an object describing the route cache and providing a method to access the component used to render the route. The preferred method to initiate a `StaticPaths` instance is to pass it an [app instance](/en/reference/modules/astro-app/#the-app-instance).

The following example initializes a `StaticPaths` instance from an app in an adapter server entrypoint:

```
import { createApp } from 'astro/app/entrypoint';import { StaticPaths } from 'astro:static-paths';
const app = createApp();const staticPaths = new StaticPaths(app);
export const handler = (event, context) => {  // do something with `staticPaths`};
```

#### `StaticPaths.getAll()`

[Section titled “StaticPaths.getAll()”](#staticpathsgetall)

**Type:** `() => Promise<Array<{ pathname: string, route: [RouteData](/en/reference/integrations-reference/#routedata) }>>`

Retrieves all paths that should be prerendered. This returns a promise that resolves to an array of objects describing the route path and its data.

The following example collects all static paths to be pre-rendered before returning them as `Response` in an adapter handler:

```
import { StaticPaths } from 'astro:static-paths';
export function createHandler(app) {  return async (request) => {    const { pathname } = new URL(request.url);
    // Endpoint to collect static paths during build    if (pathname === '/__astro_static_paths') {      const staticPaths = new StaticPaths(app);      const paths = await staticPaths.getAll();      // Returns array of { pathname: string, route: RouteData }      return new Response(JSON.stringify({ paths }));    }
    // ... handle other requests  };}
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


