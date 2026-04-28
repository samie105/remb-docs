---
title: "Streaming HTTP Server with Async Iterators"
source: "https://bun.com/docs/guides/http/stream-iterator"
canonical_url: "https://bun.com/docs/guides/http/stream-iterator"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:42.125Z"
content_hash: "80d56ada88722e2be61e4d46b1bc5a20f0435ae99d8f365d7e20d17e6217fd07"
menu_path: ["Streaming HTTP Server with Async Iterators"]
section_path: []
nav_prev: {"path": "bun/docs/guides/http/stream-file/index.md", "title": "Stream a file as an HTTP Response"}
nav_next: {"path": "bun/docs/guides/http/stream-node-streams-in-bun/index.md", "title": "Streaming HTTP Server with Node.js Streams"}
---

In Bun, [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) objects can accept an async generator function as their body. This allows you to stream data to the client as it becomes available, rather than waiting for the entire response to be ready.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)stream-iterator.ts

```
Bun.serve({
  port: 3000,
  fetch(req) {
    return new Response(
      // An async generator function
      async function* () {
        yield "Hello, ";
        await Bun.sleep(100);
        yield "world!";

        // you can also yield a TypedArray or Buffer
        yield new Uint8Array(["\n".charCodeAt(0)]);
      },
      { headers: { "Content-Type": "text/plain" } },
    );
  },
});
```

* * *

You can pass any async iterable directly to `Response`:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)stream-iterator.ts

```
Bun.serve({
  port: 3000,
  fetch(req) {
    return new Response(
      {
        [Symbol.asyncIterator]: async function* () {
          yield "Hello, ";
          await Bun.sleep(100);
          yield "world!";
        },
      },
      { headers: { "Content-Type": "text/plain" } },
    );
  },
});
```

Was this page helpful?
