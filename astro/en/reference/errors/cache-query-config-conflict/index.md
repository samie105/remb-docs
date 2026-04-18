---
title: "Conflicting cache query configuration."
source: "https://docs.astro.build/en/reference/errors/cache-query-config-conflict/"
canonical_url: "https://docs.astro.build/en/reference/errors/cache-query-config-conflict/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:41.032Z"
content_hash: "38e3c678b6c974ccf90947daf7484feaf41ebc1cf60937983c47e2f7874574c3"
menu_path: ["Conflicting cache query configuration."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/cache-provider-not-found/index.md", "title": "Cache provider not found."}
nav_next: {"path": "astro/en/reference/errors/cannot-extract-font-type/index.md", "title": "Cannot extract the font type from the given URL."}
---

# Conflicting cache query configuration.

> `query.include` and `query.exclude` cannot be used together.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The memory cache provider’s `query.include` and `query.exclude` options are mutually exclusive. Use `include` to allowlist specific query parameters that affect the cache key, or `exclude` to blocklist parameters. When `include` is set, all other parameters are automatically ignored.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


