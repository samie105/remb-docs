---
title: "Legacy content config file found."
source: "https://docs.astro.build/en/reference/errors/legacy-content-config-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/legacy-content-config-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:28.735Z"
content_hash: "584df7fd2fb1ed8421086763f1a3268a7388424ac0e2d0d800acd73ae6486a96"
menu_path: ["Legacy content config file found."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/invalid-rewrite404/index.md", "title": "You attempted to rewrite a 404 inside a static page, and this isn't allowed."}
nav_next: {"path": "astro/en/reference/errors/live-content-config-error/index.md", "title": "Error in live content config."}
---

# Legacy content config file found.

> **Example error message:**  
> Found legacy content config file in “src/content/config.ts”. Please move this file to “src/content.config.ts” and ensure each collection has a loader defined.  

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A legacy content config file was found. Move the file to `src/content.config.ts` and update any collection definitions if needed. See the [Astro 6 migration guide](/en/guides/upgrade-to/v6/#removed-legacy-content-collections) for more information.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
