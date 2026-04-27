---
title: "dynamicParams"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:31.298Z"
content_hash: "fc413d6cde2bc65ab4543f5c4297a106435fe975242f6f951c81edf388012ccf"
menu_path: ["dynamicParams"]
section_path: []
version: "latest"
content_language: "en"
---
[File-system conventions](/docs/app/api-reference/file-conventions)[Route Segment Config](/docs/app/api-reference/file-conventions/route-segment-config)dynamicParams

# dynamicParams

Last updated April 23, 2026

The `dynamicParams` option allows you to control what happens when a dynamic segment is visited that was not generated with [generateStaticParams](/docs/app/api-reference/functions/generate-static-params).

layout.tsx | page.tsx

JavaScriptTypeScript

```
export const dynamicParams = true // true | false
```

-   **`true`** (default): Dynamic route segments not included in `generateStaticParams` are generated at request time.
-   **`false`**: Dynamic route segments not included in `generateStaticParams` will return a 404.

> **Good to know**:
> 
> -   This option replaces the `fallback: true | false | blocking` option of `getStaticPaths` in the `pages` directory.
> -   `dynamicParams` is not available when [Cache Components](/docs/app/api-reference/config/next-config-js/cacheComponents) is enabled.

Was this helpful?
