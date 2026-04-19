---
title: "mask-size"
source: "https://tailwindcss.com/docs/mask-size"
canonical_url: "https://tailwindcss.com/docs/mask-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:33.270Z"
content_hash: "f4b17619cb849cffef2aa0060f102e8687fc98be8eef622114020a7ddc2671d8"
menu_path: ["mask-size"]
section_path: []
nav_prev: {"path": "tailwind/docs/mask-repeat/index.md", "title": "mask-repeat"}
nav_next: {"path": "tailwind/docs/mask-type/index.md", "title": "mask-type"}
---

# mask-size

Utilities for controlling the size of an element's mask image.

Class

Styles

`mask-auto`

`mask-size: auto;`

`mask-cover`

`mask-size: cover;`

`mask-contain`

`mask-size: contain;`

`mask-size-(<custom-property>)`

`mask-size: var(<custom-property>);`

`mask-size-[<value>]`

`mask-size: <value>;`

## [Examples](#examples)

### [Filling the container](#filling-the-container)

Use the `mask-cover` utility to scale the mask image until it fills the mask layer, cropping the image if needed:

```
<div class="mask-cover mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Filling without cropping](#filling-without-cropping)

Use the `mask-contain` utility to scale the mask image to the outer edges without cropping or stretching:

```
<div class="mask-contain mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Using the default size](#using-the-default-size)

Use the `mask-auto` utility to display the mask image at its default size:

```
<div class="mask-auto mask-[url(/img/scribble.png)] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `mask-size-[<value>]` syntax to set the mask image size based on a completely custom value:

```
<div class="mask-size-[auto_100px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `mask-size-(<custom-property>)` syntax:

```
<div class="mask-size-(--my-mask-size) ...">  <!-- ... --></div>
```

This is just a shorthand for `mask-size-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `mask-size` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-auto md:mask-contain ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Filling the container](#filling-the-container)
    *   [Filling without cropping](#filling-without-cropping)
    *   [Using the default size](#using-the-default-size)
    *   [Using a custom value](#using-a-custom-value)
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
