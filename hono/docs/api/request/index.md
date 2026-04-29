---
title: "HonoRequest ​"
source: "https://hono.dev/docs/api/request"
canonical_url: "https://hono.dev/docs/api/request"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:45.211Z"
content_hash: "384f4c80d158e1ed4d7a23283097c05feaedcbd8cfee2ea56a210e6f4c958e27"
menu_path: ["HonoRequest ​"]
section_path: []
nav_prev: {"path": "../context/index.md", "title": "Context \u200b"}
nav_next: {"path": "../exception/index.md", "title": "HTTPException \u200b"}
---

The `HonoRequest` is an object that can be taken from `c.req` which wraps a [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object.

## param() [​](#param)

Get the values of path parameters.

ts

```
// Captured params
app.get('/entry/:id', async (c) => {
  const id = c.req.param('id')
  // ...
})

// Get all params at once
app.get('/entry/:id/comment/:commentId', async (c) => {
  const { id, commentId } = c.req.param()
})
```

## query() [​](#query)

Get querystring parameters.

ts

```
// Query params
app.get('/search', async (c) => {
  const query = c.req.query('q')
})

// Get all params at once
app.get('/search', async (c) => {
  const { q, limit, offset } = c.req.query()
})
```

## queries() [​](#queries)

Get multiple querystring parameter values, e.g. `/search?tags=A&tags=B`

ts

```
app.get('/search', async (c) => {
  // tags will be string[]
  const tags = c.req.queries('tags')
  // ...
})
```

## header() [​](#header)

Get the request header value.

ts

```
app.get('/', (c) => {
  const userAgent = c.req.header('User-Agent')
  return c.text(`Your user agent is ${userAgent}`)
})
```

WARNING

When `c.req.header()` is called with no arguments, all keys in the returned record are **lowercase**.

If you want to get the value of a header with an uppercase name, use `c.req.header(“X-Foo”)`.

ts

```
// ❌ Will not work
const headerRecord = c.req.header()
const foo = headerRecord['X-Foo']

// ✅ Will work
const foo = c.req.header('X-Foo')
```

## parseBody() [​](#parsebody)

Parse Request body of type `multipart/form-data` or `application/x-www-form-urlencoded`

ts

```
app.post('/entry', async (c) => {
  const body = await c.req.parseBody()
  // ...
})
```

`parseBody()` supports the following behaviors.

**Single file**

ts

```
const body = await c.req.parseBody()
const data = body['foo']
```

`body['foo']` is `(string | File)`.

If multiple files are uploaded, the last one will be used.

### Multiple files [​](#multiple-files)

ts

```
const body = await c.req.parseBody()
body['foo[]']
```

`body['foo[]']` is always `(string | File)[]`.

`[]` postfix is required.

### Multiple files or fields with same name [​](#multiple-files-or-fields-with-same-name)

If you have an input field that allows multiple `<input type="file" multiple />` or multiple checkboxes with the same name `<input type="checkbox" name="favorites" value="Hono"/>`.

ts

```
const body = await c.req.parseBody({ all: true })
body['foo']
```

`all` option is disabled by default.

*   If `body['foo']` is multiple files, it will be parsed to `(string | File)[]`.
*   If `body['foo']` is single file, it will be parsed to `(string | File)`.

### Dot notation [​](#dot-notation)

If you set the `dot` option `true`, the return value is structured based on the dot notation.

Imagine receiving the following data:

ts

```
const data = new FormData()
data.append('obj.key1', 'value1')
data.append('obj.key2', 'value2')
```

You can get the structured value by setting the `dot` option `true`:

ts

```
const body = await c.req.parseBody({ dot: true })
// body is `{ obj: { key1: 'value1', key2: 'value2' } }`
```

## json() [​](#json)

Parses the request body of type `application/json`

ts

```
app.post('/entry', async (c) => {
  const body = await c.req.json()
  // ...
})
```

## text() [​](#text)

Parses the request body of type `text/plain`

ts

```
app.post('/entry', async (c) => {
  const body = await c.req.text()
  // ...
})
```

## arrayBuffer() [​](#arraybuffer)

Parses the request body as an `ArrayBuffer`

ts

```
app.post('/entry', async (c) => {
  const body = await c.req.arrayBuffer()
  // ...
})
```

## blob() [​](#blob)

Parses the request body as a `Blob`.

ts

```
app.post('/entry', async (c) => {
  const body = await c.req.blob()
  // ...
})
```

## formData() [​](#formdata)

Parses the request body as a `FormData`.

ts

```
app.post('/entry', async (c) => {
  const body = await c.req.formData()
  // ...
})
```

## valid() [​](#valid)

Get the validated data.

ts

```
app.post('/posts', async (c) => {
  const { title, body } = c.req.valid('form')
  // ...
})
```

Available targets are below.

*   `form`
*   `json`
*   `query`
*   `header`
*   `cookie`
*   `param`

See the [Validation section](../../guides/validation/index.md) for usage examples.

## routePath [​](#routepath)

WARNING

**Deprecated in v4.8.0**: This property is deprecated. Use `routePath()` from [Route Helper](../../helpers/route/index.md) instead.

You can retrieve the registered path within the handler like this:

ts

```
app.get('/posts/:id', (c) => {
  return c.json({ path: c.req.routePath })
})
```

If you access `/posts/123`, it will return `/posts/:id`:

json

```
{ "path": "/posts/:id" }
```

## matchedRoutes [​](#matchedroutes)

WARNING

**Deprecated in v4.8.0**: This property is deprecated. Use `matchedRoutes()` from [Route Helper](../../helpers/route/index.md) instead.

It returns matched routes within the handler, which is useful for debugging.

ts

```
app.use(async function logger(c, next) {
  await next()
  c.req.matchedRoutes.forEach(({ handler, method, path }, i) => {
    const name =
      handler.name ||
      (handler.length < 2 ? '[handler]' : '[middleware]')
    console.log(
      method,
      ' ',
      path,
      ' '.repeat(Math.max(10 - path.length, 0)),
      name,
      i === c.req.routeIndex ? '<- respond from here' : ''
    )
  })
})
```

## path [​](#path)

The request pathname.

ts

```
app.get('/about/me', async (c) => {
  const pathname = c.req.path // `/about/me`
  // ...
})
```

## url [​](#url)

The request url strings.

ts

```
app.get('/about/me', async (c) => {
  const url = c.req.url // `http://localhost:8787/about/me`
  // ...
})
```

## method [​](#method)

The method name of the request.

ts

```
app.get('/about/me', async (c) => {
  const method = c.req.method // `GET`
  // ...
})
```

## raw [​](#raw)

The raw [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object.

ts

```
// For Cloudflare Workers
app.post('/', async (c) => {
  const metadata = c.req.raw.cf?.hostMetadata?
  // ...
})
```

## cloneRawRequest() [​](#clonerawrequest)

Clones the raw Request object from a HonoRequest. Works even after the request body has been consumed by validators or HonoRequest methods.

ts

```
import { Hono } from 'hono'
const app = new Hono()

import { cloneRawRequest } from 'hono/request'
import { validator } from 'hono/validator'

app.post(
  '/forward',
  validator('json', (data) => data),
  async (c) => {
    // Clone after validation
    const clonedReq = await cloneRawRequest(c.req)
    // Does not throw the error
    await clonedReq.json()
    // ...
  }
)
```
