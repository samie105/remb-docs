---
title: "Convert a Blob to a DataView"
source: "https://bun.com/docs/guides/binary/blob-to-dataview"
canonical_url: "https://bun.com/docs/guides/binary/blob-to-dataview"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:59.019Z"
content_hash: "dab982324ea6318eb4c805f884b32eeccbbe53996aa5d64ff8ee9158ebb96ee4"
menu_path: ["Convert a Blob to a DataView"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/binary/blob-to-stream/index.md", "title": "Convert a Blob to a ReadableStream"}
nav_next: {"path": "bun/bun/docs/guides/binary/blob-to-string/index.md", "title": "Convert a Blob to a string"}
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

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides a number of methods for consuming its contents in different formats. This snippets reads the contents to an `ArrayBuffer`, then creates a `DataView` from the buffer.

```
const blob = new Blob(["hello world"]);
const arr = new DataView(await blob.arrayBuffer());
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/blob-to-dataview.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/blob-to-dataview>)

[

Convert a Blob to a Uint8Array

Previous

](/docs/guides/binary/blob-to-typedarray)[

Convert a Blob to a ReadableStream

Next

](/docs/guides/binary/blob-to-stream)
