---
title: "Read a file as a ReadableStream"
source: "https://bun.com/docs/guides/read-file/stream"
canonical_url: "https://bun.com/docs/guides/read-file/stream"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:46.068Z"
content_hash: "e827b3b0cf00b57b69e053e5527bb7965391d4bacdb63e6160cb612d6b68acdd"
menu_path: ["Read a file as a ReadableStream"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/read-file/mime/index.md", "title": "Get the MIME type of a file"}
nav_next: {"path": "bun/bun/docs/guides/read-file/string/index.md", "title": "Read a file as a string"}
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

The `Bun.file()` function accepts a path and returns a `BunFile` instance. The `BunFile` class extends `Blob` and allows you to lazily read the file in a variety of formats. Use `.stream()` to consume the file incrementally as a `ReadableStream`.

```
const path = "/path/to/package.json";
const file = Bun.file(path);

const stream = file.stream();
```

* * *

The chunks of the stream can be consumed as an [async iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols) using `for await`.

```
for await (const chunk of stream) {
  chunk; // => Uint8Array
}
```

* * *

Refer to the [Streams](/docs/runtime/streams) documentation for more information on working with streams in Bun.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/read-file/stream.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/read-file/stream>)

[

Watch a directory for changes

Previous

](/docs/guides/read-file/watch)[

Write a string to a file

Next

](/docs/guides/write-file/basic)

