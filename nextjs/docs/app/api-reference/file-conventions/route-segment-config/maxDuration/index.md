---
title: "maxDuration"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/maxDuration"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/maxDuration"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:34.113Z"
content_hash: "bb2a992e6d5628c0b1635bbde2057996f769aa1e694f4f3e5229d9f666ed2ed1"
menu_path: ["maxDuration"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../dynamicParams/index.md", "title": "dynamicParams"}
nav_next: {"path": "../preferredRegion/index.md", "title": "preferredRegion"}
---

# maxDuration

Last updated April 23, 2026

The `maxDuration` option allows you to set the maximum execution time (in seconds) for server-side logic in a route segment. Deployment platforms can use `maxDuration` from the Next.js build output to add specific execution limits.

layout.tsx | page.tsx | route.ts

JavaScriptTypeScript

```
export const maxDuration = 5
```

## Server Actions[](#server-actions)

If using [Server Actions](/docs/app/getting-started/mutating-data), set the `maxDuration` at the page level to change the default timeout of all Server Actions used on the page.

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v13.4.10` | `maxDuration` introduced. |

Was this helpful?
