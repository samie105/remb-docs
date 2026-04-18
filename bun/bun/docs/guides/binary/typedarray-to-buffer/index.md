---
title: "Convert a Uint8Array to a Buffer"
source: "https://bun.com/docs/guides/binary/typedarray-to-buffer"
canonical_url: "https://bun.com/docs/guides/binary/typedarray-to-buffer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:26.347Z"
content_hash: "e280d5182acf364227e36fc8f9d3ad61864a973bf1f0edd639de46def4d28506"
menu_path: ["Convert a Uint8Array to a Buffer"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/binary/typedarray-to-arraybuffer/index.md", "title": "Convert a Uint8Array to an ArrayBuffer"}
nav_next: {"path": "bun/bun/docs/guides/binary/typedarray-to-readablestream/index.md", "title": "Convert a Uint8Array to a ReadableStream"}
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

The [`Buffer`](https://nodejs.org/api/buffer.html) class extends [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) with a number of additional methods. Use `Buffer.from()` to create a `Buffer` instance from a `Uint8Array`.

```
const arr: Uint8Array = ...
const buf = Buffer.from(arr);
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/typedarray-to-buffer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/typedarray-to-buffer>)

[

Convert a Uint8Array to an ArrayBuffer

Previous

](/docs/guides/binary/typedarray-to-arraybuffer)[

Convert a Uint8Array to a Blob

Next

](/docs/guides/binary/typedarray-to-blob)


