---
title: "Convert an ArrayBuffer to an array of numbers"
source: "https://bun.com/docs/guides/binary/arraybuffer-to-array"
canonical_url: "https://bun.com/docs/guides/binary/arraybuffer-to-array"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:02.786Z"
content_hash: "dfe08d2d1d3a677d6efd29498a3850b6c2b8358c5e4d9c16c9de4e9ca0c407bd"
menu_path: ["Convert an ArrayBuffer to an array of numbers"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/index.md", "title": "Guides"}
nav_next: {"path": "bun/bun/docs/guides/binary/arraybuffer-to-blob/index.md", "title": "Convert an ArrayBuffer to a Blob"}
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

To retrieve the contents of an `ArrayBuffer` as an array of numbers, create a [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) over of the buffer. and use the [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from) method to convert it to an array.

```
const buf = new ArrayBuffer(64);
const arr = new Uint8Array(buf);
arr.length; // 64
arr[0]; // 0 (instantiated with all zeros)
```

* * *

The `Uint8Array` class supports array indexing and iteration. However if you wish to convert the instance to a regular `Array`, use `Array.from()`. (This will likely be slower than using the `Uint8Array` directly.)

```
const buf = new ArrayBuffer(64);
const uintArr = new Uint8Array(buf);
const regularArr = Array.from(uintArr);
// number[]
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/arraybuffer-to-array.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/arraybuffer-to-array>)

[

Convert an ArrayBuffer to a Blob

Previous

](/docs/guides/binary/arraybuffer-to-blob)[

Convert an ArrayBuffer to a Uint8Array

Next

](/docs/guides/binary/arraybuffer-to-typedarray)
