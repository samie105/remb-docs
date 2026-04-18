---
title: "mask-origin"
source: "https://tailwindcss.com/docs/mask-origin"
canonical_url: "https://tailwindcss.com/docs/mask-origin"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:55.302Z"
content_hash: "81f2056ae12a0020f7640e9522fb903511e2b9cd2e0ca52d92e2b5de85132bdf"
menu_path: ["mask-origin"]
section_path: []
nav_prev: {"path": "tailwind/docs/mask-mode/index.md", "title": "mask-mode"}
nav_next: {"path": "tailwind/docs/mask-position/index.md", "title": "mask-position"}
---

# mask-origin

Utilities for controlling how an element's mask image is positioned relative to borders, padding, and content.

Class

Styles

`mask-origin-border`

`mask-origin: border-box;`

`mask-origin-padding`

`mask-origin: padding-box;`

`mask-origin-content`

`mask-origin: content-box;`

`mask-origin-fill`

`mask-origin: fill-box;`

`mask-origin-stroke`

`mask-origin: stroke-box;`

`mask-origin-view`

`mask-origin: view-box;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `mask-origin-border`, `mask-origin-padding`, and `mask-origin-content` to control where an element's mask is rendered:

mask-origin-border

mask-origin-padding

mask-origin-content

```
<div class="mask-origin-border border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-origin-padding border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-origin-content border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Responsive design](#responsive-design)

Prefix a `mask-origin` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-origin-border md:mask-origin-padding ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)

