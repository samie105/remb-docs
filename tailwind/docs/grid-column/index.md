---
title: "grid-column"
source: "https://tailwindcss.com/docs/grid-column"
canonical_url: "https://tailwindcss.com/docs/grid-column"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:58:21.920Z"
content_hash: "95f80e8d86dd10e455d4fcaae8e0116d877da7c42fa80d963bf8e1c6b8eb2b04"
menu_path: ["grid-column"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/grid-template-columns/index.md", "title": "grid-template-columns"}
nav_next: {"path": "tailwind/docs/grid-template-rows/index.md", "title": "grid-template-rows"}
---

Flexbox & Grid

Utilities for controlling how elements are sized and placed across grid columns.

## [Examples](#examples)

### [Spanning columns](#spanning-columns)

Use `col-span-<number>` utilities like `col-span-2` and `col-span-4` to make an element span _n_ columns:

01

02

03

04

05

06

07

```
<div class="grid grid-cols-3 gap-4">  <div class="...">01</div>  <div class="...">02</div>  <div class="...">03</div>  <div class="col-span-2 ...">04</div>  <div class="...">05</div>  <div class="...">06</div>  <div class="col-span-2 ...">07</div></div>
```

### [Starting and ending lines](#starting-and-ending-lines)

Use `col-start-<number>` or `col-end-<number>` utilities like `col-start-2` and `col-end-3` to make an element start or end at the _nth_ grid line:

01

02

03

04

```
<div class="grid grid-cols-6 gap-4">  <div class="col-span-4 col-start-2 ...">01</div>  <div class="col-start-1 col-end-3 ...">02</div>  <div class="col-span-2 col-end-7 ...">03</div>  <div class="col-start-1 col-end-7 ...">04</div></div>
```

These can also be combined with the `col-span-<number>` utilities to span a specific number of columns.

### [Using a custom value](#using-a-custom-value)

Use utilities like `col-[<value>]`,`col-span-[<value>]`,`col-start-[<value>]`, and `col-end-[<value>]` to set the grid column size and location based on a completely custom value:

```
<div class="col-[16_/_span_16] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `col-(<custom-property>)` syntax:

```
<div class="col-(--my-columns) ...">  <!-- ... --></div>
```

This is just a shorthand for `col-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix `grid-column`,`grid-column-start`, and `grid-column-end` utilities with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="col-span-2 md:col-span-6 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).
