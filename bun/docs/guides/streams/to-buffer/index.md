---
title: "Convert a ReadableStream to a Buffer"
source: "https://bun.com/docs/guides/streams/to-buffer"
canonical_url: "https://bun.com/docs/guides/streams/to-buffer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:07.170Z"
content_hash: "c5da3615104c6f483c73167a866cc41c5899edb515a46fb5a42bdb959f932533"
menu_path: ["Convert a ReadableStream to a Buffer"]
section_path: []
nav_prev: {"path": "../to-blob/index.md", "title": "Error loading page"}
nav_next: {"path": "../to-json/index.md", "title": "Convert a ReadableStream to JSON"}
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

Bun provides several convenience functions for reading the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into different formats. This snippet reads the contents of a `ReadableStream` to an [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), then creates a [`Buffer`](https://nodejs.org/api/buffer.html) that points to it.

```
const stream = new ReadableStream();
const arrBuf = await Bun.readableStreamToArrayBuffer(stream);
const nodeBuf = Buffer.from(arrBuf);
```

* * *

See [Docs > API > Utils](/docs/runtime/utils#bun-readablestreamto) for documentation on Bun’s other `ReadableStream` conversion functions.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/to-buffer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/to-buffer>)

[

Convert a ReadableStream to a Blob

Previous

](/docs/guides/streams/to-blob)[

Convert a ReadableStream to an ArrayBuffer

Next

](/docs/guides/streams/to-arraybuffer)
