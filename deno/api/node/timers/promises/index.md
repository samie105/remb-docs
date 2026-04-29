---
title: "timers/promises - Node documentation"
source: "https://docs.deno.com/api/node/timers/promises/"
canonical_url: "https://docs.deno.com/api/node/timers/promises/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:14:20.577Z"
content_hash: "3731f17a53ba54b7d294ff6ddd53f45585ec445b09f9cdee5d90e786121462b2"
menu_path: ["timers/promises - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../index.md", "title": "timers - Node documentation"}
nav_next: {"path": "../../tls/index.md", "title": "tls - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:timers/promises";
```

The `timers/promises` API provides an alternative set of timer functions that return `Promise` objects. The API is accessible via `require('node:timers/promises')`.

```js
import {
  setTimeout,
  setImmediate,
  setInterval,
} from 'node:timers/promises';
```

f

[setImmediate](../.././timers/promises/~/setImmediate "setImmediate")

No documentation available

f

[setInterval](../.././timers/promises/~/setInterval "setInterval")

Returns an async iterator that generates values in an interval of `delay` ms. If `ref` is `true`, you need to call `next()` of async iterator explicitly or implicitly to keep the event loop alive.

f

[setTimeout](../.././timers/promises/~/setTimeout "setTimeout")

No documentation available

I

[Scheduler](../.././timers/promises/~/Scheduler "Scheduler")

No documentation available

-   [wait](../.././timers/promises/~/Scheduler#method_wait_0)
-   [yield](../.././timers/promises/~/Scheduler#method_yield_0)

v

[scheduler](../.././timers/promises/~/scheduler "scheduler")

No documentation available
