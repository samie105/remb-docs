---
title: "expireTime"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:17.322Z"
content_hash: "63b0edb29074bd48c5737f8536dfbdc34cb51c1685496f853cb86eb72b81626f"
menu_path: ["expireTime"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../env/index.md", "title": "env"}
nav_next: {"path": "../exportPathMap/index.md", "title": "exportPathMap"}
---

# expireTime

Last updated April 23, 2026

You can specify a custom `stale-while-revalidate` expire time for CDNs to consume in the `Cache-Control` header for ISR enabled pages.

Open `next.config.js` and add the `expireTime` config:

next.config.js

```
module.exports = {
  // one hour in seconds
  expireTime: 3600,
}
```

Now when sending the `Cache-Control` header the expire time will be calculated depending on the specific revalidate period.

For example, if you have a revalidate of 15 minutes on a path and the expire time is one hour the generated `Cache-Control` header will be `s-maxage=900, stale-while-revalidate=2700` so that it can stay stale for 15 minutes less than the configured expire time.

Was this helpful?
