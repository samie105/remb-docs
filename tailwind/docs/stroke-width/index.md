---
title: "stroke-width"
source: "https://tailwindcss.com/docs/stroke-width"
canonical_url: "https://tailwindcss.com/docs/stroke-width"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:18:31.720Z"
content_hash: "d182d8e0a27cbb240dc702c6e65d88c4f03f956afc54458f12b76102b4109bd4"
menu_path: ["stroke-width"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  SVG
2.  stroke-width

SVG

# stroke-width

Utilities for styling the stroke width of SVG elements.

Class

Styles

`stroke-<number>`

`stroke-width: <number>;`

`stroke-(length:<custom-property>)`

`stroke-width: var(<custom-property>);`

`stroke-[<value>]`

`stroke-width: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use `stroke-<number>` utilities like `stroke-1` and `stroke-2` to set the stroke width of an SVG:

```
<svg class="stroke-1 ..."></svg><svg class="stroke-2 ..."></svg>
```

This can be useful for styling icon sets like [Heroicons](https://heroicons.com).

### [Using a custom value](#using-a-custom-value)

Use the `stroke-[<value>]` syntax to set the stroke width based on a completely custom value:

```
<div class="stroke-[1.5] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `stroke-(length:<custom-property>)` syntax:

```
<div class="stroke-(length:--my-stroke-width) ...">  <!-- ... --></div>
```

This is just a shorthand for `stroke-[length:var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `stroke-width` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="stroke-1 md:stroke-2 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
