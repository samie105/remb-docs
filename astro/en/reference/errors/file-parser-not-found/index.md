---
title: "File parser not found"
source: "https://docs.astro.build/en/reference/errors/file-parser-not-found/"
canonical_url: "https://docs.astro.build/en/reference/errors/file-parser-not-found/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:41.917Z"
content_hash: "f211dd554248b5f908ecc6af0d972fe9569f9faa15ae5b2b77bbfaa6202ecde0"
menu_path: ["File parser not found"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/file-glob-not-supported/index.md", "title": "Glob patterns are not supported in the file loader"}
nav_next: {"path": "astro/en/reference/errors/font-family-not-found/index.md", "title": "Font family not found"}
---

# File parser not found

> **FileParserNotFound**: No parser was found for ‘FILE\_NAME’. Pass a parser function (e.g. `parser: csv`) to the `file` loader.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `file` loader can’t determine which parser to use. Please provide a custom parser (e.g. `csv-parse`) to create a collection from your file type.

**See Also:**

*   [Passing a `parser` to the `file` loader](../../content-loader-reference/index.md#parser)

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
