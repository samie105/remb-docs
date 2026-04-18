---
title: "transform-origin"
source: "https://tailwindcss.com/docs/transform-origin"
canonical_url: "https://tailwindcss.com/docs/transform-origin"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:22.095Z"
content_hash: "27d5932e48f4f8df63e1bd51af59056960a44b890e37ad39f0f41268722f7cbb"
menu_path: ["transform-origin"]
section_path: []
nav_prev: {"path": "tailwind/docs/transform/index.md", "title": "transform"}
nav_next: {"path": "tailwind/docs/transform-style/index.md", "title": "transform-style"}
---

# transform-origin

Utilities for specifying the origin for an element's transformations.

Class

Styles

`origin-center`

`transform-origin: center;`

`origin-top`

`transform-origin: top;`

`origin-top-right`

`transform-origin: top right;`

`origin-right`

`transform-origin: right;`

`origin-bottom-right`

`transform-origin: bottom right;`

`origin-bottom`

`transform-origin: bottom;`

`origin-bottom-left`

`transform-origin: bottom left;`

`origin-left`

`transform-origin: left;`

`origin-top-left`

`transform-origin: top left;`

`origin-(<custom-property>)`

`transform-origin: var(<custom-property>);`

`origin-[<value>]`

`transform-origin: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `origin-top` and `origin-bottom-left` to set an element's transform origin:

origin-center

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

origin-top-left

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

origin-bottom

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="origin-center rotate-45 ..." src="/img/mountains.jpg" /><img class="origin-top-left rotate-12 ..." src="/img/mountains.jpg" /><img class="origin-bottom -rotate-12 ..." src="/img/mountains.jpg" />
```

### [Using a custom value](#using-a-custom-value)

Use the `origin-[<value>]` syntax to set the transform origin based on a completely custom value:

```
<img class="origin-[33%_75%] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `origin-(<custom-property>)` syntax:

```
<img class="origin-(--my-transform-origin) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `origin-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `transform-origin` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="origin-center md:origin-top ..." src="/img/mountains.jpg" />
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

