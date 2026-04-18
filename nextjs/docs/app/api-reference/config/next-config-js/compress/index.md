---
title: "compress"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/compress"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/compress"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:10.242Z"
content_hash: "09c55c598dad989591bd420606b3b8ba566308443fec83cdc68082a432f836db"
menu_path: ["compress"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/cacheLife/index.md", "title": "cacheLife"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/crossOrigin/index.md", "title": "crossOrigin"}
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

[Previous

cacheLife

](/docs/app/api-reference/config/next-config-js/cacheLife)

[Next

crossOrigin

](/docs/app/api-reference/config/next-config-js/crossOrigin)

Was this helpful?

supported.

Send




