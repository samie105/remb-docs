---
title: "Route Segment Config"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:29.700Z"
content_hash: "2475295ecf58241d2037aaba0cdc31643196ce6145f10d9105d70ec2fe719f09"
menu_path: ["Route Segment Config"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/metadata/sitemap/index.md", "title": "sitemap.xml"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/index.md", "title": "Functions"}
---

# Route Segment Config

Last updated April 23, 2026

The Route Segment Config options allow you to configure the behavior of a [Page](../page/index.md), [Layout](../layout/index.md), or [Route Handler](../route/index.md) by directly exporting the following variables:

| Option | Type | Default |
| --- | --- | --- |
| [`dynamicParams`](dynamicParams/index.md) | `boolean` | `true` |
| [`runtime`](runtime/index.md) | `'nodejs' | 'edge'` | `'nodejs'` |
| [`preferredRegion`](preferredRegion/index.md) | `'auto' | 'global' | 'home' | string | string[]` | `'auto'` |
| [`maxDuration`](maxDuration/index.md) | `number` | Set by deployment platform |

## Version History[](#version-history)

| Version |  |
| --- | --- |
| `v16.0.0` | `dynamic`, `dynamicParams`, `revalidate`, and `fetchCache` removed when [Cache Components](../../config/next-config-js/cacheComponents/index.md) is enabled. See [Caching and Revalidating (Previous Model)](../../../guides/caching-without-cache-components/index.md#route-segment-config). |
| `v16.0.0` | `export const experimental_ppr = true` removed. A [codemod](../../../guides/upgrading/codemods/index.md#remove-experimental_ppr-route-segment-config-from-app-router-pages-and-layouts) is available. |
| `v15.0.0-RC` | `export const runtime = "experimental-edge"` deprecated. A [codemod](../../../guides/upgrading/codemods/index.md#transform-app-router-route-segment-config-runtime-value-from-experimental-edge-to-edge) is available. |

[

### dynamicParams

API reference for the dynamicParams route segment config option.

](dynamicParams/index.md)[

### maxDuration

API reference for the maxDuration route segment config option.

](maxDuration/index.md)[

### preferredRegion

API reference for the preferredRegion route segment config option.

](preferredRegion/index.md)[

### runtime

API reference for the runtime route segment config option.

](runtime/index.md)

Was this helpful?
