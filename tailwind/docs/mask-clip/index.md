---
title: "mask-clip"
source: "https://tailwindcss.com/docs/mask-clip"
canonical_url: "https://tailwindcss.com/docs/mask-clip"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:22:13.096Z"
content_hash: "ad7c3c89ef0dd906373da75882d0279deb891aa44751c7cff22c9d25b3e19bfa"
menu_path: ["mask-clip"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/background-blend-mode/index.md", "title": "background-blend-mode"}
nav_next: {"path": "tailwind/docs/mask-composite/index.md", "title": "mask-composite"}
---

# mask-clip

Utilities for controlling the bounding box of an element's mask.

| Class | Styles |
| --- | --- |
| `mask-clip-border` | 
`mask-clip: border-box;`

 |
| `mask-clip-padding` | 

`mask-clip: padding-box;`

 |
| `mask-clip-content` | 

`mask-clip: content-box;`

 |
| `mask-clip-fill` | 

`mask-clip: fill-box;`

 |
| `mask-clip-stroke` | 

`mask-clip: stroke-box;`

 |
| `mask-clip-view` | 

`mask-clip: view-box;`

 |
| `mask-no-clip` | 

`mask-clip: no-clip;`

 |

Use utilities like `mask-clip-border`, `mask-clip-padding`, and `mask-clip-content` to control the bounding box of an element's mask:

mask-clip-border

mask-clip-padding

mask-clip-content

```
<div class="mask-clip-border border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-clip-padding border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-clip-content border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

Prefix a `mask-clip` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-clip-border md:mask-clip-padding ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

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
