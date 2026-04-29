---
title: "backdrop-filter: opacity()"
source: "https://tailwindcss.com/docs/backdrop-filter-opacity"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-opacity"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:29:46.399Z"
content_hash: "ab44847ba4cf149025fb787de3e816d8f7eb1bc675b65c145648377a368abf83"
menu_path: ["backdrop-filter: opacity()"]
section_path: []
content_language: "en"
nav_prev: {"path": "../backdrop-filter-invert/index.md", "title": "backdrop-filter: invert()"}
nav_next: {"path": "../backdrop-filter-saturate/index.md", "title": "backdrop-filter: saturate()"}
---

# backdrop-filter: opacity()

Utilities for applying backdrop opacity filters to an element.

| Class | Styles |
| --- | --- |
| `backdrop-opacity-<number>` | 
`backdrop-filter: opacity(<number>%);`

 |
| `backdrop-opacity-(<custom-property>)` | 

`backdrop-filter: opacity(var(<custom-property>));`

 |
| `backdrop-opacity-[<value>]` | 

`backdrop-filter: opacity(<value>);`

 |

Use utilities like `backdrop-opacity-50` and `backdrop-opacity-75` to control the opacity of all the backdrop filters applied to an element:

backdrop-opacity-10

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-opacity-60

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-opacity-95

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert backdrop-opacity-10 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert backdrop-opacity-60 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert backdrop-opacity-95 ..."></div></div>
```

Use the `backdrop-opacity-[<value>]` syntax to set the backdrop filter opacity based on a completely custom value:

```
<div class="backdrop-opacity-[.15] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-opacity-(<custom-property>)` syntax:

```
<div class="backdrop-opacity-(--my-backdrop-filter-opacity) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-opacity-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `backdrop-filter: opacity()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-opacity-100 md:backdrop-opacity-60 ...">  <!-- ... --></div>
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
