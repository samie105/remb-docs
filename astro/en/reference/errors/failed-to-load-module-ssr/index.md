---
title: "Could not import file."
source: "https://docs.astro.build/en/reference/errors/failed-to-load-module-ssr/"
canonical_url: "https://docs.astro.build/en/reference/errors/failed-to-load-module-ssr/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:38.715Z"
content_hash: "dc67ca54924c37a0385aa6e310f266d2e90208cc14f442535f1b49f032db7a78"
menu_path: ["Could not import file."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/failed-to-find-page-map-ssr/index.md", "title": "Astro couldn't find the correct page to render"}
nav_next: {"path": "astro/en/reference/errors/file-glob-not-supported/index.md", "title": "Glob patterns are not supported in the file loader"}
---

# Could not import file.

> **FailedToLoadModuleSSR**: Could not import `IMPORT_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not import the requested file. Oftentimes, this is caused by the import path being wrong (either because the file does not exist, or there is a typo in the path)

This message can also appear when a type is imported without specifying that it is a [type import](/en/guides/typescript/#type-imports).

**See Also:**

*   [Type Imports](/en/guides/typescript/#type-imports)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
