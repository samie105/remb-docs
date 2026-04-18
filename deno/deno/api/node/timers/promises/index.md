---
title: "timers/promises - Node documentation"
source: "https://docs.deno.com/api/node/timers/promises/"
canonical_url: "https://docs.deno.com/api/node/timers/promises/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:09.912Z"
content_hash: "979c647c32fdfa90c47f452ad688748fa5f5ed1c9bf2be933d039970a07f1fa8"
menu_path: ["timers/promises - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/timers/index.md", "title": "timers - Node documentation"}
nav_next: {"path": "deno/deno/api/node/tls/index.md", "title": "tls - Node documentation"}
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

### Functions [#](#Functions)

f

[setImmediate](../.././timers/promises/~/setImmediate "setImmediate")

No documentation available

f

[setInterval](../.././timers/promises/~/setInterval "setInterval")

Returns an async iterator that generates values in an interval of `delay` ms. If `ref` is `true`, you need to call `next()` of async iterator explicitly or implicitly to keep the event loop alive.

f

[setTimeout](../.././timers/promises/~/setTimeout "setTimeout")

No documentation available

### Interfaces [#](#Interfaces)

I

[Scheduler](../.././timers/promises/~/Scheduler "Scheduler")

No documentation available

*   [wait](../.././timers/promises/~/Scheduler#method_wait_0)
*   [yield](../.././timers/promises/~/Scheduler#method_yield_0)

### Variables [#](#Variables)

v

[scheduler](../.././timers/promises/~/scheduler "scheduler")

No documentation available

