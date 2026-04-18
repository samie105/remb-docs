---
title: "mask-position"
source: "https://tailwindcss.com/docs/mask-position"
canonical_url: "https://tailwindcss.com/docs/mask-position"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:56.600Z"
content_hash: "1866ca4562be266bd0eca5b6875d88ffcf669e28379c849b2435a0641bfb254d"
menu_path: ["mask-position"]
section_path: []
---
Utilities for controlling the position of an element's mask image.

Class

Styles

`mask-top-left`

`mask-position: top left;`

`mask-top`

`mask-position: top;`

`mask-top-right`

`mask-position: top right;`

`mask-left`

`mask-position: left;`

`mask-center`

`mask-position: center;`

`mask-right`

`mask-position: right;`

`mask-bottom-left`

`mask-position: bottom left;`

`mask-bottom`

`mask-position: bottom;`

`mask-bottom-right`

`mask-position: bottom right;`

`mask-position-(<custom-property>)`

`mask-position: var(<custom-property>);`

`mask-position-[<value>]`

`mask-position: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `mask-center`, `mask-right`, and `mask-left-top` to control the position of an element's mask image:

mask-top-left

mask-top

mask-top-right

mask-left

mask-center

mask-right

mask-bottom-left

mask-bottom

mask-bottom-right

```
<div class="mask-top-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-top mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-top-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-center mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom-left mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div><div class="mask-bottom-right mask-[url(/img/circle.png)] mask-size-[50%] bg-[url(/img/mountains.jpg)] ..."></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `mask-position-[<value>]` syntax to set the mask position based on a completely custom value:

```
<div class="mask-position-[center_top_1rem] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `mask-position-(<custom-property>)` syntax:

```
<div class="mask-position-(--my-mask-position) ...">  <!-- ... --></div>
```

This is just a shorthand for `mask-position-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `mask-position` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-center md:mask-top ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).
