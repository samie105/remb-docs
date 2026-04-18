---
title: "i18n Not Enabled"
source: "https://docs.astro.build/en/reference/errors/i18n-not-enabled/"
canonical_url: "https://docs.astro.build/en/reference/errors/i18n-not-enabled/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:57.132Z"
content_hash: "b7c14ec1f0408279ea7725e7764b86b87dd6f1d3784c2fcb86b9d7cdc44580f8"
menu_path: ["i18n Not Enabled"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/i18n-no-locale-found-in-path/index.md", "title": "The path doesn't contain any locale"}
nav_next: {"path": "astro/en/reference/errors/image-not-found/index.md", "title": "Image not found."}
---

# i18n Not Enabled

> **i18nNotEnabled**: The `astro:i18n` module cannot be used without enabling i18n in your Astro config.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `astro:i18n` module cannot be used without enabling i18n in your Astro config. To enable i18n, add a default locale and a list of supported locales to your Astro config:

```
import { defineConfig } from 'astro'export default defineConfig({ i18n: {   locales: ['en', 'fr'],   defaultLocale: 'en',  },})
```

For more information on internationalization support in Astro, see our [Internationalization guide](/en/guides/internationalization/).

**See Also:**

*   [Internationalization](/en/guides/internationalization/)
*   [`i18n` Configuration Reference](/en/reference/configuration-reference/#i18n)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


