---
title: "background-blend-mode"
source: "https://tailwindcss.com/docs/background-blend-mode"
canonical_url: "https://tailwindcss.com/docs/background-blend-mode"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:04:43.603Z"
content_hash: "d0ec42471e770a7b5cbed94926e8711fbbb35128826522c676ba1f173fc48f3e"
menu_path: ["background-blend-mode"]
section_path: []
nav_prev: {"path": "tailwind/docs/mix-blend-mode/index.md", "title": "mix-blend-mode"}
nav_next: {"path": "tailwind/docs/mask-clip/index.md", "title": "mask-clip"}
---

# background-blend-mode

Utilities for controlling how an element's background image should blend with its background color.

Class

Styles

`bg-blend-normal`

`background-blend-mode: normal;`

`bg-blend-multiply`

`background-blend-mode: multiply;`

`bg-blend-screen`

`background-blend-mode: screen;`

`bg-blend-overlay`

`background-blend-mode: overlay;`

`bg-blend-darken`

`background-blend-mode: darken;`

`bg-blend-lighten`

`background-blend-mode: lighten;`

`bg-blend-color-dodge`

`background-blend-mode: color-dodge;`

`bg-blend-color-burn`

`background-blend-mode: color-burn;`

`bg-blend-hard-light`

`background-blend-mode: hard-light;`

`bg-blend-soft-light`

`background-blend-mode: soft-light;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `bg-blend-difference` and `bg-blend-saturation` to control how the background image and color of an element are blended:

bg-blend-multiply

bg-blend-soft-light

bg-blend-overlay

```
<div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-multiply ..."></div><div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-soft-light ..."></div><div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-overlay ..."></div>
```

### [Responsive design](#responsive-design)

Prefix a `background-blend-mode` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-lighten md:bg-blend-darken ...">  <!-- ... --></div>
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
