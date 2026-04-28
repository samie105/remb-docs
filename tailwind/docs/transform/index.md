---
title: "transform"
source: "https://tailwindcss.com/docs/transform"
canonical_url: "https://tailwindcss.com/docs/transform"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:35:00.557Z"
content_hash: "fac5aa1f68bd4fa2d9965e138d9a6ec8e1a54c8fb82626d757f952d8c60bc6dd"
menu_path: ["transform"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/skew/index.md", "title": "skew"}
nav_next: {"path": "tailwind/docs/transform-origin/index.md", "title": "transform-origin"}
---

# transform

Utilities for transforming elements.

| Class | Styles |
| --- | --- |
| `transform-(<custom-property>)` | 
`transform: var(<custom-property>);`

 |
| `transform-[<value>]` | 

`transform: <value>;`

 |
| `transform-none` | 

`transform: none;`

 |
| `transform-gpu` | 

`transform: translateZ(0) var(--tw-rotate-x) var(--tw-rotate-y) var(--tw-rotate-z) var(--tw-skew-x) var(--tw-skew-y);`

 |
| `transform-cpu` | 

`transform: var(--tw-rotate-x) var(--tw-rotate-y) var(--tw-rotate-z) var(--tw-skew-x) var(--tw-skew-y);`

 |

If your transition performs better when rendered by the GPU instead of the CPU, you can force hardware acceleration by adding the `transform-gpu` utility:

```
<div class="scale-150 transform-gpu">  <!-- ... --></div>
```

Use the `transform-cpu` utility to force things back to the CPU if you need to undo this conditionally.

Use the `transform-none` utility to remove all of the transforms on an element at once:

```
<div class="skew-y-3 md:transform-none">  <!-- ... --></div>
```

Use the `transform-[<value>]` syntax to set the transform based on a completely custom value:

```
<div class="transform-[matrix(1,2,3,4,5,6)] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `transform-(<custom-property>)` syntax:

```
<div class="transform-(--my-transform) ...">  <!-- ... --></div>
```

This is just a shorthand for `transform-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Hardware acceleration](#hardware-acceleration)
    -   [Removing transforms](#removing-transforms)
    -   [Using a custom value](#using-a-custom-value)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
