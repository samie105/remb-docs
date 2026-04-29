---
title: "break-after"
source: "https://tailwindcss.com/docs/break-after"
canonical_url: "https://tailwindcss.com/docs/break-after"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:51:05.930Z"
content_hash: "1964e059911965471d3f12d03764c92da3984b8730ed25081ecd39e90a77f612"
menu_path: ["break-after"]
section_path: []
content_language: "en"
nav_prev: {"path": "../columns/index.md", "title": "columns"}
nav_next: {"path": "../break-before/index.md", "title": "break-before"}
---

# break-after

Utilities for controlling how a column or page should break after an element.

| Class | Styles |
| --- | --- |
| `break-after-auto` | 
`break-after: auto;`

 |
| `break-after-avoid` | 

`break-after: avoid;`

 |
| `break-after-all` | 

`break-after: all;`

 |
| `break-after-avoid-page` | 

`break-after: avoid-page;`

 |
| `break-after-page` | 

`break-after: page;`

 |
| `break-after-left` | 

`break-after: left;`

 |
| `break-after-right` | 

`break-after: right;`

 |
| `break-after-column` | 

`break-after: column;`

 |

Use utilities like `break-after-column` and `break-after-page` to control how a column or page break should behave after an element:

```
<div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-after-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>
```

Prefix a `break-after` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="break-after-column md:break-after-auto ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
