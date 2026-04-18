---
title: "filter: sepia()"
source: "https://tailwindcss.com/docs/filter-sepia"
canonical_url: "https://tailwindcss.com/docs/filter-sepia"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:56.202Z"
content_hash: "a7ed12c7b1e5f247533e32f31d89ccdc7d9b96dbbe5178c6ab42ad635b9f6b1c"
menu_path: ["filter: sepia()"]
section_path: []
nav_prev: {"path": "tailwind/docs/filter-saturate/index.md", "title": "filter: saturate()"}
nav_next: {"path": "tailwind/docs/backdrop-filter/index.md", "title": "backdrop-filter"}
---

# filter: sepia()

Utilities for applying sepia filters to an element.

Class

Styles

`sepia`

`filter: sepia(100%);`

`sepia-<number>`

`filter: sepia(<number>%);`

`sepia-(<custom-property>)`

`filter: sepia(var(<custom-property>));`

`sepia-[<value>]`

`filter: sepia(<value>);`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `sepia` and `sepia-50` to control the sepia effect applied to an element:

sepia-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

sepia-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

sepia

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="sepia-0" src="/img/mountains.jpg" /><img class="sepia-50" src="/img/mountains.jpg" /><img class="sepia" src="/img/mountains.jpg" />
```

### [Using a custom value](#using-a-custom-value)

Use the `sepia-[<value>]` syntax to set the sepia amount based on a completely custom value:

```
<img class="sepia-[.25] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `sepia-(<custom-property>)` syntax:

```
<img class="sepia-(--my-sepia) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `sepia-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `filter: sepia()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="sepia md:sepia-0 ..." src="/img/mountains.jpg" />
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

