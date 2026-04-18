---
title: "Prerendered dynamic endpoint has path collision."
source: "https://docs.astro.build/en/reference/errors/prerender-dynamic-endpoint-path-collide/"
canonical_url: "https://docs.astro.build/en/reference/errors/prerender-dynamic-endpoint-path-collide/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:17.316Z"
content_hash: "2e3b5db78c35ae14feda51a9570b792d234b5d3adf7d8f879378bc091748fdf4"
menu_path: ["Prerendered dynamic endpoint has path collision."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/prerender-client-address-not-available/index.md", "title": "Astro.clientAddress cannot be used inside prerendered routes."}
nav_next: {"path": "astro/en/reference/errors/prerender-route-conflict/index.md", "title": "Prerendered route generates the same path as another route."}
---

# Prerendered dynamic endpoint has path collision.

> **PrerenderDynamicEndpointPathCollide**: Could not render `PATHNAME` with an `undefined` param as the generated path will collide during prerendering. Prevent passing `undefined` as `params` for the endpoint’s `getStaticPaths()` function, or add an additional extension to the endpoint’s filename.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The endpoint is prerendered with an `undefined` param so the generated path will collide with another route.

If you cannot prevent passing `undefined`, then an additional extension can be added to the endpoint file name to generate the file with a different name. For example, renaming `pages/api/[slug].ts` to `pages/api/[slug].json.ts`.

**See Also:**

*   [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
*   [`params`](/en/reference/api-reference/#params)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
