---
title: "outline-offset"
source: "https://tailwindcss.com/docs/outline-offset"
canonical_url: "https://tailwindcss.com/docs/outline-offset"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:04:03.335Z"
content_hash: "678bf551d07150556d540a525a7a9c1eef05861d32cfcca59370fe7aed3a6dab"
menu_path: ["outline-offset"]
section_path: []
nav_prev: {"path": "tailwind/docs/outline-style/index.md", "title": "outline-style"}
nav_next: {"path": "tailwind/docs/box-shadow/index.md", "title": "box-shadow"}
---

# outline-offset

Utilities for controlling the offset of an element's outline.

Class

Styles

`outline-offset-<number>`

`outline-offset: <number>px;`

`-outline-offset-<number>`

`outline-offset: calc(<number>px * -1);`

`outline-offset-(<custom-property>)`

`outline-offset: var(<custom-property>);`

`outline-offset-[<value>]`

`outline-offset: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `outline-offset-2` and `outline-offset-4` to change the offset of an element's outline:

outline-offset-0

outline-offset-2

outline-offset-4

```
<button class="outline-2 outline-offset-0 ...">Button A</button><button class="outline-2 outline-offset-2 ...">Button B</button><button class="outline-2 outline-offset-4 ...">Button C</button>
```

### [Using a custom value](#using-a-custom-value)

Use the `outline-offset-[<value>]` syntax to set the outline offset based on a completely custom value:

```
<div class="outline-offset-[2vw] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `outline-offset-(<custom-property>)` syntax:

```
<div class="outline-offset-(--my-outline-offset) ...">  <!-- ... --></div>
```

This is just a shorthand for `outline-offset-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix an `outline-offset` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="outline md:outline-offset-2 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
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
