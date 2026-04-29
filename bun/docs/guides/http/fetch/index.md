---
title: "Send an HTTP request using fetch"
source: "https://bun.com/docs/guides/http/fetch"
canonical_url: "https://bun.com/docs/guides/http/fetch"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:41.724Z"
content_hash: "d19015194da905826dba3fd95aec7f95b75c3cc0a476d26f969afe9888412bf8"
menu_path: ["Send an HTTP request using fetch"]
section_path: []
nav_prev: {"path": "../cluster/index.md", "title": "Start a cluster of HTTP servers"}
nav_next: {"path": "../fetch-unix/index.md", "title": "fetch with unix domain sockets in Bun"}
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

Bun implements the Web-standard [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) API for sending HTTP requests. To send a simple `GET` request to a URL:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)fetch.ts

```
const response = await fetch("https://bun.com");
const html = await response.text(); // HTML string
```

* * *

To send a `POST` request to an API endpoint.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)fetch.ts

```
const response = await fetch("https://bun.com/api", {
  method: "POST",
  body: JSON.stringify({ message: "Hello from Bun!" }),
  headers: { "Content-Type": "application/json" },
});

const body = await response.json();
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/http/fetch.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/http/fetch>)

[

Write a simple HTTP server

Previous

](/docs/guides/http/simple)[

Hot reload an HTTP server

Next

](/docs/guides/http/hot)
