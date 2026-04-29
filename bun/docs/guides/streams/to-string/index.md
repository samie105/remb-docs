---
title: "Convert a ReadableStream to a string"
source: "https://bun.com/docs/guides/streams/to-string"
canonical_url: "https://bun.com/docs/guides/streams/to-string"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:11.858Z"
content_hash: "935ed258ec77befbe036a580915bf6b8be3574e49905a2a8ca35bda36f4c3603"
menu_path: ["Convert a ReadableStream to a string"]
section_path: []
nav_prev: {"path": "bun/docs/guides/streams/to-json/index.md", "title": "Convert a ReadableStream to JSON"}
nav_next: {"path": "bun/docs/guides/streams/to-typedarray/index.md", "title": "Convert a ReadableStream to a Uint8Array"}
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

Bun provides several convenience functions for reading the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into different formats.

```
const stream = new ReadableStream();
const str = await Bun.readableStreamToText(stream);
```

* * *

See [Docs > API > Utils](../../../runtime/utils/index.md#bun-readablestreamto) for documentation on Bun’s other `ReadableStream` conversion functions.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/to-string.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/to-string>)

[

Convert a DataView to a string

Previous

](../../binary/dataview-to-string/index.md)[

Convert a ReadableStream to JSON

Next

](../to-json/index.md)
