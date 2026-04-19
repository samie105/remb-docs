---
title: "Context ​"
source: "https://hono.dev/docs/api/context"
canonical_url: "https://hono.dev/docs/api/context"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:55.464Z"
content_hash: "53b6bd807bc029ba30cbbef5071c7f45553b0b0d1ee3561a4993da6f7bb94a7e"
menu_path: ["Context ​"]
section_path: []
nav_prev: {"path": "hono/docs/api/routing/index.md", "title": "Routing \u200b"}
nav_next: {"path": "hono/docs/api/request/index.md", "title": "HonoRequest \u200b"}
---

The `Context` object is instantiated for each request and kept until the response is returned. You can put values in it, set headers and a status code you want to return, and access HonoRequest and Response objects.

## req [​](#req)

`req` is an instance of HonoRequest. For more details, see [HonoRequest](hono/docs/api/request/index.md).

ts

```
app.get('/hello', (c) => {
  const userAgent = c.req.header('User-Agent')
  // ...
})
```

## status() [​](#status)

You can set an HTTP status code with `c.status()`. The default is `200`. You don't have to use `c.status()` if the code is `200`.

ts

```
app.post('/posts', (c) => {
  // Set HTTP status code
  c.status(201)
  return c.text('Your post is created!')
})
```

## header() [​](#header)

You can set HTTP Headers for the response.

ts

```
app.get('/', (c) => {
  // Set headers
  c.header('X-Message', 'My custom message')
  return c.text('Hello!')
})
```

## body() [​](#body)

Return an HTTP response.

INFO

**Note**: When returning text or HTML, it is recommended to use `c.text()` or `c.html()`.

ts

```
app.get('/welcome', (c) => {
  c.header('Content-Type', 'text/plain')
  // Return the response body
  return c.body('Thank you for coming')
})
```

You can also write the following.

ts

```
app.get('/welcome', (c) => {
  return c.body('Thank you for coming', 201, {
    'X-Message': 'Hello!',
    'Content-Type': 'text/plain',
  })
})
```

The response is the same `Response` object as below.

ts

```
new Response('Thank you for coming', {
  status: 201,
  headers: {
    'X-Message': 'Hello!',
    'Content-Type': 'text/plain',
  },
})
```

## text() [​](#text)

Render text as `Content-Type: text/plain`.

ts

```
app.get('/say', (c) => {
  return c.text('Hello!')
})
```

## json() [​](#json)

Render JSON as `Content-Type: application/json`.

ts

```
app.get('/api', (c) => {
  return c.json({ message: 'Hello!' })
})
```

## html() [​](#html)

Render HTML as `Content-Type: text/html`.

ts

```
app.get('/', (c) => {
  return c.html('<h1>Hello! Hono!</h1>')
})
```

## notFound() [​](#notfound)

Return a `Not Found` Response. You can customize it with [`app.notFound()`](hono/docs/api/hono/index.md#not-found).

ts

```
app.get('/notfound', (c) => {
  return c.notFound()
})
```

## redirect() [​](#redirect)

Redirect, default status code is `302`.

ts

```
app.get('/redirect', (c) => {
  return c.redirect('/')
})
app.get('/redirect-permanently', (c) => {
  return c.redirect('/', 301)
})
```

## res [​](#res)

You can access the [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object that will be returned.

ts

```
// Response object
app.use('/', async (c, next) => {
  await next()
  c.res.headers.append('X-Debug', 'Debug message')
})
```

## set() / get() [​](#set-get)

Get and set arbitrary key-value pairs, with a lifetime of the current request. This allows passing specific values between middleware or from middleware to route handlers.

ts

```
app.use(async (c, next) => {
  c.set('message', 'Hono is cool!!')
  await next()
})

app.get('/', (c) => {
  const message = c.get('message')
  return c.text(`The message is "${message}"`)
})
```

Pass the `Variables` as Generics to the constructor of `Hono` to make it type-safe.

ts

```
type Variables = {
  message: string
}

const app = new Hono<{ Variables: Variables }>()
```

The value of `c.set` / `c.get` are retained only within the same request. They cannot be shared or persisted across different requests.

## var [​](#var)

You can also access the value of a variable with `c.var`.

ts

```
const result = c.var.client.oneMethod()
```

If you want to create the middleware which provides a custom method, write like the following:

ts

```
type Env = {
  Variables: {
    echo: (str: string) => string
  }
}

const app = new Hono()

const echoMiddleware = createMiddleware<Env>(async (c, next) => {
  c.set('echo', (str) => str)
  await next()
})

app.get('/echo', echoMiddleware, (c) => {
  return c.text(c.var.echo('Hello!'))
})
```

If you want to use the middleware in multiple handlers, you can use `app.use()`. Then, you have to pass the `Env` as Generics to the constructor of `Hono` to make it type-safe.

ts

```
const app = new Hono<Env>()

app.use(echoMiddleware)

app.get('/echo', (c) => {
  return c.text(c.var.echo('Hello!'))
})
```

## render() / setRenderer() [​](#render-setrenderer)

You can set a layout using `c.setRenderer()` within a custom middleware.

tsx

```
app.use(async (c, next) => {
  c.setRenderer((content) => {
    return c.html(
      <html>
        <body>
          <p>{content}</p>
        </body>
      </html>
    )
  })
  await next()
})
```

Then, you can utilize `c.render()` to create responses within this layout.

ts

```
app.get('/', (c) => {
  return c.render('Hello!')
})
```

The output of which will be:

html

```
<html>
  <body>
    <p>Hello!</p>
  </body>
</html>
```

Additionally, this feature offers the flexibility to customize arguments. To ensure type safety, types can be defined as:

ts

```
declare module 'hono' {
  interface ContextRenderer {
    (
      content: string | Promise<string>,
      head: { title: string }
    ): Response | Promise<Response>
  }
}
```

Here's an example of how you can use this:

ts

```
app.use('/pages/*', async (c, next) => {
  c.setRenderer((content, head) => {
    return c.html(
      <html>
        <head>
          <title>{head.title}</title>
        </head>
        <body>
          <header>{head.title}</header>
          <p>{content}</p>
        </body>
      </html>
    )
  })
  await next()
})

app.get('/pages/my-favorite', (c) => {
  return c.render(<p>Ramen and Sushi</p>, {
    title: 'My favorite',
  })
})

app.get('/pages/my-hobbies', (c) => {
  return c.render(<p>Watching baseball</p>, {
    title: 'My hobbies',
  })
})
```

## executionCtx [​](#executionctx)

You can access Cloudflare Workers' specific [ExecutionContext](https://developers.cloudflare.com/workers/runtime-apis/context/).

ts

```
// ExecutionContext object
app.get('/foo', async (c) => {
  c.executionCtx.waitUntil(c.env.KV.put(key, data))
  // ...
})
```

The `ExecutionContext` also has an [`exports`](https://developers.cloudflare.com/workers/runtime-apis/context/#exports) field. To get autocomplete with Wrangler's generated types, you can use module augmentation:

ts

```
import 'hono'

declare module 'hono' {
  interface ExecutionContext {
    readonly exports: Cloudflare.Exports
  }
}
```

## event [​](#event)

You can access Cloudflare Workers' specific `FetchEvent`. This was used in "Service Worker" syntax. But, it is not recommended now.

ts

```
// Type definition to make type inference
type Bindings = {
  MY_KV: KVNamespace
}

const app = new Hono<{ Bindings: Bindings }>()

// FetchEvent object (only set when using Service Worker syntax)
app.get('/foo', async (c) => {
  c.event.waitUntil(c.env.MY_KV.put(key, data))
  // ...
})
```

## env [​](#env)

In Cloudflare Workers Environment variables, secrets, KV namespaces, D1 database, R2 bucket etc. that are bound to a worker are known as bindings. Regardless of type, bindings are always available as global variables and can be accessed via the context `c.env.BINDING_KEY`.

ts

```
// Type definition to make type inference
type Bindings = {
  MY_KV: KVNamespace
}

const app = new Hono<{ Bindings: Bindings }>()

// Environment object for Cloudflare Workers
app.get('/', async (c) => {
  c.env.MY_KV.get('my-key')
  // ...
})
```

## error [​](#error)

If the Handler throws an error, the error object is placed in `c.error`. You can access it in your middleware.

ts

```
app.use(async (c, next) => {
  await next()
  if (c.error) {
    // do something...
  }
})
```

## ContextVariableMap [​](#contextvariablemap)

For instance, if you wish to add type definitions to variables when a specific middleware is used, you can extend `ContextVariableMap`. For example:

ts

```
declare module 'hono' {
  interface ContextVariableMap {
    result: string
  }
}
```

You can then utilize this in your middleware:

ts

```
const mw = createMiddleware(async (c, next) => {
  c.set('result', 'some values') // result is a string
  await next()
})
```

In a handler, the variable is inferred as the proper type:

ts

```
app.get('/', (c) => {
  const val = c.get('result') // val is a string
  // ...
  return c.json({ result: val })
})
```
