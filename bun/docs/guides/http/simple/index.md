---
title: "Write a simple HTTP server"
source: "https://bun.com/docs/guides/http/simple"
canonical_url: "https://bun.com/docs/guides/http/simple"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:21.515Z"
content_hash: "a73889c3909be8a539e614773d3e5fa56ce83e6022b70977e3b25d4bbd0fba16"
menu_path: ["Write a simple HTTP server"]
section_path: []
nav_prev: {"path": "../server/index.md", "title": "Common HTTP server usage"}
nav_next: {"path": "../sse/index.md", "title": "Server-Sent Events (SSE) with Bun"}
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

This starts an HTTP server listening on port `3000`. It responds to all requests with a `Response` with status `200` and body `"Welcome to Bun!"`. See [`Bun.serve`](/docs/runtime/http/server) for details.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const server = Bun.serve({
  port: 3000,
  fetch(request) {
    return new Response("Welcome to Bun!");
  },
});

console.log(`Listening on ${server.url}`);
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/http/simple.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/http/simple>)

[

Common HTTP server usage

Previous

](/docs/guides/http/server)[

Send an HTTP request using fetch

Next

](/docs/guides/http/fetch)
