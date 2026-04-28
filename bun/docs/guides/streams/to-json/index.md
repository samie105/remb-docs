---
title: "Convert a ReadableStream to JSON"
source: "https://bun.com/docs/guides/streams/to-json"
canonical_url: "https://bun.com/docs/guides/streams/to-json"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:14.737Z"
content_hash: "63b20e8e5bea169edfd2e9174f8968fd4b459297989d2ef3b14cc95652b0dbfa"
menu_path: ["Convert a ReadableStream to JSON"]
section_path: []
nav_prev: {"path": "bun/docs/guides/streams/to-buffer/index.md", "title": "Convert a ReadableStream to a Buffer"}
nav_next: {"path": "bun/docs/guides/streams/to-string/index.md", "title": "Convert a ReadableStream to a string"}
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

Bun provides several convenience functions for reading the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into different formats.

```
const stream = new ReadableStream();
const json = await stream.json();
```

* * *

See [Docs > API > Utils](/docs/runtime/utils#bun-readablestreamto) for documentation on Bun’s other `ReadableStream` conversion functions.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/to-json.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/to-json>)

[

Convert a ReadableStream to a string

Previous

](/docs/guides/streams/to-string)[

Convert a ReadableStream to a Blob

Next

](/docs/guides/streams/to-blob)
