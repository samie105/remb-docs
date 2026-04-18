---
title: "Get the directory of the current file"
source: "https://bun.com/docs/guides/util/import-meta-dir"
canonical_url: "https://bun.com/docs/guides/util/import-meta-dir"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:59.452Z"
content_hash: "13ec58feeb9b8ae612555833ed1860790a8286888f8a141b2bf90a888b3b63b2"
menu_path: ["Get the directory of the current file"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/util/hash-a-password/index.md", "title": "Hash a password"}
nav_next: {"path": "bun/bun/docs/guides/util/import-meta-file/index.md", "title": "Get the file name of the current file"}
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

Bun provides a handful of module-specific utilities on the [`import.meta`](/docs/runtime/module-resolution#import-meta) object.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)/a/b/c.ts

```
import.meta.dir; // => "/a/b"
```

* * *

See [Docs > API > import.meta](/docs/runtime/module-resolution#import-meta) for complete documentation.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/import-meta-dir.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/import-meta-dir>)

[

Get the path to an executable bin file

Previous

](/docs/guides/util/which-path-to-executable-bin)[

Get the file name of the current file

Next

](/docs/guides/util/import-meta-file)

