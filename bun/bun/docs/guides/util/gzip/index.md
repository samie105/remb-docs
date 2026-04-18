---
title: "Compress and decompress data with gzip"
source: "https://bun.com/docs/guides/util/gzip"
canonical_url: "https://bun.com/docs/guides/util/gzip"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:55.587Z"
content_hash: "332a4ce890d8f75f993900205618ab9f5222f848ff261a9f3a614b141baf9ea6"
menu_path: ["Compress and decompress data with gzip"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/util/file-url-to-path/index.md", "title": "Convert a file URL to an absolute path"}
nav_next: {"path": "bun/bun/docs/guides/util/hash-a-password/index.md", "title": "Hash a password"}
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

Use `Bun.gzipSync()` to compress a `Uint8Array` with gzip.

```
const data = Buffer.from("Hello, world!");
const compressed = Bun.gzipSync(data);
// => Uint8Array

const decompressed = Bun.gunzipSync(compressed);
// => Uint8Array
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/gzip.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/gzip>)

[

Encode and decode base64 strings

Previous

](/docs/guides/util/base64)[

Compress and decompress data with DEFLATE

Next

](/docs/guides/util/deflate)

