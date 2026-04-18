---
title: "The middleware didn't return a Response."
source: "https://docs.astro.build/en/reference/errors/middleware-no-data-or-next-called/"
canonical_url: "https://docs.astro.build/en/reference/errors/middleware-no-data-or-next-called/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:45.003Z"
content_hash: "ef8b024f343f73aa7a59809e18e1e4e860ecf06a6d1141cef67591c353b9479b"
menu_path: ["The middleware didn't return a Response."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/middleware-cant-be-loaded/index.md", "title": "Can't load the middleware."}
nav_next: {"path": "astro/en/reference/errors/middleware-not-aresponse/index.md", "title": "The middleware returned something that is not a Response object."}
---

# The middleware didn't return a Response.

> **MiddlewareNoDataOrNextCalled**: Make sure your middleware returns a `Response` object, either directly or by returning the `Response` from calling the `next` function.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when the middleware does not return any data or call the `next` function.

For example:

```
import {defineMiddleware} from "astro:middleware";export const onRequest = defineMiddleware((context, _) => {  // doesn't return anything or call `next`  context.locals.someData = false;});
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
