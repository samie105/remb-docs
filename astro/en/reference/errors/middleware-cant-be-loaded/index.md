---
title: "Can't load the middleware."
source: "https://docs.astro.build/en/reference/errors/middleware-cant-be-loaded/"
canonical_url: "https://docs.astro.build/en/reference/errors/middleware-cant-be-loaded/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:42.542Z"
content_hash: "1b64075a1a398477e9feab29c19cb53a924603218cf0bb2af7441e4c42de23ef"
menu_path: ["Can't load the middleware."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/mdx-integration-missing-error/index.md", "title": "MDX integration missing."}
nav_next: {"path": "astro/en/reference/errors/middleware-no-data-or-next-called/index.md", "title": "The middleware didn't return a Response."}
---

# Can't load the middleware.

> **MiddlewareCantBeLoaded**: An unknown error was thrown while loading your middleware.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when middleware throws an error while attempting to loading it.

For example:

```
import {defineMiddleware} from "astro:middleware";throw new Error("Error thrown while loading the middleware.")export const onRequest = defineMiddleware(() => {  return "string"});
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
