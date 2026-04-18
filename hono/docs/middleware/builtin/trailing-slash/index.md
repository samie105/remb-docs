---
title: "Trailing Slash Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/trailing-slash"
canonical_url: "https://hono.dev/docs/middleware/builtin/trailing-slash"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:14.034Z"
content_hash: "030c7bcec5c43706932666d825191af5988250c82bbfba1a7b568b2992f18c92"
menu_path: ["Trailing Slash Middleware ​"]
section_path: []
nav_prev: {"path": "hono/docs/middleware/builtin/timing/index.md", "title": "Server-Timing Middleware \u200b"}
nav_next: {"path": "hono/docs/middleware/third-party/index.md", "title": "Third-party Middleware \u200b"}
---

## Trailing Slash Middleware [​](#trailing-slash-middleware)

This middleware handles Trailing Slash in the URL on a GET request.

`appendTrailingSlash` redirects the URL to which it added the Trailing Slash if the content was not found. Also, `trimTrailingSlash` will remove the Trailing Slash.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import {
  appendTrailingSlash,
  trimTrailingSlash,
} from 'hono/trailing-slash'
```

## Usage [​](#usage)

Example of redirecting a GET request of `/about/me` to `/about/me/`.

ts

```
import { Hono } from 'hono'
import { appendTrailingSlash } from 'hono/trailing-slash'

const app = new Hono({ strict: true })

app.use(appendTrailingSlash())
app.get('/about/me/', (c) => c.text('With Trailing Slash'))
```

Example of redirecting a GET request of `/about/me/` to `/about/me`.

ts

```
import { Hono } from 'hono'
import { trimTrailingSlash } from 'hono/trailing-slash'

const app = new Hono({ strict: true })

app.use(trimTrailingSlash())
app.get('/about/me', (c) => c.text('Without Trailing Slash'))
```

## Options [​](#options)

### optional alwaysRedirect: `boolean` [​](#alwaysredirect-boolean)

By default, trailing slash middleware only redirects when the response status is `404`. When `alwaysRedirect` is set to `true`, the middleware redirects before executing handlers. This is useful for wildcard routes (`*`) where the default behavior doesn't work.

ts

```
const app = new Hono()

app.use(trimTrailingSlash({ alwaysRedirect: true }))
app.get('/my-path/*', (c) => c.text('Wildcard route'))
```

This option is available for both `trimTrailingSlash` and `appendTrailingSlash`.

### optional skip: `(path: string) => boolean` [​](#skip-path-string-boolean)

A function that determines whether the redirect should be skipped based on the request path. If the function returns `true`, the redirect will be skipped. This is useful when you want to exclude certain paths, such as those with file extensions, from being redirected.

ts

```
app.use(
  appendTrailingSlash({
    skip: (path) => /\.\w+$/.test(path),
  })
)
```

This option is available for both `trimTrailingSlash` and `appendTrailingSlash`.

## Note [​](#note)

It will be enabled when the request method is `GET` and the response status is `404`.

