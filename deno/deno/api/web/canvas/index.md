---
title: "Canvas - Web documentation"
source: "https://docs.deno.com/api/web/canvas"
canonical_url: "https://docs.deno.com/api/web/canvas"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:12:18.597Z"
content_hash: "fde877aaf3f76191628e24cd8a679a0a4d3fe049907ce327337304156837666a"
menu_path: ["Canvas - Web documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/web/cache/index.md", "title": "Cache - Web documentation"}
nav_next: {"path": "deno/deno/api/web/crypto/index.md", "title": "Crypto - Web documentation"}
---

### Functions [#](#Functions)

f

[createImageBitmap](./././~/createImageBitmap "createImageBitmap")

Create a new [`ImageBitmap`](./././~/ImageBitmap) object from a given source.

### Interfaces [#](#Interfaces)

I

v

[ImageBitmap](./././~/ImageBitmap "ImageBitmap")

`ImageBitmap` interface represents a bitmap image which can be drawn to a canvas.

*   [close](./././~/ImageBitmap#method_close_0)
*   [height](./././~/ImageBitmap#property_height)
*   [prototype](./././~/ImageBitmap#property_prototype)
*   [width](./././~/ImageBitmap#property_width)

I

[ImageBitmapOptions](./././~/ImageBitmapOptions "ImageBitmapOptions")

The options of [`createImageBitmap`](./././~/createImageBitmap).

*   [colorSpaceConversion](./././~/ImageBitmapOptions#property_colorspaceconversion)
*   [imageOrientation](./././~/ImageBitmapOptions#property_imageorientation)
*   [premultiplyAlpha](./././~/ImageBitmapOptions#property_premultiplyalpha)
*   [resizeHeight](./././~/ImageBitmapOptions#property_resizeheight)
*   [resizeQuality](./././~/ImageBitmapOptions#property_resizequality)
*   [resizeWidth](./././~/ImageBitmapOptions#property_resizewidth)

### Type Aliases [#](<#Type Aliases>)

T

[ColorSpaceConversion](./././~/ColorSpaceConversion "ColorSpaceConversion")

Specifies whether the image should be decoded using color space conversion. Either none or default (default). The value default indicates that implementation-specific behavior is used.

T

[ImageBitmapSource](./././~/ImageBitmapSource "ImageBitmapSource")

The `ImageBitmapSource` type represents an image data source that can be used to create an `ImageBitmap`.

T

[ImageOrientation](./././~/ImageOrientation "ImageOrientation")

Specifies how the bitmap image should be oriented.

T

[PremultiplyAlpha](./././~/PremultiplyAlpha "PremultiplyAlpha")

Specifies whether the bitmap's color channels should be premultiplied by the alpha channel.

T

[ResizeQuality](./././~/ResizeQuality "ResizeQuality")

Specifies the algorithm to be used for resizing the input to match the output dimensions. One of `pixelated`, `low` (default), `medium`, or `high`.


