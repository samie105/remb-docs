---
title: "Convert a Blob to a ReadableStream"
source: "https://bun.com/docs/guides/binary/blob-to-stream"
canonical_url: "https://bun.com/docs/guides/binary/blob-to-stream"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:48.422Z"
content_hash: "2f55797756fbd9724adde300e040772ed0f0aace1fb81ffc2510a45e62c77fd1"
menu_path: ["Convert a Blob to a ReadableStream"]
section_path: []
nav_prev: {"path": "bun/docs/guides/binary/blob-to-dataview/index.md", "title": "Convert a Blob to a DataView"}
nav_next: {"path": "bun/docs/guides/binary/blob-to-string/index.md", "title": "Convert a Blob to a string"}
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

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides a number of methods for consuming its contents in different formats, including `.stream()`. This returns `Promise<ReadableStream>`.

```
const blob = new Blob(["hello world"]);
const stream = await blob.stream();
```

* * *

See [Docs > API > Binary Data](../../../runtime/binary-data/index.md#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/blob-to-stream.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/blob-to-stream>)

[

Convert a Blob to a DataView

Previous

](../blob-to-dataview/index.md)[

Convert a Uint8Array to a string

Next

](../typedarray-to-string/index.md)
