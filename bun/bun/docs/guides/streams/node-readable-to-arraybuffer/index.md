---
title: "Convert a Node.js Readable to an ArrayBuffer"
source: "https://bun.com/docs/guides/streams/node-readable-to-arraybuffer"
canonical_url: "https://bun.com/docs/guides/streams/node-readable-to-arraybuffer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:36.285Z"
content_hash: "3d1c9194ee440e606e51c15e9fba82872c98ee5569c1f1f67dcb808f6f907677"
menu_path: ["Convert a Node.js Readable to an ArrayBuffer"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/runtime/web-debugger/index.md", "title": "Debugging Bun with the web debugger"}
nav_next: {"path": "bun/bun/docs/guides/streams/node-readable-to-blob/index.md", "title": "Convert a Node.js Readable to a Blob"}
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

To convert a Node.js `Readable` stream to an `ArrayBuffer` in Bun, you can create a new `Response` object with the stream as the body, then use `arrayBuffer()` to read the stream into an `ArrayBuffer`.

```
import { Readable } from "stream";
const stream = Readable.from(["Hello, ", "world!"]);
const buf = await new Response(stream).arrayBuffer();
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/node-readable-to-arraybuffer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/node-readable-to-arraybuffer>)

[

Convert a Node.js Readable to an Uint8Array

Previous

](/docs/guides/streams/node-readable-to-uint8array)

