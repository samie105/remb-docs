---
title: "fill"
source: "https://tailwindcss.com/docs/fill"
canonical_url: "https://tailwindcss.com/docs/fill"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:18:30.711Z"
content_hash: "1a7533369d15607173e5e705c050eada10181c518abbf91a3acefb7e0931a6f9"
menu_path: ["fill"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  SVG
2.  fill

SVG

# fill

Utilities for styling the fill of SVG elements.

Class

Styles

`fill-none`

`fill: none;`

`fill-inherit`

`fill: inherit;`

`fill-current`

`fill: currentColor;`

`fill-transparent`

`fill: transparent;`

`fill-black`

`fill: var(--color-black); /* #000 */`

`fill-white`

`fill: var(--color-white); /* #fff */`

`fill-red-50`

`fill: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */`

`fill-red-100`

`fill: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */`

`fill-red-200`

`fill: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */`

`fill-red-300`

`fill: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `fill-indigo-500` and `fill-lime-600` to change the fill color of an SVG:

```
<svg class="fill-blue-500 ...">  <!-- ... --></svg>
```

This can be useful for styling icon sets like [Heroicons](https://heroicons.com).

### [Using the current color](#using-the-current-color)

Use the `fill-current` utility to set the fill color to the current text color:

Hover over the button to see the fill color change

```
<button class="bg-white text-indigo-600 hover:bg-indigo-600 hover:text-white ...">  <svg class="size-5 fill-current ...">    <!-- ... -->  </svg>  Check for updates</button>
```

### [Using a custom value](#using-a-custom-value)

Use the `fill-[<value>]` syntax to set the fill color based on a completely custom value:

```
<svg class="fill-[#243c5a] ...">  <!-- ... --></svg>
```

For CSS variables, you can also use the `fill-(<custom-property>)` syntax:

```
<svg class="fill-(--my-fill-color) ...">  <!-- ... --></svg>
```

This is just a shorthand for `fill-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `fill` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<svg class="fill-cyan-500 md:fill-cyan-700 ...">  <!-- ... --></svg>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

## [Customizing your theme](#customizing-your-theme)

Use the `--color-*` theme variables to customize the color utilities in your project:

```
@theme {  --color-regal-blue: #243c5a; }
```

Now the `fill-regal-blue` utility can be used in your markup:

```
<svg class="fill-regal-blue">  <!-- ... --></svg>
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

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
