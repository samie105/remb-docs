---
title: "backdrop-filter: sepia()"
source: "https://tailwindcss.com/docs/backdrop-filter-sepia"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-sepia"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:30:21.112Z"
content_hash: "69317c48f2e90e94105205ed3be9a129051b1236988d34a9cbd7b7e30c518938"
menu_path: ["backdrop-filter: sepia()"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/backdrop-filter-saturate/index.md", "title": "backdrop-filter: saturate()"}
nav_next: {"path": "tailwind/docs/border-collapse/index.md", "title": "border-collapse"}
---

# backdrop-filter: sepia()

Utilities for applying backdrop sepia filters to an element.

| Class | Styles |
| --- | --- |
| `backdrop-sepia` | 
`backdrop-filter: sepia(100%);`

 |
| `backdrop-sepia-<number>` | 

`backdrop-filter: sepia(<number>%);`

 |
| `backdrop-sepia-(<custom-property>)` | 

`backdrop-filter: sepia(var(<custom-property>));`

 |
| `backdrop-sepia-[<value>]` | 

`backdrop-filter: sepia(<value>);`

 |

Use utilities like `backdrop-sepia` and `backdrop-sepia-50` to control the sepia effect applied to an element's backdrop:

backdrop-sepia-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-sepia-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-sepia

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-sepia-0 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-sepia-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-sepia ..."></div></div>
```

Use the `backdrop-sepia-[<value>]` syntax to set the backdrop sepia based on a completely custom value:

```
<div class="backdrop-sepia-[.25] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-sepia-(<custom-property>)` syntax:

```
<div class="backdrop-sepia-(--my-backdrop-sepia) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-sepia-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `backdrop-filter: sepia()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-sepia md:backdrop-sepia-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

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
