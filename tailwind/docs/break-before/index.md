---
title: "break-before"
source: "https://tailwindcss.com/docs/break-before"
canonical_url: "https://tailwindcss.com/docs/break-before"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:34.158Z"
content_hash: "00c49062058fa7f380b2ca0700cc12cf51d5df63c58c1cde4695c32f90bf901a"
menu_path: ["break-before"]
section_path: []
nav_prev: {"path": "tailwind/docs/break-after/index.md", "title": "break-after"}
nav_next: {"path": "tailwind/docs/break-inside/index.md", "title": "break-inside"}
---

# break-before

Utilities for controlling how a column or page should break before an element.

Class

Styles

`break-before-auto`

`break-before: auto;`

`break-before-avoid`

`break-before: avoid;`

`break-before-all`

`break-before: all;`

`break-before-avoid-page`

`break-before: avoid-page;`

`break-before-page`

`break-before: page;`

`break-before-left`

`break-before: left;`

`break-before-right`

`break-before: right;`

`break-before-column`

`break-before: column;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `break-before-column` and `break-before-page` to control how a column or page break should behave before an element:

```
<div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-before-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>
```

### [Responsive design](#responsive-design)

Prefix a `break-before` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="break-before-column md:break-before-auto ...">  <!-- ... --></div>
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
