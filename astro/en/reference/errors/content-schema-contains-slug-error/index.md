---
title: "Content Schema should not contain slug."
source: "https://docs.astro.build/en/reference/errors/content-schema-contains-slug-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/content-schema-contains-slug-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:14.306Z"
content_hash: "fd2d824d5938de5933c46ed4a7eb5e7ad129400916c2f9042e55b0b2939c4f3f"
menu_path: ["Content Schema should not contain slug."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/could-not-transform-image/index.md", "title": "Could not transform image."}
nav_next: {"path": "astro/en/reference/errors/csp-not-enabled/index.md", "title": "CSP feature isn't enabled"}
---

# Content Schema should not contain slug.

> **ContentSchemaContainsSlugError**: A content collection schema should not contain `slug` since it is reserved for slug generation. Remove this from your COLLECTION\_NAME collection schema.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A legacy content collection schema should not contain the `slug` field. This is reserved by Astro for generating entry slugs. Remove `slug` from your schema. You can still use custom slugs in your frontmatter.

**See Also:**

*   [Legacy content collections](/en/guides/upgrade-to/v5/#updating-existing-collections)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

