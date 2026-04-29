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
nav_prev: {"path": "bun/docs/runtime/binary-data/index.md", "title": "Binary Data"}
nav_next: {"path": "bun/docs/runtime/bunfig/index.md", "title": "bunfig.toml"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](../../index.md)[Package Manager

](../../pm/cli/install/index.md)[Bundler

](../../bundler/index.md)[Test Runner

](../../test/index.md)[Guides

](../../guides/index.md)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](../../feedback/index.md)

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

[`Bun.serve`](../http/server/index.md)

Shell

[`$`](../shell/index.md)

Bundler

[`Bun.build`](../../bundler/index.md)

File I/O

[`Bun.file`](../file-io/index.md#reading-files-bun-file), [`Bun.write`](../file-io/index.md#writing-files-bun-write), `Bun.stdin`, `Bun.stdout`, `Bun.stderr`

Child Processes

[`Bun.spawn`](../child-process/index.md#spawn-a-process-bun-spawn), [`Bun.spawnSync`](../child-process/index.md#blocking-api-bun-spawnsync)

TCP Sockets

[`Bun.listen`](../networking/tcp/index.md#start-a-server-bun-listen), [`Bun.connect`](../networking/tcp/index.md#start-a-server-bun-listen)

UDP Sockets

[`Bun.udpSocket`](../networking/udp/index.md)

WebSockets

`new WebSocket()` (client), [`Bun.serve`](../http/websockets/index.md) (server)

Transpiler

[`Bun.Transpiler`](../transpiler/index.md)

Routing

[`Bun.FileSystemRouter`](../file-system-router/index.md)

Streaming HTML

[`HTMLRewriter`](../html-rewriter/index.md)

Headless Browser

[`Bun.WebView`](/docs/runtime/webview)

Hashing

[`Bun.password`](../hashing/index.md#bun-password), [`Bun.hash`](../hashing/index.md#bun-hash), [`Bun.CryptoHasher`](../hashing/index.md#bun-cryptohasher), `Bun.sha`

CSRF Protection

[`Bun.CSRF.generate`](../csrf/index.md), [`Bun.CSRF.verify`](../csrf/index.md)

SQLite

[`bun:sqlite`](../sqlite/index.md)

PostgreSQL Client

[`Bun.SQL`](../sql/index.md), `Bun.sql`

Redis (Valkey) Client

[`Bun.RedisClient`](../redis/index.md), `Bun.redis`

FFI (Foreign Function Interface)

[`bun:ffi`](../ffi/index.md)

DNS

[`Bun.dns.lookup`](../networking/dns/index.md), `Bun.dns.prefetch`, `Bun.dns.getCacheStats`

Testing

[`bun:test`](../../test/index.md)

Workers

[`new Worker()`](../workers/index.md)

Module Loaders

[`Bun.plugin`](../../bundler/plugins/index.md)

Glob

[`Bun.Glob`](../glob/index.md)

Cookies

[`Bun.Cookie`](../cookies/index.md), [`Bun.CookieMap`](../cookies/index.md)

Node-API

[`Node-API`](../node-api/index.md)

`import.meta`

[`import.meta`](../module-resolution/index.md#import-meta)

Utilities

[`Bun.version`](../utils/index.md#bun-version), [`Bun.revision`](../utils/index.md#bun-revision), [`Bun.env`](../utils/index.md#bun-env), [`Bun.main`](../utils/index.md#bun-main)

Sleep & Timing

[`Bun.sleep()`](../utils/index.md#bun-sleep), [`Bun.sleepSync()`](../utils/index.md#bun-sleepsync), [`Bun.nanoseconds()`](../utils/index.md#bun-nanoseconds)

Random & UUID

[`Bun.randomUUIDv7()`](../utils/index.md#bun-randomuuidv7)

System & Environment

[`Bun.which()`](../utils/index.md#bun-which)

Comparison & Inspection

[`Bun.peek()`](../utils/index.md#bun-peek), [`Bun.deepEquals()`](../utils/index.md#bun-deepequals), `Bun.deepMatch`, [`Bun.inspect()`](../utils/index.md#bun-inspect)

String & Text Processing

[`Bun.escapeHTML()`](../utils/index.md#bun-escapehtml), [`Bun.stringWidth()`](../utils/index.md#bun-stringwidth), `Bun.indexOfLine`

URL & Path Utilities

[`Bun.fileURLToPath()`](../utils/index.md#bun-fileurltopath), [`Bun.pathToFileURL()`](../utils/index.md#bun-pathtofileurl)

Compression

[`Bun.gzipSync()`](../utils/index.md#bun-gzipsync), [`Bun.gunzipSync()`](../utils/index.md#bun-gunzipsync), [`Bun.deflateSync()`](../utils/index.md#bun-deflatesync), [`Bun.inflateSync()`](../utils/index.md#bun-inflatesync), `Bun.zstdCompressSync()`, `Bun.zstdDecompressSync()`, `Bun.zstdCompress()`, `Bun.zstdDecompress()`

Stream Processing

[`Bun.readableStreamTo*()`](../utils/index.md#bun-readablestreamto), `Bun.readableStreamToBytes()`, `Bun.readableStreamToBlob()`, `Bun.readableStreamToFormData()`, `Bun.readableStreamToJSON()`, `Bun.readableStreamToArray()`

Memory & Buffer Management

`Bun.ArrayBufferSink`, `Bun.allocUnsafe`, `Bun.concatArrayBuffers`

Module Resolution

[`Bun.resolveSync()`](../utils/index.md#bun-resolvesync)

Parsing & Formatting

[`Bun.semver`](../semver/index.md), [`Bun.TOML.parse`](../toml/index.md), [`Bun.markdown`](../markdown/index.md), [`Bun.color`](../color/index.md)

Low-level / Internals

`Bun.mmap`, `Bun.gc`, `Bun.generateHeapSnapshot`, [`bun:jsc`](https://bun.com/reference/bun/jsc)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/bun-apis.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/bun-apis>)

[

Globals

Previous

](../globals/index.md)[

Web APIs

Next

](../web-apis/index.md)
