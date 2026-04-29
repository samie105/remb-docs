---
title: "You can't use the current function with the current strategy"
source: "https://docs.astro.build/en/reference/errors/incorrect-strategy-for-i18n/"
canonical_url: "https://docs.astro.build/en/reference/errors/incorrect-strategy-for-i18n/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:06.063Z"
content_hash: "8aaaee1820fb3f619d4de4158d52988549fbd086451a53f4aa19f40a38c05f81"
menu_path: ["You can't use the current function with the current strategy"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/incompatible-descriptor-options/index.md", "title": "Cannot set both densities and widths"}
nav_next: {"path": "astro/en/reference/errors/invalid-component-args/index.md", "title": "Invalid component arguments."}
---

# You can't use the current function with the current strategy

> **IncorrectStrategyForI18n**: The function `FUNCTION_NAME` can only be used when the `i18n.routing.strategy` is set to `"manual"`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Some internationalization functions are only available when Astro’s own i18n routing is disabled by the configuration setting `i18n.routing: "manual"`.

**See Also:**

*   [`i18n` routing](../../../guides/internationalization/index.md#routing)

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
