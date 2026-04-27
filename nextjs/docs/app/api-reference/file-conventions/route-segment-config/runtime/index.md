---
title: "runtime"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/runtime"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/runtime"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:38.192Z"
content_hash: "6bbbd2c074e6a192680805a1be60c676f16ae9cacd584186524f0992abd9ce97"
menu_path: ["runtime"]
section_path: []
version: "latest"
content_language: "en"
---
[File-system conventions](/docs/app/api-reference/file-conventions)[Route Segment Config](/docs/app/api-reference/file-conventions/route-segment-config)runtime

# runtime

Last updated April 23, 2026

The `runtime` option allows you to select the JavaScript runtime used for rendering your route.

layout.tsx | page.tsx | route.ts

JavaScriptTypeScript

```
export const runtime = 'nodejs'
// 'nodejs' | 'edge'
```

-   **`'nodejs'`** (default)
-   **`'edge'`**

> **Good to know**:
> 
> -   Using `runtime: 'edge'` is **not supported** for Cache Components.
> -   This option cannot be used in [Proxy](/docs/app/api-reference/file-conventions/proxy).

Was this helpful?
