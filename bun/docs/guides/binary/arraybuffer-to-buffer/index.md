---
title: "Convert an ArrayBuffer to a Buffer"
source: "https://bun.com/docs/guides/binary/arraybuffer-to-buffer"
canonical_url: "https://bun.com/docs/guides/binary/arraybuffer-to-buffer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:14.112Z"
content_hash: "1a41ee47a59fd7aa86609c9a0826f017f870aa7535a8faae499d52912f074869"
menu_path: ["Convert an ArrayBuffer to a Buffer"]
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

The Node.js [`Buffer`](https://nodejs.org/api/buffer.html) API predates the introduction of `ArrayBuffer` into the JavaScript language. Bun implements both. Use the static `Buffer.from()` method to create a `Buffer` from an `ArrayBuffer`.

```
const arrBuffer = new ArrayBuffer(64);
const nodeBuffer = Buffer.from(arrBuffer);
```

* * *

To create a `Buffer` that only views a portion of the underlying buffer, pass the offset and length to the constructor.

```
const arrBuffer = new ArrayBuffer(64);
const nodeBuffer = Buffer.from(arrBuffer, 0, 16); // view first 16 bytes
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/arraybuffer-to-buffer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/arraybuffer-to-buffer>)

[

Convert an ArrayBuffer to a string

Previous

](/docs/guides/binary/arraybuffer-to-string)[

Convert an ArrayBuffer to a Blob

Next

](/docs/guides/binary/arraybuffer-to-blob)
