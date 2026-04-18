---
title: "Value assigned to locals is not accepted."
source: "https://docs.astro.build/en/reference/errors/locals-not-an-object/"
canonical_url: "https://docs.astro.build/en/reference/errors/locals-not-an-object/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:33.188Z"
content_hash: "74a581f33a5cbd879a746353c475bb6cd0d01431648200fa6e1f85bb457c7851"
menu_path: ["Value assigned to locals is not accepted."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/local-image-used-wrongly/index.md", "title": "Local images must be imported."}
nav_next: {"path": "astro/en/reference/errors/locals-not-serializable/index.md", "title": "Astro.locals is not serializable"}
---

# Value assigned to locals is not accepted.

> **LocalsNotAnObject**: `locals` can only be assigned to an object. Other values like numbers, strings, etc. are not accepted.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when `locals` is overwritten with something that is not an object

For example:

```
import {defineMiddleware} from "astro:middleware";export const onRequest = defineMiddleware((context, next) => {  context.locals = 1541;  return next();});
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

