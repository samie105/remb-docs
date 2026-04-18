---
title: "The middleware returned something that is not a Response object."
source: "https://docs.astro.build/en/reference/errors/middleware-not-aresponse/"
canonical_url: "https://docs.astro.build/en/reference/errors/middleware-not-aresponse/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:45.735Z"
content_hash: "4ecb92e93ca6a211443f38d442eed9b4fb60e5fc9c25c348b7937d7a08342b4f"
menu_path: ["The middleware returned something that is not a Response object."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/middleware-no-data-or-next-called/index.md", "title": "The middleware didn't return a Response."}
nav_next: {"path": "astro/en/reference/errors/missing-image-dimension/index.md", "title": "Missing image dimensions"}
---

# The middleware returned something that is not a Response object.

> **MiddlewareNotAResponse**: Any data returned from middleware must be a valid `Response` object.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when middleware returns something that is not a `Response` object.

For example:

```
import {defineMiddleware} from "astro:middleware";export const onRequest = defineMiddleware(() => {  return "string"});
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

