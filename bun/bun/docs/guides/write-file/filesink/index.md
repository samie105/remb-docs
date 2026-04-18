---
title: "Write a file incrementally"
source: "https://bun.com/docs/guides/write-file/filesink"
canonical_url: "https://bun.com/docs/guides/write-file/filesink"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:50.574Z"
content_hash: "e1b2b25dfad5586259ca10dcd900e11d086e0437ed87fe78206fddd0bbe78cea"
menu_path: ["Write a file incrementally"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/write-file/file-cp/index.md", "title": "Copy a file to another location"}
nav_next: {"path": "bun/bun/docs/guides/write-file/response/index.md", "title": "Write a Response to a file"}
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

Bun provides an API for incrementally writing to a file. This is useful for writing large files, or for writing to a file over a long period of time. Call `.writer()` on a `BunFile` to retrieve a `FileSink` instance. This instance can be used to efficiently buffer data and periodically “flush” it to disk. You can write & flush many times.

```
const file = Bun.file("/path/to/file.txt");
const writer = file.writer();

writer.write("lorem");
writer.write("ipsum");
writer.write("dolor");

writer.flush();

// continue writing & flushing
```

* * *

The `.write()` method can accept strings or binary data.

```
w.write("hello");
w.write(Buffer.from("there"));
w.write(new Uint8Array([0, 255, 128]));
writer.flush();
```

* * *

The `FileSink` will also auto-flush when its internal buffer is full. You can configure the buffer size with the `highWaterMark` option.

```
const file = Bun.file("/path/to/file.txt");
const writer = file.writer({ highWaterMark: 1024 * 1024 }); // 1MB
```

* * *

When you’re done writing to the file, call `.end()` to auto-flush the buffer and close the file.

```
writer.end();
```

* * *

Full documentation: [FileSink](/docs/runtime/file-io#incremental-writing-with-filesink).

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/write-file/filesink.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/write-file/filesink>)

[

Append content to a file

Previous

](/docs/guides/write-file/append)[

Write a ReadableStream to a file

Next

](/docs/guides/write-file/stream)


