---
title: "Convert a Node.js Readable to a string"
source: "https://bun.com/docs/guides/streams/node-readable-to-string"
canonical_url: "https://bun.com/docs/guides/streams/node-readable-to-string"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:46.176Z"
content_hash: "d97a5a57f0e307bbc7bda0e5d96417ea0be110ea5f9c7d2ea8385a3aaab8ae15"
menu_path: ["Convert a Node.js Readable to a string"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/streams/node-readable-to-json/index.md", "title": "Convert a Node.js Readable to JSON"}
nav_next: {"path": "bun/bun/docs/guides/streams/node-readable-to-uint8array/index.md", "title": "Convert a Node.js Readable to an Uint8Array"}
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

To convert a Node.js `Readable` stream to a string in Bun, you can create a new [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object with the stream as the body, then use [`response.text()`](https://developer.mozilla.org/en-US/docs/Web/API/Response/text) to read the stream into a string.

```
import { Readable } from "stream";
const stream = Readable.from([Buffer.from("Hello, world!")]);
const text = await new Response(stream).text();
console.log(text); // "Hello, world!"
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/node-readable-to-string.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/node-readable-to-string>)

[

Convert a ReadableStream to an array of chunks

Previous

](/docs/guides/streams/to-array)[

Convert a Node.js Readable to JSON

Next

](/docs/guides/streams/node-readable-to-json)

