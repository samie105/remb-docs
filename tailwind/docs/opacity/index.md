---
title: "opacity"
source: "https://tailwindcss.com/docs/opacity"
canonical_url: "https://tailwindcss.com/docs/opacity"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:21:05.065Z"
content_hash: "b70481cf461d07bbba614713bada98d6ab24069fee0d753daf9a4b6d5d6f35a9"
menu_path: ["opacity"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/text-shadow/index.md", "title": "text-shadow"}
nav_next: {"path": "tailwind/docs/mix-blend-mode/index.md", "title": "mix-blend-mode"}
---

# opacity

Utilities for controlling the opacity of an element.

| Class | Styles |
| --- | --- |
| `opacity-<number>` | 
`opacity: <number>%;`

 |
| `opacity-(<custom-property>)` | 

`opacity: var(<custom-property>);`

 |
| `opacity-[<value>]` | 

`opacity: <value>;`

 |

Use `opacity-<number>` utilities like `opacity-25` and `opacity-100` to set the opacity of an element:

opacity-100

opacity-75

opacity-50

opacity-25

```
<button class="bg-indigo-500 opacity-100 ..."></button><button class="bg-indigo-500 opacity-75 ..."></button><button class="bg-indigo-500 opacity-50 ..."></button><button class="bg-indigo-500 opacity-25 ..."></button>
```

Prefix an `opacity` utility with a variant like `disabled:*` to only apply the utility in that state:

```
<input class="opacity-100 disabled:opacity-75 ..." type="text" />
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

Use the `opacity-[<value>]` syntax to set the opacity based on a completely custom value:

```
<button class="opacity-[.67] ...">  <!-- ... --></button>
```

For CSS variables, you can also use the `opacity-(<custom-property>)` syntax:

```
<button class="opacity-(--my-opacity) ...">  <!-- ... --></button>
```

This is just a shorthand for `opacity-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix an `opacity` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<button class="opacity-50 md:opacity-100 ...">  <!-- ... --></button>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Applying conditionally](#applying-conditionally)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
