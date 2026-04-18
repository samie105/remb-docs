---
title: "Glob patterns are not supported in the file loader"
source: "https://docs.astro.build/en/reference/errors/file-glob-not-supported/"
canonical_url: "https://docs.astro.build/en/reference/errors/file-glob-not-supported/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:39.343Z"
content_hash: "e07ef4282456b4c881f472754bdfacac0151dc7ad8a6bbb72610e1825babce95"
menu_path: ["Glob patterns are not supported in the file loader"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/failed-to-load-module-ssr/index.md", "title": "Could not import file."}
nav_next: {"path": "astro/en/reference/errors/file-parser-not-found/index.md", "title": "File parser not found"}
---

# Glob patterns are not supported in the file loader

> **FileGlobNotSupported**: Glob patterns are not supported in the `file` loader. Use the `glob` loader instead.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `file` loader must be passed a single local file. Glob patterns are not supported. Use the built-in `glob` loader to create entries from patterns of multiple local files.

**See Also:**

*   [Astro’s built-in `file()` loader](/en/reference/content-loader-reference/#file-loader)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

