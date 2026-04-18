---
title: "ETag Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/etag"
canonical_url: "https://hono.dev/docs/middleware/builtin/etag"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:27.289Z"
content_hash: "7053ff415d57b99239de454a3e39d39d3035cf7e584eebb6483038cb44016c92"
menu_path: ["ETag Middleware ​"]
section_path: []
nav_prev: {"path": "hono/docs/middleware/builtin/csrf/index.md", "title": "CSRF Protection \u200b"}
nav_next: {"path": "hono/docs/middleware/builtin/ip-restriction/index.md", "title": "IP Restriction Middleware \u200b"}
---

## ETag Middleware [​](#etag-middleware)

Using this middleware, you can add ETag headers easily.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { etag } from 'hono/etag'
```

## Usage [​](#usage)

ts

```
const app = new Hono()

app.use('/etag/*', etag())
app.get('/etag/abc', (c) => {
  return c.text('Hono is cool')
})
```

## The retained headers [​](#the-retained-headers)

The 304 Response must include the headers that would have been sent in an equivalent 200 OK response. The default headers are Cache-Control, Content-Location, Date, ETag, Expires, and Vary.

If you want to add the header that is sent, you can use `retainedHeaders` option and `RETAINED_304_HEADERS` strings array variable that includes the default headers:

ts

```
import { etag, RETAINED_304_HEADERS } from 'hono/etag'

// ...

app.use(
  '/etag/*',
  etag({
    retainedHeaders: ['x-message', ...RETAINED_304_HEADERS],
  })
)
```

## Options [​](#options)

### optional weak: `boolean` [​](#weak-boolean)

Define using or not using a [weak validation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests#weak_validation). If `true` is set, then `w/` is added to the prefix of the value. The default is `false`.

### optional retainedHeaders: `string[]` [​](#retainedheaders-string)

The headers that you want to retain in the 304 Response.

### optional generateDigest: `(body: Uint8Array) => ArrayBuffer | Promise<ArrayBuffer>` [​](#generatedigest-body-uint8array-arraybuffer-promise-arraybuffer)

A custom digest generation function. By default, it uses `SHA-1`. This function is called with the response body as a `Uint8Array` and should return a hash as an `ArrayBuffer` or a Promise of one.
