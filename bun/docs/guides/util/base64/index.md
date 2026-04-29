---
title: "Encode and decode base64 strings"
source: "https://bun.com/docs/guides/util/base64"
canonical_url: "https://bun.com/docs/guides/util/base64"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:38.749Z"
content_hash: "714ec0d8e05c3bd9a934d50514abb0a21fb8bd960ba2fcbbda87f0d001b31d07"
menu_path: ["Encode and decode base64 strings"]
section_path: []
nav_prev: {"path": "../../test/watch-mode/index.md", "title": "Run tests in watch mode with Bun"}
nav_next: {"path": "../deep-equals/index.md", "title": "Check if two objects are deeply equal"}
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

Bun implements the Web-standard [`atob`](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/atob) and [`btoa`](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/btoa) functions for encoding and decoding base64 strings.

```
const data = "hello world";
const encoded = btoa(data); // => "aGVsbG8gd29ybGQ="
const decoded = atob(encoded); // => "hello world"
```

* * *

See [Docs > Web APIs](/docs/runtime/web-apis) for a complete breakdown of the Web APIs implemented in Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/base64.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/base64>)

[

Generate a UUID

Previous

](/docs/guides/util/javascript-uuid)[

Compress and decompress data with gzip

Next

](/docs/guides/util/gzip)
