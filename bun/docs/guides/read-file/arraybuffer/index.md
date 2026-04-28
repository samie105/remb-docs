---
title: "Read a file to an ArrayBuffer"
source: "https://bun.com/docs/guides/read-file/arraybuffer"
canonical_url: "https://bun.com/docs/guides/read-file/arraybuffer"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:19.541Z"
content_hash: "16c247e5edd2f12544d674372d93d228497d32d380b2a318f8dc52cffaee0c85"
menu_path: ["Read a file to an ArrayBuffer"]
section_path: []
nav_prev: {"path": "bun/docs/guides/process/stdin/index.md", "title": "Read from stdin"}
nav_next: {"path": "bun/docs/guides/read-file/buffer/index.md", "title": "Read a file to a Buffer"}
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

The `Bun.file()` function accepts a path and returns a `BunFile` instance. The `BunFile` class extends `Blob` and allows you to lazily read the file in a variety of formats. Use `.arrayBuffer()` to read the file as an `ArrayBuffer`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
const path = "/path/to/package.json";
const file = Bun.file(path);

const buffer = await file.arrayBuffer();
```

* * *

The binary content in the `ArrayBuffer` can then be read as a typed array, such as `Int8Array`. For `Uint8Array`, use [`.bytes()`](/docs/guides/read-file/uint8array).

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
const buffer = await file.arrayBuffer();
const bytes = new Int8Array(buffer);

bytes[0];
bytes.length;
```

* * *

Refer to the [Typed arrays](/docs/runtime/binary-data#typedarray) docs for more information on working with typed arrays in Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/read-file/arraybuffer.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/read-file/arraybuffer>)

[

Read a file to a Uint8Array

Previous

](/docs/guides/read-file/uint8array)[

Read a JSON file

Next

](/docs/guides/read-file/json)
