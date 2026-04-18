---
title: "Convert an absolute path to a file URL"
source: "https://bun.com/docs/guides/util/path-to-file-url"
canonical_url: "https://bun.com/docs/guides/util/path-to-file-url"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:13.556Z"
content_hash: "9cb59431101848c67366c40ea61e1044ed07b1861b5098901253f71a54baa260"
menu_path: ["Convert an absolute path to a file URL"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/util/main/index.md", "title": "Get the absolute path to the current entrypoint"}
nav_next: {"path": "bun/bun/docs/guides/util/sleep/index.md", "title": "Sleep for a fixed number of milliseconds"}
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

Use `Bun.pathToFileURL()` to convert an absolute path to a `file://` URL.

```
Bun.pathToFileURL("/path/to/file.txt");
// => "file:///path/to/file.txt"
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/path-to-file-url.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/path-to-file-url>)

[

Convert a file URL to an absolute path

Previous

](/docs/guides/util/file-url-to-path)[

Get the path to an executable bin file

Next

](/docs/guides/util/which-path-to-executable-bin)
