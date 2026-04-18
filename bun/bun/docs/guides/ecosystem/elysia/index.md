---
title: "Build an HTTP server using Elysia and Bun"
source: "https://bun.com/docs/guides/ecosystem/elysia"
canonical_url: "https://bun.com/docs/guides/ecosystem/elysia"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:05.355Z"
content_hash: "921ad8f104566825b1082e87dfd3ab6065d601351e771beff8bd7dffceb99e4f"
menu_path: ["Build an HTTP server using Elysia and Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/express/index.md", "title": "Build an HTTP server using Express and Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/drizzle/index.md", "title": "Use Drizzle ORM with Bun"}
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

[Elysia](https://elysiajs.com) is a Bun-first performance focused web framework that takes full advantage of Bun’s HTTP, file system, and hot reloading APIs. Get started with `bun create`.

terminal

```
bun create elysia myapp
cd myapp
bun run dev
```

* * *

To define an HTTP route and start a server with Elysia:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
import { Elysia } from "elysia";

const app = new Elysia().get("/", () => "Hello Elysia").listen(8080);

console.log(`🦊 Elysia is running at on port ${app.server?.port}...`);
```

* * *

Elysia is a full-featured server framework with Express-like syntax, type inference, middleware, file uploads, and plugins for JWT authentication, tRPC, and more. It’s also is one of the [fastest Bun web frameworks](https://github.com/SaltyAom/bun-http-framework-benchmark). Refer to the Elysia [documentation](https://elysiajs.com/quick-start.html) for more information.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/elysia.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/elysia>)

[

Use Gel with Bun

Previous

](/docs/guides/ecosystem/gel)[

Build an HTTP server using Express and Bun

Next

](/docs/guides/ecosystem/express)
