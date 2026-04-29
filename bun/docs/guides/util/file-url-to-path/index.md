---
title: "Convert a file URL to an absolute path"
source: "https://bun.com/docs/guides/util/file-url-to-path"
canonical_url: "https://bun.com/docs/guides/util/file-url-to-path"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:53.503Z"
content_hash: "0c694aa756ffb13d05f3511fd63c7d4a0f14f26f40c227fbf656b1a0cc64a2b8"
menu_path: ["Convert a file URL to an absolute path"]
section_path: []
nav_prev: {"path": "bun/docs/guides/util/escape-html/index.md", "title": "Escape an HTML string"}
nav_next: {"path": "bun/docs/guides/util/gzip/index.md", "title": "Compress and decompress data with gzip"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](../../../index.md)[Package Manager

](../../../pm/cli/install/index.md)[Bundler

](../../../bundler/index.md)[Test Runner

](../../../test/index.md)[Guides

](../../index.md)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](../../../feedback/index.md)

Use `Bun.fileURLToPath()` to convert a `file://` URL to an absolute path.

```
Bun.fileURLToPath("file:///path/to/file.txt");
// => "/path/to/file.txt"
```

* * *

See [Docs > API > Utils](../../../runtime/utils/index.md) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/file-url-to-path.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/file-url-to-path>)

[

Sleep for a fixed number of milliseconds

Previous

](../sleep/index.md)[

Convert an absolute path to a file URL

Next

](../path-to-file-url/index.md)
