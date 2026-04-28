---
title: "Copy a file to another location"
source: "https://bun.com/docs/guides/write-file/file-cp"
canonical_url: "https://bun.com/docs/guides/write-file/file-cp"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:49.132Z"
content_hash: "c9934f18fad8a707627d9a9c85a46ea850354c150c5203869b96c758a61c95e7"
menu_path: ["Copy a file to another location"]
section_path: []
nav_prev: {"path": "bun/docs/guides/write-file/cat/index.md", "title": "Write a file to stdout"}
nav_next: {"path": "bun/docs/guides/write-file/filesink/index.md", "title": "Write a file incrementally"}
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

This code snippet copies a file to another location on disk. It uses the fast [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write) API to efficiently write data to disk. The first argument is a _destination_, like an absolute path or `BunFile` instance. The second argument is the _data_ to write.

```
const file = Bun.file("/path/to/original.txt");
await Bun.write("/path/to/copy.txt", file);
```

* * *

See [Docs > API > File I/O](/docs/runtime/file-io#writing-files-bun-write) for complete documentation of `Bun.write()`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/write-file/file-cp.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/write-file/file-cp>)

[

Write a file to stdout

Previous

](/docs/guides/write-file/cat)[

Delete a file

Next

](/docs/guides/write-file/unlink)
