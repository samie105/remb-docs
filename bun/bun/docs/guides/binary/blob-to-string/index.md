---
title: "Convert a Blob to a string"
source: "https://bun.com/docs/guides/binary/blob-to-string"
canonical_url: "https://bun.com/docs/guides/binary/blob-to-string"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:09.278Z"
content_hash: "c4e14862a453a2ba9269f7b1a0b219ff76a046547589d8537bf82c3a386f2597"
menu_path: ["Convert a Blob to a string"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/binary/blob-to-dataview/index.md", "title": "Convert a Blob to a DataView"}
nav_next: {"path": "bun/bun/docs/guides/binary/buffer-to-arraybuffer/index.md", "title": "Convert a Buffer to an ArrayBuffer"}
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

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides a number of methods for consuming its contents in different formats, including `.text()`.

```
const blob = new Blob(["hello world"]);
const str = await blob.text();
// => "hello world"
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/blob-to-string.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/blob-to-string>)

[

Convert a Buffer to a ReadableStream

Previous

](/docs/guides/binary/buffer-to-readablestream)[

Convert a Blob to an ArrayBuffer

Next

](/docs/guides/binary/blob-to-arraybuffer)
