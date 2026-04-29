---
title: "Astro.glob() used outside of an Astro file."
source: "https://docs.astro.build/en/reference/errors/astro-glob-used-outside/"
canonical_url: "https://docs.astro.build/en/reference/errors/astro-glob-used-outside/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:33.591Z"
content_hash: "87fdd8929691f5b9731244f5d90e7a6203d66a1e80f0337ac5c3896e5d7976e5"
menu_path: ["Astro.glob() used outside of an Astro file."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/astro-glob-no-match/index.md", "title": "Astro.glob() did not match any files."}
nav_next: {"path": "astro/en/reference/errors/astro-response-headers-reassigned/index.md", "title": "Astro.response.headers must not be reassigned."}
---

# Astro.glob() used outside of an Astro file.

> **AstroGlobUsedOutside**: `Astro.glob(GLOB_STR)` can only be used in `.astro` files. `import.meta.glob(GLOB_STR)` can be used instead to achieve a similar result.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.glob()` can only be used in `.astro` files. You can use [`import.meta.glob()`](https://vite.dev/guide/features.html#glob-import) instead to achieve the same result.

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
