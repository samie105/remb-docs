---
title: "expireTime"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:26.727Z"
content_hash: "403da7503abf7745442a189e3cbaadc936f48a9ff277ef7a01c95a9132fc9146"
menu_path: ["expireTime"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/env/index.md", "title": "env"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/exportPathMap/index.md", "title": "exportPathMap"}
---

# expireTime

Last updated April 15, 2026

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

[Previous

env

](/docs/app/api-reference/config/next-config-js/env)

[Next

exportPathMap

](/docs/app/api-reference/config/next-config-js/exportPathMap)

Was this helpful?

supported.

Send


