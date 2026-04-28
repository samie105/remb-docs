---
title: "mask-repeat"
source: "https://tailwindcss.com/docs/mask-repeat"
canonical_url: "https://tailwindcss.com/docs/mask-repeat"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:24:00.493Z"
content_hash: "cd1f76e75c9abe9dbc3f8ca7f8669774f1edbfbc1fcb4a9b9d9b9460f3623682"
menu_path: ["mask-repeat"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/mask-position/index.md", "title": "mask-position"}
nav_next: {"path": "tailwind/docs/mask-size/index.md", "title": "mask-size"}
---

# mask-repeat

Utilities for controlling the repetition of an element's mask image.

| Class | Styles |
| --- | --- |
| `mask-repeat` | 
`mask-repeat: repeat;`

 |
| `mask-no-repeat` | 

`mask-repeat: no-repeat;`

 |
| `mask-repeat-x` | 

`mask-repeat: repeat-x;`

 |
| `mask-repeat-y` | 

`mask-repeat: repeat-y;`

 |
| `mask-repeat-space` | 

`mask-repeat: space;`

 |
| `mask-repeat-round` | 

`mask-repeat: round;`

 |

Use the `mask-repeat` utility to repeat the mask image both vertically and horizontally:

```
<div class="mask-repeat mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

Use the `mask-repeat-x` utility to only repeat the mask image horizontally:

```
<div class="mask-repeat-x mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)]..."></div>
```

Use the `mask-repeat-y` utility to only repeat the mask image vertically:

```
<div class="mask-repeat-y mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)]..."></div>
```

Use the `mask-repeat-space` utility to repeat the mask image without clipping:

```
<div class="mask-repeat-space mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

Use the `mask-repeat-round` utility to repeat the mask image without clipping, stretching if needed to avoid gaps:

```
<div class="mask-repeat-round mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

Use the `mask-no-repeat` utility to prevent a mask image from repeating:

```
<div class="mask-no-repeat mask-[url(/img/circle.png)] mask-size-[50px_50px] bg-[url(/img/mountains.jpg)] ..."></div>
```

Prefix a `mask-repeat` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-repeat md:mask-repeat-x ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Repeating horizontally](#repeating-horizontally)
    -   [Repeating vertically](#repeating-vertically)
    -   [Preventing clipping](#preventing-clipping)
    -   [Preventing clipping and gaps](#preventing-clipping-and-gaps)
    -   [Disabling repeating](#disabling-repeating)
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
