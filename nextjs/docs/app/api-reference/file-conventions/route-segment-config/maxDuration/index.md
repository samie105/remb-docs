---
title: "maxDuration"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/maxDuration"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/maxDuration"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:50.879Z"
content_hash: "4814c61429fb1ca6f37bf52d4d7b73e5968ced286754c8ed77b55249cf4a5b02"
menu_path: ["maxDuration"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams/index.md", "title": "dynamicParams"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion/index.md", "title": "preferredRegion"}
---

# maxDuration

Last updated April 15, 2026

The `maxDuration` option allows you to set the maximum execution time (in seconds) for server-side logic in a route segment. Deployment platforms can use `maxDuration` from the Next.js build output to add specific execution limits.

layout.tsx | page.tsx | route.ts

TypeScript

JavaScriptTypeScript

```
export const maxDuration = 5
```

## Server Actions[](#server-actions)

If using [Server Actions](/docs/app/getting-started/mutating-data), set the `maxDuration` at the page level to change the default timeout of all Server Actions used on the page.

## Version History[](#version-history)

Version

Changes

`v13.4.10`

`maxDuration` introduced.

[Previous

dynamicParams

](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)

[Next

preferredRegion

](/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion)

Was this helpful?

supported.

Send
