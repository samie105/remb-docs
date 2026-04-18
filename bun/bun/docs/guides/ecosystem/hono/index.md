---
title: "Build an HTTP server using Hono and Bun"
source: "https://bun.com/docs/guides/ecosystem/hono"
canonical_url: "https://bun.com/docs/guides/ecosystem/hono"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:37.356Z"
content_hash: "3270e7fa1dafa5c7bd56b67284942344eb4cafc472b781877f45fe010f808863"
menu_path: ["Build an HTTP server using Hono and Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/gel/index.md", "title": "Use Gel with Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/mongoose/index.md", "title": "Read and write data to MongoDB using Mongoose and Bun"}
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

[Hono](https://github.com/honojs/hono) is a lightweight ultrafast web framework designed for the edge.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
import { Hono } from "hono";
const app = new Hono();

app.get("/", c => c.text("Hono!"));

export default app;
```

* * *

Use `create-hono` to get started with one of Hono’s project templates. Select `bun` when prompted for a template.

terminal

```
bun create hono myapp
```

```
✔ Which template do you want to use? › bun
cloned honojs/starter#main to /path/to/myapp
✔ Copied project files
```

terminal

```
cd myapp
bun install
```

* * *

Then start the dev server and visit [localhost:3000](http://localhost:3000).

terminal

```
bun run dev
```

* * *

Refer to Hono’s guide on [getting started with Bun](https://hono.dev/getting-started/bun) for more information.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/hono.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/hono>)

[

Build an HTTP server using Express and Bun

Previous

](/docs/guides/ecosystem/express)[

Read and write data to MongoDB using Mongoose and Bun

Next

](/docs/guides/ecosystem/mongoose)
