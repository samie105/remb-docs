---
title: "Node APIs"
source: "https://docs.deno.com/runtime/reference/node_apis/"
canonical_url: "https://docs.deno.com/runtime/reference/node_apis/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:25.267Z"
content_hash: "b3000aa4d83ce952d372fca58ce5be44208fd7dd13ed3b171defb9f2162c0c57"
menu_path: ["Node APIs"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/deno_namespace_apis/index.md", "title": "Deno Namespace APIs"}
nav_next: {"path": "deno/deno/runtime/reference/std/math/index.md", "title": "@std/math"}
---

On this page

*   [Fully supported modules](#fully-supported-modules)
    *   [node:assert](#node%3Aassert)
    *   [node:buffer](#node%3Abuffer)
    *   [node:child\_process](#node%3Achild_process)
    *   [node:console](#node%3Aconsole)
    *   [node:crypto](#node%3Acrypto)
    *   [node:diagnostics\_channel](#node%3Adiagnostics_channel)
    *   [node:events](#node%3Aevents)
    *   [node:fs](#node%3Afs)
    *   [node:fs/promises](#node%3Afs%2Fpromises)
    *   [node:module](#node%3Amodule)
    *   [node:os](#node%3Aos)
    *   [node:path](#node%3Apath)
    *   [node:punycode](#node%3Apunycode)
    *   [node:querystring](#node%3Aquerystring)
    *   [node:readline](#node%3Areadline)
    *   [node:sqlite](#node%3Asqlite)
    *   [node:stream](#node%3Astream)
    *   [node:string\_decoder](#node%3Astring_decoder)
    *   [node:test](#node%3Atest)
    *   [node:timers](#node%3Atimers)
    *   [node:tty](#node%3Atty)
    *   [node:url](#node%3Aurl)
*   [Partially supported modules](#partially-supported-modules)
    *   [node:async\_hooks](#node%3Aasync_hooks)
    *   [node:dgram](#node%3Adgram)
    *   [node:dns](#node%3Adns)
    *   [node:http](#node%3Ahttp)
    *   [node:http2](#node%3Ahttp2)
    *   [node:https](#node%3Ahttps)
    *   [node:inspector](#node%3Ainspector)
    *   [node:net](#node%3Anet)
    *   [node:perf\_hooks](#node%3Aperf_hooks)
    *   [node:process](#node%3Aprocess)
    *   [node:tls](#node%3Atls)
    *   [node:util](#node%3Autil)
    *   [node:v8](#node%3Av8)
    *   [node:vm](#node%3Avm)
    *   [node:worker\_threads](#node%3Aworker_threads)
    *   [node:zlib](#node%3Azlib)
*   [Unsupported modules](#unsupported-modules)
    *   [node:cluster](#node%3Acluster)
    *   [node:domain](#node%3Adomain)
    *   [node:repl](#node%3Arepl)
    *   [node:sea](#node%3Asea)
    *   [node:trace\_events](#node%3Atrace_events)
    *   [node:wasi](#node%3Awasi)
*   [Globals](#globals)
*   [Node test results](#node-test-results)

Deno provides polyfills for a number of built-in Node.js modules and globals.

[Explore built-in Node APIs](/api/node/)

Node compatibility is an ongoing project - help us identify gaps and let us know which modules you need by [opening an issue on GitHub](https://github.com/denoland/deno).

## Fully supported modules (22/44)

### [node:assert](/api/node/assert)

### [node:buffer](/api/node/buffer)

### [node:child\_process](/api/node/child_process)

### [node:console](/api/node/console)

### [node:crypto](/api/node/crypto)

**Certificate**: The methods are non-functional stubs.

**generateKeyPair**: The `x448` option is not supported.

**generatePrime**: The `safe`, `add` and `rem` option is not supported.

**KeyObject**: The following are non-functional stubs:

*   from
*   symmetricKeySize
*   equals

**publicDecrypt**: This symbol is a non-functional stub.

**secureHeapUsed**: This symbol is a non-functional stub.

**setEngine**: This symbol is a non-functional stub.

**ECDH**: The `convertKey` method is a non-functional sub.

**Sign**: The `sign` and `verify` methods are not supported with non BinaryLike input.

### [node:diagnostics\_channel](/api/node/diagnostics_channel)

### [node:events](/api/node/events)

### [node:fs](/api/node/fs)

**writeFile**: Missing `utf16le`, `latin1` and `ucs2` encoding.

**writeFileSync**: Missing `utf16le`, `latin1` and `ucs2` encoding.

### [node:fs/promises](/api/node/fs/promises)

**lchmod**: The lchmod implementation is a not implemented.

### [node:module](/api/node/module)

**Module**: The `register` method is a non-functional stub.

### [node:os](/api/node/os)

### [node:path](/api/node/path)

### [node:punycode](/api/node/punycode)

### [node:querystring](/api/node/querystring)

### [node:readline](/api/node/readline)

### [node:sqlite](/api/node/sqlite)

This module has been added in Deno v2.2.

### [node:stream](/api/node/stream)

### [node:string\_decoder](/api/node/string_decoder)

### [node:test](/api/node/test)

### [node:timers](/api/node/timers)

### [node:tty](/api/node/tty)

### [node:url](/api/node/url)

## Partially supported modules (16/44)

### [node:async\_hooks](/api/node/async_hooks)

**AsyncResource**: The AsyncResource implementation is a non-functional stub.

**executionAsyncId**: The executionAsyncId implementation is a non-functional stub.

**createHook**: The createHook implementation is a non-functional stub.

### [node:dgram](/api/node/dgram)

**Socket**: The following methods are non-functional stubs:

*   addMembership
*   addSourceSpecificMembership
*   dropMembership
*   dropSourceSpecificMembership
*   setBroadcast
*   setMulticastInterface
*   setMulticastLoopback
*   setMulticastTtl
*   setTtl

### [node:dns](/api/node/dns)

**resolve**: The `ttl` option is not supported.

**resolve4**: The `ttl` option is not supported.

**resolve6**: The `ttl` option is not supported.

**resolveCname**: The `ttl` option is not supported.

**resolveCaa**: The `ttl` option is not supported.

**resolveMx**: The `ttl` option is not supported.

**resolveNaptr**: The `ttl` option is not supported.

**resolveNs**: The `ttl` option is not supported.

**resolvePtr**: The `ttl` option is not supported.

**resolveSoa**: The `ttl` option is not supported.

**resolveSrv**: The `ttl` option is not supported.

**resolveTxt**: The `ttl` option is not supported.

**resolveAny**: The `ttl` option is not supported.

### [node:http](/api/node/http)

**RequestOptions**: Option `createConnection` is not supported.

**ClientRequestArgs**: Option `createConnection` is not supported.

**ClientRequest**: Constructor option `createConnection` is not supported.

**request**: Constructor option `createConnection` is not supported.

**get**: Constructor option `createConnection` is not supported.

### [node:http2](/api/node/http2)

**Http2Session**: The following methods are non-functional stubs:

*   setLocalWindowSize
*   ping
*   localSettings
*   remoteSettings
*   settings
*   ref
*   unref

**ServerHttp2Session**: All methods are non-functional stubs.

**Http2Stream**: The following methods are non-functional stubs:

*   aborted
*   bufferSize
*   endAfterHeaders
*   id
*   pending
*   priority
*   rstCode
*   sentHeaders
*   sentInfoHeaders
*   sentTrailers
*   state

**ClientHttp2Stream**: All methods are non-functional stubs.

**getDefaultSettings**: This function is a non-functional stub.

**getPackedSettings**: This function is a non-functional stub.

**getUnpackedSettings**: This function is a non-functional stub.

### [node:https](/api/node/https)

**Server**: The `cert` and `key` options do not support an array input.

### [node:inspector](/api/node/inspector)

`console` is supported. Other APIs are non-functional stubs.

### [node:net](/api/node/net)

**Socket**: The `fd` option is not supported.

### [node:perf\_hooks](/api/node/perf_hooks)

**performance**: The `eventLoopUtilization` method is a non-functional stub. The `timerify` method is not implemented.

**monitorEventLoopDelay**: This symbol is not implemented.

### [node:process](/api/node/process)

The `multipleResolves` and `worker` events are not supported.

### [node:tls](/api/node/tls)

**createSecurePair**: This symbol is currently not supported.

### [node:util](/api/node/util)

**transferableAbortSignal**: This symbol is currently not supported.

**transferableAbortController**: This symbol is currently not supported.

**MIMEParams**: This symbol is currently not supported.

**MIMEType**: This symbol is currently not supported.

**getSystemErrorMap**: This symbol is currently not supported.

### [node:v8](/api/node/v8)

`cachedDataVersionTag` and `getHeapStatistics`, `serialize` and `deserialize` are supported. `setFlagsFromStrings` is a noop. Other APIs are not supported and will throw and error.

**setFlagsFromStrings**: This function is a noop.

### [node:vm](/api/node/vm)

**measureMemory**: This is a non-functional stub.

**compile**: The `importModuleDynamically` parameter is not supported.

**createContext**: The `importModuleDynamically` parameter is not supported.

**Script**: The `importModuleDynamically` parameter is not supported. The `runInContext` method does not support break on `SIGINT`.

### [node:worker\_threads](/api/node/worker_threads)

**parentPort**: The `emit` method is not supported. The `removeAllListeners` method is not supported.

**markAsUntransferable**: This symbol is not supported.

**moveMessagePortToContext**: This symbol is not supported.

**receiveMessageOnPort**: This symbol is not supported.

**Worker**: The `getHeapSnapshot` method is not supported.

### [node:zlib](/api/node/zlib)

**Options**: This class is not supported.

**BrotliOptions**: This class is not supported.

**BrotliCompress**: This class is not supported.

**BrotliDecompress**: This class is not supported.

**ZlibBase**: This class is not supported.

## Unsupported modules (6/44)

### [node:cluster](/api/node/cluster)

All exports are non-functional stubs.

**All symbols**: This symbol is a non-functional stub.

### [node:domain](/api/node/domain)

All exports are non-functional stubs. This is a deprecated Node module.

**All symbols**: This symbol is a non-functional stub.

### [node:repl](/api/node/repl)

All symbols are not supported.

**All symbols**: This symbol is not supported.

### [node:sea](/api/node/sea)

All symbols are not supported.

**All symbols**: This symbol is not supported.

### [node:trace\_events](/api/node/trace_events)

All exports are non-functional stubs.

**All symbols**: This symbol is a non-functional stub.

### [node:wasi](/api/node/wasi)

All exports are non-functional stubs.

**All symbols**: This symbol is a non-functional stub.

## Globals

This is the list of Node globals that Deno supports. These globals are only available in the `npm` package scope. In your own code you can use them by importing them from the relevant `node:` module.

Global name

Status

[`AbortController`](https://nodejs.org/api/globals.html#class-abortcontroller)

✅

[`AbortSignal`](https://nodejs.org/api/globals.html#class-abortsignal)

✅

[`Blob`](https://nodejs.org/api/globals.html#class-blob)

✅

[`Buffer`](https://nodejs.org/api/globals.html#class-buffer)

✅

[`ByteLengthQueuingStrategy`](https://nodejs.org/api/globals.html#class-bytelengthqueuingstrategy)

✅

[`__dirname`](https://nodejs.org/api/globals.html#__dirname)

⚠️ [Info](#node.js-global-objects)

[`__filename`](https://nodejs.org/api/globals.html#__filename)

⚠️ [Info](#nodejs-global-objects)

[`atob`](https://nodejs.org/api/globals.html#atobdata)

✅

[`BroadcastChannel`](https://nodejs.org/api/globals.html#broadcastchannel)

✅

[`btoa`](https://nodejs.org/api/globals.html#btoadata)

✅

[`clearImmediate`](https://nodejs.org/api/globals.html#clearimmediateimmediateobject)

✅

[`clearInterval`](https://nodejs.org/api/globals.html#clearintervalintervalobject)

✅

[`clearTimeout`](https://nodejs.org/api/globals.html#cleartimeouttimeoutobject)

✅

[`CompressionStream`](https://nodejs.org/api/globals.html#class-compressionstream)

✅

[`console`](https://nodejs.org/api/globals.html#console)

✅

[`CountQueuingStrategy`](https://nodejs.org/api/globals.html#class-countqueuingstrategy)

✅

[`Crypto`](https://nodejs.org/api/globals.html#crypto)

✅

[`CryptoKey`](https://nodejs.org/api/globals.html#cryptokey)

✅

[`CustomEvent`](https://nodejs.org/api/globals.html#customevent)

✅

[`CustomEvent`](https://nodejs.org/api/globals.html#customevent)

✅

[`DecompressionStream`](https://nodejs.org/api/globals.html#class-decompressionstream)

✅

[`Event`](https://nodejs.org/api/globals.html#event)

✅

[`EventTarget`](https://nodejs.org/api/globals.html#eventtarget)

✅

[`exports`](https://nodejs.org/api/globals.html#exports)

✅

[`fetch`](https://nodejs.org/api/globals.html#fetch)

✅

[`File`](https://nodejs.org/api/globals.html#class-file)

✅

[`FormData`](https://nodejs.org/api/globals.html#class-formdata)

✅

[`global`](https://nodejs.org/api/globals.html#global)

✅

[`Headers`](https://nodejs.org/api/globals.html#class-headers)

✅

[`MessageChannel`](https://nodejs.org/api/globals.html#messagechannel)

✅

[`MessageEvent`](https://nodejs.org/api/globals.html#messageevent)

✅

[`MessagePort`](https://nodejs.org/api/globals.html#messageport)

✅

[`module`](https://nodejs.org/api/globals.html#module)

✅

[`PerformanceEntry`](https://nodejs.org/api/globals.html#performanceentry)

✅

[`PerformanceMark`](https://nodejs.org/api/globals.html#performancemark)

✅

[`PerformanceMeasure`](https://nodejs.org/api/globals.html#performancemeasure)

✅

[`PerformanceObserver`](https://nodejs.org/api/globals.html#performanceobserver)

✅

[`PerformanceObserverEntryList`](https://nodejs.org/api/globals.html#performanceobserverentrylist)

❌

[`PerformanceResourceTiming`](https://nodejs.org/api/globals.html#performanceresourcetiming)

❌

[`performance`](https://nodejs.org/api/globals.html#performance)

✅

[`process`](https://nodejs.org/api/globals.html#process)

✅

[`queueMicrotask`](https://nodejs.org/api/globals.html#queuemicrotaskcallback)

✅

[`ReadableByteStreamController`](https://nodejs.org/api/globals.html#class-readablebytestreamcontroller)

✅

[`ReadableStream`](https://nodejs.org/api/globals.html#class-readablestream)

✅

[`ReadableStreamBYOBReader`](https://nodejs.org/api/globals.html#class-readablestreambyobreader)

✅

[`ReadableStreamBYOBRequest`](https://nodejs.org/api/globals.html#class-readablestreambyobrequest)

✅

[`ReadableStreamDefaultController`](https://nodejs.org/api/globals.html#class-readablestreamdefaultcontroller)

✅

[`ReadableStreamDefaultReader`](https://nodejs.org/api/globals.html#class-readablestreamdefaultreader)

✅

[`require`](https://nodejs.org/api/globals.html#require)

✅

[`Response`](https://nodejs.org/api/globals.html#response)

✅

[`Request`](https://nodejs.org/api/globals.html#request)

✅

[`setImmediate`](https://nodejs.org/api/globals.html#setimmediatecallback-args)

✅

[`setInterval`](https://nodejs.org/api/globals.html#setintervalcallback-delay-args)

✅

[`setTimeout`](https://nodejs.org/api/globals.html#settimeoutcallback-delay-args)

✅

[`structuredClone`](https://nodejs.org/api/globals.html#structuredclonevalue-options)

✅

[`structuredClone`](https://nodejs.org/api/globals.html#structuredclonevalue-options)

✅

[`SubtleCrypto`](https://nodejs.org/api/globals.html#subtlecrypto)

✅

[`DOMException`](https://nodejs.org/api/globals.html#domexception)

✅

[`TextDecoder`](https://nodejs.org/api/globals.html#textdecoder)

✅

[`TextDecoderStream`](https://nodejs.org/api/globals.html#class-textdecoderstream)

✅

[`TextEncoder`](https://nodejs.org/api/globals.html#textencoder)

✅

[`TextEncoderStream`](https://nodejs.org/api/globals.html#class-textencoderstream)

✅

[`TransformStream`](https://nodejs.org/api/globals.html#class-transformstream)

✅

[`TransformStreamDefaultController`](https://nodejs.org/api/globals.html#class-transformstreamdefaultcontroller)

✅

[`URL`](https://nodejs.org/api/globals.html#url)

✅

[`URLSearchParams`](https://nodejs.org/api/globals.html#urlsearchparams)

✅

[`URLSearchParams`](https://nodejs.org/api/globals.html#urlsearchparams)

✅

[`WebAssembly`](https://nodejs.org/api/globals.html#webassembly)

✅

[`WritableStream`](https://nodejs.org/api/globals.html#class-writablestream)

✅

[`WritableStreamDefaultController`](https://nodejs.org/api/globals.html#class-writablestreamdefaultcontroller)

✅

[`WritableStreamDefaultWriter`](https://nodejs.org/api/globals.html#class-writablestreamdefaultwriter)

✅

## Node test results

If you're interested in a more detailed view of compatibility on a per-test-case basis, you can find a list of both passing and failing Node.js test cases on [this page](https://node-test-viewer.deno.dev/).
