---
title: "background-color"
source: "https://tailwindcss.com/docs/background-color"
canonical_url: "https://tailwindcss.com/docs/background-color"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:16:20.011Z"
content_hash: "7caf0e1d22d6f433dd1096b5f92185eafde775a724f3c360242f8b3e0635f239"
menu_path: ["background-color"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Backgrounds
2.  background-color

Backgrounds

# background-color

Utilities for controlling an element's background color.

| Class | Styles |
| --- | --- |
| `bg-inherit` | 
`background-color: inherit;`

 |
| `bg-current` | 

`background-color: currentColor;`

 |
| `bg-transparent` | 

`background-color: transparent;`

 |
| `bg-black` | 

`background-color: var(--color-black); /* #000 */`

 |
| `bg-white` | 

`background-color: var(--color-white); /* #fff */`

 |
| `bg-red-50` | 

`background-color: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */`

 |
| `bg-red-100` | 

`background-color: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */`

 |
| `bg-red-200` | 

`background-color: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */`

 |
| `bg-red-300` | 

`background-color: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */`

 |
| `bg-red-400` | 

`background-color: var(--color-red-400); /* oklch(70.4% 0.191 22.216) */`

 |

Use utilities like `bg-white`, `bg-indigo-500` and `bg-transparent` to control the background color of an element:

bg-blue-500

bg-cyan-500

bg-pink-500

```
<button class="bg-blue-500 ...">Button A</button><button class="bg-cyan-500 ...">Button B</button><button class="bg-pink-500 ...">Button C</button>
```

Use the color opacity modifier to control the opacity of an element's background color:

bg-sky-500/100

bg-sky-500/75

bg-sky-500/50

```
<button class="bg-sky-500/100 ..."></button><button class="bg-sky-500/75 ..."></button><button class="bg-sky-500/50 ..."></button>
```

Use the `bg-[<value>]` syntax to set the background color based on a completely custom value:

```
<div class="bg-[#50d71e] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `bg-(<custom-property>)` syntax:

```
<div class="bg-(--my-color) ...">  <!-- ... --></div>
```

This is just a shorthand for `bg-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `background-color` utility with a variant like `hover:*` to only apply the utility in that state:

```
<button class="bg-indigo-500 hover:bg-fuchsia-500 ...">Save changes</button>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

Prefix a `background-color` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="bg-blue-500 md:bg-green-500 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

Use the `--color-*` theme variables to customize the color utilities in your project:

```
@theme {  --color-regal-blue: #243c5a; }
```

Now the `bg-regal-blue` utility can be used in your markup:

```
<div class="bg-regal-blue">  <!-- ... --></div>
```

Learn more about customizing your theme in the [theme documentation](/docs/theme#customizing-your-theme).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Changing the opacity](#changing-the-opacity)
    -   [Using a custom value](#using-a-custom-value)
    -   [Applying on hover](#applying-on-hover)
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
