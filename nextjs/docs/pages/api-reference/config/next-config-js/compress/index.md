---
title: "compress"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:24.913Z"
content_hash: "540ec21b16eb950fd09a78e61d0a807f380fa69c788d748408693234b79c71ae"
menu_path: ["compress"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies/index.md", "title": "bundlePagesRouterDependencies"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/crossOrigin/index.md", "title": "crossOrigin"}
---

# compress

Last updated April 15, 2026

By default, Next.js uses `gzip` to compress rendered content and static files when using `next start` or a custom server. This is an optimization for applications that do not have compression configured. If compression is _already_ configured in your application via a custom server, Next.js will not add compression.

You can check if compression is enabled and which algorithm is used by looking at the [`Accept-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding) (browser accepted options) and [`Content-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) (currently used) headers in the response.

## Disabling compression[](#disabling-compression)

To disable **compression**, set the `compress` config option to `false`:

next.config.js

```
module.exports = {
  compress: false,
}
```

We **do not recommend disabling compression** unless you have compression configured on your server, as compression reduces bandwidth usage and improves the performance of your application. For example, you're using [nginx](https://nginx.org/) and want to switch to `brotli`, set the `compress` option to `false` to allow nginx to handle compression.

Was this helpful?

supported.

Send
