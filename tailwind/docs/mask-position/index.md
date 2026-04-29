---
title: "mask-position"
source: "https://tailwindcss.com/docs/mask-position"
canonical_url: "https://tailwindcss.com/docs/mask-position"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:23:24.761Z"
content_hash: "7e4209f1e04507448512c7e5e31acda831da7be451a48f5ce79071e66537a8e8"
menu_path: ["mask-position"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/mask-origin/index.md", "title": "mask-origin"}
nav_next: {"path": "tailwind/docs/mask-repeat/index.md", "title": "mask-repeat"}
---

Utilities for controlling the position of an element's mask image.

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

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
