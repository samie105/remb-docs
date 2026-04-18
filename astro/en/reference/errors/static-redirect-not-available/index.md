---
title: "Astro.redirect is not available in static mode."
source: "https://docs.astro.build/en/reference/errors/static-redirect-not-available/"
canonical_url: "https://docs.astro.build/en/reference/errors/static-redirect-not-available/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:41.791Z"
content_hash: "7d94dfed57706b73fac204d848c5eadb5b176f8a028a1b41bfa40a1265fd4b5b"
menu_path: ["Astro.redirect is not available in static mode."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/static-client-address-not-available/index.md", "title": "Astro.clientAddress is not available in prerendered pages."}
nav_next: {"path": "astro/en/reference/errors/unavailable-astro-global/index.md", "title": "Unavailable Astro global in getStaticPaths()"}
---

# Astro.redirect is not available in static mode.

> **StaticRedirectNotAvailable**: Redirects are only available when using `output: 'server'` or `output: 'hybrid'`. Update your Astro config if you need SSR features.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `Astro.redirect` function is only available when [Server-side rendering](/en/guides/on-demand-rendering/) is enabled.

To redirect on a static website, the [meta refresh attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta) can be used. Certain hosts also provide config-based redirects (ex: [Netlify redirects](https://docs.netlify.com/routing/redirects/)).

**See Also:**

*   [Enabling SSR in Your Project](/en/guides/on-demand-rendering/)
*   [Astro.redirect](/en/reference/api-reference/#redirect)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

