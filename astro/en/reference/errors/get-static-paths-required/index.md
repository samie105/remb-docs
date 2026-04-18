---
title: "getStaticPaths() function required for dynamic routes."
source: "https://docs.astro.build/en/reference/errors/get-static-paths-required/"
canonical_url: "https://docs.astro.build/en/reference/errors/get-static-paths-required/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:54.253Z"
content_hash: "fd7e067ce13297a1700e452c0a08a410a78ea79c24b00b63dc8b4f146484de2b"
menu_path: ["getStaticPaths() function required for dynamic routes."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/get-static-paths-invalid-route-param/index.md", "title": "Invalid route parameter returned by getStaticPaths()."}
nav_next: {"path": "astro/en/reference/errors/i18n-no-locale-found-in-path/index.md", "title": "The path doesn't contain any locale"}
---

# getStaticPaths() function required for dynamic routes.

> **GetStaticPathsRequired**: `getStaticPaths()` function is required for dynamic routes. Make sure that you `export` a `getStaticPaths` function from your dynamic route.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

In [Static Mode](/en/guides/routing/#static-ssg-mode), all routes must be determined at build time. As such, dynamic routes must `export` a `getStaticPaths` function returning the different paths to generate.

**See Also:**

*   [Dynamic Routes](/en/guides/routing/#dynamic-routes)
*   [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
*   [Server-side Rendering](/en/guides/on-demand-rendering/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

