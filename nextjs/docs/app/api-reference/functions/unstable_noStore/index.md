---
title: "unstable_noStore"
source: "https://nextjs.org/docs/app/api-reference/functions/unstable_noStore"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/unstable_noStore"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:12:20.363Z"
content_hash: "d63e6b23976cf8e19504da958ee5b1e8c1ff1f28740433ce9a689472e1ba894d"
menu_path: ["unstable_noStore"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/unstable_cache/index.md", "title": "unstable_cache"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/unstable_rethrow/index.md", "title": "unstable_rethrow"}
---

# unstable\_noStore

This is a legacy API and no longer recommended. It's still supported for backward compatibility.

Last updated April 15, 2026

**In version 15, we recommend using [`connection`](/docs/app/api-reference/functions/connection) instead of `unstable_noStore`.**

`unstable_noStore` can be used to declaratively opt out of prerendering and indicate a particular component should not be cached.

```
import { unstable_noStore as noStore } from 'next/cache';
 
export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

> **Good to know**:
> 
> *   `unstable_noStore` is equivalent to `cache: 'no-store'` on a `fetch`
> *   `unstable_noStore` is preferred over `export const dynamic = 'force-dynamic'` as it is more granular and can be used on a per-component basis

*   Using `unstable_noStore` inside [`unstable_cache`](/docs/app/api-reference/functions/unstable_cache) will not opt out of static generation. Instead, it will defer to the cache configuration to determine whether to cache the result or not.

## Usage[](#usage)

If you prefer not to pass additional options to `fetch`, like `cache: 'no-store'`, `next: { revalidate: 0 }` or in cases where `fetch` is not available, you can use `noStore()` as a replacement for all of these use cases.

```
import { unstable_noStore as noStore } from 'next/cache';
 
export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

## Version History[](#version-history)

Version

Changes

`v15.0.0`

`unstable_noStore` deprecated for `connection`.

`v14.0.0`

`unstable_noStore` introduced.

[Previous

unstable\_cache

](/docs/app/api-reference/functions/unstable_cache)

[Next

unstable\_rethrow

](/docs/app/api-reference/functions/unstable_rethrow)

Was this helpful?

supported.

Send
