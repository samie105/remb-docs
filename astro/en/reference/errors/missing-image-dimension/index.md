---
title: "Missing image dimensions"
source: "https://docs.astro.build/en/reference/errors/missing-image-dimension/"
canonical_url: "https://docs.astro.build/en/reference/errors/missing-image-dimension/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:46.798Z"
content_hash: "cc8ed68ef2f898e26ca70d3466b253b7f070870dad82c0395ad1c6853fbff4ef"
menu_path: ["Missing image dimensions"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/middleware-not-aresponse/index.md", "title": "The middleware returned something that is not a Response object."}
nav_next: {"path": "astro/en/reference/errors/missing-index-for-internationalization/index.md", "title": "Index page not found."}
---

# Missing image dimensions

> Missing width and height attributes for `IMAGE_URL`. When using remote images, both dimensions are required in order to avoid cumulative layout shift (CLS).

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

For remote images, `width` and `height` cannot automatically be inferred from the original file. To avoid cumulative layout shift (CLS), either specify these two properties, or set [`inferSize`](../../modules/astro-assets/index.md#infersize) to `true` to fetch a remote image’s original dimensions.

If your image is inside your `src` folder, you probably meant to import it instead. See [the Imports guide for more information](../../../guides/imports/index.md#other-assets).

**See Also:**

*   [Images](../../../guides/images/index.md)
*   [Image component#width-and-height-required](../../modules/astro-assets/index.md#width-and-height-required-for-images-in-public)

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
