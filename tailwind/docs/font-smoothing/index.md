---
title: "font-smoothing"
source: "https://tailwindcss.com/docs/font-smoothing"
canonical_url: "https://tailwindcss.com/docs/font-smoothing"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:45.992Z"
content_hash: "d02118b64e1b9337eb1dfcf9a85b9884cec7c2ba30d22c96204c46b469953e39"
menu_path: ["font-smoothing"]
section_path: []
nav_prev: {"path": "tailwind/docs/font-size/index.md", "title": "font-size"}
nav_next: {"path": "tailwind/docs/font-style/index.md", "title": "font-style"}
---

# font-smoothing

Utilities for controlling the font smoothing of an element.

Class

Styles

`antialiased`

`-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`

`subpixel-antialiased`

`-webkit-font-smoothing: auto; -moz-osx-font-smoothing: auto;`

## [Examples](#examples)

### [Grayscale antialiasing](#grayscale-antialiasing)

Use the `antialiased` utility to render text using grayscale antialiasing:

The quick brown fox jumps over the lazy dog.

```
<p class="antialiased ...">The quick brown fox ...</p>
```

### [Subpixel antialiasing](#subpixel-antialiasing)

Use the `subpixel-antialiased` utility to render text using subpixel antialiasing:

The quick brown fox jumps over the lazy dog.

```
<p class="subpixel-antialiased ...">The quick brown fox ...</p>
```

### [Responsive design](#responsive-design)

Prefix `-webkit-font-smoothing` and `-moz-osx-font-smoothing` utilities with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="antialiased md:subpixel-antialiased ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Grayscale antialiasing](#grayscale-antialiasing)
    *   [Subpixel antialiasing](#subpixel-antialiasing)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
