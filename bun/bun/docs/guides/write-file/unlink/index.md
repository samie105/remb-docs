---
title: "Delete a file"
source: "https://bun.com/docs/guides/write-file/unlink"
canonical_url: "https://bun.com/docs/guides/write-file/unlink"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:58.255Z"
content_hash: "6f8b91f4ef74e8177fe634fd112328d55c5494c98ca515dd2d890bd33058fece"
menu_path: ["Delete a file"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/write-file/stream/index.md", "title": "Write a ReadableStream to a file"}
nav_next: {"path": "bun/bun/docs/installation/index.md", "title": "Installation"}
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

The `Bun.file()` function accepts a path and returns a `BunFile` instance. Use the `.delete()` method to delete the file.

```
const path = "/path/to/file.txt";
const file = Bun.file(path);

await file.delete();
```

* * *

See [Docs > API > File I/O](/docs/runtime/file-io#reading-files-bun-file) for complete documentation of `Bun.file()`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/write-file/unlink.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/write-file/unlink>)

[

Copy a file to another location

Previous

](/docs/guides/write-file/file-cp)[

Delete files

Next

](/docs/guides/runtime/delete-file)
