---
title: "vertical-align"
source: "https://tailwindcss.com/docs/vertical-align"
canonical_url: "https://tailwindcss.com/docs/vertical-align"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:41.406Z"
content_hash: "63084324e1c7de69af367d5d9d2d108ecec4b7963b4149f10134a5ebaf436c8a"
menu_path: ["vertical-align"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Typography
2.  vertical-align

Typography

# vertical-align

Utilities for controlling the vertical alignment of an inline or table-cell box.

Class

Styles

`align-baseline`

`vertical-align: baseline;`

`align-top`

`vertical-align: top;`

`align-middle`

`vertical-align: middle;`

`align-bottom`

`vertical-align: bottom;`

`align-text-top`

`vertical-align: text-top;`

`align-text-bottom`

`vertical-align: text-bottom;`

`align-sub`

`vertical-align: sub;`

`align-super`

`vertical-align: super;`

`align-(<custom-property>)`

`vertical-align: var(<custom-property>);`

`align-[<value>]`

`vertical-align: <value>;`

## [Examples](#examples)

### [Aligning to baseline](#aligning-to-baseline)

Use the `align-baseline` utility to align the baseline of an element with the baseline of its parent:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-baseline">The quick brown fox...</span>
```

### [Aligning to top](#aligning-to-top)

Use the `align-top` utility to align the top of an element and its descendants with the top of the entire line:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-top">The quick brown fox...</span>
```

### [Aligning to middle](#aligning-to-middle)

Use the `align-middle` utility to align the middle of an element with the baseline plus half the x-height of the parent:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-middle">The quick brown fox...</span>
```

### [Aligning to bottom](#aligning-to-bottom)

Use the `align-bottom` utility to align the bottom of an element and its descendants with the bottom of the entire line:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-bottom">The quick brown fox...</span>
```

### [Aligning to parent top](#aligning-to-parent-top)

Use the `align-text-top` utility to align the top of an element with the top of the parent element's font:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-text-top">The quick brown fox...</span>
```

### [Aligning to parent bottom](#aligning-to-parent-bottom)

Use the `align-text-bottom` utility to align the bottom of an element with the bottom of the parent element's font:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-text-bottom">The quick brown fox...</span>
```

### [Using a custom value](#using-a-custom-value)

Use the `align-[<value>]` syntax to set the vertical alignment based on a completely custom value:

```
<span class="align-[4px] ...">  <!-- ... --></span>
```

For CSS variables, you can also use the `align-(<custom-property>)` syntax:

```
<span class="align-(--my-alignment) ...">  <!-- ... --></span>
```

This is just a shorthand for `align-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `vertical-align` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<span class="align-middle md:align-top ...">  <!-- ... --></span>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Aligning to baseline](#aligning-to-baseline)
    *   [Aligning to top](#aligning-to-top)
    *   [Aligning to middle](#aligning-to-middle)
    *   [Aligning to bottom](#aligning-to-bottom)
    *   [Aligning to parent top](#aligning-to-parent-top)
    *   [Aligning to parent bottom](#aligning-to-parent-bottom)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
