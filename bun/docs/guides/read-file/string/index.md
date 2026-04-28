---
title: "Read a file as a string"
source: "https://bun.com/docs/guides/read-file/string"
canonical_url: "https://bun.com/docs/guides/read-file/string"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:48.527Z"
content_hash: "de874ab71b330d441cbe98bad0ea2eaecd91b4580ae4290f8c1c481597bf6304"
menu_path: ["Read a file as a string"]
section_path: []
nav_prev: {"path": "bun/docs/guides/read-file/stream/index.md", "title": "Read a file as a ReadableStream"}
nav_next: {"path": "bun/docs/guides/read-file/uint8array/index.md", "title": "Read a file to a Uint8Array"}
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

The `Bun.file()` function accepts a path and returns a `BunFile` instance. The `BunFile` class extends `Blob` and allows you to lazily read the file in a variety of formats. Use `.text()` to read the contents as a string.

```
const path = "/path/to/file.txt";
const file = Bun.file(path);

const text = await file.text();
// string
```

* * *

Any relative paths will be resolved relative to the project root (the nearest directory containing a `package.json` file).

```
const path = "./file.txt";
const file = Bun.file(path);
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/read-file/string.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/read-file/string>)

[

Get the absolute path to the current entrypoint

Previous

](/docs/guides/util/main)[

Read a file to a Buffer

Next

](/docs/guides/read-file/buffer)
