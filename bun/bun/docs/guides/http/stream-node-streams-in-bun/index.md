---
title: "Streaming HTTP Server with Node.js Streams"
source: "https://bun.com/docs/guides/http/stream-node-streams-in-bun"
canonical_url: "https://bun.com/docs/guides/http/stream-node-streams-in-bun"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:47.887Z"
content_hash: "6bbcd9e5cff9a36ff23bfb13f261b5dadc595ec0a0784ce389dd9cecb89b30f1"
menu_path: ["Streaming HTTP Server with Node.js Streams"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/http/stream-iterator/index.md", "title": "Streaming HTTP Server with Async Iterators"}
nav_next: {"path": "bun/bun/docs/guides/http/tls/index.md", "title": "Configure TLS on an HTTP server"}
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

In Bun, [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) objects can accept a Node.js [`Readable`](https://nodejs.org/api/stream.html#stream_readable_streams). This works because Bun’s `Response` object allows any async iterable as its body. Node.js streams are async iterables, so you can pass them directly to `Response`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
import { Readable } from "stream";
import { serve } from "bun";
serve({
  port: 3000,
  fetch(req) {
    return new Response(Readable.from(["Hello, ", "world!"]), {
      headers: { "Content-Type": "text/plain" },
    });
  },
});
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/http/stream-node-streams-in-bun.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/http/stream-node-streams-in-bun>)

[

Server-Sent Events (SSE) with Bun

Previous

](/docs/guides/http/sse)[

Build a simple WebSocket server

Next

](/docs/guides/websocket/simple)
