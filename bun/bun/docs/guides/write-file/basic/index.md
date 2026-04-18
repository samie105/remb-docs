---
title: "Write a string to a file"
source: "https://bun.com/docs/guides/write-file/basic"
canonical_url: "https://bun.com/docs/guides/write-file/basic"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:38.389Z"
content_hash: "e7c7f62edb8e4c330f866123bd111cd3b6e84f2a9a2dadb09a3ee7dc46d327eb"
menu_path: ["Write a string to a file"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/websocket/simple/index.md", "title": "Build a simple WebSocket server"}
nav_next: {"path": "bun/bun/docs/guides/write-file/append/index.md", "title": "Append content to a file"}
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

This code snippet writes a string to disk at a particular _absolute path_. It uses the fast [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write) API to efficiently write data to disk. The first argument is a _destination_; the second is the _data_ to write.

```
const path = "/path/to/file.txt";
await Bun.write(path, "Lorem ipsum");
```

* * *

Any relative paths will be resolved relative to the project root (the nearest directory containing a `package.json` file).

```
const path = "./file.txt";
await Bun.write(path, "Lorem ipsum");
```

* * *

You can pass a `BunFile` as the destination. `Bun.write()` will write the data to its associated path.

```
const path = Bun.file("./file.txt");
await Bun.write(path, "Lorem ipsum");
```

* * *

`Bun.write()` returns the number of bytes written to disk.

```
const path = "./file.txt";
const bytes = await Bun.write(path, "Lorem ipsum");
// => 11
```

* * *

See [Docs > API > File I/O](/docs/runtime/file-io#writing-files-bun-write) for complete documentation of `Bun.write()`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/write-file/basic.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/write-file/basic>)

[

Read a file as a ReadableStream

Previous

](/docs/guides/read-file/stream)[

Write a Blob to a file

Next

](/docs/guides/write-file/blob)
