---
title: "Combine Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/combine"
canonical_url: "https://hono.dev/docs/middleware/builtin/combine"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:09.984Z"
content_hash: "bdfebc7eea4869bb2f7e597c8f84d5ab9d30e90e98c10a8b913ecb4765ac216d"
menu_path: ["Combine Middleware ​"]
section_path: []
nav_prev: {"path": "../cache/index.md", "title": "Cache Middleware \u200b"}
nav_next: {"path": "../compress/index.md", "title": "Compress Middleware \u200b"}
---

## Combine Middleware [​](#combine-middleware)

Combine Middleware combines multiple middleware functions into a single middleware. It provides three functions:

*   `some` - Runs only one of the given middleware.
*   `every` - Runs all given middleware.
*   `except` - Runs all given middleware only if a condition is not met.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { some, every, except } from 'hono/combine'
```

## Usage [​](#usage)

Here's an example of complex access control rules using Combine Middleware.

ts

```
import { Hono } from 'hono'
import { bearerAuth } from 'hono/bearer-auth'
import { getConnInfo } from 'hono/cloudflare-workers'
import { every, some } from 'hono/combine'
import { ipRestriction } from 'hono/ip-restriction'
import { rateLimit } from '@/my-rate-limit'

const app = new Hono()

app.use(
  '*',
  some(
    every(
      ipRestriction(getConnInfo, { allowList: ['192.168.0.2'] }),
      bearerAuth({ token })
    ),
    // If both conditions are met, rateLimit will not execute.
    rateLimit()
  )
)

app.get('/', (c) => c.text('Hello Hono!'))
```

### some [​](#some)

Runs the first middleware that returns true. Middleware is applied in order, and if any middleware exits successfully, subsequent middleware will not run.

ts

```
import { some } from 'hono/combine'
import { bearerAuth } from 'hono/bearer-auth'
import { myRateLimit } from '@/rate-limit'

// If client has a valid token, skip rate limiting.
// Otherwise, apply rate limiting.
app.use(
  '/api/*',
  some(bearerAuth({ token }), myRateLimit({ limit: 100 }))
)
```

### every [​](#every)

Runs all middleware and stops if any of them fail. Middleware is applied in order, and if any middleware throws an error, subsequent middleware will not run.

ts

```
import { some, every } from 'hono/combine'
import { bearerAuth } from 'hono/bearer-auth'
import { myCheckLocalNetwork } from '@/check-local-network'
import { myRateLimit } from '@/rate-limit'

// If client is in local network, skip authentication and rate limiting.
// Otherwise, apply authentication and rate limiting.
app.use(
  '/api/*',
  some(
    myCheckLocalNetwork(),
    every(bearerAuth({ token }), myRateLimit({ limit: 100 }))
  )
)
```

### except [​](#except)

Runs all middleware except when the condition is met. You can pass a string or function as the condition. If multiple targets need to be matched, pass them as an array.

ts

```
import { except } from 'hono/combine'
import { bearerAuth } from 'hono/bearer-auth'

// If client is accessing public API, skip authentication.
// Otherwise, require a valid token.
app.use('/api/*', except('/api/public/*', bearerAuth({ token })))
```
