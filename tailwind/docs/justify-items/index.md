---
title: "justify-items"
source: "https://tailwindcss.com/docs/justify-items"
canonical_url: "https://tailwindcss.com/docs/justify-items"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:00:39.900Z"
content_hash: "b57260be32a024aabd33a6e8d0566a9da49fbf2b192550e0990578c34c5ed96e"
menu_path: ["justify-items"]
section_path: []
content_language: "en"
nav_prev: {"path": "../justify-content/index.md", "title": "justify-content"}
nav_next: {"path": "../justify-self/index.md", "title": "justify-self"}
---

# justify-items

Utilities for controlling how grid items are aligned along their inline axis.

| Class | Styles |
| --- | --- |
| `justify-items-start` | 
`justify-items: start;`

 |
| `justify-items-end` | 

`justify-items: end;`

 |
| `justify-items-end-safe` | 

`justify-items: safe end;`

 |
| `justify-items-center` | 

`justify-items: center;`

 |
| `justify-items-center-safe` | 

`justify-items: safe center;`

 |
| `justify-items-stretch` | 

`justify-items: stretch;`

 |
| `justify-items-normal` | 

`justify-items: normal;`

 |

Use the `justify-items-start` utility to justify grid items against the start of their inline axis:

01

02

03

04

05

06

```
<div class="grid justify-items-start ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

Use the `justify-items-end` or `justify-items-end-safe` utilities to justify grid items against the end of their inline axis:

Resize the container to see the alignment behavior

justify-items-end

01

02

03

justify-items-end-safe

01

02

03

justify-items-end

```
<div class="grid grid-flow-col justify-items-end ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

justify-items-end-safe

```
<div class="grid grid-flow-col justify-items-end-safe ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

When there is not enough space available, the `justify-items-end-safe` utility will align items to the start of the container instead of the end.

Use the `justify-items-center` or `justify-items-center-safe` utilities to justify grid items against the end of their inline axis:

Resize the container to see the alignment behavior

justify-items-center

01

02

03

justify-items-center-safe

01

02

03

justify-items-center

```
<div class="grid grid-flow-col justify-items-center ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

justify-items-center-safe

```
<div class="grid grid-flow-col justify-items-center-safe ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

When there is not enough space available, the `justify-items-center-safe` utility will align items to the start of the container instead of the center.

Use the `justify-items-stretch` utility to stretch items along their inline axis:

01

02

03

04

05

06

```
<div class="grid justify-items-stretch ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

Prefix a `justify-items` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid justify-items-start md:justify-items-center ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Start](#start)
    -   [End](#end)
    -   [Center](#center)
    -   [Stretch](#stretch)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
