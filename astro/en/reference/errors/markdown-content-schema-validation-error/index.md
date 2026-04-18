---
title: "Content collection frontmatter invalid."
source: "https://docs.astro.build/en/reference/errors/markdown-content-schema-validation-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/markdown-content-schema-validation-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:37.140Z"
content_hash: "f90fb8daafadf855df8e28db35ff27cbcd2e6d595e082cda7317315dad4d3196"
menu_path: ["Content collection frontmatter invalid."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/locals-reassigned/index.md", "title": "locals must not be reassigned."}
nav_next: {"path": "astro/en/reference/errors/markdown-frontmatter-parse-error/index.md", "title": "Failed to parse Markdown frontmatter."}
---

# Content collection frontmatter invalid.

> **Example error message:**  
> Could not parse frontmatter in **blog** → **post.md**  
> “title” is required.  
> “date” must be a valid date.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A Markdown document’s frontmatter in `src/content/` does not match its collection schema. Make sure that all required fields are present, and that all fields are of the correct type. You can check against the collection schema in your `src/content/config.*` file. See the [Content collections documentation](/en/guides/content-collections/) for more information.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


