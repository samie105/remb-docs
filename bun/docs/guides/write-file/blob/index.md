---
title: "Write a Blob to a file"
source: "https://bun.com/docs/guides/write-file/blob"
canonical_url: "https://bun.com/docs/guides/write-file/blob"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:42.522Z"
content_hash: "a0adef4fc8a3ed1d7ee6f084e505fad4fd3a5e19b2c2f605c9432a194ee5fed0"
menu_path: ["Write a Blob to a file"]
section_path: []
nav_prev: {"path": "bun/docs/guides/write-file/basic/index.md", "title": "Write a string to a file"}
nav_next: {"path": "bun/docs/guides/write-file/cat/index.md", "title": "Write a file to stdout"}
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

This code snippet writes a `Blob` to disk at a particular path. It uses the fast [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write) API to efficiently write data to disk. The first argument is a _destination_, like an absolute path or `BunFile` instance. The second argument is the _data_ to write.

```
const path = "/path/to/file.txt";
await Bun.write(path, "Lorem ipsum");
```

* * *

The `BunFile` class extends `Blob`, so you can pass a `BunFile` directly into `Bun.write()` as well.

```
const path = "./out.txt";
const data = Bun.file("./in.txt");

// write the contents of ./in.txt to ./out.txt
await Bun.write(path, data);
```

* * *

See [Docs > API > File I/O](/docs/runtime/file-io#writing-files-bun-write) for complete documentation of `Bun.write()`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/write-file/blob.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/write-file/blob>)

[

Write a string to a file

Previous

](/docs/guides/write-file/basic)[

Write a Response to a file

Next

](/docs/guides/write-file/response)
