---
title: "grid-auto-columns"
source: "https://tailwindcss.com/docs/grid-auto-columns"
canonical_url: "https://tailwindcss.com/docs/grid-auto-columns"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:59:30.800Z"
content_hash: "1d17a098b22d38cfc69742a460595de80c1cb32aa9df38ec13646d9aecfd1393"
menu_path: ["grid-auto-columns"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/grid-auto-flow/index.md", "title": "grid-auto-flow"}
nav_next: {"path": "tailwind/docs/grid-auto-rows/index.md", "title": "grid-auto-rows"}
---

# grid-auto-columns

Utilities for controlling the size of implicitly-created grid columns.

| Class | Styles |
| --- | --- |
| `auto-cols-auto` | 
`grid-auto-columns: auto;`

 |
| `auto-cols-min` | 

`grid-auto-columns: min-content;`

 |
| `auto-cols-max` | 

`grid-auto-columns: max-content;`

 |
| `auto-cols-fr` | 

`grid-auto-columns: minmax(0, 1fr);`

 |
| `auto-cols-(<custom-property>)` | 

`grid-auto-columns: var(<custom-property>);`

 |
| `auto-cols-[<value>]` | 

`grid-auto-columns: <value>;`

 |

Use utilities like `auto-cols-min` and `auto-cols-max` to control the size of implicitly-created grid columns:

```
<div class="grid auto-cols-max grid-flow-col">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use the `auto-cols-[<value>]` syntax to set the size of implicitly-created grid columns based on a completely custom value:

```
<div class="auto-cols-[minmax(0,2fr)] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `auto-cols-(<custom-property>)` syntax:

```
<div class="auto-cols-(--my-auto-cols) ...">  <!-- ... --></div>
```

This is just a shorthand for `auto-cols-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `grid-auto-columns` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid grid-flow-col auto-cols-max md:auto-cols-min ...">  <!-- ... --></div>
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
