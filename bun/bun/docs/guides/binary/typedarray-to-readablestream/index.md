---
title: "Convert a Uint8Array to a ReadableStream"
source: "https://bun.com/docs/guides/binary/typedarray-to-readablestream"
canonical_url: "https://bun.com/docs/guides/binary/typedarray-to-readablestream"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:33.627Z"
content_hash: "6ed128dd5e93468437a1abf1ed8a10fe57746922c8567cfd8924142df63773b4"
menu_path: ["Convert a Uint8Array to a ReadableStream"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/binary/typedarray-to-buffer/index.md", "title": "Convert a Uint8Array to a Buffer"}
nav_next: {"path": "bun/bun/docs/guides/binary/typedarray-to-dataview/index.md", "title": "Convert a Uint8Array to a DataView"}
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

The naive approach to creating a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) from a [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) is to use the [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) constructor and enqueue the entire array as a single chunk. For larger chunks, this may be undesirable as it isn’t actually “streaming” the data.

```
const arr = new Uint8Array(64);
const stream = new ReadableStream({
  start(controller) {
    controller.enqueue(arr);
    controller.close();
  },
});
```

* * *

To stream the data in smaller chunks, first create a `Blob` instance from the `Uint8Array`. Then use the [`Blob.stream()`](https://developer.mozilla.org/en-US/docs/Web/API/Blob/stream) method to create a `ReadableStream` that streams the data in chunks of a specified size.

```
const arr = new Uint8Array(64);
const blob = new Blob([arr]);
const stream = blob.stream();
```

* * *

The chunk size can be set by passing a number to the `.stream()` method.

```
const arr = new Uint8Array(64);
const blob = new Blob([arr]);

// set chunk size of 1024 bytes
const stream = blob.stream(1024);
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/typedarray-to-readablestream.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/typedarray-to-readablestream>)

[

Convert a Uint8Array to a DataView

Previous

](/docs/guides/binary/typedarray-to-dataview)[

Convert a DataView to a string

Next

](/docs/guides/binary/dataview-to-string)

