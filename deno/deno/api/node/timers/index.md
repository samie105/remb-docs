---
title: "timers - Node documentation"
source: "https://docs.deno.com/api/node/timers/"
canonical_url: "https://docs.deno.com/api/node/timers/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:05.974Z"
content_hash: "9d4c49f81cc13cdb9ab8273a86181277b36c65fe58ef832e2cbba0832aa14aad"
menu_path: ["timers - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/test/reporters/index.md", "title": "test/reporters - Node documentation"}
nav_next: {"path": "deno/deno/api/node/timers/promises/index.md", "title": "timers/promises - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:timers";
```

The `timer` module exposes a global API for scheduling functions to be called at some future period of time. Because the timer functions are globals, there is no need to import `node:timers` to use the API.

The timer functions within Node.js implement a similar API as the timers API provided by Web Browsers but use a different internal implementation that is built around the Node.js [Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#setimmediate-vs-settimeout).

### Functions [#](#Functions)

f

[clearImmediate](.././timers/~/clearImmediate "clearImmediate")

Cancels an `Immediate` object created by `setImmediate()`.

f

[clearInterval](.././timers/~/clearInterval "clearInterval")

Cancels a `Timeout` object created by `setInterval()`.

f

[clearTimeout](.././timers/~/clearTimeout "clearTimeout")

Cancels a `Timeout` object created by `setTimeout()`.

f

[promises.setImmediate](.././timers/promises/~/promises.setImmediate "promises.setImmediate")

No documentation available

f

[promises.setInterval](.././timers/promises/~/promises.setInterval "promises.setInterval")

Returns an async iterator that generates values in an interval of `delay` ms. If `ref` is `true`, you need to call `next()` of async iterator explicitly or implicitly to keep the event loop alive.

f

[promises.setTimeout](.././timers/promises/~/promises.setTimeout "promises.setTimeout")

No documentation available

f

[queueMicrotask](.././timers/~/queueMicrotask "queueMicrotask")

The `queueMicrotask()` method queues a microtask to invoke `callback`. If `callback` throws an exception, the `process` object `'uncaughtException'` event will be emitted.

f

N

[setImmediate](.././timers/~/setImmediate "setImmediate")

Schedules the "immediate" execution of the `callback` after I/O events' callbacks.

f

[setImmediate.setImmediate](.././timers/promises/~/setImmediate.setImmediate "setImmediate.setImmediate")

No documentation available

f

[setInterval](.././timers/~/setInterval "setInterval")

Schedules repeated execution of `callback` every `delay` milliseconds.

f

N

[setTimeout](.././timers/~/setTimeout "setTimeout")

Schedules execution of a one-time `callback` after `delay` milliseconds.

f

[setTimeout.setTimeout](.././timers/promises/~/setTimeout.setTimeout "setTimeout.setTimeout")

No documentation available

### Interfaces [#](#Interfaces)

I

[Immediate](.././timers/~/Immediate "Immediate")

This object is created internally and is returned from `setImmediate()`. It can be passed to `clearImmediate()` in order to cancel the scheduled actions.

*   [\_onImmediate](.././timers/~/Immediate#method__onimmediate_0)
*   [hasRef](.././timers/~/Immediate#method_hasref_0)
*   [ref](.././timers/~/Immediate#method_ref_0)
*   [unref](.././timers/~/Immediate#method_unref_0)

I

[promises.Scheduler](.././timers/promises/~/promises.Scheduler "promises.Scheduler")

No documentation available

*   [wait](.././timers/promises/~/promises.Scheduler#method_wait_0)
*   [yield](.././timers/promises/~/promises.Scheduler#method_yield_0)

I

[Timeout](.././timers/~/Timeout "Timeout")

This object is created internally and is returned from `setTimeout()` and `setInterval()`. It can be passed to either `clearTimeout()` or `clearInterval()` in order to cancel the scheduled actions.

*   [\_onTimeout](.././timers/~/Timeout#method__ontimeout_0)
*   [close](.././timers/~/Timeout#method_close_0)
*   [hasRef](.././timers/~/Timeout#method_hasref_0)
*   [ref](.././timers/~/Timeout#method_ref_0)
*   [refresh](.././timers/~/Timeout#method_refresh_0)
*   [unref](.././timers/~/Timeout#method_unref_0)

I

[TimerOptions](.././timers/~/TimerOptions "TimerOptions")

No documentation available

*   [ref](.././timers/~/TimerOptions#property_ref)

I

[Timer](.././timers/~/Timer "Timer")

No documentation available

*   [hasRef](.././timers/~/Timer#method_hasref_0)
*   [refresh](.././timers/~/Timer#method_refresh_0)

### Namespaces [#](#Namespaces)

N

[promises](.././timers/~/promises "promises")

The `timers/promises` API provides an alternative set of timer functions that return `Promise` objects. The API is accessible via `require('node:timers/promises')`.

### Variables [#](#Variables)

v

[promises.scheduler](.././timers/promises/~/promises.scheduler "promises.scheduler")

No documentation available


