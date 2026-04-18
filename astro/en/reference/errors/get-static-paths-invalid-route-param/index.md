---
title: "Invalid route parameter returned by getStaticPaths()."
source: "https://docs.astro.build/en/reference/errors/get-static-paths-invalid-route-param/"
canonical_url: "https://docs.astro.build/en/reference/errors/get-static-paths-invalid-route-param/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:51.657Z"
content_hash: "7397a18eb2560e2697b372f90caa31b575f6c39923457260cc5e6ab48db960e9"
menu_path: ["Invalid route parameter returned by getStaticPaths()."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/get-static-paths-removed-rsshelper/index.md", "title": "getStaticPaths RSS helper is not available anymore."}
nav_next: {"path": "astro/en/reference/errors/get-static-paths-required/index.md", "title": "getStaticPaths() function required for dynamic routes."}
---

# Invalid route parameter returned by getStaticPaths().

> **GetStaticPathsInvalidRouteParam**: Invalid `getStaticPaths()` route parameter for `KEY`. Expected a string or undefined, received `VALUE_TYPE` (`VALUE`)

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Since `params` are encoded into the URL, only certain types are supported as values.

```
---export async function getStaticPaths() {  return [    { params: { id: '1' } } // Works    { params: { id: 2 } } // Does not work    { params: { id: false } } // Does not work    { params: { id: [1, 2] } } // Does not work  ];}---
```

In routes using [rest parameters](/en/guides/routing/#rest-parameters), `undefined` can be used to represent a path with no parameters passed in the URL:

```
---export async function getStaticPaths() {  return [    { params: { id: '1' } } // /route/1    { params: { id: '2' } } // /route/2    { params: { id: undefined } } // /route/  ];}---
```

**See Also:**

*   [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
*   [`params`](/en/reference/api-reference/#params)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
