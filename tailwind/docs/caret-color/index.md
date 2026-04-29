---
title: "caret-color"
source: "https://tailwindcss.com/docs/caret-color"
canonical_url: "https://tailwindcss.com/docs/caret-color"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:36:47.838Z"
content_hash: "e97d7cc079c62d7ddc87bb0151bfd4a63cf472787c3b4143df7793695927f2c8"
menu_path: ["caret-color"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/appearance/index.md", "title": "appearance"}
nav_next: {"path": "tailwind/docs/color-scheme/index.md", "title": "color-scheme"}
---

# caret-color

Utilities for controlling the color of the text input cursor.

| Class | Styles |
| --- | --- |
| `caret-inherit` | 
`caret-color: inherit;`

 |
| `caret-current` | 

`caret-color: currentColor;`

 |
| `caret-transparent` | 

`caret-color: transparent;`

 |
| `caret-black` | 

`caret-color: var(--color-black); /* #000 */`

 |
| `caret-white` | 

`caret-color: var(--color-white); /* #fff */`

 |
| `caret-red-50` | 

`caret-color: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */`

 |
| `caret-red-100` | 

`caret-color: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */`

 |
| `caret-red-200` | 

`caret-color: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */`

 |
| `caret-red-300` | 

`caret-color: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */`

 |
| `caret-red-400` | 

`caret-color: var(--color-red-400); /* oklch(70.4% 0.191 22.216) */`

 |

Use utilities like `caret-rose-500` and `caret-lime-600` to change the color of the text input cursor:

Focus the textarea to see the new caret color

```
<textarea class="caret-pink-500 ..."></textarea>
```

Use the `caret-[<value>]` syntax to set the caret color based on a completely custom value:

```
<textarea class="caret-[#50d71e] ..."></textarea>
```

For CSS variables, you can also use the `caret-(<custom-property>)` syntax:

```
<textarea class="caret-(--my-caret-color) ..."></textarea>
```

This is just a shorthand for `caret-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `caret-color` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<textarea class="caret-rose-500 md:caret-lime-600 ..."></textarea>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

Use the `--color-*` theme variables to customize the color utilities in your project:

```
@theme {  --color-regal-blue: #243c5a; }
```

Now the `caret-regal-blue` utility can be used in your markup:

```
<textarea class="caret-regal-blue"></textarea>
```

Learn more about customizing your theme in the [theme documentation](../theme/index.md#customizing-your-theme).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)
-   [Customizing your theme](#customizing-your-theme)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
