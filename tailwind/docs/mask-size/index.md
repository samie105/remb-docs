---
title: "mask-size"
source: "https://tailwindcss.com/docs/mask-size"
canonical_url: "https://tailwindcss.com/docs/mask-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:24:00.126Z"
content_hash: "3fad8ccbfb31758efe5a3e3754996fe74c47d255b1ceae16372f4dca4c45bb9f"
menu_path: ["mask-size"]
section_path: []
content_language: "en"
nav_prev: {"path": "../mask-repeat/index.md", "title": "mask-repeat"}
nav_next: {"path": "../mask-type/index.md", "title": "mask-type"}
---

# mask-size

Utilities for controlling the size of an element's mask image.

| Class | Styles |
| --- | --- |
| `mask-auto` | 
`mask-size: auto;`

 |
| `mask-cover` | 

`mask-size: cover;`

 |
| `mask-contain` | 

`mask-size: contain;`

 |
| `mask-size-(<custom-property>)` | 

`mask-size: var(<custom-property>);`

 |
| `mask-size-[<value>]` | 

`mask-size: <value>;`

 |

Use the `mask-cover` utility to scale the mask image until it fills the mask layer, cropping the image if needed:

```
<div class="mask-cover mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

Use the `mask-contain` utility to scale the mask image to the outer edges without cropping or stretching:

```
<div class="mask-contain mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

Use the `mask-auto` utility to display the mask image at its default size:

```
<div class="mask-auto mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

Use the `mask-size-[<value>]` syntax to set the mask image size based on a completely custom value:

```
<div class="mask-size-[auto_100px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `mask-size-(<custom-property>)` syntax:

```
<div class="mask-size-(--my-mask-size) ...">  <!-- ... --></div>
```

This is just a shorthand for `mask-size-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `mask-size` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-auto md:mask-contain ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Filling the container](#filling-the-container)
    -   [Filling without cropping](#filling-without-cropping)
    -   [Using the default size](#using-the-default-size)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
