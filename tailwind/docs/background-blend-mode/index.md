---
title: "background-blend-mode"
source: "https://tailwindcss.com/docs/background-blend-mode"
canonical_url: "https://tailwindcss.com/docs/background-blend-mode"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:21:39.678Z"
content_hash: "81ded5fc3983bc8021b205e24a5d03538aacb1fc6b78255cedaa3424e2341ba4"
menu_path: ["background-blend-mode"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/mix-blend-mode/index.md", "title": "mix-blend-mode"}
nav_next: {"path": "tailwind/docs/mask-clip/index.md", "title": "mask-clip"}
---

# background-blend-mode

Utilities for controlling how an element's background image should blend with its background color.

| Class | Styles |
| --- | --- |
| `bg-blend-normal` | 
`background-blend-mode: normal;`

 |
| `bg-blend-multiply` | 

`background-blend-mode: multiply;`

 |
| `bg-blend-screen` | 

`background-blend-mode: screen;`

 |
| `bg-blend-overlay` | 

`background-blend-mode: overlay;`

 |
| `bg-blend-darken` | 

`background-blend-mode: darken;`

 |
| `bg-blend-lighten` | 

`background-blend-mode: lighten;`

 |
| `bg-blend-color-dodge` | 

`background-blend-mode: color-dodge;`

 |
| `bg-blend-color-burn` | 

`background-blend-mode: color-burn;`

 |
| `bg-blend-hard-light` | 

`background-blend-mode: hard-light;`

 |
| `bg-blend-soft-light` | 

`background-blend-mode: soft-light;`

 |

Use utilities like `bg-blend-difference` and `bg-blend-saturation` to control how the background image and color of an element are blended:

bg-blend-multiply

bg-blend-soft-light

bg-blend-overlay

```
<div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-multiply ..."></div><div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-soft-light ..."></div><div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-overlay ..."></div>
```

Prefix a `background-blend-mode` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="bg-blue-500 bg-[url(/img/mountains.jpg)] bg-blend-lighten md:bg-blend-darken ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

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
