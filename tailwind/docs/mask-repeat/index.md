---
title: "mask-repeat"
source: "https://tailwindcss.com/docs/mask-repeat"
canonical_url: "https://tailwindcss.com/docs/mask-repeat"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:33.629Z"
content_hash: "5bbf13ea60f4850f8fa65016a53a27432115462cad30fcd8f7085b59112abb3c"
menu_path: ["mask-repeat"]
section_path: []
nav_prev: {"path": "tailwind/docs/mask-position/index.md", "title": "mask-position"}
nav_next: {"path": "tailwind/docs/mask-size/index.md", "title": "mask-size"}
---

# mask-repeat

Utilities for controlling the repetition of an element's mask image.

Class

Styles

`mask-repeat`

`mask-repeat: repeat;`

`mask-no-repeat`

`mask-repeat: no-repeat;`

`mask-repeat-x`

`mask-repeat: repeat-x;`

`mask-repeat-y`

`mask-repeat: repeat-y;`

`mask-repeat-space`

`mask-repeat: space;`

`mask-repeat-round`

`mask-repeat: round;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `mask-repeat` utility to repeat the mask image both vertically and horizontally:

```
<div class="mask-repeat mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Repeating horizontally](#repeating-horizontally)

Use the `mask-repeat-x` utility to only repeat the mask image horizontally:

```
<div class="mask-repeat-x mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)]..."></div>
```

### [Repeating vertically](#repeating-vertically)

Use the `mask-repeat-y` utility to only repeat the mask image vertically:

```
<div class="mask-repeat-y mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)]..."></div>
```

### [Preventing clipping](#preventing-clipping)

Use the `mask-repeat-space` utility to repeat the mask image without clipping:

```
<div class="mask-repeat-space mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Preventing clipping and gaps](#preventing-clipping-and-gaps)

Use the `mask-repeat-round` utility to repeat the mask image without clipping, stretching if needed to avoid gaps:

```
<div class="mask-repeat-round mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Disabling repeating](#disabling-repeating)

Use the `mask-no-repeat` utility to prevent a mask image from repeating:

```
<div class="mask-no-repeat mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Responsive design](#responsive-design)

Prefix a `mask-repeat` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-repeat md:mask-repeat-x ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Repeating horizontally](#repeating-horizontally)
    *   [Repeating vertically](#repeating-vertically)
    *   [Preventing clipping](#preventing-clipping)
    *   [Preventing clipping and gaps](#preventing-clipping-and-gaps)
    *   [Disabling repeating](#disabling-repeating)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)

