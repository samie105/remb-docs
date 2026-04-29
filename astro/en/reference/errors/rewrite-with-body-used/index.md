---
title: "Cannot use Astro.rewrite after the request body has been read"
source: "https://docs.astro.build/en/reference/errors/rewrite-with-body-used/"
canonical_url: "https://docs.astro.build/en/reference/errors/rewrite-with-body-used/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:27.563Z"
content_hash: "cb6314a78100d5bb625b9c2e61d6b34e77521c380bf643219916c41555cb19b7"
menu_path: ["Cannot use Astro.rewrite after the request body has been read"]
section_path: []
nav_prev: {"path": "../rewrite-encountered-an-error/index.md", "title": "Astro couldn't find the route to rewrite, or if was found but it emitted an error during the rendering phase."}
nav_next: {"path": "../route-not-found/index.md", "title": "Route not found."}
---

# Cannot use Astro.rewrite after the request body has been read

> **RewriteWithBodyUsed**: Astro.rewrite() cannot be used if the request body has already been read. If you need to read the body, first clone the request.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.rewrite()` cannot be used if the request body has already been read. If you need to read the body, first clone the request. For example:

```
const data = await Astro.request.clone().formData();
Astro.rewrite("/target")
```

**See Also:**

*   [Request.clone()](https://developer.mozilla.org/en-US/docs/Web/API/Request/clone)
*   [Astro.rewrite](/en/reference/api-reference/#rewrite)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
