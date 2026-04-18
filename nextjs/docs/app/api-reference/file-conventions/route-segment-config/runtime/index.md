---
title: "runtime"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/runtime"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/runtime"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:55.555Z"
content_hash: "99d4512211d798b6f8d943cfe2d576a76620bc790b1df1493fdde8a02f699d46"
menu_path: ["runtime"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion/index.md", "title": "preferredRegion"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/route-groups/index.md", "title": "Route Groups"}
---

# runtime

Last updated April 15, 2026

The `runtime` option allows you to select the JavaScript runtime used for rendering your route.

layout.tsx | page.tsx | route.ts

TypeScript

JavaScriptTypeScript

```
export const runtime = 'nodejs'
// 'nodejs' | 'edge'
```

*   **`'nodejs'`** (default)
*   **`'edge'`**

> **Good to know**:
> 
> *   Using `runtime: 'edge'` is **not supported** for Cache Components.
> *   This option cannot be used in [Proxy](/docs/app/api-reference/file-conventions/proxy).

[Previous

preferredRegion

](/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion)

[Next

Functions

](/docs/app/api-reference/functions)

Was this helpful?

supported.

Send
