---
title: "Invalid value returned by getStaticPaths."
source: "https://docs.astro.build/en/reference/errors/invalid-get-static-paths-return/"
canonical_url: "https://docs.astro.build/en/reference/errors/invalid-get-static-paths-return/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:18.703Z"
content_hash: "8175ac930cfcb09e41e3c9cf80c44cc54dbab0a720239b1f42cd5109ed5b6098"
menu_path: ["Invalid value returned by getStaticPaths."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/invalid-get-static-paths-entry/index.md", "title": "Invalid entry inside getStaticPath's return value"}
nav_next: {"path": "astro/en/reference/errors/invalid-glob/index.md", "title": "Invalid glob pattern."}
---

# Invalid value returned by getStaticPaths.

> **InvalidGetStaticPathsReturn**: Invalid type returned by `getStaticPaths`. Expected an `array`, got `RETURN_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getStaticPaths`’s return value must be an array of objects.

```
export async function getStaticPaths() {  return [ // <-- Array    { params: { slug: "blog" } },    { params: { slug: "about" } }  ];}
```

**See Also:**

*   [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
*   [`params`](/en/reference/api-reference/#params)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
