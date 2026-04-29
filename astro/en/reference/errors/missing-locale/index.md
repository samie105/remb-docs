---
title: "The provided locale does not exist."
source: "https://docs.astro.build/en/reference/errors/missing-locale/"
canonical_url: "https://docs.astro.build/en/reference/errors/missing-locale/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:49.644Z"
content_hash: "9bfcc4098c82ccb78dde0c73edb68cfc77f1e44452b2eae1896614882e9614a4"
menu_path: ["The provided locale does not exist."]
section_path: []
nav_prev: {"path": "../missing-index-for-internationalization/index.md", "title": "Index page not found."}
nav_next: {"path": "../missing-media-query-directive/index.md", "title": "Missing value for client:media directive."}
---

# The provided locale does not exist.

> **MissingLocale**: The locale/path `LOCALE` does not exist in the configured `i18n.locales`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro can’t find the requested locale. All supported locales must be configured in [i18n.locales](/en/reference/configuration-reference/#i18nlocales) and have corresponding directories within `src/pages/`.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
