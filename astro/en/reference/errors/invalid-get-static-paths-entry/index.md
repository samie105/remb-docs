---
title: "Invalid entry inside getStaticPath's return value"
source: "https://docs.astro.build/en/reference/errors/invalid-get-static-paths-entry/"
canonical_url: "https://docs.astro.build/en/reference/errors/invalid-get-static-paths-entry/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:16.915Z"
content_hash: "0db3dc1a7b0eaeb5870cb6cc6ead843368abbd185cf0ead9641bebb1775b3217"
menu_path: ["Invalid entry inside getStaticPath's return value"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/invalid-get-static-path-param/index.md", "title": "Invalid value returned by a getStaticPaths path."}
nav_next: {"path": "astro/en/reference/errors/invalid-get-static-paths-return/index.md", "title": "Invalid value returned by getStaticPaths."}
---

# Invalid entry inside getStaticPath's return value

> **InvalidGetStaticPathsEntry**: Invalid entry returned by getStaticPaths. Expected an object, got `ENTRY_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getStaticPaths`’s return value must be an array of objects. In most cases, this error happens because an array of array was returned. Using [`.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap) or a [`.flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat) call may be useful.

```
export async function getStaticPaths() {  return [ // <-- Array    { params: { slug: "blog" } }, // <-- Object    { params: { slug: "about" } }  ];}
```

**See Also:**

*   [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
