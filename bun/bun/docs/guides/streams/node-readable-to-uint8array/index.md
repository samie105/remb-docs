---
title: "Convert a Node.js Readable to an Uint8Array"
source: "https://bun.com/docs/guides/streams/node-readable-to-uint8array"
canonical_url: "https://bun.com/docs/guides/streams/node-readable-to-uint8array"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:49.887Z"
content_hash: "3f13af586174cedb04b168982da671c627c5ba2d6e271c8494e0a2de7f59c9a2"
menu_path: ["Convert a Node.js Readable to an Uint8Array"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/streams/node-readable-to-string/index.md", "title": "Convert a Node.js Readable to a string"}
nav_next: {"path": "bun/bun/docs/guides/streams/to-array/index.md", "title": "Convert a ReadableStream to an array of chunks"}
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

To convert a Node.js `Readable` stream to an `Uint8Array` in Bun, you can create a new `Response` object with the stream as the body, then use `bytes()` to read the stream into an `Uint8Array`.

```
import { Readable } from "stream";
const stream = Readable.from(["Hello, ", "world!"]);
const buf = await new Response(stream).bytes();
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/node-readable-to-uint8array.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/node-readable-to-uint8array>)

[

Convert a Node.js Readable to a Blob

Previous

](/docs/guides/streams/node-readable-to-blob)[

Convert a Node.js Readable to an ArrayBuffer

Next

](/docs/guides/streams/node-readable-to-arraybuffer)

