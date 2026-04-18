---
title: "Image missing required \"alt\" property."
source: "https://docs.astro.build/en/reference/errors/image-missing-alt/"
canonical_url: "https://docs.astro.build/en/reference/errors/image-missing-alt/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:00.909Z"
content_hash: "19cd7214ca9444b943053b1b50bcabb147e40cdd5beab844ab24202e9a66a11d"
menu_path: ["Image missing required \"alt\" property."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/image-not-found/index.md", "title": "Image not found."}
nav_next: {"path": "astro/en/reference/errors/incompatible-descriptor-options/index.md", "title": "Cannot set both densities and widths"}
---

# Image missing required "alt" property.

> **ImageMissingAlt**: Image missing “alt” property. “alt” text is required to describe important images on the page.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `alt` property allows you to provide descriptive alt text to users of screen readers and other assistive technologies. In order to ensure your images are accessible, the `Image` component requires that an `alt` be specified.

If the image is merely decorative (i.e. doesn’t contribute to the understanding of the page), set `alt=""` so that screen readers know to ignore the image.

**See Also:**

*   [Images](/en/guides/images/)
*   [Image component](/en/reference/modules/astro-assets/#image-)
*    [Image component#alt](/en/reference/modules/astro-assets/#alt-required)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
