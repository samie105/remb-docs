---
title: "outline-color"
source: "https://tailwindcss.com/docs/outline-color"
canonical_url: "https://tailwindcss.com/docs/outline-color"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:19:53.350Z"
content_hash: "b5961dfcc917ea22da9cc82aceec5061a63a1640eb230256f824d210090f3300"
menu_path: ["outline-color"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Borders
2.  outline-color

Borders

# outline-color

Utilities for controlling the color of an element's outline.

| Class | Styles |
| --- | --- |
| `outline-inherit` | 
`outline-color: inherit;`

 |
| `outline-current` | 

`outline-color: currentColor;`

 |
| `outline-transparent` | 

`outline-color: transparent;`

 |
| `outline-black` | 

`outline-color: var(--color-black); /* #000 */`

 |
| `outline-white` | 

`outline-color: var(--color-white); /* #fff */`

 |
| `outline-red-50` | 

`outline-color: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */`

 |
| `outline-red-100` | 

`outline-color: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */`

 |
| `outline-red-200` | 

`outline-color: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */`

 |
| `outline-red-300` | 

`outline-color: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */`

 |
| `outline-red-400` | 

`outline-color: var(--color-red-400); /* oklch(70.4% 0.191 22.216) */`

 |

Use utilities like `outline-rose-500` and `outline-lime-100` to control the color of an element's outline:

outline-blue-500

outline-cyan-500

outline-pink-500

```
<button class="outline-2 outline-offset-2 outline-blue-500 ...">Button A</button><button class="outline-2 outline-offset-2 outline-cyan-500 ...">Button B</button><button class="outline-2 outline-offset-2 outline-pink-500 ...">Button C</button>
```

Use the color opacity modifier to control the opacity of an element's outline color:

outline-blue-500/100

outline-blue-500/75

outline-blue-500/50

```
<button class="outline-2 outline-blue-500/100 ...">Button A</button><button class="outline-2 outline-blue-500/75 ...">Button B</button><button class="outline-2 outline-blue-500/50 ...">Button C</button>
```

Use the `outline-[<value>]` syntax to set the outline color based on a completely custom value:

```
<div class="outline-[#243c5a] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `outline-(<custom-property>)` syntax:

```
<div class="outline-(--my-color) ...">  <!-- ... --></div>
```

This is just a shorthand for `outline-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix an `outline-color` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="outline md:outline-blue-400 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

Use the `--color-*` theme variables to customize the color utilities in your project:

```
@theme {  --color-regal-blue: #243c5a; }
```

Now the `outline-regal-blue` utility can be used in your markup:

```
<div class="outline-regal-blue">  <!-- ... --></div>
```

Learn more about customizing your theme in the [theme documentation](/docs/theme#customizing-your-theme).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Changing the opacity](#changing-the-opacity)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)
-   [Customizing your theme](#customizing-your-theme)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
