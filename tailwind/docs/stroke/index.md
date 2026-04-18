---
title: "stroke"
source: "https://tailwindcss.com/docs/stroke"
canonical_url: "https://tailwindcss.com/docs/stroke"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:18:32.336Z"
content_hash: "2c869adc304461a1e3a7926d1a67c085519a6d487bce0255608c5fe046f17552"
menu_path: ["stroke"]
section_path: []
nav_prev: {"path": "tailwind/docs/fill/index.md", "title": "fill"}
nav_next: {"path": "tailwind/docs/stroke-width/index.md", "title": "stroke-width"}
---

# stroke

Utilities for styling the stroke of SVG elements.

Class

Styles

`stroke-none`

`stroke: none;`

`stroke-inherit`

`stroke: inherit;`

`stroke-current`

`stroke: currentColor;`

`stroke-transparent`

`stroke: transparent;`

`stroke-black`

`stroke: var(--color-black); /* #000 */`

`stroke-white`

`stroke: var(--color-white); /* #fff */`

`stroke-red-50`

`stroke: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */`

`stroke-red-100`

`stroke: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */`

`stroke-red-200`

`stroke: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */`

`stroke-red-300`

`stroke: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `stroke-indigo-500` and `stroke-lime-600` to change the stroke color of an SVG:

```
<svg class="stroke-cyan-500 ...">  <!-- ... --></svg>
```

This can be useful for styling icon sets like [Heroicons](https://heroicons.com).

### [Using the current color](#using-the-current-color)

Use the `stroke-current` utility to set the stroke color to the current text color:

Hover over the button to see the stroke color change

```
<button class="bg-white text-pink-600 hover:bg-pink-600 hover:text-white ...">  <svg class="size-5 stroke-current ..." fill="none">    <!-- ... -->  </svg>  Download file</button>
```

### [Using a custom value](#using-a-custom-value)

Use the `stroke-[<value>]` syntax to set the stroke color based on a completely custom value:

```
<svg class="stroke-[#243c5a] ...">  <!-- ... --></svg>
```

For CSS variables, you can also use the `stroke-(<custom-property>)` syntax:

```
<svg class="stroke-(--my-stroke-color) ...">  <!-- ... --></svg>
```

This is just a shorthand for `stroke-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `stroke` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<svg class="stroke-cyan-500 md:stroke-cyan-700 ...">  <!-- ... --></svg>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

## [Customizing your theme](#customizing-your-theme)

Use the `--color-*` theme variables to customize the color utilities in your project:

```
@theme {  --color-regal-blue: #243c5a; }
```

Now the `stroke-regal-blue` utility can be used in your markup:

```
<svg class="stroke-regal-blue">  <!-- ... --></svg>
```

Learn more about customizing your theme in the [theme documentation](/docs/theme#customizing-your-theme).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Using the current color](#using-the-current-color)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)
*   [Customizing your theme](#customizing-your-theme)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)

