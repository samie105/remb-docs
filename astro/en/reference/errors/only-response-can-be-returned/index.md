---
title: "Invalid type returned by Astro page."
source: "https://docs.astro.build/en/reference/errors/only-response-can-be-returned/"
canonical_url: "https://docs.astro.build/en/reference/errors/only-response-can-be-returned/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:13.589Z"
content_hash: "8377985f16050fb21aa69f6a7f729d88b7796c2309122b29f1485478783feaa3"
menu_path: ["Invalid type returned by Astro page."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/no-prerendered-routes-with-domains/index.md", "title": "Prerendered routes aren't supported when internationalization domains are enabled."}
nav_next: {"path": "astro/en/reference/errors/page-number-param-not-found/index.md", "title": "Page number param not found."}
---

# Invalid type returned by Astro page.

> Route returned a `RETURNED_VALUE`. Only a Response can be returned from Astro files.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Only instances of [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) can be returned inside Astro files.

```
---return new Response(null, { status: 404, statusText: 'Not found'});
// Alternatively, for redirects, Astro.redirect also returns an instance of Responsereturn Astro.redirect('/login');---
```

**See Also:**

*   [Response](/en/guides/on-demand-rendering/#response)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

