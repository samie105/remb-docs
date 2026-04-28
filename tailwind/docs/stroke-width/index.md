---
title: "stroke-width"
source: "https://tailwindcss.com/docs/stroke-width"
canonical_url: "https://tailwindcss.com/docs/stroke-width"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:42:02.595Z"
content_hash: "b0a56097bb0bcc62e4168835f874e1c6902e772c6b0a567234424d79e7fb7544"
menu_path: ["stroke-width"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/stroke/index.md", "title": "stroke"}
nav_next: {"path": "tailwind/docs/forced-color-adjust/index.md", "title": "forced-color-adjust"}
---

# stroke-width

Utilities for styling the stroke width of SVG elements.

| Class | Styles |
| --- | --- |
| `stroke-<number>` | 
`stroke-width: <number>;`

 |
| `stroke-(length:<custom-property>)` | 

`stroke-width: var(<custom-property>);`

 |
| `stroke-[<value>]` | 

`stroke-width: <value>;`

 |

Use `stroke-<number>` utilities like `stroke-1` and `stroke-2` to set the stroke width of an SVG:

```
<svg class="stroke-1 ..."></svg><svg class="stroke-2 ..."></svg>
```

This can be useful for styling icon sets like [Heroicons](https://heroicons.com).

Use the `stroke-[<value>]` syntax to set the stroke width based on a completely custom value:

```
<div class="stroke-[1.5] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `stroke-(length:<custom-property>)` syntax:

```
<div class="stroke-(length:--my-stroke-width) ...">  <!-- ... --></div>
```

This is just a shorthand for `stroke-[length:var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `stroke-width` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="stroke-1 md:stroke-2 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
