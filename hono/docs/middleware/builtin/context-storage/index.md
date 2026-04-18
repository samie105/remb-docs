---
title: "Context Storage Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/context-storage"
canonical_url: "https://hono.dev/docs/middleware/builtin/context-storage"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:46.239Z"
content_hash: "e2a1cca8842b45498345fdba3ec586cc7c724914c9341ab4a8b739c0e091e975"
menu_path: ["Context Storage Middleware ​"]
section_path: []
---
## Context Storage Middleware [​](#context-storage-middleware)

The Context Storage Middleware stores the Hono `Context` in the `AsyncLocalStorage`, to make it globally accessible.

INFO

**Note** This middleware uses `AsyncLocalStorage`. The runtime should support it.

**Cloudflare Workers**: To enable `AsyncLocalStorage`, add the [`nodejs_compat` or `nodejs_als` flag](https://developers.cloudflare.com/workers/configuration/compatibility-dates/#nodejs-compatibility-flag) to your `wrangler.toml` file.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import {
  contextStorage,
  getContext,
  tryGetContext,
} from 'hono/context-storage'
```

## Usage [​](#usage)

The `getContext()` will return the current Context object if the `contextStorage()` is applied as a middleware.

ts

```
type Env = {
  Variables: {
    message: string
  }
}

const app = new Hono<Env>()

app.use(contextStorage())

app.use(async (c, next) => {
  c.set('message', 'Hello!')
  await next()
})

// You can access the variable outside the handler.
const getMessage = () => {
  return getContext<Env>().var.message
}

app.get('/', (c) => {
  return c.text(getMessage())
})
```

On Cloudflare Workers, you can access the bindings outside the handler.

ts

```
type Env = {
  Bindings: {
    KV: KVNamespace
  }
}

const app = new Hono<Env>()

app.use(contextStorage())

const setKV = (value: string) => {
  return getContext<Env>().env.KV.put('key', value)
}
```

## tryGetContext [​](#trygetcontext)

`tryGetContext()` works like `getContext()`, but returns `undefined` instead of throwing an error when the context is not available:

ts

```
const context = tryGetContext<Env>()
if (context) {
  // Context is available
  console.log(context.var.message)
}
```
