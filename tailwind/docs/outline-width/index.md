---
title: "outline-width"
source: "https://tailwindcss.com/docs/outline-width"
canonical_url: "https://tailwindcss.com/docs/outline-width"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:26.386Z"
content_hash: "a32f03b6bd854e0a0defaf81bab60d80a4b2e8f0f55c925d11049f19917157f3"
menu_path: ["outline-width"]
section_path: []
nav_prev: {"path": "tailwind/docs/border-style/index.md", "title": "border-style"}
nav_next: {"path": "tailwind/docs/outline-color/index.md", "title": "outline-color"}
---

# outline-width

Utilities for controlling the width of an element's outline.

Class

Styles

`outline`

`outline-width: 1px;`

`outline-<number>`

`outline-width: <number>px;`

`outline-(length:<custom-property>)`

`outline-width: var(<custom-property>);`

`outline-[<value>]`

`outline-width: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use `outline` or `outline-<number>` utilities like `outline-2` and `outline-4` to set the width of an element's outline:

outline

outline-2

outline-4

```
<button class="outline outline-offset-2 ...">Button A</button><button class="outline-2 outline-offset-2 ...">Button B</button><button class="outline-4 outline-offset-2 ...">Button C</button>
```

### [Applying on focus](#applying-on-focus)

Prefix an `outline-width` utility with a variant like `focus:*` to only apply the utility in that state:

Focus the button to see the outline added

```
<button class="outline-offset-2 outline-sky-500 focus:outline-2 ...">Save Changes</button>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### [Using a custom value](#using-a-custom-value)

Use the `outline-[<value>]` syntax to set the outline width based on a completely custom value:

```
<div class="outline-[2vw] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `outline-(length:<custom-property>)` syntax:

```
<div class="outline-(length:--my-outline-width) ...">  <!-- ... --></div>
```

This is just a shorthand for `outline-[length:var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix an `outline-width` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="outline md:outline-2 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Applying on focus](#applying-on-focus)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
