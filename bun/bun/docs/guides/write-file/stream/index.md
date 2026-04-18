---
title: "Write a ReadableStream to a file"
source: "https://bun.com/docs/guides/write-file/stream"
canonical_url: "https://bun.com/docs/guides/write-file/stream"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:56.341Z"
content_hash: "c5eef501cd588aa967af4d1672817f139a6a4bb52bbbc7f33544b67ce9a34b4a"
menu_path: ["Write a ReadableStream to a file"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/write-file/stdout/index.md", "title": "Write to stdout"}
nav_next: {"path": "bun/bun/docs/guides/write-file/unlink/index.md", "title": "Delete a file"}
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

To write a `ReadableStream` to disk, first create a `Response` instance from the stream. This `Response` can then be written to disk using [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write).

```
const stream: ReadableStream = ...;
const path = "./file.txt";
const response = new Response(stream);

await Bun.write(path, response);
```

* * *

See [Docs > API > File I/O](/docs/runtime/file-io#writing-files-bun-write) for complete documentation of `Bun.write()`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/write-file/stream.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/write-file/stream>)

[

Write a file incrementally

Previous

](/docs/guides/write-file/filesink)[

Write to stdout

Next

](/docs/guides/write-file/stdout)


