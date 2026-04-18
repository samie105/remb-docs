---
title: "Hot reload an HTTP server"
source: "https://bun.com/docs/guides/http/hot"
canonical_url: "https://bun.com/docs/guides/http/hot"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:03.934Z"
content_hash: "da297c3a0a970b51ad9d19a5a244b8f9e4f7ff15f4c8043a699a22ca627a3c21"
menu_path: ["Hot reload an HTTP server"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/http/file-uploads/index.md", "title": "Upload files via HTTP using FormData"}
nav_next: {"path": "bun/bun/docs/guides/http/proxy/index.md", "title": "Proxy HTTP requests using fetch()"}
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

Bun supports the [`--hot`](/docs/runtime/watch-mode#hot-mode) flag to run a file with hot reloading enabled. When any module or file changes, Bun re-runs the file.

terminal

```
bun --hot run index.ts
```

* * *

Bun detects when you are running an HTTP server with `Bun.serve()`. It reloads your fetch handler when source files change, _without_ restarting the `bun` process. This makes hot reloads nearly instantaneous.

Note that this doesn’t reload the page on your browser.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
Bun.serve({
  port: 3000,
  fetch(req) {
    return new Response("Hello world");
  },
});
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/http/hot.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/http/hot>)

[

Send an HTTP request using fetch

Previous

](/docs/guides/http/fetch)[

Start a cluster of HTTP servers

Next

](/docs/guides/http/cluster)


