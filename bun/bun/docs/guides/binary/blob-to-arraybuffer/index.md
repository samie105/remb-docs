---
title: "Convert a Blob to an ArrayBuffer"
source: "https://bun.com/docs/guides/binary/blob-to-arraybuffer"
canonical_url: "https://bun.com/docs/guides/binary/blob-to-arraybuffer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:37.447Z"
content_hash: "dcecd11e6b216935707a38132e41ed7f6a00ced317dedae0e50bc31320b367a7"
menu_path: ["Convert a Blob to an ArrayBuffer"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/binary/arraybuffer-to-string/index.md", "title": "Convert an ArrayBuffer to a string"}
nav_next: {"path": "bun/bun/docs/guides/binary/blob-to-stream/index.md", "title": "Convert a Blob to a ReadableStream"}
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

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides a number of methods for consuming its contents in different formats, including `.arrayBuffer()`.

```
const blob = new Blob(["hello world"]);
const buf = await blob.arrayBuffer();
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/blob-to-arraybuffer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/blob-to-arraybuffer>)

[

Convert a Blob to a string

Previous

](/docs/guides/binary/blob-to-string)[

Convert a Blob to a Uint8Array

Next

](/docs/guides/binary/blob-to-typedarray)


