---
title: "Read a file to a Buffer"
source: "https://bun.com/docs/guides/read-file/buffer"
canonical_url: "https://bun.com/docs/guides/read-file/buffer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:24.780Z"
content_hash: "eb1e9abc5a71956747b292e4da92420ec59ded3257a2185b8334255cfbb23013"
menu_path: ["Read a file to a Buffer"]
section_path: []
nav_prev: {"path": "../arraybuffer/index.md", "title": "Read a file to an ArrayBuffer"}
nav_next: {"path": "../exists/index.md", "title": "Check if a file exists"}
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

The `Bun.file()` function accepts a path and returns a `BunFile` instance. The `BunFile` class extends `Blob` and allows you to lazily read the file in a variety of formats. To read the file into a `Buffer` instance, first use `.arrayBuffer()` to consume the file as an `ArrayBuffer`, then use `Buffer.from()` to create a `Buffer` from the `ArrayBuffer`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
const path = "/path/to/package.json";
const file = Bun.file(path);

const arrbuf = await file.arrayBuffer();
const buffer = Buffer.from(arrbuf);
```

* * *

Refer to [Binary data > Buffer](/docs/runtime/binary-data#buffer) for more information on working with `Buffer` and other binary data formats in Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/read-file/buffer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/read-file/buffer>)

[

Read a file as a string

Previous

](/docs/guides/read-file/string)[

Read a file to a Uint8Array

Next

](/docs/guides/read-file/uint8array)
