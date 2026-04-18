---
title: "Convert a Buffer to a Uint8Array"
source: "https://bun.com/docs/guides/binary/buffer-to-typedarray"
canonical_url: "https://bun.com/docs/guides/binary/buffer-to-typedarray"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:55.416Z"
content_hash: "7d7f50431b8f50d894be8ee0c9631957c9dda6669ba35aa1c29f227a533650d8"
menu_path: ["Convert a Buffer to a Uint8Array"]
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

The Node.js [`Buffer`](https://nodejs.org/api/buffer.html) class extends [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array), so no conversion is needed. All properties and methods on `Uint8Array` are available on `Buffer`.

```
const buf = Buffer.alloc(64);
buf instanceof Uint8Array; // => true
```

* * *

See [Docs > API > Binary Data](/docs/runtime/binary-data#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/buffer-to-typedarray.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/buffer-to-typedarray>)

[

Convert a Buffer to a blob

Previous

](/docs/guides/binary/buffer-to-blob)[

Convert a Buffer to a ReadableStream

Next

](/docs/guides/binary/buffer-to-readablestream)
