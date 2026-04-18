---
title: "Route Segment Config"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:47.557Z"
content_hash: "2c392d8c069b7f5b1118eeae1b3c73f4acbccb0aa613eef2cb7d22ed0c3b1078"
menu_path: ["Route Segment Config"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/metadata/sitemap/index.md", "title": "sitemap.xml"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/index.md", "title": "Functions"}
---

# Route Segment Config

Last updated April 15, 2026

The Route Segment Config options allow you to configure the behavior of a [Page](/docs/app/api-reference/file-conventions/page), [Layout](/docs/app/api-reference/file-conventions/layout), or [Route Handler](/docs/app/api-reference/file-conventions/route) by directly exporting the following variables:

Option

Type

Default

[`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)

`boolean`

`true`

[`runtime`](/docs/app/api-reference/file-conventions/route-segment-config/runtime)

`'nodejs' | 'edge'`

`'nodejs'`

[`preferredRegion`](/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion)

`'auto' | 'global' | 'home' | string | string[]`

`'auto'`

[`maxDuration`](/docs/app/api-reference/file-conventions/route-segment-config/maxDuration)

`number`

Set by deployment platform

## Version History[](#version-history)

Version

`v16.0.0`

`dynamic`, `dynamicParams`, `revalidate`, and `fetchCache` removed when [Cache Components](/docs/app/api-reference/config/next-config-js/cacheComponents) is enabled. See [Caching and Revalidating (Previous Model)](/docs/app/guides/caching-without-cache-components#route-segment-config).

`v16.0.0`

`export const experimental_ppr = true` removed. A [codemod](/docs/app/guides/upgrading/codemods#remove-experimental_ppr-route-segment-config-from-app-router-pages-and-layouts) is available.

`v15.0.0-RC`

`export const runtime = "experimental-edge"` deprecated. A [codemod](/docs/app/guides/upgrading/codemods#transform-app-router-route-segment-config-runtime-value-from-experimental-edge-to-edge) is available.

[

### dynamicParams

API reference for the dynamicParams route segment config option.

](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)[

### maxDuration

API reference for the maxDuration route segment config option.

](/docs/app/api-reference/file-conventions/route-segment-config/maxDuration)[

### preferredRegion

API reference for the preferredRegion route segment config option.

](/docs/app/api-reference/file-conventions/route-segment-config/preferredRegion)[

### runtime

API reference for the runtime route segment config option.

](/docs/app/api-reference/file-conventions/route-segment-config/runtime)

[Previous

sitemap.xml

](/docs/app/api-reference/file-conventions/metadata/sitemap)

[Next

dynamicParams

](/docs/app/api-reference/file-conventions/route-segment-config/dynamicParams)

Was this helpful?

supported.

Send


