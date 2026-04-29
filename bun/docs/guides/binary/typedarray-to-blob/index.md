---
title: "Convert a Uint8Array to a Blob"
source: "https://bun.com/docs/guides/binary/typedarray-to-blob"
canonical_url: "https://bun.com/docs/guides/binary/typedarray-to-blob"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:18.217Z"
content_hash: "62ce14e352e5bee168418a4827f098c7d00f407284538e0b4165d869f7bee4ee"
menu_path: ["Convert a Uint8Array to a Blob"]
section_path: []
nav_prev: {"path": "../typedarray-to-arraybuffer/index.md", "title": "Convert a Uint8Array to an ArrayBuffer"}
nav_next: {"path": "../typedarray-to-buffer/index.md", "title": "Convert a Uint8Array to a Buffer"}
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

A [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) can be constructed from an array of “chunks”, where each chunk is a string, binary data structure (including `Uint8Array`), or another `Blob`.

```
const arr = new Uint8Array([0x68, 0x65, 0x6c, 0x6c, 0x6f]);
const blob = new Blob([arr]);
console.log(await blob.text());
// => "hello"
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/typedarray-to-blob.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/typedarray-to-blob>)

[

Convert a Uint8Array to a Buffer

Previous

](/docs/guides/binary/typedarray-to-buffer)[

Convert a Uint8Array to a DataView

Next

](/docs/guides/binary/typedarray-to-dataview)
