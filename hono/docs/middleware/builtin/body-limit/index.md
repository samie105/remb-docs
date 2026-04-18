---
title: "Body Limit Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/body-limit"
canonical_url: "https://hono.dev/docs/middleware/builtin/body-limit"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:27.453Z"
content_hash: "794089e37d12608e53c2ba656dd87ed2295f2c4ce642f19b5027db6a8e490a8f"
menu_path: ["Body Limit Middleware ​"]
section_path: []
nav_prev: {"path": "hono/docs/middleware/builtin/bearer-auth/index.md", "title": "Bearer Auth Middleware \u200b"}
nav_next: {"path": "hono/docs/middleware/builtin/cache/index.md", "title": "Cache Middleware \u200b"}
---

## Body Limit Middleware [​](#body-limit-middleware)

The Body Limit Middleware can limit the file size of the request body.

This middleware first uses the value of the `Content-Length` header in the request, if present. If it is not set, it reads the body in the stream and executes an error handler if it is larger than the specified file size.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { bodyLimit } from 'hono/body-limit'
```

## Usage [​](#usage)

ts

```
const app = new Hono()

app.post(
  '/upload',
  bodyLimit({
    maxSize: 50 * 1024, // 50kb
    onError: (c) => {
      return c.text('overflow :(', 413)
    },
  }),
  async (c) => {
    const body = await c.req.parseBody()
    if (body['file'] instanceof File) {
      console.log(`Got file sized: ${body['file'].size}`)
    }
    return c.text('pass :)')
  }
)
```

## Options [​](#options)

### required maxSize: `number` [​](#maxsize-number)

The maximum file size of the file you want to limit. The default is `100 * 1024` - `100kb`.

### optional onError: `OnError` [​](#onerror-onerror)

The error handler to be invoked if the specified file size is exceeded.

## Usage with Bun for large requests [​](#usage-with-bun-for-large-requests)

If the Body Limit Middleware is used explicitly to allow a request body larger than the default, it might be necessary to make changes to your `Bun.serve` configuration accordingly. [At the time of writing](https://github.com/oven-sh/bun/blob/f2cfa15e4ef9d730fc6842ad8b79fb7ab4c71cb9/packages/bun-types/bun.d.ts#L2191), `Bun.serve`'s default request body limit is 128MiB. If you set Hono's Body Limit Middleware to a value bigger than that, your requests will still fail and, additionally, the `onError` handler specified in the middleware will not be called. This is because `Bun.serve()` will set the status code to `413` and terminate the connection before passing the request to Hono.

If you want to accept requests larger than 128MiB with Hono and Bun, you need to set the limit for Bun as well:

ts

```
export default {
  port: process.env['PORT'] || 3000,
  fetch: app.fetch,
  maxRequestBodySize: 1024 * 1024 * 200, // your value here
}
```

or, depending on your setup:

ts

```
Bun.serve({
  fetch(req, server) {
    return app.fetch(req, { ip: server.requestIP(req) })
  },
  maxRequestBodySize: 1024 * 1024 * 200, // your value here
})
```
