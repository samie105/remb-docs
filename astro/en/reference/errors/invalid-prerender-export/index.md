---
title: "Invalid prerender export."
source: "https://docs.astro.build/en/reference/errors/invalid-prerender-export/"
canonical_url: "https://docs.astro.build/en/reference/errors/invalid-prerender-export/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:24.089Z"
content_hash: "c08d809bc5e35a36cfbd9d35ec94f7f09aee9052dda2a2b8e534d4db60ca6ba1"
menu_path: ["Invalid prerender export."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/invalid-image-service/index.md", "title": "Error while loading image service."}
nav_next: {"path": "astro/en/reference/errors/invalid-redirect-destination/index.md", "title": "Invalid redirect destination."}
---

# Invalid prerender export.

> **Example error messages:**  
> InvalidPrerenderExport: A `prerender` export has been detected, but its value cannot be statically analyzed.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `prerender` feature only supports a subset of valid JavaScript — be sure to use exactly `export const prerender = true` so that our compiler can detect this directive at build time. Variables, `let`, and `var` declarations are not supported.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
