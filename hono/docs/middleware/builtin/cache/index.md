---
title: "Cache Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/cache"
canonical_url: "https://hono.dev/docs/middleware/builtin/cache"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:11.242Z"
content_hash: "b8963488be6d648636ffdcab3342fac8cf12168efa97523504984050e0af20a4"
menu_path: ["Cache Middleware ​"]
section_path: []
nav_prev: {"path": "hono/docs/middleware/builtin/body-limit/index.md", "title": "Body Limit Middleware \u200b"}
nav_next: {"path": "hono/docs/middleware/builtin/combine/index.md", "title": "Combine Middleware \u200b"}
---

## Cache Middleware [​](#cache-middleware)

The Cache middleware uses the Web Standards' [Cache API](https://developer.mozilla.org/en-US/docs/Web/API/Cache).

The Cache middleware currently supports Cloudflare Workers projects using custom domains and Deno projects using [Deno 1.26+](https://github.com/denoland/deno/releases/tag/v1.26.0). Also available with Deno Deploy.

Cloudflare Workers respects the `Cache-Control` header and return cached responses. For details, refer to [Cache on Cloudflare Docs](https://developers.cloudflare.com/workers/runtime-apis/cache/). Deno does not respect headers, so if you need to update the cache, you will need to implement your own mechanism.

See [Usage](#usage) below for instructions on each platform.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { cache } from 'hono/cache'
```

## Usage [​](#usage)

Cloudflare WorkersDeno

ts

```
app.get(
  '*',
  cache({
    cacheName: 'my-app',
    cacheControl: 'max-age=3600',
  })
)
```

ts

```
// Must use `wait: true` for the Deno runtime
app.get(
  '*',
  cache({
    cacheName: 'my-app',
    cacheControl: 'max-age=3600',
    wait: true,
  })
)
```

## Options [​](#options)

### required cacheName: `string` | `(c: Context) => string` | `Promise<string>` [​](#cachename-string-c-context-string-promise-string)

The name of the cache. Can be used to store multiple caches with different identifiers.

### optional wait: `boolean` [​](#wait-boolean)

A boolean indicating if Hono should wait for the Promise of the `cache.put` function to resolve before continuing with the request. _Required to be true for the Deno environment_. The default is `false`.

### optional cacheControl: `string` [​](#cachecontrol-string)

A string of directives for the `Cache-Control` header. See the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) for more information. When this option is not provided, no `Cache-Control` header is added to requests.

### optional vary: `string` | `string[]` [​](#vary-string-string)

Sets the `Vary` header in the response. If the original response header already contains a `Vary` header, the values are merged, removing any duplicates. Setting this to `*` will result in an error. For more details on the Vary header and its implications for caching strategies, refer to the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary).

### optional keyGenerator: `(c: Context) => string | Promise<string>` [​](#keygenerator-c-context-string-promise-string)

Generates keys for every request in the `cacheName` store. This can be used to cache data based on request parameters or context parameters. The default is `c.req.url`.

### optional cacheableStatusCodes: `number[]` [​](#cacheablestatuscodes-number)

An array of status codes that should be cached. The default is `[200]`. Use this option to cache responses with specific status codes.

ts

```
app.get(
  '*',
  cache({
    cacheName: 'my-app',
    cacheControl: 'max-age=3600',
    cacheableStatusCodes: [200, 404, 412],
  })
)
```

### optional onCacheNotAvailable: `(() => void | Promise<void>)` | `false` [​](#oncachenotavailable-void-promise-void-false)

A callback function or `false` that controls the behavior when the Cache API is not available in the global scope. By default, a message is logged with `console.log`. You can provide a custom function to customize the behavior, or set it to `false` to suppress the log entirely.

ts

```
// Custom logging
app.use(
  cache({
    cacheName: 'my-app-v1',
    onCacheNotAvailable: () => {
      console.log('Custom log: Cache API is not available.')
    },
  })
)
```

ts

```
// Suppress logging
app.use(
  cache({
    cacheName: 'my-app-v1',
    onCacheNotAvailable: false,
  })
)
```


