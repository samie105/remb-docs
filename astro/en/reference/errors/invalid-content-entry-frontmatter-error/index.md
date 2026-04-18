---
title: "Content entry frontmatter does not match schema."
source: "https://docs.astro.build/en/reference/errors/invalid-content-entry-frontmatter-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/invalid-content-entry-frontmatter-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:10.430Z"
content_hash: "b9ebb46cbd8abd2a69ea08bac45e47cf23d11098d003a256d74b188810d80600"
menu_path: ["Content entry frontmatter does not match schema."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/invalid-content-entry-data-error/index.md", "title": "Content entry data does not match schema."}
nav_next: {"path": "astro/en/reference/errors/invalid-content-entry-slug-error/index.md", "title": "Invalid content entry slug."}
---

# Content entry frontmatter does not match schema.

> **Example error message:**  
> **blog** → **post.md** frontmatter does not match collection schema.  
> “title” is required.  
> “date” must be a valid date.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A Markdown or MDX entry does not match its collection schema. Make sure that all required fields are present, and that all fields are of the correct type. You can check against the collection schema in your `src/content.config.*` file. See the [Content collections documentation](/en/guides/content-collections/) for more information.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

