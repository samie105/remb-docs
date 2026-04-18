---
title: "CORS Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/cors"
canonical_url: "https://hono.dev/docs/middleware/builtin/cors"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:50.220Z"
content_hash: "581b36e80a44eea24df1db5c0aafe05e9c7f9feeed7fe60f9560634005980c80"
menu_path: ["CORS Middleware ​"]
section_path: []
---
## CORS Middleware [​](#cors-middleware)

There are many use cases of Cloudflare Workers as Web APIs and calling them from external front-end application. For them we have to implement CORS, let's do this with middleware as well.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { cors } from 'hono/cors'
```

## Usage [​](#usage)

ts

```
const app = new Hono()

// CORS should be called before the route
app.use('/api/*', cors())
app.use(
  '/api2/*',
  cors({
    origin: 'http://example.com',
    allowHeaders: ['X-Custom-Header', 'Upgrade-Insecure-Requests'],
    allowMethods: ['POST', 'GET', 'OPTIONS'],
    exposeHeaders: ['Content-Length', 'X-Kuma-Revision'],
    maxAge: 600,
    credentials: true,
  })
)

app.all('/api/abc', (c) => {
  return c.json({ success: true })
})
app.all('/api2/abc', (c) => {
  return c.json({ success: true })
})
```

Multiple origins:

ts

```
app.use(
  '/api3/*',
  cors({
    origin: ['https://example.com', 'https://example.org'],
  })
)

// Or you can use "function"
app.use(
  '/api4/*',
  cors({
    // `c` is a `Context` object
    origin: (origin, c) => {
      return origin.endsWith('.example.com')
        ? origin
        : 'http://example.com'
    },
  })
)
```

Dynamic allowed methods based on origin:

ts

```
app.use(
  '/api5/*',
  cors({
    origin: (origin) =>
      origin === 'https://example.com' ? origin : '*',
    // `c` is a `Context` object
    allowMethods: (origin, c) =>
      origin === 'https://example.com'
        ? ['GET', 'HEAD', 'POST', 'PATCH', 'DELETE']
        : ['GET', 'HEAD'],
  })
)
```

## Options [​](#options)

### optional origin: `string` | `string[]` | `(origin:string, c:Context) => string` [​](#origin-string-string-origin-string-c-context-string)

The value of "_Access-Control-Allow-Origin_" CORS header. You can also pass the callback function like `origin: (origin) => (origin.endsWith('.example.com') ? origin : 'http://example.com')`. The default is `*`.

### optional allowMethods: `string[]` | `(origin:string, c:Context) => string[]` [​](#allowmethods-string-origin-string-c-context-string)

The value of "_Access-Control-Allow-Methods_" CORS header. You can also pass a callback function to dynamically determine allowed methods based on the origin. The default is `['GET', 'HEAD', 'PUT', 'POST', 'DELETE', 'PATCH']`.

### optional allowHeaders: `string[]` [​](#allowheaders-string)

The value of "_Access-Control-Allow-Headers_" CORS header. The default is `[]`.

### optional maxAge: `number` [​](#maxage-number)

The value of "_Access-Control-Max-Age_" CORS header.

### optional credentials: `boolean` [​](#credentials-boolean)

The value of "_Access-Control-Allow-Credentials_" CORS header.

### optional exposeHeaders: `string[]` [​](#exposeheaders-string)

The value of "_Access-Control-Expose-Headers_" CORS header. The default is `[]`.

## Environment-dependent CORS configuration [​](#environment-dependent-cors-configuration)

If you want to adjust CORS configuration according to the execution environment, such as development or production, injecting values from environment variables is convenient as it eliminates the need for the application to be aware of its own execution environment. See the example below for clarification.

ts

```
app.use('*', async (c, next) => {
  const corsMiddlewareHandler = cors({
    origin: c.env.CORS_ORIGIN,
  })
  return corsMiddlewareHandler(c, next)
})
```

## Using with Vite [​](#using-with-vite)

When using Hono with Vite, you should disable Vite's built-in CORS feature by setting `server.cors` to `false` in your `vite.config.ts`. This prevents conflicts with Hono's CORS middleware.

ts

```
// vite.config.ts
import { cloudflare } from '@cloudflare/vite-plugin'
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    cors: false, // disable Vite's built-in CORS setting
  },
  plugins: [cloudflare()],
})
```
