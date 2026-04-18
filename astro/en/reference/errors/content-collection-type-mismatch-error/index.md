---
title: "Collection contains entries of a different type."
source: "https://docs.astro.build/en/reference/errors/content-collection-type-mismatch-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/content-collection-type-mismatch-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:05.438Z"
content_hash: "3e9a5a9269b0f988d551cd4d5095cf9b179bccd822e7301cc3992c60067cc6b6"
menu_path: ["Collection contains entries of a different type."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/content-collection-missing-loader/index.md", "title": "Content collection is missing a loader definition."}
nav_next: {"path": "astro/en/reference/errors/content-entry-data-error/index.md", "title": "Content entry data does not match schema."}
---

# Collection contains entries of a different type.

> **ContentCollectionTypeMismatchError**: COLLECTION contains EXPECTED\_TYPE entries, but is configured as a ACTUAL\_TYPE collection.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Legacy content collections must contain entries of the type configured. Collections are `type: 'content'` by default. Try adding `type: 'data'` to your collection config for data collections.

**See Also:**

*   [Legacy content collections](/en/guides/upgrade-to/v5/#updating-existing-collections)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

