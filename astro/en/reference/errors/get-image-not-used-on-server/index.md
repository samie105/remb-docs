---
title: "getImage() must be used on the server."
source: "https://docs.astro.build/en/reference/errors/get-image-not-used-on-server/"
canonical_url: "https://docs.astro.build/en/reference/errors/get-image-not-used-on-server/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:47.547Z"
content_hash: "2f6da97a9556d90a478acde39ba9124d223dac0e13e2efacff3361d67399d9f1"
menu_path: ["getImage() must be used on the server."]
section_path: []
---
# getImage() must be used on the server.

> **GetImageNotUsedOnServer**: `getImage()` should only be used on the server. To use images on the client, render the `src` from `getImage()` during the server render, then pass it to the client for usage.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `getImage()` function is only available on the server. To use images on the client, either render the `src` from `getImage()` during the server render so it can be used in client-side scripts, or use a standard `<img>` tag.

```
---import { getImage } from "astro:assets";import myImage from "../assets/my_image.png";
const optimizedImage = await getImage({ src: myImage, width: 300 });---
<script define:vars={{ imageSrc: optimizedImage.src }}>  // Use imageSrc in client-side code  document.getElementById('myImage').src = imageSrc;</script>
```

**See Also:**

*   [Images](/en/guides/images/)
*   [getImage()](/en/reference/modules/astro-assets/#getimage)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
