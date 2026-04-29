---
title: "Build an HTTP server using Express and Bun"
source: "https://bun.com/docs/guides/ecosystem/express"
canonical_url: "https://bun.com/docs/guides/ecosystem/express"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:58.257Z"
content_hash: "134e9ac3f87b1dc868854659278d3d4abfb93e4f581e998fa67405010c021a46"
menu_path: ["Build an HTTP server using Express and Bun"]
section_path: []
nav_prev: {"path": "bun/docs/guides/ecosystem/elysia/index.md", "title": "Build an HTTP server using Elysia and Bun"}
nav_next: {"path": "bun/docs/guides/ecosystem/gel/index.md", "title": "Use Gel with Bun"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](../../../index.md)[Package Manager

](../../../pm/cli/install/index.md)[Bundler

](../../../bundler/index.md)[Test Runner

](../../../test/index.md)[Guides

](../../index.md)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](../../../feedback/index.md)

Express and other major Node.js HTTP libraries should work out of the box. Bun implements the [`node:http`](https://nodejs.org/api/http.html) and [`node:https`](https://nodejs.org/api/https.html) modules that these libraries rely on.

Refer to the [Runtime > Node.js APIs](../../../runtime/nodejs-compat/index.md#node-http) page for more detailed compatibility information.

terminal

```
bun add express
```

* * *

To define an HTTP route and start a server with Express:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
import express from "express";

const app = express();
const port = 8080;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Listening on port ${port}...`);
});
```

* * *

To start the server on `localhost`:

terminal

```
bun server.ts
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/express.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/express>)

[

Build an HTTP server using Elysia and Bun

Previous

](../elysia/index.md)[

Build an HTTP server using Hono and Bun

Next

](../hono/index.md)
