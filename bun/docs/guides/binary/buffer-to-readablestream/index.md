---
title: "Convert a Buffer to a ReadableStream"
source: "https://bun.com/docs/guides/binary/buffer-to-readablestream"
canonical_url: "https://bun.com/docs/guides/binary/buffer-to-readablestream"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:43.292Z"
content_hash: "c01e96e28624e9f15dc3866d575df8b3157a63ab55283df2b83c126b1e64523e"
menu_path: ["Convert a Buffer to a ReadableStream"]
section_path: []
nav_prev: {"path": "../buffer-to-blob/index.md", "title": "Convert a Buffer to a blob"}
nav_next: {"path": "../buffer-to-string/index.md", "title": "Convert a Buffer to a string"}
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

The naive approach to creating a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) from a [`Buffer`](https://nodejs.org/api/buffer.html) is to use the `ReadableStream` constructor and enqueue the entire array as a single chunk. For a large buffer, this may be undesirable as this approach does not “streaming” the data in smaller chunks.

```
const buf = Buffer.from("hello world");
const stream = new ReadableStream({
  start(controller) {
    controller.enqueue(buf);
    controller.close();
  },
});
```

* * *

To stream the data in smaller chunks, first create a `Blob` instance from the `Buffer`. Then use the [`Blob.stream()`](https://developer.mozilla.org/en-US/docs/Web/API/Blob/stream) method to create a `ReadableStream` that streams the data in chunks of a specified size.

```
const buf = Buffer.from("hello world");
const blob = new Blob([buf]);
const stream = blob.stream();
```

* * *

The chunk size can be set by passing a number to the `.stream()` method.

```
const buf = Buffer.from("hello world");
const blob = new Blob([buf]);

// set chunk size of 1024 bytes
const stream = blob.stream(1024);
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/buffer-to-readablestream.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/buffer-to-readablestream>)

[

Convert a Buffer to a Uint8Array

Previous

](/docs/guides/binary/buffer-to-typedarray)[

Convert a Blob to a string

Next

](/docs/guides/binary/blob-to-string)
