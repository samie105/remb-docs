---
title: "order"
source: "https://tailwindcss.com/docs/order"
canonical_url: "https://tailwindcss.com/docs/order"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:10.659Z"
content_hash: "bd75e17d10dd58e22a1996a85e2e7bd7a66ee560b712560becb1f1a9435d89c3"
menu_path: ["order"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  order

Flexbox & Grid

# order

Utilities for controlling the order of flex and grid items.

Class

Styles

`order-<number>`

`order: <number>;`

`-order-<number>`

`order: calc(<number> * -1);`

`order-first`

`order: -9999;`

`order-last`

`order: 9999;`

`order-none`

`order: 0;`

`order-(<custom-property>)`

`order: var(<custom-property>);`

`order-[<value>]`

`order: <value>;`

## [Examples](#examples)

### [Explicitly setting a sort order](#explicitly-setting-a-sort-order)

Use `order-<number>` utilities like `order-1` and `order-3` to render flex and grid items in a different order than they appear in the document:

01

02

03

```
<div class="flex justify-between ...">  <div class="order-3 ...">01</div>  <div class="order-1 ...">02</div>  <div class="order-2 ...">03</div></div>
```

### [Ordering items first or last](#ordering-items-first-or-last)

Use the `order-first` and `order-last` utilities to render flex and grid items first or last:

01

02

03

```
<div class="flex justify-between ...">  <div class="order-last ...">01</div>  <div class="...">02</div>  <div class="order-first ...">03</div></div>
```

### [Using negative values](#using-negative-values)

To use a negative order value, prefix the class name with a dash to convert it to a negative value:

```
<div class="-order-1">  <!-- ... --></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `order-[<value>]` syntax to set the order based on a completely custom value:

```
<div class="order-[min(var(--total-items),10)] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `order-(<custom-property>)` syntax:

```
<div class="order-(--my-order) ...">  <!-- ... --></div>
```

This is just a shorthand for `order-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix an `order` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="order-first md:order-last ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Explicitly setting a sort order](#explicitly-setting-a-sort-order)
    *   [Ordering items first or last](#ordering-items-first-or-last)
    *   [Using negative values](#using-negative-values)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
