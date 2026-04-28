---
title: "mask-origin"
source: "https://tailwindcss.com/docs/mask-origin"
canonical_url: "https://tailwindcss.com/docs/mask-origin"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:23:24.272Z"
content_hash: "dac8040f0668233608a53bd3ea8d8330419b6e9f455155bc5e3c5be1c55d2033"
menu_path: ["mask-origin"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/mask-mode/index.md", "title": "mask-mode"}
nav_next: {"path": "tailwind/docs/mask-position/index.md", "title": "mask-position"}
---

# mask-origin

Utilities for controlling how an element's mask image is positioned relative to borders, padding, and content.

| Class | Styles |
| --- | --- |
| `mask-origin-border` | 
`mask-origin: border-box;`

 |
| `mask-origin-padding` | 

`mask-origin: padding-box;`

 |
| `mask-origin-content` | 

`mask-origin: content-box;`

 |
| `mask-origin-fill` | 

`mask-origin: fill-box;`

 |
| `mask-origin-stroke` | 

`mask-origin: stroke-box;`

 |
| `mask-origin-view` | 

`mask-origin: view-box;`

 |

Use utilities like `mask-origin-border`, `mask-origin-padding`, and `mask-origin-content` to control where an element's mask is rendered:

mask-origin-border

mask-origin-padding

mask-origin-content

```
<div class="mask-origin-border border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-origin-padding border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-origin-content border-3 p-1.5 mask-[url(/img/circle.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

Prefix a `mask-origin` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-origin-border md:mask-origin-padding ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
