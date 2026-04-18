---
title: "Stream a file as an HTTP Response"
source: "https://bun.com/docs/guides/http/stream-file"
canonical_url: "https://bun.com/docs/guides/http/stream-file"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:36.599Z"
content_hash: "0bb1e25836dfa0385989fcb7db4880844558671e586e2b1f3684499748e884e5"
menu_path: ["Stream a file as an HTTP Response"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/http/sse/index.md", "title": "Server-Sent Events (SSE) with Bun"}
nav_next: {"path": "bun/bun/docs/guides/http/stream-iterator/index.md", "title": "Streaming HTTP Server with Async Iterators"}
---

This snippet reads a file from disk using [`Bun.file()`](bun/bun/docs/runtime/file-io/index.md#reading-files-bun-file). This returns a `BunFile` instance, which can be passed directly into the `new Response` constructor.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const path = "/path/to/file.txt";
const file = Bun.file(path);
const resp = new Response(file);
```

* * *

The `Content-Type` is read from the file and automatically set on the `Response`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
new Response(Bun.file("./package.json")).headers.get("Content-Type");
// => application/json;charset=utf-8

new Response(Bun.file("./test.txt")).headers.get("Content-Type");
// => text/plain;charset=utf-8

new Response(Bun.file("./index.tsx")).headers.get("Content-Type");
// => text/javascript;charset=utf-8

new Response(Bun.file("./img.png")).headers.get("Content-Type");
// => image/png
```

* * *

Putting it all together with [`Bun.serve()`](bun/bun/docs/runtime/http/server/index.md).

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
// static file server
Bun.serve({
  async fetch(req) {
    const path = new URL(req.url).pathname;
    const file = Bun.file(path);
    return new Response(file);
  },
});
```

* * *

See [Docs > API > File I/O](bun/bun/docs/runtime/file-io/index.md#writing-files-bun-write) for complete documentation of `Bun.write()`.

Was this page helpful?

