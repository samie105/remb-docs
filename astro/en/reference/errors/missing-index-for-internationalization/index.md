---
title: "Index page not found."
source: "https://docs.astro.build/en/reference/errors/missing-index-for-internationalization/"
canonical_url: "https://docs.astro.build/en/reference/errors/missing-index-for-internationalization/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:49.457Z"
content_hash: "bb2e9813da5d0629f9315fa2e92d075d5c2f712a26b9e70672bf2072bc9f85d8"
menu_path: ["Index page not found."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/missing-image-dimension/index.md", "title": "Missing image dimensions"}
nav_next: {"path": "astro/en/reference/errors/missing-locale/index.md", "title": "The provided locale does not exist."}
---

# Index page not found.

> **MissingIndexForInternationalization**: Could not find index page. A root index page is required in order to create a redirect to the index URL of the default locale. (`/DEFAULT_LOCALE`)

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not find the index URL of your website. An index page is required so that Astro can create a redirect from the main index page to the localized index page of the default locale when using [`i18n.routing.prefixDefaultLocale`](../../configuration-reference/index.md#i18nroutingprefixdefaultlocale).

**See Also:**

*   [Internationalization](../../../guides/internationalization/index.md#routing)
*   [`i18n.routing` Configuration Reference](../../configuration-reference/index.md#i18nrouting)

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
