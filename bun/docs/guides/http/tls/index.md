---
title: "Configure TLS on an HTTP server"
source: "https://bun.com/docs/guides/http/tls"
canonical_url: "https://bun.com/docs/guides/http/tls"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:54.852Z"
content_hash: "d40f6352ad04d7db46eb3924f6da599e7eb6dd6e8f38768c77a4650ab70041a7"
menu_path: ["Configure TLS on an HTTP server"]
section_path: []
nav_prev: {"path": "bun/docs/guides/http/stream-node-streams-in-bun/index.md", "title": "Streaming HTTP Server with Node.js Streams"}
nav_next: {"path": "bun/docs/guides/install/add/index.md", "title": "Add a dependency"}
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

Set the `tls` key to configure TLS. Both `key` and `cert` are required. The `key` should be the contents of your private key; `cert` should be the contents of your issued certificate. Use [`Bun.file()`](/docs/runtime/file-io#reading-files-bun-file) to read the contents.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const server = Bun.serve({
  fetch: request => new Response("Welcome to Bun!"),
  tls: {
    cert: Bun.file("cert.pem"),
    key: Bun.file("key.pem"),
  },
});
```

* * *

By default Bun trusts the default Mozilla-curated list of well-known root CAs. To override this list, pass an array of certificates as `ca`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const server = Bun.serve({
  fetch: request => new Response("Welcome to Bun!"),
  tls: {
    cert: Bun.file("cert.pem"),
    key: Bun.file("key.pem"),
    ca: [Bun.file("ca1.pem"), Bun.file("ca2.pem")],
  },
});
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/http/tls.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/http/tls>)

[

Start a cluster of HTTP servers

Previous

](/docs/guides/http/cluster)[

Proxy HTTP requests using fetch()

Next

](/docs/guides/http/proxy)
