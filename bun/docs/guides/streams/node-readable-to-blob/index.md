---
title: "Convert a Node.js Readable to a Blob"
source: "https://bun.com/docs/guides/streams/node-readable-to-blob"
canonical_url: "https://bun.com/docs/guides/streams/node-readable-to-blob"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:40.296Z"
content_hash: "b3cd2bc7ab1fb105ca736a683145bbe6226cc06efc948f0dbbfa49a0e40ac99f"
menu_path: ["Convert a Node.js Readable to a Blob"]
section_path: []
nav_prev: {"path": "bun/docs/guides/streams/node-readable-to-arraybuffer/index.md", "title": "Convert a Node.js Readable to an ArrayBuffer"}
nav_next: {"path": "bun/docs/guides/streams/node-readable-to-json/index.md", "title": "Convert a Node.js Readable to JSON"}
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

To convert a Node.js `Readable` stream to a [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) in Bun, you can create a new [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object with the stream as the body, then use [`response.blob()`](https://developer.mozilla.org/en-US/docs/Web/API/Response/blob) to read the stream into a [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob).

```
import { Readable } from "stream";
const stream = Readable.from(["Hello, ", "world!"]);
const blob = await new Response(stream).blob();
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/node-readable-to-blob.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/node-readable-to-blob>)

[

Convert a Node.js Readable to JSON

Previous

](../node-readable-to-json/index.md)[

Convert a Node.js Readable to an Uint8Array

Next

](../node-readable-to-uint8array/index.md)
