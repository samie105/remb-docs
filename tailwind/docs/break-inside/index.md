---
title: "break-inside"
source: "https://tailwindcss.com/docs/break-inside"
canonical_url: "https://tailwindcss.com/docs/break-inside"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:22.725Z"
content_hash: "6a7fab08134c0e5ecf5335c387a0c9dfae1baad2f45928e657ae490be02b40f3"
menu_path: ["break-inside"]
section_path: []
nav_prev: {"path": "tailwind/docs/break-before/index.md", "title": "break-before"}
nav_next: {"path": "tailwind/docs/box-decoration-break/index.md", "title": "box-decoration-break"}
---

# break-inside

Utilities for controlling how a column or page should break within an element.

Class

Styles

`break-inside-auto`

`break-inside: auto;`

`break-inside-avoid`

`break-inside: avoid;`

`break-inside-avoid-page`

`break-inside: avoid-page;`

`break-inside-avoid-column`

`break-inside: avoid-column;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `break-inside-column` and `break-inside-avoid-page` to control how a column or page break should behave within an element:

```
<div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-inside-avoid-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>
```

### [Responsive design](#responsive-design)

Prefix a `break-inside` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="break-inside-avoid-column md:break-inside-auto ...">  <!-- ... --></div>
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


