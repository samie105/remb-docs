---
title: "border-width"
source: "https://tailwindcss.com/docs/border-width"
canonical_url: "https://tailwindcss.com/docs/border-width"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:18:40.245Z"
content_hash: "5b2c61d17d6def875989af9520152a581d94a675e6fd475afe3badde0cbcab6d"
menu_path: ["border-width"]
section_path: []
content_language: "en"
nav_prev: {"path": "../border-radius/index.md", "title": "border-radius"}
nav_next: {"path": "../border-color/index.md", "title": "border-color"}
---

Utilities for controlling the width of an element's borders.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `border` or `border-<number>` utilities like `border-2` and `border-4` to set the border width for all sides of an element:

border

border-2

border-4

border-8

```
<div class="border border-indigo-600 ..."></div><div class="border-2 border-indigo-600 ..."></div><div class="border-4 border-indigo-600 ..."></div><div class="border-8 border-indigo-600 ..."></div>
```

### [Individual sides](#individual-sides)

Use utilities like `border-r` and `border-t-4` to set the border width for one side of an element:

border-t-4

border-r-4

border-b-4

border-l-4

```
<div class="border-t-4 border-indigo-500 ..."></div><div class="border-r-4 border-indigo-500 ..."></div><div class="border-b-4 border-indigo-500 ..."></div><div class="border-l-4 border-indigo-500 ..."></div>
```

### [Horizontal and vertical sides](#horizontal-and-vertical-sides)

Use utilities like `border-x` and `border-y-4` to set the border width on two sides of an element at the same time:

border-x-4

border-y-4

```
<div class="border-x-4 border-indigo-500 ..."></div><div class="border-y-4 border-indigo-500 ..."></div>
```

### [Using logical properties](#using-logical-properties)

Use utilities like `border-s` and `border-e-4` to set the `border-inline-start-width` and `border-inline-end-width` [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts), which map to either the left or right border based on the text direction:

Left-to-right

Right-to-left

```
<div dir="ltr">  <div class="border-s-4 ..."></div></div><div dir="rtl">  <div class="border-s-4 ..."></div></div>
```

Use the `border-bs-<number>` and `border-be-<number>` utilities to set the `border-block-start-width` and `border-block-end-width` logical properties, which map to either the top or bottom border based on the writing mode:

```
<div class="border-bs-4 ..."></div>
```

### [Between children](#between-children)

Use utilities like `divide-x` and `divide-y-4` to add borders between child elements:

01

02

03

```
<div class="grid grid-cols-3 divide-x-4">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

#### [Reversing children order](#reversing-children-order)

If your elements are in reverse order (using say `flex-row-reverse` or `flex-col-reverse`), use the `divide-x-reverse` or `divide-y-reverse` utilities to ensure the border is added to the correct side of each element:

01

02

03

```
<div class="flex flex-col-reverse divide-y-4 divide-y-reverse divide-gray-200">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `border-[<value>]` syntax to set the border width based on a completely custom value:

```
<div class="border-[2vw] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `border-(length:<custom-property>)` syntax:

```
<div class="border-(length:--my-border-width) ...">  <!-- ... --></div>
```

This is just a shorthand for `border-[length:var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `border-width` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="border-2 md:border-t-4 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
