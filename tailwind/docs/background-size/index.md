---
title: "background-size"
source: "https://tailwindcss.com/docs/background-size"
canonical_url: "https://tailwindcss.com/docs/background-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:18:05.034Z"
content_hash: "c87d8eb6eeb3b6b88d73c5ccfa47f25963499b98b949b1cc18cff70783ea679f"
menu_path: ["background-size"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/background-repeat/index.md", "title": "background-repeat"}
nav_next: {"path": "tailwind/docs/border-radius/index.md", "title": "border-radius"}
---

# background-size

Utilities for controlling the background size of an element's background image.

| Class | Styles |
| --- | --- |
| `bg-auto` | 
`background-size: auto;`

 |
| `bg-cover` | 

`background-size: cover;`

 |
| `bg-contain` | 

`background-size: contain;`

 |
| `bg-size-(<custom-property>)` | 

`background-size: var(<custom-property>);`

 |
| `bg-size-[<value>]` | 

`background-size: <value>;`

 |

Use the `bg-cover` utility to scale the background image until it fills the background layer, cropping the image if needed:

```
<div class="bg-[url(/img/mountains.jpg)] bg-cover bg-center"></div>
```

Use the `bg-contain` utility to scale the background image to the outer edges without cropping or stretching:

```
<div class="bg-[url(/img/mountains.jpg)] bg-contain bg-center"></div>
```

Use the `bg-auto` utility to display the background image at its default size:

```
<div class="bg-[url(/img/mountains.jpg)] bg-auto bg-center bg-no-repeat"></div>
```

Use the `bg-size-[<value>]` syntax to set the background size based on a completely custom value:

```
<div class="bg-size-[auto_100px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `bg-size-(<custom-property>)` syntax:

```
<div class="bg-size-(--my-image-size) ...">  <!-- ... --></div>
```

This is just a shorthand for `bg-size-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `background-size` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="bg-auto md:bg-contain ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

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
