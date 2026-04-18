---
title: "Invalid value returned by a getStaticPaths path."
source: "https://docs.astro.build/en/reference/errors/invalid-get-static-path-param/"
canonical_url: "https://docs.astro.build/en/reference/errors/invalid-get-static-path-param/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:15.934Z"
content_hash: "c748bae18f4895ab22d7a43a63f7d75c41fc9473ee4d5ff87d65374755a42e62"
menu_path: ["Invalid value returned by a getStaticPaths path."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/invalid-frontmatter-injection-error/index.md", "title": "Invalid frontmatter injection."}
nav_next: {"path": "astro/en/reference/errors/invalid-get-static-paths-entry/index.md", "title": "Invalid entry inside getStaticPath's return value"}
---

# Invalid value returned by a getStaticPaths path.

> **InvalidGetStaticPathParam**: Invalid params given to `getStaticPaths` path. Expected an `object`, got `PARAM_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `params` property in `getStaticPaths`’s return value (an array of objects) should also be an object.

```
---export async function getStaticPaths() {  return [    { params: { slug: "blog" } },    { params: { slug: "about" } }  ];}---
```

**See Also:**

*   [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
*   [`params`](/en/reference/api-reference/#params)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


