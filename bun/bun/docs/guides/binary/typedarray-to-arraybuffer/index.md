---
title: "Convert a Uint8Array to an ArrayBuffer"
source: "https://bun.com/docs/guides/binary/typedarray-to-arraybuffer"
canonical_url: "https://bun.com/docs/guides/binary/typedarray-to-arraybuffer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:21.036Z"
content_hash: "77f0d3493541bb741bfae6758838e4e143e4c6d458428a7496c5685ed205b308"
menu_path: ["Convert a Uint8Array to an ArrayBuffer"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/binary/typedarray-to-blob/index.md", "title": "Convert a Uint8Array to a Blob"}
nav_next: {"path": "bun/bun/docs/guides/binary/typedarray-to-buffer/index.md", "title": "Convert a Uint8Array to a Buffer"}
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

A [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) is a _typed array_ class, meaning it is a mechanism for viewing data in an underlying `ArrayBuffer`. The underlying `ArrayBuffer` is accessible via the `buffer` property.

```
const arr = new Uint8Array(64);
arr.buffer; // => ArrayBuffer(64)
```

* * *

The `Uint8Array` may be a view over a _subset_ of the data in the underlying `ArrayBuffer`. In this case, the `buffer` property will return the entire buffer, and the `byteOffset` and `byteLength` properties will indicate the subset.

```
const arr = new Uint8Array(64, 16, 32);
arr.buffer; // => ArrayBuffer(64)
arr.byteOffset; // => 16
arr.byteLength; // => 32
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/typedarray-to-arraybuffer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/typedarray-to-arraybuffer>)

[

Convert a Uint8Array to a string

Previous

](/docs/guides/binary/typedarray-to-string)[

Convert a Uint8Array to a Buffer

Next

](/docs/guides/binary/typedarray-to-buffer)


