---
title: "The path doesn't contain any locale"
source: "https://docs.astro.build/en/reference/errors/i18n-no-locale-found-in-path/"
canonical_url: "https://docs.astro.build/en/reference/errors/i18n-no-locale-found-in-path/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:55.664Z"
content_hash: "cfca4698c52cb78b36fc477cb61e053caec15283a0ed6ab14ab81458dec4525a"
menu_path: ["The path doesn't contain any locale"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/get-static-paths-required/index.md", "title": "getStaticPaths() function required for dynamic routes."}
nav_next: {"path": "astro/en/reference/errors/i18n-not-enabled/index.md", "title": "i18n Not Enabled"}
---

# The path doesn't contain any locale

> **i18nNoLocaleFoundInPath**: You tried to use an i18n utility on a path that doesn’t contain any locale. You can use `pathHasLocale` first to determine if the path has a locale.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An i18n utility tried to use the locale from a URL path that does not contain one. You can prevent this error by using pathHasLocale to check URLs for a locale first before using i18n utilities.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
