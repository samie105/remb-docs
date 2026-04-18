---
title: "App - Hono ​"
source: "https://hono.dev/docs/api/hono"
canonical_url: "https://hono.dev/docs/api/hono"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:48.347Z"
content_hash: "2e59f321090262cd8d7eb62db166b1f1236011ee88fb87b04f3cbbf6ca4456bf"
menu_path: ["App - Hono ​"]
section_path: []
nav_prev: {"path": "hono/docs/getting-started/nodejs/index.md", "title": "Node.js \u200b"}
nav_next: {"path": "hono/docs/api/routing/index.md", "title": "Routing \u200b"}
---

`Hono` is the primary object. It will be imported first and used until the end.

ts

```
import { Hono } from 'hono'

const app = new Hono()
//...

export default app // for Cloudflare Workers or Bun
```

## Methods [​](#methods)

An instance of `Hono` has the following methods.

*   app.**HTTP\_METHOD**(\[path,\]handler|middleware...)
*   app.**all**(\[path,\]handler|middleware...)
*   app.**on**(method|method\[\], path|path\[\], handler|middleware...)
*   app.**use**(\[path,\]middleware)
*   app.**route**(path, \[app\])
*   app.**basePath**(path)
*   app.**notFound**(handler)
*   app.**onError**(err, handler)
*   app.**mount**(path, anotherApp)
*   app.**fire**()
*   app.**fetch**(request, env, event)
*   app.**request**(path, options)

The first part of them is used for routing, please refer to the [routing section](hono/docs/api/routing/index.md).

## Not Found [​](#not-found)

`app.notFound` allows you to customize a Not Found Response.

ts

```
app.notFound((c) => {
  return c.text('Custom 404 Message', 404)
})
```

WARNING

The `notFound` method is only called from the top-level app. For more information, see this [issue](https://github.com/honojs/hono/issues/3465#issuecomment-2381210165).

## Error Handling [​](#error-handling)

`app.onError` allows you to handle uncaught errors and return a custom Response.

ts

```
app.onError((err, c) => {
  console.error(`${err}`)
  return c.text('Custom Error Message', 500)
})
```

INFO

If both a parent app and its routes have `onError` handlers, the route-level handlers get priority.

## fire() [​](#fire)

`app.fire()` automatically adds a global `fetch` event listener.

This can be useful for environments that adhere to the [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API), such as [non-ES module Cloudflare Workers](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/).

`app.fire()` executes the following for you:

ts

```
addEventListener('fetch', (event: FetchEventLike): void => {
  event.respondWith(this.dispatch(...))
})
```

## fetch() [​](#fetch)

`app.fetch` will be the entry point of your application.

For Cloudflare Workers, you can use the following:

ts

```
export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    return app.fetch(request, env, ctx)
  },
}
```

or just do:

ts

```
export default app
```

Bun:

ts

```
export default app 
export default {  
  port: 3000, 
  fetch: app.fetch, 
} 
```

## request() [​](#request)

`request` is a useful method for testing.

You can pass a URL or pathname to send a GET request. `app` will return a `Response` object.

ts

```
test('GET /hello is ok', async () => {
  const res = await app.request('/hello')
  expect(res.status).toBe(200)
})
```

You can also pass a `Request` object:

ts

```
test('POST /message is ok', async () => {
  const req = new Request('Hello!', {
    method: 'POST',
  })
  const res = await app.request(req)
  expect(res.status).toBe(201)
})
```

## mount() [​](#mount)

The `mount()` allows you to mount applications built with other frameworks into your Hono application.

ts

```
import { Router as IttyRouter } from 'itty-router'
import { Hono } from 'hono'

// Create itty-router application
const ittyRouter = IttyRouter()

// Handle `GET /itty-router/hello`
ittyRouter.get('/hello', () => new Response('Hello from itty-router'))

// Hono application
const app = new Hono()

// Mount!
app.mount('/itty-router', ittyRouter.handle)
```

## strict mode [​](#strict-mode)

Strict mode defaults to `true` and distinguishes the following routes.

*   `/hello`
*   `/hello/`

`app.get('/hello')` will not match `GET /hello/`.

By setting strict mode to `false`, both paths will be treated equally.

ts

```
const app = new Hono({ strict: false })
```

## router option [​](#router-option)

The `router` option specifies which router to use. The default router is `SmartRouter`. If you want to use `RegExpRouter`, pass it to a new `Hono` instance:

ts

```
import { RegExpRouter } from 'hono/router/reg-exp-router'

const app = new Hono({ router: new RegExpRouter() })
```

## Generics [​](#generics)

You can pass Generics to specify the types of Cloudflare Workers Bindings and variables used in `c.set`/`c.get`.

ts

```
type Bindings = {
  TOKEN: string
}

type Variables = {
  user: User
}

const app = new Hono<{
  Bindings: Bindings
  Variables: Variables
}>()

app.use('/auth/*', async (c, next) => {
  const token = c.env.TOKEN // token is `string`
  // ...
  c.set('user', user) // user should be `User`
  await next()
})
```

