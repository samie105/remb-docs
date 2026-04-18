---
title: "Read a JSON file"
source: "https://bun.com/docs/guides/read-file/json"
canonical_url: "https://bun.com/docs/guides/read-file/json"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:35.346Z"
content_hash: "adc51e0ff2fbdd6bd304141a44714027892d9be5b31243f2e0ae85c876a0b7c4"
menu_path: ["Read a JSON file"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/read-file/exists/index.md", "title": "Check if a file exists"}
nav_next: {"path": "bun/bun/docs/guides/read-file/mime/index.md", "title": "Get the MIME type of a file"}
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

The `Bun.file()` function accepts a path and returns a `BunFile` instance. The `BunFile` class extends `Blob` and allows you to lazily read the file in a variety of formats. Use `.json()` to read and parse the contents of a `.json` file as a plain object. The MIME type of the `BunFile` will be set accordingly.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
const path = "/path/to/package.json";
const file = Bun.file(path);

const contents = await file.json();
// { name: "my-package" }

file.type; // => "application/json;charset=utf-8";
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/read-file/json.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/read-file/json>)

[

Read a file to an ArrayBuffer

Previous

](/docs/guides/read-file/arraybuffer)[

Get the MIME type of a file

Next

](/docs/guides/read-file/mime)
