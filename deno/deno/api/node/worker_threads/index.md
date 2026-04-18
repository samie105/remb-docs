---
title: "worker_threads - Node documentation"
source: "https://docs.deno.com/api/node/worker_threads/"
canonical_url: "https://docs.deno.com/api/node/worker_threads/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:04.755Z"
content_hash: "dfae88183de892ffb55870cd567ab09a49770c3ca82cfb4da5869374e0807c2a"
menu_path: ["worker_threads - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/wasi/index.md", "title": "wasi - Node documentation"}
nav_next: {"path": "deno/deno/api/node/vm/index.md", "title": "vm - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:worker_threads";
```

The `node:worker_threads` module enables the use of threads that execute JavaScript in parallel. To access it:

```js
import worker from 'node:worker_threads';
```

Workers (threads) are useful for performing CPU-intensive JavaScript operations. They do not help much with I/O-intensive work. The Node.js built-in asynchronous I/O operations are more efficient than Workers can be.

Unlike `child_process` or `cluster`, `worker_threads` can share memory. They do so by transferring `ArrayBuffer` instances or sharing `SharedArrayBuffer` instances.

```js
import {
  Worker, isMainThread, parentPort, workerData,
} from 'node:worker_threads';
import { parse } from 'some-js-parsing-library';

if (isMainThread) {
  module.exports = function parseJSAsync(script) {
    return new Promise((resolve, reject) => {
      const worker = new Worker(__filename, {
        workerData: script,
      });
      worker.on('message', resolve);
      worker.on('error', reject);
      worker.on('exit', (code) => {
        if (code !== 0)
          reject(new Error(`Worker stopped with exit code ${code}`));
      });
    });
  };
} else {
  const script = workerData;
  parentPort.postMessage(parse(script));
}
```

The above example spawns a Worker thread for each `parseJSAsync()` call. In practice, use a pool of Workers for these kinds of tasks. Otherwise, the overhead of creating Workers would likely exceed their benefit.

When implementing a worker pool, use the `AsyncResource` API to inform diagnostic tools (e.g. to provide asynchronous stack traces) about the correlation between tasks and their outcomes. See `"Using AsyncResource for a Worker thread pool"` in the `async_hooks` documentation for an example implementation.

Worker threads inherit non-process-specific options by default. Refer to `Worker constructor options` to know how to customize worker thread options, specifically `argv` and `execArgv` options.

### Classes [#](#Classes)

c

v

[MessageChannel](.././worker_threads/~/MessageChannel "MessageChannel")

Instances of the `worker.MessageChannel` class represent an asynchronous, two-way communications channel. The `MessageChannel` has no methods of its own. `new MessageChannel()` yields an object with `port1` and `port2` properties, which refer to linked `MessagePort` instances.

*   [port1](.././worker_threads/~/MessageChannel#property_port1)
*   [port2](.././worker_threads/~/MessageChannel#property_port2)

c

v

[MessagePort](.././worker_threads/~/MessagePort "MessagePort")

Instances of the `worker.MessagePort` class represent one end of an asynchronous, two-way communications channel. It can be used to transfer structured data, memory regions and other `MessagePort`s between different `Worker`s.

*   [addEventListener](.././worker_threads/~/MessagePort#property_addeventlistener)
*   [addListener](.././worker_threads/~/MessagePort#method_addlistener_0)
*   [close](.././worker_threads/~/MessagePort#method_close_0)
*   [dispatchEvent](.././worker_threads/~/MessagePort#property_dispatchevent)
*   [emit](.././worker_threads/~/MessagePort#method_emit_0)
*   [off](.././worker_threads/~/MessagePort#method_off_0)
*   [on](.././worker_threads/~/MessagePort#method_on_0)
*   [once](.././worker_threads/~/MessagePort#method_once_0)
*   [postMessage](.././worker_threads/~/MessagePort#method_postmessage_0)
*   [prependListener](.././worker_threads/~/MessagePort#method_prependlistener_0)
*   [prependOnceListener](.././worker_threads/~/MessagePort#method_prependoncelistener_0)
*   [ref](.././worker_threads/~/MessagePort#method_ref_0)
*   [removeEventListener](.././worker_threads/~/MessagePort#property_removeeventlistener)
*   [removeListener](.././worker_threads/~/MessagePort#method_removelistener_0)
*   [start](.././worker_threads/~/MessagePort#method_start_0)
*   [unref](.././worker_threads/~/MessagePort#method_unref_0)

c

[Worker](.././worker_threads/~/Worker "Worker")

No documentation available

*   [addListener](.././worker_threads/~/Worker#method_addlistener_0)
*   [emit](.././worker_threads/~/Worker#method_emit_0)
*   [getHeapSnapshot](.././worker_threads/~/Worker#method_getheapsnapshot_0)
*   [off](.././worker_threads/~/Worker#method_off_0)
*   [on](.././worker_threads/~/Worker#method_on_0)
*   [once](.././worker_threads/~/Worker#method_once_0)
*   [performance](.././worker_threads/~/Worker#property_performance)
*   [postMessage](.././worker_threads/~/Worker#method_postmessage_0)
*   [postMessageToThread](.././worker_threads/~/Worker#method_postmessagetothread_0)
*   [prependListener](.././worker_threads/~/Worker#method_prependlistener_0)
*   [prependOnceListener](.././worker_threads/~/Worker#method_prependoncelistener_0)
*   [ref](.././worker_threads/~/Worker#method_ref_0)
*   [removeListener](.././worker_threads/~/Worker#method_removelistener_0)
*   [resourceLimits](.././worker_threads/~/Worker#property_resourcelimits)
*   [stderr](.././worker_threads/~/Worker#property_stderr)
*   [stdin](.././worker_threads/~/Worker#property_stdin)
*   [stdout](.././worker_threads/~/Worker#property_stdout)
*   [terminate](.././worker_threads/~/Worker#method_terminate_0)
*   [threadId](.././worker_threads/~/Worker#property_threadid)
*   [unref](.././worker_threads/~/Worker#method_unref_0)

### Functions [#](#Functions)

f

[getEnvironmentData](.././worker_threads/~/getEnvironmentData "getEnvironmentData")

Within a worker thread, `worker.getEnvironmentData()` returns a clone of data passed to the spawning thread's `worker.setEnvironmentData()`. Every new `Worker` receives its own copy of the environment data automatically.

f

[isMarkedAsUntransferable](.././worker_threads/~/isMarkedAsUntransferable "isMarkedAsUntransferable")

Check if an object is marked as not transferable with [markAsUntransferable](.././worker_threads/~/markAsUntransferable).

f

[markAsUncloneable](.././worker_threads/~/markAsUncloneable "markAsUncloneable")

Mark an object as not cloneable. If `object` is used as `message` in a `port.postMessage()` call, an error is thrown. This is a no-op if `object` is a primitive value.

f

[markAsUntransferable](.././worker_threads/~/markAsUntransferable "markAsUntransferable")

No documentation available

f

[moveMessagePortToContext](.././worker_threads/~/moveMessagePortToContext "moveMessagePortToContext")

No documentation available

f

[receiveMessageOnPort](.././worker_threads/~/receiveMessageOnPort "receiveMessageOnPort")

No documentation available

f

[setEnvironmentData](.././worker_threads/~/setEnvironmentData "setEnvironmentData")

The `worker.setEnvironmentData()` API sets the content of `worker.getEnvironmentData()` in the current thread and all new `Worker` instances spawned from the current context.

### Interfaces [#](#Interfaces)

c

I

v

[BroadcastChannel](.././worker_threads/~/BroadcastChannel "BroadcastChannel")

Instances of `BroadcastChannel` allow asynchronous one-to-many communication with all other `BroadcastChannel` instances bound to the same channel name.

*   [close](.././worker_threads/~/BroadcastChannel#method_close_0)
*   [name](.././worker_threads/~/BroadcastChannel#property_name)
*   [onmessage](.././worker_threads/~/BroadcastChannel#property_onmessage)
*   [onmessageerror](.././worker_threads/~/BroadcastChannel#property_onmessageerror)
*   [postMessage](.././worker_threads/~/BroadcastChannel#method_postmessage_0)

I

[ResourceLimits](.././worker_threads/~/ResourceLimits "ResourceLimits")

No documentation available

*   [codeRangeSizeMb](.././worker_threads/~/ResourceLimits#property_coderangesizemb)
*   [maxOldGenerationSizeMb](.././worker_threads/~/ResourceLimits#property_maxoldgenerationsizemb)
*   [maxYoungGenerationSizeMb](.././worker_threads/~/ResourceLimits#property_maxyounggenerationsizemb)
*   [stackSizeMb](.././worker_threads/~/ResourceLimits#property_stacksizemb)

I

[WorkerOptions](.././worker_threads/~/WorkerOptions "WorkerOptions")

No documentation available

*   [argv](.././worker_threads/~/WorkerOptions#property_argv)
*   [env](.././worker_threads/~/WorkerOptions#property_env)
*   [eval](.././worker_threads/~/WorkerOptions#property_eval)
*   [execArgv](.././worker_threads/~/WorkerOptions#property_execargv)
*   [name](.././worker_threads/~/WorkerOptions#property_name)
*   [resourceLimits](.././worker_threads/~/WorkerOptions#property_resourcelimits)
*   [stderr](.././worker_threads/~/WorkerOptions#property_stderr)
*   [stdin](.././worker_threads/~/WorkerOptions#property_stdin)
*   [stdout](.././worker_threads/~/WorkerOptions#property_stdout)
*   [trackUnmanagedFds](.././worker_threads/~/WorkerOptions#property_trackunmanagedfds)
*   [transferList](.././worker_threads/~/WorkerOptions#property_transferlist)
*   [workerData](.././worker_threads/~/WorkerOptions#property_workerdata)

I

[WorkerPerformance](.././worker_threads/~/WorkerPerformance "WorkerPerformance")

No documentation available

*   [eventLoopUtilization](.././worker_threads/~/WorkerPerformance#property_eventlooputilization)

### Type Aliases [#](<#Type Aliases>)

T

[Serializable](.././worker_threads/~/Serializable "Serializable")

No documentation available

T

[TransferListItem](.././worker_threads/~/TransferListItem "TransferListItem")

No documentation available

### Variables [#](#Variables)

v

[isInternalThread](.././worker_threads/~/isInternalThread "isInternalThread")

No documentation available

v

[isMainThread](.././worker_threads/~/isMainThread "isMainThread")

No documentation available

v

[parentPort](.././worker_threads/~/parentPort "parentPort")

No documentation available

v

[resourceLimits](.././worker_threads/~/resourceLimits "resourceLimits")

No documentation available

v

[SHARE\_ENV](.././worker_threads/~/SHARE_ENV "SHARE_ENV")

No documentation available

v

[threadId](.././worker_threads/~/threadId "threadId")

No documentation available

v

[workerData](.././worker_threads/~/workerData "workerData")

No documentation available

