---
title: "dynamicParams"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:49.163Z"
content_hash: "64a31c713b5d05d9bbcb69051d5b2406473f8506ad3626d048fa6605d5acc7a5"
menu_path: ["dynamicParams"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/route/index.md", "title": "route.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/route-segment-config/maxDuration/index.md", "title": "maxDuration"}
---

# dynamicParams

Last updated April 15, 2026

The `dynamicParams` option allows you to control what happens when a dynamic segment is visited that was not generated with [generateStaticParams](/docs/app/api-reference/functions/generate-static-params).

layout.tsx | page.tsx

TypeScript

JavaScriptTypeScript

```
export const dynamicParams = true // true | false
```

*   **`true`** (default): Dynamic route segments not included in `generateStaticParams` are generated at request time.
*   **`false`**: Dynamic route segments not included in `generateStaticParams` will return a 404.

> **Good to know**:
> 
> *   This option replaces the `fallback: true | false | blocking` option of `getStaticPaths` in the `pages` directory.
> *   `dynamicParams` is not available when [Cache Components](/docs/app/api-reference/config/next-config-js/cacheComponents) is enabled.

[Previous

Route Segment Config

](/docs/app/api-reference/file-conventions/route-segment-config)

[Next

maxDuration

](/docs/app/api-reference/file-conventions/route-segment-config/maxDuration)

Was this helpful?

supported.

Send




