---
title: "Convert a Buffer to a blob"
source: "https://bun.com/docs/guides/binary/buffer-to-blob"
canonical_url: "https://bun.com/docs/guides/binary/buffer-to-blob"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:28.724Z"
content_hash: "b3629fbc2c602302d00f6026fc5fc283f5030c53f61ea352371a87d676f4cec8"
menu_path: ["Convert a Buffer to a blob"]
section_path: []
nav_prev: {"path": "bun/docs/guides/binary/buffer-to-arraybuffer/index.md", "title": "Convert a Buffer to an ArrayBuffer"}
nav_next: {"path": "bun/docs/guides/binary/buffer-to-readablestream/index.md", "title": "Convert a Buffer to a ReadableStream"}
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

A [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) can be constructed from an array of “chunks”, where each chunk is a string, binary data structure (including `Buffer`), or another `Blob`.

```
const buf = Buffer.from("hello");
const blob = new Blob([buf]);
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/buffer-to-blob.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/buffer-to-blob>)

[

Convert a Buffer to an ArrayBuffer

Previous

](/docs/guides/binary/buffer-to-arraybuffer)[

Convert a Buffer to a Uint8Array

Next

](/docs/guides/binary/buffer-to-typedarray)
