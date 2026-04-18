---
title: "Missing params property on getStaticPaths route."
source: "https://docs.astro.build/en/reference/errors/get-static-paths-expected-params/"
canonical_url: "https://docs.astro.build/en/reference/errors/get-static-paths-expected-params/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:50.814Z"
content_hash: "d074504d998c3184f1ce32b5af8b7b05eb19d60947a147fdb49391234d022114"
menu_path: ["Missing params property on getStaticPaths route."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/get-image-not-used-on-server/index.md", "title": "getImage() must be used on the server."}
nav_next: {"path": "astro/en/reference/errors/get-static-paths-removed-rsshelper/index.md", "title": "getStaticPaths RSS helper is not available anymore."}
---

# Missing params property on getStaticPaths route.

> **GetStaticPathsExpectedParams**: Missing or empty required `params` property on `getStaticPaths` route.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Every route specified by `getStaticPaths` require a `params` property specifying the path parameters needed to match the route.

For instance, the following code:

```
---export async function getStaticPaths() {  return [    { params: { id: '1' } }  ];}---
```

Will create the following route: `site.com/blog/1`.

**See Also:**

*   [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
*   [`params`](/en/reference/api-reference/#params)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
