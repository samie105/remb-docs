---
title: "background-origin"
source: "https://tailwindcss.com/docs/background-origin"
canonical_url: "https://tailwindcss.com/docs/background-origin"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:33.386Z"
content_hash: "eb6ecd542ad8de8f4dbb471c6072a26ec47996c16f50cc43a38a4ed98690b56a"
menu_path: ["background-origin"]
section_path: []
nav_prev: {"path": "tailwind/docs/background-image/index.md", "title": "background-image"}
nav_next: {"path": "tailwind/docs/background-position/index.md", "title": "background-position"}
---

# background-origin

Utilities for controlling how an element's background is positioned relative to borders, padding, and content.

Class

Styles

`bg-origin-border`

`background-origin: border-box;`

`bg-origin-padding`

`background-origin: padding-box;`

`bg-origin-content`

`background-origin: content-box;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `bg-origin-border`, `bg-origin-padding`, and `bg-origin-content` utilities to control where an element's background is rendered:

bg-origin-border

bg-origin-padding

bg-origin-content

```
<div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-border p-3 ..."></div><div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-padding p-3 ..."></div><div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-content p-3 ..."></div>
```

### [Responsive design](#responsive-design)

Prefix a `background-origin` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="bg-origin-border md:bg-origin-padding ...">  <!-- ... --></div>
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

