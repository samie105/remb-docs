---
title: "backdrop-filter: invert()"
source: "https://tailwindcss.com/docs/backdrop-filter-invert"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-invert"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:29:13.690Z"
content_hash: "ff4c750bb96d034c651521b1c76bda402eae620abe40227870135efb7ebcbb63"
menu_path: ["backdrop-filter: invert()"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/backdrop-filter-hue-rotate/index.md", "title": "backdrop-filter: hue-rotate()"}
nav_next: {"path": "tailwind/docs/backdrop-filter-opacity/index.md", "title": "backdrop-filter: opacity()"}
---

# backdrop-filter: invert()

Utilities for applying backdrop invert filters to an element.

| Class | Styles |
| --- | --- |
| `backdrop-invert` | 
`backdrop-filter: invert(100%);`

 |
| `backdrop-invert-<number>` | 

`backdrop-filter: invert(<number>%);`

 |
| `backdrop-invert-(<custom-property>)` | 

`backdrop-filter: invert(var(<custom-property>))`

 |
| `backdrop-invert-[<value>]` | 

`backdrop-filter: invert(<value>);`

 |

Use utilities like `backdrop-invert` and `backdrop-invert-65` to control the color inversion of an element's backdrop:

backdrop-invert-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-invert-65

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-invert

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert-0 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert-65 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-invert ..."></div></div>
```

Use the `backdrop-invert-[<value>]` syntax to set the backdrop inversion based on a completely custom value:

```
<div class="backdrop-invert-[.25] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-invert-(<custom-property>)` syntax:

```
<div class="backdrop-invert-(--my-backdrop-inversion) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-invert-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `backdrop-filter: invert()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-invert-0 md:backdrop-invert ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a custom value](#using-a-custom-value)
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
