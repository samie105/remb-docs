---
title: "background-repeat"
source: "https://tailwindcss.com/docs/background-repeat"
canonical_url: "https://tailwindcss.com/docs/background-repeat"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:17:30.534Z"
content_hash: "183052af4be35d0961c87a843b15fca194277fa0011665c05c0539328a5b3a02"
menu_path: ["background-repeat"]
section_path: []
content_language: "en"
nav_prev: {"path": "../background-position/index.md", "title": "background-position"}
nav_next: {"path": "../background-size/index.md", "title": "background-size"}
---

# background-repeat

Utilities for controlling the repetition of an element's background image.

| Class | Styles |
| --- | --- |
| `bg-repeat` | 
`background-repeat: repeat;`

 |
| `bg-repeat-x` | 

`background-repeat: repeat-x;`

 |
| `bg-repeat-y` | 

`background-repeat: repeat-y;`

 |
| `bg-repeat-space` | 

`background-repeat: space;`

 |
| `bg-repeat-round` | 

`background-repeat: round;`

 |
| `bg-no-repeat` | 

`background-repeat: no-repeat;`

 |

Use the `bg-repeat` utility to repeat the background image both vertically and horizontally:

```
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat ..."></div>
```

Use the `bg-repeat-x` utility to only repeat the background image horizontally:

```
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-x ..."></div>
```

Use the `bg-repeat-y` utility to only repeat the background image vertically:

```
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-y ..."></div>
```

Use the `bg-repeat-space` utility to repeat the background image without clipping:

```
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-space ..."></div>
```

Use the `bg-repeat-round` utility to repeat the background image without clipping, stretching if needed to avoid gaps:

```
<div class="bg-[url(/img/clouds.svg)] bg-center bg-repeat-round ..."></div>
```

Use the `bg-no-repeat` utility to prevent a background image from repeating:

```
<div class="bg-[url(/img/clouds.svg)] bg-center bg-no-repeat ..."></div>
```

Prefix a `background-repeat` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="bg-repeat md:bg-repeat-x ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Repeating horizontally](#repeating-horizontally)
    -   [Repeating vertically](#repeating-vertically)
    -   [Preventing clipping](#preventing-clipping)
    -   [Preventing clipping and gaps](#preventing-clipping-and-gaps)
    -   [Disabling repeating](#disabling-repeating)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
