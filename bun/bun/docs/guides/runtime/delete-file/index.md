---
title: "Delete files"
source: "https://bun.com/docs/guides/runtime/delete-file"
canonical_url: "https://bun.com/docs/guides/runtime/delete-file"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:31.275Z"
content_hash: "8d0998f3cd8775fb38f5fc06544662d0844966edcced9d642a686d560ec86132"
menu_path: ["Delete files"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/runtime/delete-directory/index.md", "title": "Delete directories"}
nav_next: {"path": "bun/bun/docs/guides/runtime/heap-snapshot/index.md", "title": "Inspect memory usage using V8 heap snapshots"}
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

To delete a file, use `Bun.file(path).delete()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)delete-file.ts

```
// Delete a file
const file = Bun.file("path/to/file.txt");
await file.delete();

// Now the file doesn't exist
const exists = await file.exists();
// => false
```

* * *

See [Docs > API > FileSystem](/docs/runtime/file-io) for more filesystem operations.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/delete-file.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/delete-file>)

[

Delete a file

Previous

](/docs/guides/write-file/unlink)[

Delete directories

Next

](/docs/guides/runtime/delete-directory)


