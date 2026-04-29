---
title: "Check if a file exists"
source: "https://bun.com/docs/guides/read-file/exists"
canonical_url: "https://bun.com/docs/guides/read-file/exists"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:27.537Z"
content_hash: "90c3a44183680f94f3959d17fb8760918a8832feae5445be6d12b6d8ae52aa94"
menu_path: ["Check if a file exists"]
section_path: []
nav_prev: {"path": "bun/docs/guides/read-file/buffer/index.md", "title": "Read a file to a Buffer"}
nav_next: {"path": "bun/docs/guides/read-file/json/index.md", "title": "Read a JSON file"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](../../../index.md)[Package Manager

](../../../pm/cli/install/index.md)[Bundler

](../../../bundler/index.md)[Test Runner

](../../../test/index.md)[Guides

](../../index.md)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](../../../feedback/index.md)

The `Bun.file()` function accepts a path and returns a `BunFile` instance. Use the `.exists()` method to check if a file exists at the given path.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
const path = "/path/to/package.json";
const file = Bun.file(path);

await file.exists(); // boolean;
```

* * *

Refer to [API > File I/O](../../../runtime/file-io/index.md) for more information on working with `BunFile`.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/read-file/exists.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/read-file/exists>)

[

Get the MIME type of a file

Previous

](../mime/index.md)[

Watch a directory for changes

Next

](../watch/index.md)
