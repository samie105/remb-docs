---
title: "backdrop-filter: brightness()"
source: "https://tailwindcss.com/docs/backdrop-filter-brightness"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-brightness"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:28:04.724Z"
content_hash: "eb8b19d14e9bd6558797b3cd7a2a3fd2cb753f7701f696ae5428f31a2673c56b"
menu_path: ["backdrop-filter: brightness()"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/backdrop-filter-blur/index.md", "title": "backdrop-filter: blur()"}
nav_next: {"path": "tailwind/docs/backdrop-filter-contrast/index.md", "title": "backdrop-filter: contrast()"}
---

# backdrop-filter: brightness()

Utilities for applying backdrop brightness filters to an element.

| Class | Styles |
| --- | --- |
| `backdrop-brightness-<number>` | 
`backdrop-filter: brightness(<number>%);`

 |
| `backdrop-brightness-(<custom-property>)` | 

`backdrop-filter: brightness(var(<custom-property>));`

 |
| `backdrop-brightness-[<value>]` | 

`backdrop-filter: brightness(<value>);`

 |

Use utilities like `backdrop-brightness-50` and `backdrop-brightness-100` to control an element's backdrop brightness:

backdrop-brightness-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-brightness-150

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-brightness-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-brightness-150 ..."></div></div>
```

Use the `backdrop-brightness-[<value>]` syntax to set the backdrop brightness based on a completely custom value:

```
<div class="backdrop-brightness-[1.75] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-brightness-(<custom-property>)` syntax:

```
<div class="backdrop-brightness-(--my-backdrop-brightness) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-brightness-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `backdrop-filter: brightness()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-brightness-110 md:backdrop-brightness-150 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
