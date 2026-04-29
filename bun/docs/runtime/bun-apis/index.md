---
title: "Bun APIs"
source: "https://bun.com/docs/runtime/bun-apis"
canonical_url: "https://bun.com/docs/runtime/bun-apis"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:44.739Z"
content_hash: "4197a180ba9cca24a63e43e601ec92a48e518d734ee9eec91f6c5946fe4bafb3"
menu_path: ["Bun APIs"]
section_path: []
nav_prev: {"path": "../binary-data/index.md", "title": "Binary Data"}
nav_next: {"path": "../bunfig/index.md", "title": "bunfig.toml"}
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

Bun implements a set of native APIs on the `Bun` global object and through several built-in modules. These APIs are heavily optimized and represent the canonical “Bun-native” way to implement some common functionality. Bun strives to implement standard Web APIs wherever possible. Bun introduces new APIs primarily for server-side tasks where no standard exists, such as file I/O and starting an HTTP server. In these cases, Bun’s approach still builds atop standard APIs like `Blob`, `URL`, and `Request`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
Bun.serve({
  fetch(req: Request) {
    return new Response("Success!");
  },
});
```

Click the link in the right column to jump to the associated documentation.

Topic

APIs

HTTP Server

[`Bun.serve`](/docs/runtime/http/server)

Shell

[`$`](/docs/runtime/shell)

Bundler

[`Bun.build`](/docs/bundler)

File I/O

[`Bun.file`](/docs/runtime/file-io#reading-files-bun-file), [`Bun.write`](/docs/runtime/file-io#writing-files-bun-write), `Bun.stdin`, `Bun.stdout`, `Bun.stderr`

Child Processes

[`Bun.spawn`](/docs/runtime/child-process#spawn-a-process-bun-spawn), [`Bun.spawnSync`](/docs/runtime/child-process#blocking-api-bun-spawnsync)

TCP Sockets

[`Bun.listen`](/docs/runtime/networking/tcp#start-a-server-bun-listen), [`Bun.connect`](/docs/runtime/networking/tcp#start-a-server-bun-listen)

UDP Sockets

[`Bun.udpSocket`](/docs/runtime/networking/udp)

WebSockets

`new WebSocket()` (client), [`Bun.serve`](/docs/runtime/http/websockets) (server)

Transpiler

[`Bun.Transpiler`](/docs/runtime/transpiler)

Routing

[`Bun.FileSystemRouter`](/docs/runtime/file-system-router)

Streaming HTML

[`HTMLRewriter`](/docs/runtime/html-rewriter)

Headless Browser

[`Bun.WebView`](/docs/runtime/webview)

Hashing

[`Bun.password`](/docs/runtime/hashing#bun-password), [`Bun.hash`](/docs/runtime/hashing#bun-hash), [`Bun.CryptoHasher`](/docs/runtime/hashing#bun-cryptohasher), `Bun.sha`

CSRF Protection

[`Bun.CSRF.generate`](/docs/runtime/csrf), [`Bun.CSRF.verify`](/docs/runtime/csrf)

SQLite

[`bun:sqlite`](/docs/runtime/sqlite)

PostgreSQL Client

[`Bun.SQL`](/docs/runtime/sql), `Bun.sql`

Redis (Valkey) Client

[`Bun.RedisClient`](/docs/runtime/redis), `Bun.redis`

FFI (Foreign Function Interface)

[`bun:ffi`](/docs/runtime/ffi)

DNS

[`Bun.dns.lookup`](/docs/runtime/networking/dns), `Bun.dns.prefetch`, `Bun.dns.getCacheStats`

Testing

[`bun:test`](/docs/test)

Workers

[`new Worker()`](/docs/runtime/workers)

Module Loaders

[`Bun.plugin`](/docs/bundler/plugins)

Glob

[`Bun.Glob`](/docs/runtime/glob)

Cookies

[`Bun.Cookie`](/docs/runtime/cookies), [`Bun.CookieMap`](/docs/runtime/cookies)

Node-API

[`Node-API`](/docs/runtime/node-api)

`import.meta`

[`import.meta`](/docs/runtime/module-resolution#import-meta)

Utilities

[`Bun.version`](/docs/runtime/utils#bun-version), [`Bun.revision`](/docs/runtime/utils#bun-revision), [`Bun.env`](/docs/runtime/utils#bun-env), [`Bun.main`](/docs/runtime/utils#bun-main)

Sleep & Timing

[`Bun.sleep()`](/docs/runtime/utils#bun-sleep), [`Bun.sleepSync()`](/docs/runtime/utils#bun-sleepsync), [`Bun.nanoseconds()`](/docs/runtime/utils#bun-nanoseconds)

Random & UUID

[`Bun.randomUUIDv7()`](/docs/runtime/utils#bun-randomuuidv7)

System & Environment

[`Bun.which()`](/docs/runtime/utils#bun-which)

Comparison & Inspection

[`Bun.peek()`](/docs/runtime/utils#bun-peek), [`Bun.deepEquals()`](/docs/runtime/utils#bun-deepequals), `Bun.deepMatch`, [`Bun.inspect()`](/docs/runtime/utils#bun-inspect)

String & Text Processing

[`Bun.escapeHTML()`](/docs/runtime/utils#bun-escapehtml), [`Bun.stringWidth()`](/docs/runtime/utils#bun-stringwidth), `Bun.indexOfLine`

URL & Path Utilities

[`Bun.fileURLToPath()`](/docs/runtime/utils#bun-fileurltopath), [`Bun.pathToFileURL()`](/docs/runtime/utils#bun-pathtofileurl)

Compression

[`Bun.gzipSync()`](/docs/runtime/utils#bun-gzipsync), [`Bun.gunzipSync()`](/docs/runtime/utils#bun-gunzipsync), [`Bun.deflateSync()`](/docs/runtime/utils#bun-deflatesync), [`Bun.inflateSync()`](/docs/runtime/utils#bun-inflatesync), `Bun.zstdCompressSync()`, `Bun.zstdDecompressSync()`, `Bun.zstdCompress()`, `Bun.zstdDecompress()`

Stream Processing

[`Bun.readableStreamTo*()`](/docs/runtime/utils#bun-readablestreamto), `Bun.readableStreamToBytes()`, `Bun.readableStreamToBlob()`, `Bun.readableStreamToFormData()`, `Bun.readableStreamToJSON()`, `Bun.readableStreamToArray()`

Memory & Buffer Management

`Bun.ArrayBufferSink`, `Bun.allocUnsafe`, `Bun.concatArrayBuffers`

Module Resolution

[`Bun.resolveSync()`](/docs/runtime/utils#bun-resolvesync)

Parsing & Formatting

[`Bun.semver`](/docs/runtime/semver), [`Bun.TOML.parse`](/docs/runtime/toml), [`Bun.markdown`](/docs/runtime/markdown), [`Bun.color`](/docs/runtime/color)

Low-level / Internals

`Bun.mmap`, `Bun.gc`, `Bun.generateHeapSnapshot`, [`bun:jsc`](https://bun.com/reference/bun/jsc)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/bun-apis.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/bun-apis>)

[

Globals

Previous

](/docs/runtime/globals)[

Web APIs

Next

](/docs/runtime/web-apis)
