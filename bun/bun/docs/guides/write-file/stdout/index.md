---
title: "Write to stdout"
source: "https://bun.com/docs/guides/write-file/stdout"
canonical_url: "https://bun.com/docs/guides/write-file/stdout"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:55.125Z"
content_hash: "44322afa143bd23091c9d1fb4190df0a0a14dced3848a9abddd2d6905c5b47c2"
menu_path: ["Write to stdout"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/write-file/response/index.md", "title": "Write a Response to a file"}
nav_next: {"path": "bun/bun/docs/guides/write-file/stream/index.md", "title": "Write a ReadableStream to a file"}
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

The `console.log` function writes to `stdout`. It will automatically append a line break at the end of the printed data.

```
console.log("Lorem ipsum");
```

* * *

For more advanced use cases, Bun exposes `stdout` as a `BunFile` via the `Bun.stdout` property. This can be used as a destination for [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write).

```
await Bun.write(Bun.stdout, "Lorem ipsum");
```

* * *

See [Docs > API > File I/O](/docs/runtime/file-io#writing-files-bun-write) for complete documentation of `Bun.write()`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/write-file/stdout.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/write-file/stdout>)

[

Write a ReadableStream to a file

Previous

](/docs/guides/write-file/stream)[

Write a file to stdout

Next

](/docs/guides/write-file/cat)

