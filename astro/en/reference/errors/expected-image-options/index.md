---
title: "Expected image options."
source: "https://docs.astro.build/en/reference/errors/expected-image-options/"
canonical_url: "https://docs.astro.build/en/reference/errors/expected-image-options/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:29.785Z"
content_hash: "0a786a4220e494269ad344d521ebfee742c0f0ccf5be3a2dfd67ae346283f79e"
menu_path: ["Expected image options."]
section_path: []
---
# Expected image options.

> **ExpectedImageOptions**: Expected getImage() parameter to be an object. Received `OPTIONS`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getImage()`’s first parameter should be an object with the different properties to apply to your image.

```
import { getImage } from "astro:assets";import myImage from "../assets/my_image.png";
const optimizedImage = await getImage({src: myImage, width: 300, height: 300});
```

In most cases, this error happens because parameters were passed directly instead of inside an object.

**See Also:**

*   [Images](/en/guides/images/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
