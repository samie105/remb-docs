---
title: "filter: grayscale()"
source: "https://tailwindcss.com/docs/filter-grayscale"
canonical_url: "https://tailwindcss.com/docs/filter-grayscale"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:26:20.252Z"
content_hash: "ecfba0b96c05430d0e94cf6a8a246f5b0a64f279a1835cfa8159f1480aa2fd57"
menu_path: ["filter: grayscale()"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/filter-drop-shadow/index.md", "title": "filter: drop-shadow()"}
nav_next: {"path": "tailwind/docs/filter-hue-rotate/index.md", "title": "filter: hue-rotate()"}
---

# filter: grayscale()

Utilities for applying grayscale filters to an element.

| Class | Styles |
| --- | --- |
| `grayscale` | 
`filter: grayscale(100%);`

 |
| `grayscale-<number>` | 

`filter: grayscale(<number>%);`

 |
| `grayscale-(<custom-property>)` | 

`filter: grayscale(var(<custom-property>));`

 |
| `grayscale-[<value>]` | 

`filter: grayscale(<value>);`

 |

Use utilities like `grayscale` and `grayscale-75` to control the amount of grayscale effect applied to an element:

grayscale-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

grayscale-25

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

grayscale-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

grayscale

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="grayscale-0 ..." src="/img/mountains.jpg" /><img class="grayscale-25 ..." src="/img/mountains.jpg" /><img class="grayscale-50 ..." src="/img/mountains.jpg" /><img class="grayscale ..." src="/img/mountains.jpg" />
```

Use the `grayscale-[<value>]` syntax to set the grayscale based on a completely custom value:

```
<img class="grayscale-[0.5] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `grayscale-(<custom-property>)` syntax:

```
<img class="grayscale-(--my-grayscale) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `grayscale-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `filter: grayscale()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="grayscale md:grayscale-0 ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
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
