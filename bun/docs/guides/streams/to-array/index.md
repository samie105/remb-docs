---
title: "Convert a ReadableStream to an array of chunks"
source: "https://bun.com/docs/guides/streams/to-array"
canonical_url: "https://bun.com/docs/guides/streams/to-array"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:53.430Z"
content_hash: "aa79276f7bc219ead9d0b20b1cc878d0ee6c27ee33a530c44a9f668eb78fefae"
menu_path: ["Convert a ReadableStream to an array of chunks"]
section_path: []
nav_prev: {"path": "../node-readable-to-uint8array/index.md", "title": "Convert a Node.js Readable to an Uint8Array"}
nav_next: {"path": "../to-arraybuffer/index.md", "title": "Convert a ReadableStream to an ArrayBuffer"}
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

Bun provides several convenience functions for reading the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into different formats. The `Bun.readableStreamToArray` function reads the contents of a `ReadableStream` to an array of chunks.

```
const stream = new ReadableStream();
const str = await Bun.readableStreamToArray(stream);
```

* * *

See [Docs > API > Utils](/docs/runtime/utils#bun-readablestreamto) for documentation on Bun’s other `ReadableStream` conversion functions.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/to-array.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/to-array>)

[

Convert a ReadableStream to a Uint8Array

Previous

](/docs/guides/streams/to-typedarray)[

Convert a Node.js Readable to a string

Next

](/docs/guides/streams/node-readable-to-string)
