---
title: "Get the path to an executable bin file"
source: "https://bun.com/docs/guides/util/which-path-to-executable-bin"
canonical_url: "https://bun.com/docs/guides/util/which-path-to-executable-bin"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:21.749Z"
content_hash: "b60eb7b8bc3362980621d0750ff9a12978066e9ad39284007c5e2c7468e395fa"
menu_path: ["Get the path to an executable bin file"]
section_path: []
nav_prev: {"path": "bun/docs/guides/util/version/index.md", "title": "Get the current Bun version"}
nav_next: {"path": "bun/docs/guides/websocket/compression/index.md", "title": "Enable compression for WebSocket messages"}
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

`Bun.which` is a utility function to find the absolute path of an executable file. It is similar to the `which` command in Unix-like systems.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)foo.ts

```
Bun.which("sh"); // => "/bin/sh"
Bun.which("notfound"); // => null
Bun.which("bun"); // => "/home/user/.bun/bin/bun"
```

* * *

See [Docs > API > Utils](/docs/runtime/utils#bun-which) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/which-path-to-executable-bin.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/which-path-to-executable-bin>)

[

Convert an absolute path to a file URL

Previous

](/docs/guides/util/path-to-file-url)[

Get the directory of the current file

Next

](/docs/guides/util/import-meta-dir)
