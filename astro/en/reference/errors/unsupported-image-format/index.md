---
title: "Unsupported image format"
source: "https://docs.astro.build/en/reference/errors/unsupported-image-format/"
canonical_url: "https://docs.astro.build/en/reference/errors/unsupported-image-format/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:57.852Z"
content_hash: "687ad84f1db44cd4cfa7fecd611eb78d76c3d1d846744e05a5b49bc7a779b7ff"
menu_path: ["Unsupported image format"]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/unsupported-image-conversion/index.md", "title": "Unsupported image conversion"}
nav_next: {"path": "astro/en/tutorial/0-introduction/1/index.md", "title": "About this Tutorial"}
---

# Unsupported image format

> **UnsupportedImageFormat**: Received unsupported format `FORMAT` from `IMAGE_PATH`. Currently only SUPPORTED\_FORMATS.JOIN(’, ’) are supported by our image services.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The built-in image services do not currently support optimizing all image formats.

For unsupported formats such as GIFs, you may be able to use an `img` tag directly:

```
---import rocket from '../assets/images/rocket.gif';---
<img src={rocket.src} width={rocket.width} height={rocket.height} alt="A rocketship in space." />
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


