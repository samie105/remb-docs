---
title: "grid-auto-flow"
source: "https://tailwindcss.com/docs/grid-auto-flow"
canonical_url: "https://tailwindcss.com/docs/grid-auto-flow"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:45.016Z"
content_hash: "c581b02126bca366ab5774a091d5ee955013c32c5dfc3ce8bb84280f5b02d934"
menu_path: ["grid-auto-flow"]
section_path: []
nav_prev: {"path": "tailwind/docs/grid-row/index.md", "title": "grid-row"}
nav_next: {"path": "tailwind/docs/grid-auto-columns/index.md", "title": "grid-auto-columns"}
---

# grid-auto-flow

Utilities for controlling how elements in a grid are auto-placed.

Class

Styles

`grid-flow-row`

`grid-auto-flow: row;`

`grid-flow-col`

`grid-auto-flow: column;`

`grid-flow-dense`

`grid-auto-flow: dense;`

`grid-flow-row-dense`

`grid-auto-flow: row dense;`

`grid-flow-col-dense`

`grid-auto-flow: column dense;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `grid-flow-col` and `grid-flow-row-dense` to control how the auto-placement algorithm works for a grid layout:

01

02

03

04

05

```
<div class="grid grid-flow-row-dense grid-cols-3 grid-rows-3 ...">  <div class="col-span-2">01</div>  <div class="col-span-2">02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

### [Responsive design](#responsive-design)

Prefix a `grid-auto-flow` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid grid-flow-col md:grid-flow-row ...">  <!-- ... --></div>
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

