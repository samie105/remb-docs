---
title: "Local images must be imported."
source: "https://docs.astro.build/en/reference/errors/local-image-used-wrongly/"
canonical_url: "https://docs.astro.build/en/reference/errors/local-image-used-wrongly/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:32.572Z"
content_hash: "284905c11af7042ce020fffae82bc9389470a5fd01e4a36de3cf84ebdd6d93bc"
menu_path: ["Local images must be imported."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/live-content-config-error/index.md", "title": "Error in live content config."}
nav_next: {"path": "astro/en/reference/errors/locals-not-an-object/index.md", "title": "Value assigned to locals is not accepted."}
---

# Local images must be imported.

> **LocalImageUsedWrongly**: `Image`’s and `getImage`’s `src` parameter must be an imported image or an URL, it cannot be a string filepath. Received `IMAGE_FILE_PATH`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

When using the default image services, `Image`’s and `getImage`’s `src` parameter must be either an imported image or an URL, it cannot be a string of a filepath.

For local images from content collections, you can use the [image() schema helper](/en/guides/images/#images-in-content-collections) to resolve the images.

```
---import { Image } from "astro:assets";import myImage from "../my_image.png";---
<!-- GOOD: `src` is the full imported image. --><Image src={myImage} alt="Cool image" />
<!-- GOOD: `src` is a URL. --><Image src="https://example.com/my_image.png" alt="Cool image" />
<!-- BAD: `src` is an image's `src` path instead of the full image object. --><Image src={myImage.src} alt="Cool image" />
<!-- BAD: `src` is a string filepath. --><Image src="../my_image.png" alt="Cool image" />
```

**See Also:**

*   [Images](/en/guides/images/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
