---
title: "fetch with unix domain sockets in Bun"
source: "https://bun.com/docs/guides/http/fetch-unix"
canonical_url: "https://bun.com/docs/guides/http/fetch-unix"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:49.884Z"
content_hash: "2bb5928844e970c8d9ae76884907129fcc09a3a62114122a5b6ddec1122c4e8a"
menu_path: ["fetch with unix domain sockets in Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/html-rewriter/extract-social-meta/index.md", "title": "Extract social share images and Open Graph tags"}
nav_next: {"path": "bun/bun/docs/guides/http/file-uploads/index.md", "title": "Upload files via HTTP using FormData"}
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

In Bun, the `unix` option in `fetch()` lets you send HTTP requests over a [unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket).

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)fetch-unix.ts

```
const unix = "/var/run/docker.sock";

const response = await fetch("http://localhost/info", { unix });

const body = await response.json();
console.log(body); // { ... }
```

* * *

The `unix` option is a string that specifies the local file path to a unix domain socket. The `fetch()` function will use the socket to send the request to the server instead of using a TCP network connection. `https` is also supported by using the `https://` protocol in the URL instead of `http://`. To send a `POST` request to an API endpoint over a unix domain socket:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)fetch-unix.ts

```
const response = await fetch("https://hostname/a/path", {
  unix: "/var/run/path/to/unix.sock",
  method: "POST",
  body: JSON.stringify({ message: "Hello from Bun!" }),
  headers: {
    "Content-Type": "application/json",
  },
});

const body = await response.json();
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/http/fetch-unix.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/http/fetch-unix>)

[

Upload files via HTTP using FormData

Previous

](/docs/guides/http/file-uploads)[

Streaming HTTP Server with Async Iterators

Next

](/docs/guides/http/stream-iterator)
