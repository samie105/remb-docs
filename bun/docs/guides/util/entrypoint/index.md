---
title: "Check if the current file is the entrypoint"
source: "https://bun.com/docs/guides/util/entrypoint"
canonical_url: "https://bun.com/docs/guides/util/entrypoint"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:48.966Z"
content_hash: "81f670d3ac7a61531f79e8eade960860d1bab9748e4becf4a52a39ae597aeaeb"
menu_path: ["Check if the current file is the entrypoint"]
section_path: []
nav_prev: {"path": "../detect-bun/index.md", "title": "Detect when code is executed with Bun"}
nav_next: {"path": "../escape-html/index.md", "title": "Escape an HTML string"}
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

Bun provides a handful of module-specific utilities on the [`import.meta`](/docs/runtime/module-resolution#import-meta) object. Use `import.meta.main` to check if the current file is the entrypoint of the current process.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
if (import.meta.main) {
  // this file is directly executed with `bun run`
} else {
  // this file is being imported by another file
}
```

* * *

See [Docs > API > import.meta](/docs/runtime/module-resolution#import-meta) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/entrypoint.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/entrypoint>)

[

Get the absolute path of the current file

Previous

](/docs/guides/util/import-meta-path)[

Get the absolute path to the current entrypoint

Next

](/docs/guides/util/main)
