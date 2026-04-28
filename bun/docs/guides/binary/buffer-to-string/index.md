---
title: "Convert a Buffer to a string"
source: "https://bun.com/docs/guides/binary/buffer-to-string"
canonical_url: "https://bun.com/docs/guides/binary/buffer-to-string"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:49.585Z"
content_hash: "1683c25cfc25e4eaecc605cd02c9cb7803b4a356376e681bee027cd7745eda8a"
menu_path: ["Convert a Buffer to a string"]
section_path: []
nav_prev: {"path": "bun/docs/guides/binary/buffer-to-readablestream/index.md", "title": "Convert a Buffer to a ReadableStream"}
nav_next: {"path": "bun/docs/guides/binary/buffer-to-typedarray/index.md", "title": "Convert a Buffer to a Uint8Array"}
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

The [`Buffer`](https://nodejs.org/api/buffer.html) class provides a built-in `.toString()` method that converts a `Buffer` to a string.

```
const buf = Buffer.from("hello");
const str = buf.toString();
// => "hello"
```

* * *

You can optionally specify an encoding and byte range.

```
const buf = Buffer.from("hello world!");
const str = buf.toString("utf8", 0, 5);
// => "hello"
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/buffer-to-string.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/buffer-to-string>)

[

Convert an ArrayBuffer to a Uint8Array

Previous

](/docs/guides/binary/arraybuffer-to-typedarray)[

Convert a Buffer to an ArrayBuffer

Next

](/docs/guides/binary/buffer-to-arraybuffer)
