---
title: "Build an HTTP server using StricJS and Bun"
source: "https://bun.com/docs/guides/ecosystem/stric"
canonical_url: "https://bun.com/docs/guides/ecosystem/stric"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:29.136Z"
content_hash: "cdb7c882b632b0ef33dae8b8c048abade2d4b6b5dc05bd126a8b2e923bc74a9e"
menu_path: ["Build an HTTP server using StricJS and Bun"]
section_path: []
nav_prev: {"path": "../ssr-react/index.md", "title": "Server-side render (SSR) a React component"}
nav_next: {"path": "../sveltekit/index.md", "title": "Build an app with SvelteKit and Bun"}
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

[StricJS](https://github.com/bunsvr) is a Bun framework for building high-performance web applications and APIs.

*   **Fast** — Stric is one of the fastest Bun frameworks. See [benchmark](https://github.com/bunsvr/benchmark) for more details.
*   **Minimal** — The basic components like `@stricjs/router` and `@stricjs/utils` are under 50kB and require no external dependencies.
*   **Extensible** — Stric includes with a plugin system, dependency injection, and optional optimizations for handling requests.

* * *

Use `bun init` to create an empty project.

terminal

```
mkdir myapp
cd myapp
bun init
bun add @stricjs/router @stricjs/utils
```

* * *

To implement an HTTP server with StricJS:

index.ts

```
import { Router } from "@stricjs/router";

export default new Router().get("/", () => new Response("Hi"));
```

* * *

To serve static files from `/public`:

index.ts

```
import { dir } from "@stricjs/utils";

export default new Router().get("/", () => new Response("Hi")).get("/*", dir("./public"));
```

* * *

Run the file in watch mode to start the development server.

terminal

```
bun --watch run index.ts
```

* * *

For more info, see Stric’s [documentation](https://stricjs.netlify.app).

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/stric.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/stric>)

[

Server-side render (SSR) a React component

Previous

](/docs/guides/ecosystem/ssr-react)[

Build an app with SvelteKit and Bun

Next

](/docs/guides/ecosystem/sveltekit)
