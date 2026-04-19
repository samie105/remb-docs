---
title: "Convert a ReadableStream to a Uint8Array"
source: "https://bun.com/docs/guides/streams/to-typedarray"
canonical_url: "https://bun.com/docs/guides/streams/to-typedarray"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:19.676Z"
content_hash: "afe90f1178d1f55a472a43d9a0feb432aa3553edc916314ca0ac48a1a2fe503f"
menu_path: ["Convert a ReadableStream to a Uint8Array"]
section_path: []
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

Bun provides several convenience functions for reading the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into different formats. This snippet reads the contents of a `ReadableStream` to an [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), then creates a [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) that points to the buffer.

```
const stream = new ReadableStream();
const buf = await Bun.readableStreamToArrayBuffer(stream);
const uint8 = new Uint8Array(buf);
```

Additionally, there is a convenience method to convert to `Uint8Array` directly.

```
const stream = new ReadableStream();
const uint8 = await Bun.readableStreamToBytes(stream);
```

* * *

See [Docs > API > Utils](/docs/runtime/utils#bun-readablestreamto) for documentation on Bun’s other `ReadableStream` conversion functions.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/to-typedarray.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/to-typedarray>)

[

Convert a ReadableStream to an ArrayBuffer

Previous

](/docs/guides/streams/to-arraybuffer)[

Convert a ReadableStream to an array of chunks

Next

](/docs/guides/streams/to-array)
