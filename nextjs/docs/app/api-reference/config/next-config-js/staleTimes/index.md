---
title: "staleTimes"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:37.894Z"
content_hash: "118240fdc090891c173cfecaf76284b0b789c98b11f651bc6bb8a3913496a99e"
menu_path: ["staleTimes"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/serverExternalPackages/index.md", "title": "serverExternalPackages"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/staticGeneration/index.md", "title": "staticGeneration*"}
---

# staleTimes

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

`staleTimes` is an experimental feature that enables caching of page segments in the [Client Cache](/docs/app/glossary#client-cache).

You can enable this experimental feature and provide custom revalidation times by setting the experimental `staleTimes` flag:

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    staleTimes: {
      dynamic: 30,
      static: 180,
    },
  },
}
 
module.exports = nextConfig
```

The `static` and `dynamic` properties correspond with the time period (in seconds) based on different types of [link prefetching](/docs/app/api-reference/components/link#prefetch).

*   The `dynamic` property is used when the page is neither statically generated nor fully prefetched (e.g. with `prefetch={true}`).
    *   Default: 0 seconds (not cached)
*   The `static` property is used for statically generated pages, or when the `prefetch` prop on `Link` is set to `true`, or when calling [`router.prefetch`](/docs/app/api-reference/functions/use-router).
    *   Default: 5 minutes

> **Good to know:**
> 
> *   [Loading boundaries](/docs/app/api-reference/file-conventions/loading) are considered reusable for the `static` period defined in this configuration.
> *   This doesn't affect [partial rendering](/docs/app/getting-started/linking-and-navigating#client-side-transitions), **meaning shared layouts won't automatically be refetched on every navigation, only the page segment that changes.**
> *   This doesn't change [back/forward caching](/docs/app/glossary#client-cache) behavior to prevent layout shift and to prevent losing the browser scroll position.

### Version History[](#version-history)

Version

Changes

`v15.0.0`

The `dynamic` `staleTimes` default changed from 30s to 0s.

`v14.2.0`

Experimental `staleTimes` introduced.

[Previous

serverExternalPackages

](/docs/app/api-reference/config/next-config-js/serverExternalPackages)

[Next

staticGeneration\*

](/docs/app/api-reference/config/next-config-js/staticGeneration)

Was this helpful?

supported.

Send


