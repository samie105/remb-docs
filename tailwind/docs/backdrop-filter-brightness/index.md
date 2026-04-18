---
title: "backdrop-filter: brightness()"
source: "https://tailwindcss.com/docs/backdrop-filter-brightness"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-brightness"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:09:31.550Z"
content_hash: "4f3128bdb6e766bedca713ac8f1190ecfb84c0ae500dd47bb6fabda86d374179"
menu_path: ["backdrop-filter: brightness()"]
section_path: []
nav_prev: {"path": "tailwind/docs/backdrop-filter-blur/index.md", "title": "backdrop-filter: blur()"}
nav_next: {"path": "tailwind/docs/backdrop-filter-contrast/index.md", "title": "backdrop-filter: contrast()"}
---

# backdrop-filter: brightness()

Utilities for applying backdrop brightness filters to an element.

Class

Styles

`backdrop-brightness-<number>`

`backdrop-filter: brightness(<number>%);`

`backdrop-brightness-(<custom-property>)`

`backdrop-filter: brightness(var(<custom-property>));`

`backdrop-brightness-[<value>]`

`backdrop-filter: brightness(<value>);`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `backdrop-brightness-50` and `backdrop-brightness-100` to control an element's backdrop brightness:

backdrop-brightness-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-brightness-150

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-brightness-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-brightness-150 ..."></div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `backdrop-brightness-[<value>]` syntax to set the backdrop brightness based on a completely custom value:

```
<div class="backdrop-brightness-[1.75] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-brightness-(<custom-property>)` syntax:

```
<div class="backdrop-brightness-(--my-backdrop-brightness) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-brightness-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `backdrop-filter: brightness()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-brightness-110 md:backdrop-brightness-150 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
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


