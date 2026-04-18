---
title: "Method Override Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/method-override"
canonical_url: "https://hono.dev/docs/middleware/builtin/method-override"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:50.617Z"
content_hash: "f94327372b9e26a11352b15459d0dc7ff10b2cb150735ed3de8e4c05cf7ed822"
menu_path: ["Method Override Middleware ​"]
section_path: []
---
## Method Override Middleware [​](#method-override-middleware)

This middleware executes the handler of the specified method, which is different from the actual method of the request, depending on the value of the form, header, or query, and returns its response.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { methodOverride } from 'hono/method-override'
```

## Usage [​](#usage)

ts

```
const app = new Hono()

// If no options are specified, the value of `_method` in the form,
// e.g. DELETE, is used as the method.
app.use('/posts', methodOverride({ app }))

app.delete('/posts', (c) => {
  // ....
})
```

## For example [​](#for-example)

Since HTML forms cannot send a DELETE method, you can put the value `DELETE` in the property named `_method` and send it. And the handler for `app.delete()` will be executed.

The HTML form:

html

```
<form action="/posts" method="POST">
  <input type="hidden" name="_method" value="DELETE" />
  <input type="text" name="id" />
</form>
```

The application:

ts

```
import { methodOverride } from 'hono/method-override'

const app = new Hono()
app.use('/posts', methodOverride({ app }))

app.delete('/posts', () => {
  // ...
})
```

You can change the default values or use the header value and query value:

ts

```
app.use('/posts', methodOverride({ app, form: '_custom_name' }))
app.use(
  '/posts',
  methodOverride({ app, header: 'X-METHOD-OVERRIDE' })
)
app.use('/posts', methodOverride({ app, query: '_method' }))
```

## Options [​](#options)

### required app: `Hono` [​](#app-hono)

The instance of `Hono` is used in your application.

### optional form: `string` [​](#form-string)

Form key with a value containing the method name. The default is `_method`.

### optional header: `boolean` [​](#header-boolean)

Header name with a value containing the method name.

### optional query: `boolean` [​](#query-boolean)

Query parameter key with a value containing the method name.
