---
title: "Read environment variables"
source: "https://bun.com/docs/guides/runtime/read-env"
canonical_url: "https://bun.com/docs/guides/runtime/read-env"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:06.338Z"
content_hash: "b0287eb460655bbcd3274ecd596bf66b4f2b05bf8abb963122d57a54f950400b"
menu_path: ["Read environment variables"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/runtime/import-yaml/index.md", "title": "Import a YAML file"}
nav_next: {"path": "bun/bun/docs/guides/runtime/set-env/index.md", "title": "Set environment variables"}
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

The current environment variables can be accessed via `process.env`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
process.env.API_TOKEN; // => "secret"
```

* * *

Bun also exposes these variables via `Bun.env`, which is an alias of `process.env`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
Bun.env.API_TOKEN; // => "secret"
```

* * *

To print all currently-set environment variables to the command line, run `bun --print process.env`. This is useful for debugging.

terminal

```
bun --print process.env
```

```
BAZ=stuff
FOOBAR=aaaaaa
<lots more lines>
```

* * *

See [Docs > Runtime > Environment variables](/docs/runtime/environment-variables) for more information on using environment variables with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/read-env.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/read-env>)

[

Set environment variables

Previous

](/docs/guides/runtime/set-env)[

Add a dependency

Next

](/docs/guides/install/add)


