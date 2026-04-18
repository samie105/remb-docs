---
title: "grid-auto-rows"
source: "https://tailwindcss.com/docs/grid-auto-rows"
canonical_url: "https://tailwindcss.com/docs/grid-auto-rows"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:26.591Z"
content_hash: "067d2ee0ac3c7e1963dc551799a4ce64977350a556680c891a66e2cf0e0e7440"
menu_path: ["grid-auto-rows"]
section_path: []
nav_prev: {"path": "tailwind/docs/grid-auto-columns/index.md", "title": "grid-auto-columns"}
nav_next: {"path": "tailwind/docs/gap/index.md", "title": "gap"}
---

# grid-auto-rows

Utilities for controlling the size of implicitly-created grid rows.

Class

Styles

`auto-rows-auto`

`grid-auto-rows: auto;`

`auto-rows-min`

`grid-auto-rows: min-content;`

`auto-rows-max`

`grid-auto-rows: max-content;`

`auto-rows-fr`

`grid-auto-rows: minmax(0, 1fr);`

`auto-rows-(<custom-property>)`

`grid-auto-rows: var(<custom-property>);`

`auto-rows-[<value>]`

`grid-auto-rows: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `auto-rows-min` and `auto-rows-max` to control the size of implicitly-created grid rows:

```
<div class="grid grid-flow-row auto-rows-max">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `auto-rows-[<value>]` syntax to set the size of implicitly-created grid rows based on a completely custom value:

```
<div class="auto-rows-[minmax(0,2fr)] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `auto-rows-(<custom-property>)` syntax:

```
<div class="auto-rows-(--my-auto-rows) ...">  <!-- ... --></div>
```

This is just a shorthand for `auto-rows-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `grid-auto-rows` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid grid-flow-row auto-rows-max md:auto-rows-min ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)

