---
title: "grid-row"
source: "https://tailwindcss.com/docs/grid-row"
canonical_url: "https://tailwindcss.com/docs/grid-row"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:58:56.345Z"
content_hash: "76864c57cdb98d65be1b2a58cd0e35cb1959c0910720cfb0a64f365f8e8e42b1"
menu_path: ["grid-row"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/grid-template-rows/index.md", "title": "grid-template-rows"}
nav_next: {"path": "tailwind/docs/grid-auto-flow/index.md", "title": "grid-auto-flow"}
---

Flexbox & Grid

Utilities for controlling how elements are sized and placed across grid rows.

## [Examples](#examples)

### [Spanning rows](#spanning-rows)

Use `row-span-<number>` utilities like `row-span-2` and `row-span-4` to make an element span _n_ rows:

01

02

03

```
<div class="grid grid-flow-col grid-rows-3 gap-4">  <div class="row-span-3 ...">01</div>  <div class="col-span-2 ...">02</div>  <div class="col-span-2 row-span-2 ...">03</div></div>
```

### [Starting and ending lines](#starting-and-ending-lines)

Use `row-start-<number>` or `row-end-<number>` utilities like `row-start-2` and `row-end-3` to make an element start or end at the _nth_ grid line:

01

02

03

```
<div class="grid grid-flow-col grid-rows-3 gap-4">  <div class="row-span-2 row-start-2 ...">01</div>  <div class="row-span-2 row-end-3 ...">02</div>  <div class="row-start-1 row-end-4 ...">03</div></div>
```

These can also be combined with the `row-span-<number>` utilities to span a specific number of rows.

### [Using a custom value](#using-a-custom-value)

Use utilities like `row-[<value>]`,`row-span-[<value>]`,`row-start-[<value>]`, and `row-end-[<value>]` to set the grid row size and location based on a completely custom value:

```
<div class="row-[span_16_/_span_16] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `row-(<custom-property>)` syntax:

```
<div class="row-(--my-rows) ...">  <!-- ... --></div>
```

This is just a shorthand for `row-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix `grid-row`,`grid-row-start`, and `grid-row-end` utilities with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="row-span-3 md:row-span-4 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
