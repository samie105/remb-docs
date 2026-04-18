---
title: "Convert an ArrayBuffer to a Blob"
source: "https://bun.com/docs/guides/binary/arraybuffer-to-blob"
canonical_url: "https://bun.com/docs/guides/binary/arraybuffer-to-blob"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:52.168Z"
content_hash: "6d4f370305115631a356faf4e935c161717c8e0927d7439bfd8e493be559535e"
menu_path: ["Convert an ArrayBuffer to a Blob"]
section_path: []
nav_prev: {"path": "bun/bun/docs/feedback/index.md", "title": "Feedback"}
nav_next: {"path": "bun/bun/docs/guides/binary/arraybuffer-to-array/index.md", "title": "Convert an ArrayBuffer to an array of numbers"}
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

A [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) can be constructed from an array of “chunks”, where each chunk is a string, binary data structure, or another `Blob`.

```
const buf = new ArrayBuffer(64);
const blob = new Blob([buf]);
```

* * *

By default the `type` of the resulting `Blob` will be unset. This can be set manually.

```
const buf = new ArrayBuffer(64);
const blob = new Blob([buf], { type: "application/octet-stream" });
blob.type; // => "application/octet-stream"
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/arraybuffer-to-blob.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/arraybuffer-to-blob>)

[

Convert an ArrayBuffer to a Buffer

Previous

](/docs/guides/binary/arraybuffer-to-buffer)[

Convert an ArrayBuffer to an array of numbers

Next

](/docs/guides/binary/arraybuffer-to-array)


