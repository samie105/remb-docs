---
title: "place-items"
source: "https://tailwindcss.com/docs/place-items"
canonical_url: "https://tailwindcss.com/docs/place-items"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:02:24.769Z"
content_hash: "c53751d92482b81ba14ea912cabb032e2f993efe9801dff10b6cca5d76f6a5e6"
menu_path: ["place-items"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/place-content/index.md", "title": "place-content"}
nav_next: {"path": "tailwind/docs/place-self/index.md", "title": "place-self"}
---

# place-items

Utilities for controlling how items are justified and aligned at the same time.

| Class | Styles |
| --- | --- |
| `place-items-start` | 
`place-items: start;`

 |
| `place-items-end` | 

`place-items: end;`

 |
| `place-items-end-safe` | 

`place-items: safe end;`

 |
| `place-items-center` | 

`place-items: center;`

 |
| `place-items-center-safe` | 

`place-items: safe center;`

 |
| `place-items-baseline` | 

`place-items: baseline;`

 |
| `place-items-stretch` | 

`place-items: stretch;`

 |

Use `place-items-start` to place grid items on the start of their grid areas on both axes:

01

02

03

04

05

06

```
<div class="grid grid-cols-3 place-items-start gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

Use `place-items-end` to place grid items on the end of their grid areas on both axes:

01

02

03

04

05

06

```
<div class="grid h-56 grid-cols-3 place-items-end gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

Use `place-items-center` to place grid items on the center of their grid areas on both axes:

01

02

03

04

05

06

```
<div class="grid h-56 grid-cols-3 place-items-center gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

Use `place-items-stretch` to stretch items along their grid areas on both axes:

01

02

03

04

05

06

```
<div class="grid h-56 grid-cols-3 place-items-stretch gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

Prefix a `place-items` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid place-items-start md:place-items-center ...">  <!-- ... --></div>
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
