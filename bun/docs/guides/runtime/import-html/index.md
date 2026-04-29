---
title: "Import a HTML file as text"
source: "https://bun.com/docs/guides/runtime/import-html"
canonical_url: "https://bun.com/docs/guides/runtime/import-html"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:39.951Z"
content_hash: "426b52a7ca4b9dd9f4c400ceda2f324543c9568c16d6b859c9a4c5aca3622308"
menu_path: ["Import a HTML file as text"]
section_path: []
nav_prev: {"path": "../heap-snapshot/index.md", "title": "Inspect memory usage using V8 heap snapshots"}
nav_next: {"path": "../import-json/index.md", "title": "Import a JSON file"}
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

To import a `.html` file in Bun as a text file, use the `type: "text"` attribute in the import statement.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)file.ts

```
import html from "./file.html" with { type: "text" };

console.log(html); // <!DOCTYPE html><html><head>...
```

This can also be used with hot module reloading and/or watch mode to force Bun to reload whenever the `./file.html` file changes.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/import-html.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/import-html>)

[

Import a JSON5 file

Previous

](/docs/guides/runtime/import-json5)[

Get the directory of the current file

Next

](/docs/guides/util/import-meta-dir)
