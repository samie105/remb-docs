---
title: "mask-clip"
source: "https://tailwindcss.com/docs/mask-clip"
canonical_url: "https://tailwindcss.com/docs/mask-clip"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:19.094Z"
content_hash: "923cc7974271e8b7a63f2d0d58526dc8be61bf22c7e5c873e10f2252ffe9e60e"
menu_path: ["mask-clip"]
section_path: []
nav_prev: {"path": "tailwind/docs/background-blend-mode/index.md", "title": "background-blend-mode"}
nav_next: {"path": "tailwind/docs/mask-composite/index.md", "title": "mask-composite"}
---

# mask-clip

Utilities for controlling the bounding box of an element's mask.

Class

Styles

`mask-clip-border`

`mask-clip: border-box;`

`mask-clip-padding`

`mask-clip: padding-box;`

`mask-clip-content`

`mask-clip: content-box;`

`mask-clip-fill`

`mask-clip: fill-box;`

`mask-clip-stroke`

`mask-clip: stroke-box;`

`mask-clip-view`

`mask-clip: view-box;`

`mask-no-clip`

`mask-clip: no-clip;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `mask-clip-border`, `mask-clip-padding`, and `mask-clip-content` to control the bounding box of an element's mask:

mask-clip-border

mask-clip-padding

mask-clip-content

```
<div class="mask-clip-border border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-clip-padding border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-clip-content border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Responsive design](#responsive-design)

Prefix a `mask-clip` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-clip-border md:mask-clip-padding ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
