---
title: "flex-direction"
source: "https://tailwindcss.com/docs/flex-direction"
canonical_url: "https://tailwindcss.com/docs/flex-direction"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:48.245Z"
content_hash: "5066203fc7b0b32925d4b633b50dbc892e28b4a170f5e9bc4e95e3e65d6d5413"
menu_path: ["flex-direction"]
section_path: []
nav_prev: {"path": "tailwind/docs/flex-basis/index.md", "title": "flex-basis"}
nav_next: {"path": "tailwind/docs/flex-wrap/index.md", "title": "flex-wrap"}
---

# flex-direction

Utilities for controlling the direction of flex items.

Class

Styles

`flex-row`

`flex-direction: row;`

`flex-row-reverse`

`flex-direction: row-reverse;`

`flex-col`

`flex-direction: column;`

`flex-col-reverse`

`flex-direction: column-reverse;`

## [Examples](#examples)

### [Row](#row)

Use `flex-row` to position flex items horizontally in the same direction as text:

01

02

03

```
<div class="flex flex-row ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Row reversed](#row-reversed)

Use `flex-row-reverse` to position flex items horizontally in the opposite direction:

01

02

03

```
<div class="flex flex-row-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Column](#column)

Use `flex-col` to position flex items vertically:

01

02

03

```
<div class="flex flex-col ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Column reversed](#column-reversed)

Use `flex-col-reverse` to position flex items vertically in the opposite direction:

01

02

03

```
<div class="flex flex-col-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Responsive design](#responsive-design)

Prefix a `flex-direction` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="flex flex-col md:flex-row ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Row](#row)
    *   [Row reversed](#row-reversed)
    *   [Column](#column)
    *   [Column reversed](#column-reversed)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)


