---
title: "Expected image options, not an ESM-imported image."
source: "https://docs.astro.build/en/reference/errors/expected-not-esmimage/"
canonical_url: "https://docs.astro.build/en/reference/errors/expected-not-esmimage/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:35.356Z"
content_hash: "7b57d55e882d1fb46e31c46c637f153053fec0fcbe680e90f0dc131303f165d3"
menu_path: ["Expected image options, not an ESM-imported image."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/expected-image/index.md", "title": "Expected src to be an image."}
nav_next: {"path": "astro/en/reference/errors/failed-to-fetch-remote-image-dimensions/index.md", "title": "Failed to retrieve remote image dimensions"}
---

# Expected image options, not an ESM-imported image.

> **ExpectedNotESMImage**: An ESM-imported image cannot be passed directly to `getImage()`. Instead, pass an object with the image in the `src` property.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An ESM-imported image cannot be passed directly to `getImage()`. Instead, pass an object with the image in the `src` property.

```
import { getImage } from "astro:assets";import myImage from "../assets/my_image.png"; const optimizedImage = await getImage( myImage ); const optimizedImage = await getImage({ src: myImage });
```

**See Also:**

*   [Images](/en/guides/images/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
