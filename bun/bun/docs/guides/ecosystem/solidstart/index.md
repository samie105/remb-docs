---
title: "Build an app with SolidStart and Bun"
source: "https://bun.com/docs/guides/ecosystem/solidstart"
canonical_url: "https://bun.com/docs/guides/ecosystem/solidstart"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:22.395Z"
content_hash: "a2e27497e77c088417b3d57f382abed2e7ae9313ca6037b968f6e31b4134821d"
menu_path: ["Build an app with SolidStart and Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/remix/index.md", "title": "Build an app with Remix and Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/stric/index.md", "title": "Build an HTTP server using StricJS and Bun"}
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

Initialize a SolidStart app with `create-solid`. You can specify the `--solidstart` flag to create a SolidStart project, and `--ts` for TypeScript support. When prompted for a template, select `basic` for a minimal starter app.

terminal

```
bun create solid my-app --solidstart --ts
```

```
┌
 Create-Solid v0.6.11
│
◇  Project Name
│  my-app
│
◇  Which template would you like to use?
│  basic
│
◇  Project created 🎉
│
◇  To get started, run: ─╮
│                        │
│  cd my-app             │
│  bun install           │
│  bun dev               │
│                        │
├────────────────────────╯
```

* * *

As instructed by the `create-solid` CLI, install the dependencies.

terminal

```
cd my-app
bun install
```

Then run the development server with `bun dev`.

terminal

```
bun dev
```

```
$ vinxi dev
vinxi v0.5.8
vinxi starting dev server

  ➜ Local:    http://localhost:3000/
  ➜ Network:  use --host to expose
```

Open [localhost:3000](http://localhost:3000). Any changes you make to `src/routes/index.tsx` will be hot-reloaded automatically.

* * *

Refer to the [SolidStart website](https://docs.solidjs.com/solid-start) for complete framework documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/solidstart.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/solidstart>)

[

Add Sentry to a Bun app

Previous

](/docs/guides/ecosystem/sentry)[

Server-side render (SSR) a React component

Next

](/docs/guides/ecosystem/ssr-react)
