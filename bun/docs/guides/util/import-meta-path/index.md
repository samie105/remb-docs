---
title: "Get the absolute path of the current file"
source: "https://bun.com/docs/guides/util/import-meta-path"
canonical_url: "https://bun.com/docs/guides/util/import-meta-path"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:04.778Z"
content_hash: "643fb572bfc65968ab1ae76af70505b091b5d2da9ffbbfc737206a62221ee003"
menu_path: ["Get the absolute path of the current file"]
section_path: []
nav_prev: {"path": "../import-meta-file/index.md", "title": "Get the file name of the current file"}
nav_next: {"path": "../javascript-uuid/index.md", "title": "Generate a UUID"}
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

Bun provides a handful of module-specific utilities on the [`import.meta`](/docs/runtime/module-resolution#import-meta) object. Use `import.meta.path` to retrieve the absolute path of the current file.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)/a/b/c.ts

```
import.meta.path; // => "/a/b/c.ts"
```

* * *

See [Docs > API > import.meta](/docs/runtime/module-resolution#import-meta) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/import-meta-path.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/import-meta-path>)

[

Get the file name of the current file

Previous

](/docs/guides/util/import-meta-file)[

Check if the current file is the entrypoint

Next

](/docs/guides/util/entrypoint)
