---
title: "Get the file name of the current file"
source: "https://bun.com/docs/guides/util/import-meta-file"
canonical_url: "https://bun.com/docs/guides/util/import-meta-file"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:01.177Z"
content_hash: "d1319ad73551540058d3949a6151270e5b772aa54db7fb1810089bc4a29b3b3f"
menu_path: ["Get the file name of the current file"]
section_path: []
nav_prev: {"path": "bun/docs/guides/util/import-meta-dir/index.md", "title": "Get the directory of the current file"}
nav_next: {"path": "bun/docs/guides/util/import-meta-path/index.md", "title": "Get the absolute path of the current file"}
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

Bun provides a handful of module-specific utilities on the [`import.meta`](/docs/runtime/module-resolution#import-meta) object. Use `import.meta.file` to retrieve the name of the current file.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)/a/b/c.ts

```
import.meta.file; // => "c.ts"
```

* * *

See [Docs > API > import.meta](/docs/runtime/module-resolution#import-meta) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/import-meta-file.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/import-meta-file>)

[

Get the directory of the current file

Previous

](/docs/guides/util/import-meta-dir)[

Get the absolute path of the current file

Next

](/docs/guides/util/import-meta-path)
