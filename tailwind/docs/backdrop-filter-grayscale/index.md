---
title: "backdrop-filter: grayscale()"
source: "https://tailwindcss.com/docs/backdrop-filter-grayscale"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-grayscale"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:28:39.243Z"
content_hash: "0d8b21b699537576e01e39fd7d0493e6a6fc36e32f1ba400c489674f3db4934f"
menu_path: ["backdrop-filter: grayscale()"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/backdrop-filter-contrast/index.md", "title": "backdrop-filter: contrast()"}
nav_next: {"path": "tailwind/docs/backdrop-filter-hue-rotate/index.md", "title": "backdrop-filter: hue-rotate()"}
---

# backdrop-filter: grayscale()

Utilities for applying backdrop grayscale filters to an element.

| Class | Styles |
| --- | --- |
| `backdrop-grayscale` | 
`backdrop-filter: grayscale(100%);`

 |
| `backdrop-grayscale-<number>` | 

`backdrop-filter: grayscale(<number>%);`

 |
| `backdrop-grayscale-(<custom-property>)` | 

`backdrop-filter: grayscale(var(<custom-property>));`

 |
| `backdrop-grayscale-[<value>]` | 

`backdrop-filter: grayscale(<value>);`

 |

Use utilities like `backdrop-grayscale-50` and `backdrop-grayscale` to control the grayscale effect applied to an element's backdrop:

backdrop-grayscale-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-grayscale-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-grayscale

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-grayscale-0 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-grayscale-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-grayscale-200 ..."></div></div>
```

Use the `backdrop-grayscale-[<value>]` syntax to set the backdrop grayscale based on a completely custom value:

```
<div class="backdrop-grayscale-[0.5] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-grayscale-(<custom-property>)` syntax:

```
<div class="backdrop-grayscale-(--my-backdrop-grayscale) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-grayscale-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `backdrop-filter: grayscale()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-grayscale md:backdrop-grayscale-0 ...">  <!-- ... --></div>
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
