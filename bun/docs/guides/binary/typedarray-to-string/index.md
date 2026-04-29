---
title: "Convert a Uint8Array to a string"
source: "https://bun.com/docs/guides/binary/typedarray-to-string"
canonical_url: "https://bun.com/docs/guides/binary/typedarray-to-string"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:52.187Z"
content_hash: "a9e952e3746ec62912377c0bc3ff995e841b555d8a338261ad98dc1ca9edf943"
menu_path: ["Convert a Uint8Array to a string"]
section_path: []
nav_prev: {"path": "bun/docs/guides/binary/typedarray-to-readablestream/index.md", "title": "Convert a Uint8Array to a ReadableStream"}
nav_next: {"path": "bun/docs/guides/deployment/aws-lambda/index.md", "title": "Deploy a Bun application on AWS Lambda"}
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

Bun implements the Web-standard [`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder) class for converting from binary data types like `Uint8Array` and strings.

```
const arr = new Uint8Array([104, 101, 108, 108, 111]);
const decoder = new TextDecoder();
const str = decoder.decode(arr);
// => "hello"
```

* * *

See [Docs > API > Binary Data](../../../runtime/binary-data/index.md#conversion) for complete documentation on manipulating binary data with Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/binary/typedarray-to-string.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/binary/typedarray-to-string>)

[

Convert a Blob to a ReadableStream

Previous

](../blob-to-stream/index.md)[

Convert a Uint8Array to an ArrayBuffer

Next

](../typedarray-to-arraybuffer/index.md)
