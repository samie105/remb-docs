---
title: "No static path found for requested path."
source: "https://docs.astro.build/en/reference/errors/no-matching-static-path-found/"
canonical_url: "https://docs.astro.build/en/reference/errors/no-matching-static-path-found/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:10.338Z"
content_hash: "2eae00bc8ec71b6cde89d26439639544f6a10d32cfaec1c4cdccf20350862c05"
menu_path: ["No static path found for requested path."]
section_path: []
---
# No static path found for requested path.

> **NoMatchingStaticPathFound**: A `getStaticPaths()` route pattern was matched, but no matching static path was found for requested path `PATH_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A [dynamic route](/en/guides/routing/#dynamic-routes) was matched, but no corresponding path was found for the requested parameters. This is often caused by a typo in either the generated or the requested path.

**See Also:**

*   [getStaticPaths()](/en/reference/routing-reference/#getstaticpaths)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
