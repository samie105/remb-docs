---
title: "Could not find Sharp."
source: "https://docs.astro.build/en/reference/errors/missing-sharp/"
canonical_url: "https://docs.astro.build/en/reference/errors/missing-sharp/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:54.313Z"
content_hash: "85d174896b1f1aa5d3b286b50bc3b9195c5e39bfcfbb15229730a49c67160606"
menu_path: ["Could not find Sharp."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/missing-middleware-for-internationalization/index.md", "title": "Enabled manual internationalization routing without having a middleware."}
nav_next: {"path": "astro/en/reference/errors/mixed-content-data-collection-error/index.md", "title": "Content and data cannot be in same collection."}
---

# Could not find Sharp.

> **MissingSharp**: Could not find Sharp. Please install Sharp (`sharp`) manually into your project or migrate to another image service.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Sharp is the default image service used for `astro:assets`. When using a [strict package manager](https://pnpm.io/pnpm-vs-npm#npms-flat-tree) like pnpm, Sharp must be installed manually into your project in order to use image processing.

If you are not using `astro:assets` for image processing, and do not wish to install Sharp, you can configure the following passthrough image service that does no processing:

```
import { defineConfig, passthroughImageService } from "astro/config";export default defineConfig({ image: {   service: passthroughImageService(), },});
```

**See Also:**

*   [Default Image Service](/en/guides/images/#default-image-service)
*   [Image Services API](/en/reference/image-service-reference/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
