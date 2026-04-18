---
title: "preferredRegion"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:53.422Z"
content_hash: "92937ce90651115d5d9c701ea457d841f29b4616d05dbbddde68ae1db00559b0"
menu_path: ["preferredRegion"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/route-segment-config/maxDuration/index.md", "title": "maxDuration"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/route-segment-config/runtime/index.md", "title": "runtime"}
---

# preferredRegion

Last updated April 15, 2026

The `preferredRegion` option allows you to specify the preferred deployment region for a route segment. This value is passed to your deployment platform.

layout.tsx | page.tsx | route.ts

TypeScript

JavaScriptTypeScript

```
export const preferredRegion = // string || string[]
```

*   **`string`**: Deploy the route to a specific region. Available region codes are platform-specific. For example, `'iad1'`.
*   **`string[]`**: Deploy the route to multiple specific regions. The route is deployed to **all** listed regions, not a single one chosen from the list. For example, `['iad1', 'sfo1']`.

> **Good to know**:
> 
> *   If a `preferredRegion` is not specified, it will inherit the option of the nearest parent layout. The root layout defaults to `'auto'`.
> *   A child segment's value overrides the parent, values are not merged.
> *   Next.js passes the region values through to the deployment platform. The exact behavior and available region codes are platform-specific. Refer to your deployment platform's documentation for supported values.

## Vercel[](#vercel)

If deploying Next.js on Vercel, regions are only supported if `export const runtime = 'edge'` is set. The following options can be passed:

*   **`'auto'`** (default): Uses the default region.
*   **`'global'`**: Prefer deploying the route to all availableregions.
*   **`'home'`**: Prefer deploying the route to the home region.

If an unsupported value is passed, an error will be thrown.

[Previous

maxDuration

](/docs/app/api-reference/file-conventions/route-segment-config/maxDuration)

[Next

runtime

](/docs/app/api-reference/file-conventions/route-segment-config/runtime)

Was this helpful?

supported.

Send




