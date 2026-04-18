---
title: "Get the MIME type of a file"
source: "https://bun.com/docs/guides/read-file/mime"
canonical_url: "https://bun.com/docs/guides/read-file/mime"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:42.861Z"
content_hash: "91fe4a1c576fc74bac45ae1de90dfa6cd247308a2fefcc35f0ffd6e56a8145cf"
menu_path: ["Get the MIME type of a file"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/read-file/json/index.md", "title": "Read a JSON file"}
nav_next: {"path": "bun/bun/docs/guides/read-file/stream/index.md", "title": "Read a file as a ReadableStream"}
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

The `Bun.file()` function accepts a path and returns a `BunFile` instance. The `BunFile` class extends `Blob`, so use the `.type` property to read the MIME type.

```
const file = Bun.file("./package.json");
file.type; // application/json

const file = Bun.file("./index.html");
file.type; // text/html

const file = Bun.file("./image.png");
file.type; // image/png
```

* * *

Refer to [API > File I/O](/docs/runtime/file-io) for more information on working with `BunFile`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/read-file/mime.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/read-file/mime>)

[

Read a JSON file

Previous

](/docs/guides/read-file/json)[

Check if a file exists

Next

](/docs/guides/read-file/exists)


