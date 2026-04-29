---
title: "grid-template-columns"
source: "https://tailwindcss.com/docs/grid-template-columns"
canonical_url: "https://tailwindcss.com/docs/grid-template-columns"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:57:54.296Z"
content_hash: "169b678d07279d6dcbdeb2958996c9876e4bc310fe52b306f628a7d1d0f3f94f"
menu_path: ["grid-template-columns"]
section_path: []
content_language: "en"
nav_prev: {"path": "../order/index.md", "title": "order"}
nav_next: {"path": "../grid-column/index.md", "title": "grid-column"}
---

# grid-template-columns

Utilities for specifying the columns in a grid layout.

| Class | Styles |
| --- | --- |
| `grid-cols-<number>` | 
`grid-template-columns: repeat(<number>, minmax(0, 1fr));`

 |
| `grid-cols-none` | 

`grid-template-columns: none;`

 |
| `grid-cols-subgrid` | 

`grid-template-columns: subgrid;`

 |
| `grid-cols-[<value>]` | 

`grid-template-columns: <value>;`

 |
| `grid-cols-(<custom-property>)` | 

`grid-template-columns: var(<custom-property>);`

 |

Use `grid-cols-<number>` utilities like `grid-cols-2` and `grid-cols-4` to create grids with _n_ equally sized columns:

01

02

03

04

05

06

07

08

09

```
<div class="grid grid-cols-4 gap-4">  <div>01</div>  <!-- ... -->  <div>09</div></div>
```

Use the `grid-cols-subgrid` utility to adopt the column tracks defined by the item's parent:

01

02

03

04

05

06

```
<div class="grid grid-cols-4 gap-4">  <div>01</div>  <!-- ... -->  <div>05</div>  <div class="col-span-3 grid grid-cols-subgrid gap-4">    <div class="col-start-2">06</div>  </div></div>
```

Use the `grid-cols-[<value>]` syntax to set the columns based on a completely custom value:

```
<div class="grid-cols-[200px_minmax(900px,_1fr)_100px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `grid-cols-(<custom-property>)` syntax:

```
<div class="grid-cols-(--my-grid-cols) ...">  <!-- ... --></div>
```

This is just a shorthand for `grid-cols-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `grid-template-columns` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid grid-cols-1 md:grid-cols-6 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Specifying the grid columns](#specifying-the-grid-columns)
    -   [Implementing a subgrid](#implementing-a-subgrid)
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
