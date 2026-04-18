---
title: "Content entry data does not match schema."
source: "https://docs.astro.build/en/reference/errors/content-entry-data-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/content-entry-data-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:09.069Z"
content_hash: "173c755d421f0f73ba921beab599a48993f2ec6a393eaab8bcff8b1cd8d8c408"
menu_path: ["Content entry data does not match schema."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/content-collection-type-mismatch-error/index.md", "title": "Collection contains entries of a different type."}
nav_next: {"path": "astro/en/reference/errors/content-loader-invalid-data-error/index.md", "title": "Content entry is missing an ID"}
---

# Content entry data does not match schema.

> **Example error message:**  
> **blog** → **post** data does not match collection schema.  
> “title” is required.  
> “date” must be a valid date.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A content entry does not match its collection schema. Make sure that all required fields are present, and that all fields are of the correct type. You can check against the collection schema in your `src/content.config.*` file. See the [Content collections documentation](/en/guides/content-collections/) for more information.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


