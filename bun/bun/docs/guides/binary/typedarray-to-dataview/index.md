---
title: "Convert a Uint8Array to a DataView"
source: "https://bun.com/docs/guides/binary/typedarray-to-dataview"
canonical_url: "https://bun.com/docs/guides/binary/typedarray-to-dataview"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:38.767Z"
content_hash: "bda324c1558c6a365c13bf6cf72b73bec8a2a9a46dc81db9c621fbc1210a330c"
menu_path: ["Convert a Uint8Array to a DataView"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/binary/typedarray-to-readablestream/index.md", "title": "Convert a Uint8Array to a ReadableStream"}
nav_next: {"path": "bun/bun/docs/guides/binary/typedarray-to-string/index.md", "title": "Convert a Uint8Array to a string"}
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

A [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) is a _typed array_ class, meaning it is a mechanism for viewing data in an underlying `ArrayBuffer`. The following snippet creates a \[`DataView`\] instance over the same range of data as the `Uint8Array`.

```
const arr: Uint8Array = ...
const dv = new DataView(arr.buffer, arr.byteOffset, arr.byteLength);
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/typedarray-to-dataview.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/typedarray-to-dataview>)

[

Convert a Uint8Array to a Blob

Previous

](/docs/guides/binary/typedarray-to-blob)[

Convert a Uint8Array to a ReadableStream

Next

](/docs/guides/binary/typedarray-to-readablestream)


