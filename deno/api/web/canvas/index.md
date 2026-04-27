---
title: "Canvas - Web documentation"
source: "https://docs.deno.com/api/web/canvas"
canonical_url: "https://docs.deno.com/api/web/canvas"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:57:04.579Z"
content_hash: "93a504a48ffcd2b40a520c7ad5bfa51d4bba71bea47a4dad04b9815e1b702112"
menu_path: ["Canvas - Web documentation"]
section_path: []
content_language: "en"
---
f

[createImageBitmap](./././~/createImageBitmap "createImageBitmap")

Create a new [`ImageBitmap`](./././~/ImageBitmap) object from a given source.

I

v

[ImageBitmap](./././~/ImageBitmap "ImageBitmap")

`ImageBitmap` interface represents a bitmap image which can be drawn to a canvas.

-   [close](./././~/ImageBitmap#method_close_0)
-   [height](./././~/ImageBitmap#property_height)
-   [prototype](./././~/ImageBitmap#property_prototype)
-   [width](./././~/ImageBitmap#property_width)

I

[ImageBitmapOptions](./././~/ImageBitmapOptions "ImageBitmapOptions")

The options of [`createImageBitmap`](./././~/createImageBitmap).

-   [colorSpaceConversion](./././~/ImageBitmapOptions#property_colorspaceconversion)
-   [imageOrientation](./././~/ImageBitmapOptions#property_imageorientation)
-   [premultiplyAlpha](./././~/ImageBitmapOptions#property_premultiplyalpha)
-   [resizeHeight](./././~/ImageBitmapOptions#property_resizeheight)
-   [resizeQuality](./././~/ImageBitmapOptions#property_resizequality)
-   [resizeWidth](./././~/ImageBitmapOptions#property_resizewidth)

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
