---
title: "Proxy Helper ​"
source: "https://hono.dev/docs/helpers/proxy"
canonical_url: "https://hono.dev/docs/helpers/proxy"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:05.452Z"
content_hash: "f6645f0e5fb95e15ed26e257244baac143f0c0a347ee78196e26f3e55063bae9"
menu_path: ["Proxy Helper ​"]
section_path: []
nav_prev: {"path": "hono/docs/helpers/jwt/index.md", "title": "JWT Authentication Helper \u200b"}
nav_next: {"path": "hono/docs/helpers/route/index.md", "title": "Route Helper \u200b"}
---

Proxy Helper provides useful functions when using Hono application as a (reverse) proxy.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { proxy } from 'hono/proxy'
```

## `proxy()` [​](#proxy)

`proxy()` is a `fetch()` API wrapper for proxy. The parameters and return value are the same as for `fetch()` (except for the proxy-specific options).

The `Accept-Encoding` header is replaced with an encoding that the current runtime can handle. Unnecessary response headers are removed, and a `Response` object is returned that can be sent from the handler.

### Examples [​](#examples)

Simple usage:

ts

```
app.get('/proxy/:path', (c) => {
  return proxy(`http://${originServer}/${c.req.param('path')}`)
})
```

Complicated usage:

ts

```
app.get('/proxy/:path', async (c) => {
  const res = await proxy(
    `http://${originServer}/${c.req.param('path')}`,
    {
      headers: {
        ...c.req.header(), // optional, specify only when forwarding all the request data (including credentials) is necessary.
        'X-Forwarded-For': '127.0.0.1',
        'X-Forwarded-Host': c.req.header('host'),
        Authorization: undefined, // do not propagate request headers contained in c.req.header('Authorization')
      },
    }
  )
  res.headers.delete('Set-Cookie')
  return res
})
```

Or you can pass the `c.req` as a parameter.

ts

```
app.all('/proxy/:path', (c) => {
  return proxy(`http://${originServer}/${c.req.param('path')}`, {
    ...c.req, // optional, specify only when forwarding all the request data (including credentials) is necessary.
    headers: {
      ...c.req.header(),
      'X-Forwarded-For': '127.0.0.1',
      'X-Forwarded-Host': c.req.header('host'),
      Authorization: undefined, // do not propagate request headers contained in c.req.header('Authorization')
    },
  })
})
```

You can override the default global `fetch` function with the `customFetch` option:

ts

```
app.get('/proxy', (c) => {
  return proxy('https://example.com/', {
    customFetch,
  })
})
```

### Connection Header Processing [​](#connection-header-processing)

By default, `proxy()` ignores the `Connection` header to prevent Hop-by-Hop Header Injection attacks. You can enable strict RFC 9110 compliance with the `strictConnectionProcessing` option:

ts

```
// Default behavior (recommended for untrusted clients)
app.get('/proxy/:path', (c) => {
  return proxy(`http://${originServer}/${c.req.param('path')}`, c.req)
})

// Strict RFC 9110 compliance (use only in trusted environments)
app.get('/internal-proxy/:path', (c) => {
  return proxy(`http://${internalServer}/${c.req.param('path')}`, {
    ...c.req,
    strictConnectionProcessing: true,
  })
})
```

### `ProxyFetch` [​](#proxyfetch)

The type of `proxy()` is defined as `ProxyFetch` and is as follows

ts

```
interface ProxyRequestInit extends Omit<RequestInit, 'headers'> {
  raw?: Request
  customFetch?: (request: Request) => Promise<Response>
  strictConnectionProcessing?: boolean
  headers?:
    | HeadersInit
    | [string, string][]
    | Record<RequestHeader, string | undefined>
    | Record<string, string | undefined>
}

interface ProxyFetch {
  (
    input: string | URL | Request,
    init?: ProxyRequestInit
  ): Promise<Response>
}
```
