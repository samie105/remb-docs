---
title: "async_hooks - Node documentation"
source: "https://docs.deno.com/api/node/async_hooks/"
canonical_url: "https://docs.deno.com/api/node/async_hooks/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:02:59.840Z"
content_hash: "c290bd14891aa11c1ded1988e17962dc214fa2d60d8de6174f6eb53cb110348a"
menu_path: ["async_hooks - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/node/assert/strict/index.md", "title": "namespace assert.strict"}
nav_next: {"path": "deno/api/node/buffer/index.md", "title": "buffer - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:async_hooks";
```

We strongly discourage the use of the `async_hooks` API. Other APIs that can cover most of its use cases include:

-   [`AsyncLocalStorage`](https://nodejs.org/docs/latest-v22.x/api/async_context.html#class-asynclocalstorage) tracks async context
-   [`process.getActiveResourcesInfo()`](https://nodejs.org/docs/latest-v22.x/api/process.html#processgetactiveresourcesinfo) tracks active resources

The `node:async_hooks` module provides an API to track asynchronous resources. It can be accessed using:

```js
import async_hooks from 'node:async_hooks';
```

c

[AsyncLocalStorage](.././async_hooks/~/AsyncLocalStorage "AsyncLocalStorage")

This class creates stores that stay coherent through asynchronous operations.

-   [bind](.././async_hooks/~/AsyncLocalStorage#method_bind_0)
-   [disable](.././async_hooks/~/AsyncLocalStorage#method_disable_0)
-   [enterWith](.././async_hooks/~/AsyncLocalStorage#method_enterwith_0)
-   [exit](.././async_hooks/~/AsyncLocalStorage#method_exit_0)
-   [getStore](.././async_hooks/~/AsyncLocalStorage#method_getstore_0)
-   [run](.././async_hooks/~/AsyncLocalStorage#method_run_0)
-   [snapshot](.././async_hooks/~/AsyncLocalStorage#method_snapshot_0)

c

[AsyncResource](.././async_hooks/~/AsyncResource "AsyncResource")

No documentation available

-   [asyncId](.././async_hooks/~/AsyncResource#method_asyncid_0)
-   [bind](.././async_hooks/~/AsyncResource#method_bind_0)
-   [emitDestroy](.././async_hooks/~/AsyncResource#method_emitdestroy_0)
-   [runInAsyncScope](.././async_hooks/~/AsyncResource#method_runinasyncscope_0)
-   [triggerAsyncId](.././async_hooks/~/AsyncResource#method_triggerasyncid_0)

f

[createHook](.././async_hooks/~/createHook "createHook")

No documentation available

f

[executionAsyncId](.././async_hooks/~/executionAsyncId "executionAsyncId")

No documentation available

f

[executionAsyncResource](.././async_hooks/~/executionAsyncResource "executionAsyncResource")

Resource objects returned by `executionAsyncResource()` are most often internal Node.js handle objects with undocumented APIs. Using any functions or properties on the object is likely to crash your application and should be avoided.

f

[triggerAsyncId](.././async_hooks/~/triggerAsyncId "triggerAsyncId")

Promise contexts may not get valid `triggerAsyncId`s by default. See the section on [promise execution tracking](https://nodejs.org/docs/latest-v22.x/api/async_hooks.html#promise-execution-tracking).

I

[AsyncHook](.././async_hooks/~/AsyncHook "AsyncHook")

No documentation available

-   [disable](.././async_hooks/~/AsyncHook#method_disable_0)
-   [enable](.././async_hooks/~/AsyncHook#method_enable_0)

I

[AsyncResourceOptions](.././async_hooks/~/AsyncResourceOptions "AsyncResourceOptions")

No documentation available

-   [requireManualDestroy](.././async_hooks/~/AsyncResourceOptions#property_requiremanualdestroy)
-   [triggerAsyncId](.././async_hooks/~/AsyncResourceOptions#property_triggerasyncid)

I

[HookCallbacks](.././async_hooks/~/HookCallbacks "HookCallbacks")

No documentation available

-   [after](.././async_hooks/~/HookCallbacks#method_after_0)
-   [before](.././async_hooks/~/HookCallbacks#method_before_0)
-   [destroy](.././async_hooks/~/HookCallbacks#method_destroy_0)
-   [init](.././async_hooks/~/HookCallbacks#method_init_0)
-   [promiseResolve](.././async_hooks/~/HookCallbacks#method_promiseresolve_0)
