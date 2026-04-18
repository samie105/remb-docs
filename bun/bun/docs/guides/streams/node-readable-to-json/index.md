---
title: "Convert a Node.js Readable to JSON"
source: "https://bun.com/docs/guides/streams/node-readable-to-json"
canonical_url: "https://bun.com/docs/guides/streams/node-readable-to-json"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:42.761Z"
content_hash: "dd84f74c71dda79523bc60a546fb7abe6b3c1c662588821b3b0d00d6d993d680"
menu_path: ["Convert a Node.js Readable to JSON"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/streams/node-readable-to-blob/index.md", "title": "Convert a Node.js Readable to a Blob"}
nav_next: {"path": "bun/bun/docs/guides/streams/node-readable-to-string/index.md", "title": "Convert a Node.js Readable to a string"}
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

To convert a Node.js `Readable` stream to a JSON object in Bun, you can create a new [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object with the stream as the body, then use [`response.json()`](https://developer.mozilla.org/en-US/docs/Web/API/Response/json) to read the stream into a JSON object.

```
import { Readable } from "stream";
const stream = Readable.from([JSON.stringify({ hello: "world" })]);
const json = await new Response(stream).json();
console.log(json); // { hello: "world" }
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/streams/node-readable-to-json.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/streams/node-readable-to-json>)

[

Convert a Node.js Readable to a string

Previous

](/docs/guides/streams/node-readable-to-string)[

Convert a Node.js Readable to a Blob

Next

](/docs/guides/streams/node-readable-to-blob)


