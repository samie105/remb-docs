---
title: "Forbidden rewrite to a static route."
source: "https://docs.astro.build/en/reference/errors/forbidden-rewrite/"
canonical_url: "https://docs.astro.build/en/reference/errors/forbidden-rewrite/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:42.543Z"
content_hash: "cb8bf659a731dfa196e55d6ed8464d6dadd3498fdcdbdb1010c4cf7daf30be75"
menu_path: ["Forbidden rewrite to a static route."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/file-parser-not-found/index.md", "title": "File parser not found"}
nav_next: {"path": "astro/en/reference/errors/font-family-not-found/index.md", "title": "Font family not found"}
---

# Forbidden rewrite to a static route.

> **ForbiddenRewrite**: You tried to rewrite the on-demand route ‘FROM’ with the static route ‘TO’, when using the ‘server’ output.  
>   
> The static route ‘TO’ is rendered by the component ‘COMPONENT’, which is marked as prerendered. This is a forbidden operation because during the build, the component ‘COMPONENT’ is compiled to an HTML file, which can’t be retrieved at runtime by Astro.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.rewrite()` can’t be used to rewrite an on-demand route with a static route when using the `"server"` output.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

