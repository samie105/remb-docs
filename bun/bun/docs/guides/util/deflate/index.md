---
title: "Compress and decompress data with DEFLATE"
source: "https://bun.com/docs/guides/util/deflate"
canonical_url: "https://bun.com/docs/guides/util/deflate"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:44.528Z"
content_hash: "babda58994a1221d61e08a737b113ddde8ddfea756825b185fc53ea47407f0e3"
menu_path: ["Compress and decompress data with DEFLATE"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/util/deep-equals/index.md", "title": "Check if two objects are deeply equal"}
nav_next: {"path": "bun/bun/docs/guides/util/detect-bun/index.md", "title": "Detect when code is executed with Bun"}
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

Use `Bun.deflateSync()` to compress a `Uint8Array` with DEFLATE.

```
const data = Buffer.from("Hello, world!");
const compressed = Bun.deflateSync("Hello, world!");
// => Uint8Array

const decompressed = Bun.inflateSync(compressed);
// => Uint8Array
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/deflate.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/deflate>)

[

Compress and decompress data with gzip

Previous

](/docs/guides/util/gzip)[

Escape an HTML string

Next

](/docs/guides/util/escape-html)
