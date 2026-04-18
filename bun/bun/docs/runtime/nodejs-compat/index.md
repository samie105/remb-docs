---
title: "Node.js Compatibility"
source: "https://bun.com/docs/runtime/nodejs-compat"
canonical_url: "https://bun.com/docs/runtime/nodejs-compat"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:05.675Z"
content_hash: "aede478b61174b7b6601c9519efc28a4a0205ea90a5d08e13f0478aa1b6e8631"
menu_path: ["Node.js Compatibility"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/node-api/index.md", "title": "Node-API"}
nav_next: {"path": "bun/bun/docs/runtime/plugins/index.md", "title": "Plugins"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

Every day, Bun gets closer to 100% Node.js API compatibility. Today, popular frameworks like Next.js, Express, and millions of `npm` packages intended for Node work with Bun. To ensure compatibility, we run thousands of tests from Node.js’ test suite before every release of Bun. **If a package works in Node.js but doesn’t work in Bun, we consider it a bug in Bun.** Please [open an issue](https://bun.com/issues) and we’ll fix it. This page is updated regularly to reflect compatibility status of the latest version of Bun. The information below reflects Bun’s compatibility with _Node.js v23_.

## 

[​

](#built-in-node-js-modules)

Built-in Node.js modules

### 

[​

](#nodeassert)

[`node:assert`](https://nodejs.org/api/assert.html)

🟢 Fully implemented.

### 

[​

](#nodebuffer)

[`node:buffer`](https://nodejs.org/api/buffer.html)

🟢 Fully implemented.

### 

[​

](#nodeconsole)

[`node:console`](https://nodejs.org/api/console.html)

🟢 Fully implemented.

### 

[​

](#nodedgram)

[`node:dgram`](https://nodejs.org/api/dgram.html)

🟢 Fully implemented. > 90% of Node.js’s test suite passes.

### 

[​

](#nodediagnostics_channel)

[`node:diagnostics_channel`](https://nodejs.org/api/diagnostics_channel.html)

🟢 Fully implemented.

### 

[​

](#nodedns)

[`node:dns`](https://nodejs.org/api/dns.html)

🟢 Fully implemented. > 90% of Node.js’s test suite passes.

### 

[​

](#nodeevents)

[`node:events`](https://nodejs.org/api/events.html)

🟢 Fully implemented. 100% of Node.js’s test suite passes. `EventEmitterAsyncResource` uses `AsyncResource` underneath.

### 

[​

](#nodefs)

[`node:fs`](https://nodejs.org/api/fs.html)

🟢 Fully implemented. 92% of Node.js’s test suite passes.

### 

[​

](#nodehttp)

[`node:http`](https://nodejs.org/api/http.html)

🟢 Fully implemented. Outgoing client request body is currently buffered instead of streamed.

### 

[​

](#nodehttps)

[`node:https`](https://nodejs.org/api/https.html)

🟢 APIs are implemented, but `Agent` is not always used yet.

### 

[​

](#nodeos)

[`node:os`](https://nodejs.org/api/os.html)

🟢 Fully implemented. 100% of Node.js’s test suite passes.

### 

[​

](#nodepath)

[`node:path`](https://nodejs.org/api/path.html)

🟢 Fully implemented. 100% of Node.js’s test suite passes.

### 

[​

](#nodepunycode)

[`node:punycode`](https://nodejs.org/api/punycode.html)

🟢 Fully implemented. 100% of Node.js’s test suite passes, _deprecated by Node.js_.

### 

[​

](#nodequerystring)

[`node:querystring`](https://nodejs.org/api/querystring.html)

🟢 Fully implemented. 100% of Node.js’s test suite passes.

### 

[​

](#nodereadline)

[`node:readline`](https://nodejs.org/api/readline.html)

🟢 Fully implemented.

### 

[​

](#nodestream)

[`node:stream`](https://nodejs.org/api/stream.html)

🟢 Fully implemented.

### 

[​

](#nodestring_decoder)

[`node:string_decoder`](https://nodejs.org/api/string_decoder.html)

🟢 Fully implemented. 100% of Node.js’s test suite passes.

### 

[​

](#nodetimers)

[`node:timers`](https://nodejs.org/api/timers.html)

🟢 Recommended to use global `setTimeout`, et. al. instead.

### 

[​

](#nodetty)

[`node:tty`](https://nodejs.org/api/tty.html)

🟢 Fully implemented.

### 

[​

](#nodeurl)

[`node:url`](https://nodejs.org/api/url.html)

🟢 Fully implemented.

### 

[​

](#nodezlib)

[`node:zlib`](https://nodejs.org/api/zlib.html)

🟢 Fully implemented. 98% of Node.js’s test suite passes.

### 

[​

](#nodeasync_hooks)

[`node:async_hooks`](https://nodejs.org/api/async_hooks.html)

🟡 `AsyncLocalStorage`, and `AsyncResource` are implemented. v8 promise hooks are not called, and its usage is [strongly discouraged](https://nodejs.org/docs/latest/api/async_hooks.html#async-hooks).

### 

[​

](#nodechild_process)

[`node:child_process`](https://nodejs.org/api/child_process.html)

🟡 Missing `proc.gid` `proc.uid`. `Stream` class not exported. IPC cannot send socket handles. Node.js ↔ Bun IPC can be used with JSON serialization.

### 

[​

](#nodecluster)

[`node:cluster`](https://nodejs.org/api/cluster.html)

🟡 Handles and file descriptors cannot be passed between workers, which means load-balancing HTTP requests across processes is only supported on Linux at this time (via `SO_REUSEPORT`). Otherwise, implemented but not battle-tested.

### 

[​

](#nodecrypto)

[`node:crypto`](https://nodejs.org/api/crypto.html)

🟡 Missing `secureHeapUsed` `setEngine` `setFips`

### 

[​

](#nodedomain)

[`node:domain`](https://nodejs.org/api/domain.html)

🟡 Missing `Domain` `active`

### 

[​

](#nodehttp2)

[`node:http2`](https://nodejs.org/api/http2.html)

🟡 Client & server are implemented (95.25% of gRPC’s test suite passes). Missing `options.allowHTTP1`, `options.enableConnectProtocol`, ALTSVC extension, and `http2stream.pushStream`.

### 

[​

](#nodemodule)

[`node:module`](https://nodejs.org/api/module.html)

🟡 Missing `syncBuiltinESMExports`, `Module#load()`. Overriding `require.cache` is supported for ESM & CJS modules. `module._extensions`, `module._pathCache`, `module._cache` are no-ops. `module.register` is not implemented and we recommend using a [`Bun.plugin`](/docs/runtime/plugins) in the meantime.

### 

[​

](#nodenet)

[`node:net`](https://nodejs.org/api/net.html)

🟢 Fully implemented.

### 

[​

](#nodeperf_hooks)

[`node:perf_hooks`](https://nodejs.org/api/perf_hooks.html)

🟡 APIs are implemented, but Node.js test suite does not pass yet for this module.

### 

[​

](#nodeprocess)

[`node:process`](https://nodejs.org/api/process.html)

🟡 See [`process`](#process) Global.

### 

[​

](#nodesys)

[`node:sys`](https://nodejs.org/api/util.html)

🟡 See [`node:util`](#node-util).

### 

[​

](#nodetls)

[`node:tls`](https://nodejs.org/api/tls.html)

🟡 Missing `tls.createSecurePair`.

### 

[​

](#nodeutil)

[`node:util`](https://nodejs.org/api/util.html)

🟡 Missing `getCallSite` `getCallSites` `getSystemErrorMap` `getSystemErrorMessage` `transferableAbortSignal` `transferableAbortController`

### 

[​

](#nodev8)

[`node:v8`](https://nodejs.org/api/v8.html)

🟡 `writeHeapSnapshot` and `getHeapSnapshot` are implemented. `serialize` and `deserialize` use JavaScriptCore’s wire format instead of V8’s. Other methods are not implemented. For profiling, use [`bun:jsc`](/docs/project/benchmarking#javascript-heap-stats) instead.

### 

[​

](#nodevm)

[`node:vm`](https://nodejs.org/api/vm.html)

🟡 Core functionality and ES modules are implemented, including `vm.Script`, `vm.createContext`, `vm.runInContext`, `vm.runInNewContext`, `vm.runInThisContext`, `vm.compileFunction`, `vm.isContext`, `vm.Module`, `vm.SourceTextModule`, `vm.SyntheticModule`, and `importModuleDynamically` support. Options like `timeout` and `breakOnSigint` are fully supported. Missing `vm.measureMemory` and some `cachedData` functionality.

### 

[​

](#nodewasi)

[`node:wasi`](https://nodejs.org/api/wasi.html)

🟡 Partially implemented.

### 

[​

](#nodeworker_threads)

[`node:worker_threads`](https://nodejs.org/api/worker_threads.html)

🟡 `Worker` doesn’t support the following options: `stdin` `stdout` `stderr` `trackedUnmanagedFds` `resourceLimits`. Missing `markAsUntransferable` `moveMessagePortToContext`.

### 

[​

](#nodeinspector)

[`node:inspector`](https://nodejs.org/api/inspector.html)

🟡 Partially implemented. `Profiler` API is supported (`Profiler.enable`, `Profiler.disable`, `Profiler.start`, `Profiler.stop`, `Profiler.setSamplingInterval`). Other inspector APIs are not yet implemented.

### 

[​

](#noderepl)

[`node:repl`](https://nodejs.org/api/repl.html)

🔴 Not implemented.

### 

[​

](#nodesqlite)

[`node:sqlite`](https://nodejs.org/api/sqlite.html)

🔴 Not implemented.

### 

[​

](#nodetest)

[`node:test`](https://nodejs.org/api/test.html)

🟡 Partly implemented. Missing mocks, snapshots, timers. Use [`bun:test`](/docs/test) instead.

### 

[​

](#nodetrace_events)

[`node:trace_events`](https://nodejs.org/api/tracing.html)

🔴 Not implemented.

## 

[​

](#node-js-globals)

Node.js globals

The table below lists all globals implemented by Node.js and Bun’s current compatibility status.

### 

[​

](#abortcontroller)

[`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)

🟢 Fully implemented.

### 

[​

](#abortsignal)

[`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)

🟢 Fully implemented.

### 

[​

](#blob)

[`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob)

🟢 Fully implemented.

### 

[​

](#buffer)

[`Buffer`](https://nodejs.org/api/buffer.html#class-buffer)

🟢 Fully implemented.

### 

[​

](#bytelengthqueuingstrategy)

[`ByteLengthQueuingStrategy`](https://developer.mozilla.org/en-US/docs/Web/API/ByteLengthQueuingStrategy)

🟢 Fully implemented.

### 

[​

](#__dirname)

[`__dirname`](https://nodejs.org/api/globals.html#__dirname)

🟢 Fully implemented.

### 

[​

](#__filename)

[`__filename`](https://nodejs.org/api/globals.html#__filename)

🟢 Fully implemented.

### 

[​

](#atob)

[`atob()`](https://developer.mozilla.org/en-US/docs/Web/API/atob)

🟢 Fully implemented.

### 

[​

](#atomics)

[`Atomics`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics)

🟢 Fully implemented.

### 

[​

](#broadcastchannel)

[`BroadcastChannel`](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel)

🟢 Fully implemented.

### 

[​

](#btoa)

[`btoa()`](https://developer.mozilla.org/en-US/docs/Web/API/btoa)

🟢 Fully implemented.

### 

[​

](#clearimmediate)

[`clearImmediate()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/clearImmediate)

🟢 Fully implemented.

### 

[​

](#clearinterval)

[`clearInterval()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/clearInterval)

🟢 Fully implemented.

### 

[​

](#cleartimeout)

[`clearTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/clearTimeout)

🟢 Fully implemented.

### 

[​

](#compressionstream)

[`CompressionStream`](https://developer.mozilla.org/en-US/docs/Web/API/CompressionStream)

🟢 Fully implemented.

### 

[​

](#console)

[`console`](https://developer.mozilla.org/en-US/docs/Web/API/console)

🟢 Fully implemented.

### 

[​

](#countqueuingstrategy)

[`CountQueuingStrategy`](https://developer.mozilla.org/en-US/docs/Web/API/CountQueuingStrategy)

🟢 Fully implemented.

### 

[​

](#crypto)

[`Crypto`](https://developer.mozilla.org/en-US/docs/Web/API/Crypto)

🟢 Fully implemented.

### 

[​

](#subtlecrypto-crypto)

[`SubtleCrypto (crypto)`](https://developer.mozilla.org/en-US/docs/Web/API/crypto)

🟢 Fully implemented.

### 

[​

](#cryptokey)

[`CryptoKey`](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKey)

🟢 Fully implemented.

### 

[​

](#customevent)

[`CustomEvent`](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent)

🟢 Fully implemented.

### 

[​

](#decompressionstream)

[`DecompressionStream`](https://developer.mozilla.org/en-US/docs/Web/API/DecompressionStream)

🟢 Fully implemented.

### 

[​

](#event)

[`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event)

🟢 Fully implemented.

### 

[​

](#eventtarget)

[`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)

🟢 Fully implemented.

### 

[​

](#exports)

[`exports`](https://nodejs.org/api/globals.html#exports)

🟢 Fully implemented.

### 

[​

](#fetch)

[`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/fetch)

🟢 Fully implemented.

### 

[​

](#formdata)

[`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData)

🟢 Fully implemented.

### 

[​

](#global)

[`global`](https://nodejs.org/api/globals.html#global)

🟢 Implemented. This is an object containing all objects in the global namespace. It’s rarely referenced directly, as its contents are available without an additional prefix, e.g. `__dirname` instead of `global.__dirname`.

### 

[​

](#globalthis)

[`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)

🟢 Aliases to `global`.

### 

[​

](#headers)

[`Headers`](https://developer.mozilla.org/en-US/docs/Web/API/Headers)

🟢 Fully implemented.

### 

[​

](#messagechannel)

[`MessageChannel`](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel)

🟢 Fully implemented.

### 

[​

](#messageevent)

[`MessageEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent)

🟢 Fully implemented.

### 

[​

](#messageport)

[`MessagePort`](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort)

🟢 Fully implemented.

### 

[​

](#module)

[`module`](https://nodejs.org/api/globals.html#module)

🟢 Fully implemented.

### 

[​

](#performanceentry)

[`PerformanceEntry`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceEntry)

🟢 Fully implemented.

### 

[​

](#performancemark)

[`PerformanceMark`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceMark)

🟢 Fully implemented.

### 

[​

](#performancemeasure)

[`PerformanceMeasure`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceMeasure)

🟢 Fully implemented.

### 

[​

](#performanceobserver)

[`PerformanceObserver`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver)

🟢 Fully implemented.

### 

[​

](#performanceobserverentrylist)

[`PerformanceObserverEntryList`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserverEntryList)

🟢 Fully implemented.

### 

[​

](#performanceresourcetiming)

[`PerformanceResourceTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming)

🟢 Fully implemented.

### 

[​

](#performance)

[`performance`](https://developer.mozilla.org/en-US/docs/Web/API/performance)

🟢 Fully implemented.

### 

[​

](#process)

[`process`](https://nodejs.org/api/process.html)

🟡 Mostly implemented. `process.binding` (internal Node.js bindings some packages rely on) is partially implemented. `process.title` is currently a no-op on macOS & Linux. `getActiveResourcesInfo` `setActiveResourcesInfo`, `getActiveResources` and `setSourceMapsEnabled` are stubs. Newer APIs like `process.loadEnvFile` and `process.getBuiltinModule` are not implemented yet.

### 

[​

](#queuemicrotask)

[`queueMicrotask()`](https://developer.mozilla.org/en-US/docs/Web/API/queueMicrotask)

🟢 Fully implemented.

### 

[​

](#readablebytestreamcontroller)

[`ReadableByteStreamController`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableByteStreamController)

🟢 Fully implemented.

### 

[​

](#readablestream)

[`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream)

🟢 Fully implemented.

### 

[​

](#readablestreambyobreader)

[`ReadableStreamBYOBReader`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamBYOBReader)

🟢 Fully implemented.

### 

[​

](#readablestreambyobrequest)

[`ReadableStreamBYOBRequest`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamBYOBRequest)

🟢 Fully implemented.

### 

[​

](#readablestreamdefaultcontroller)

[`ReadableStreamDefaultController`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultController)

🟢 Fully implemented.

### 

[​

](#readablestreamdefaultreader)

[`ReadableStreamDefaultReader`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultReader)

🟢 Fully implemented.

### 

[​

](#require)

[`require()`](https://nodejs.org/api/globals.html#require)

🟢 Fully implemented, including [`require.main`](https://nodejs.org/api/modules.html#requiremain), [`require.cache`](https://nodejs.org/api/modules.html#requirecache), [`require.resolve`](https://nodejs.org/api/modules.html#requireresolverequest-options).

### 

[​

](#response)

[`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response)

🟢 Fully implemented.

### 

[​

](#request)

[`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request)

🟢 Fully implemented.

### 

[​

](#setimmediate)

[`setImmediate()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setImmediate)

🟢 Fully implemented.

### 

[​

](#setinterval)

[`setInterval()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval)

🟢 Fully implemented.

### 

[​

](#settimeout)

[`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)

🟢 Fully implemented.

### 

[​

](#structuredclone)

[`structuredClone()`](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone)

🟢 Fully implemented.

### 

[​

](#subtlecrypto)

[`SubtleCrypto`](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto)

🟢 Fully implemented.

### 

[​

](#domexception)

[`DOMException`](https://developer.mozilla.org/en-US/docs/Web/API/DOMException)

🟢 Fully implemented.

### 

[​

](#textdecoder)

[`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder)

🟢 Fully implemented.

### 

[​

](#textdecoderstream)

[`TextDecoderStream`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoderStream)

🟢 Fully implemented.

### 

[​

](#textencoder)

[`TextEncoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder)

🟢 Fully implemented.

### 

[​

](#textencoderstream)

[`TextEncoderStream`](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoderStream)

🟢 Fully implemented.

### 

[​

](#transformstream)

[`TransformStream`](https://developer.mozilla.org/en-US/docs/Web/API/TransformStream)

🟢 Fully implemented.

### 

[​

](#transformstreamdefaultcontroller)

[`TransformStreamDefaultController`](https://developer.mozilla.org/en-US/docs/Web/API/TransformStreamDefaultController)

🟢 Fully implemented.

### 

[​

](#url)

[`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL)

🟢 Fully implemented.

### 

[​

](#urlsearchparams)

[`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)

🟢 Fully implemented.

### 

[​

](#webassembly)

[`WebAssembly`](https://nodejs.org/api/globals.html#webassembly)

🟢 Fully implemented.

### 

[​

](#writablestream)

[`WritableStream`](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream)

🟢 Fully implemented.

### 

[​

](#writablestreamdefaultcontroller)

[`WritableStreamDefaultController`](https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultController)

🟢 Fully implemented.

### 

[​

](#writablestreamdefaultwriter)

[`WritableStreamDefaultWriter`](https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter)

🟢 Fully implemented.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/nodejs-compat.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/nodejs-compat>)

[

Web APIs

Previous

](/docs/runtime/web-apis)[

Roadmap

Next

](/docs/project/roadmap)
