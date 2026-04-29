---
title: "Set environment variables"
source: "https://bun.com/docs/guides/runtime/set-env"
canonical_url: "https://bun.com/docs/guides/runtime/set-env"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:10.105Z"
content_hash: "b1e6c7f608b7d4bfca099d5709c0a5c4877613fdeee2d1be44c71909fc6eb431"
menu_path: ["Set environment variables"]
section_path: []
nav_prev: {"path": "bun/docs/guides/runtime/read-env/index.md", "title": "Read environment variables"}
nav_next: {"path": "bun/docs/guides/runtime/shell/index.md", "title": "Run a Shell Command"}
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

The current environment variables can be accessed via `process.env` or `Bun.env`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
Bun.env.API_TOKEN; // => "secret"
process.env.API_TOKEN; // => "secret"
```

* * *

Set these variables in a `.env` file. Bun reads the following files automatically (listed in order of increasing precedence).

*   `.env`
*   `.env.production`, `.env.development`, `.env.test` (depending on value of `NODE_ENV`)
*   `.env.local` (not loaded when `NODE_ENV=test`)

.env

```
FOO=hello
BAR=world
```

* * *

Variables can also be set via the command line.

```
FOO=helloworld bun run dev
```

* * *

See [Docs > Runtime > Environment variables](../../../runtime/environment-variables/index.md) for more information on using environment variables with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/set-env.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/set-env>)

[

Set a time zone in Bun

Previous

](../timezone/index.md)[

Read environment variables

Next

](../read-env/index.md)
