---
title: "Expected src to be an image."
source: "https://docs.astro.build/en/reference/errors/expected-image/"
canonical_url: "https://docs.astro.build/en/reference/errors/expected-image/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:34.205Z"
content_hash: "bb345f4aee3e75ba56777a4ce596b85eb08a66568fc15aac576baea9e99e857b"
menu_path: ["Expected src to be an image."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/env-unsupported-get-secret/index.md", "title": "Unsupported astro:env getSecret"}
nav_next: {"path": "astro/en/reference/errors/failed-to-fetch-remote-image-dimensions/index.md", "title": "Failed to retrieve remote image dimensions"}
---

# Expected src to be an image.

> **ExpectedImage**: Expected `src` property for `getImage` or `<Image />` to be either an ESM imported image or a string with the path of a remote image. Received `SRC` (type: `TYPEOF_OPTIONS`).  
>   
> Full serialized options received: `FULL_OPTIONS`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An image’s `src` property is not valid. The Image component requires the `src` attribute to be either an image that has been ESM imported or a string. This is also true for the first parameter of `getImage()`.

```
---import { Image } from "astro:assets";import myImage from "../assets/my_image.png";---
<Image src={myImage} alt="..." /><Image src="https://example.com/logo.png" width={300} height={300} alt="..." />
```

In most cases, this error happens when the value passed to `src` is undefined.

**See Also:**

*   [Images](/en/guides/images/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


