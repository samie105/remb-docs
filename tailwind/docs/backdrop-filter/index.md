---
title: "backdrop-filter"
source: "https://tailwindcss.com/docs/backdrop-filter"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:27:30.328Z"
content_hash: "614841a8001d74593d135a3958be006782038ab478798eb617ec04aa021cd0cb"
menu_path: ["backdrop-filter"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Filters
2.  backdrop-filter

Filters

# backdrop-filter

Utilities for applying backdrop filters to an element.

| Class | Styles |
| --- | --- |
| `backdrop-filter-none` | 
`backdrop-filter: none;`

 |
| `backdrop-filter-(<custom-property>)` | 

`backdrop-filter: var(<custom-property>);`

 |
| `backdrop-filter-[<value>]` | 

`backdrop-filter: <value>;`

 |

Use utilities like `backdrop-blur-xs` and `backdrop-grayscale` to apply filters to an element's backdrop:

backdrop-blur-xs

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-grayscale

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

combined

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-blur-xs ..."></div></div><div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-grayscale ..."></div></div><div class="bg-[url(/img/mountains.jpg)] ...">  <div class="backdrop-blur-xs backdrop-grayscale ..."></div></div>
```

You can combine the following backdrop filter utilities: [blur](/docs/backdrop-filter-blur), [brightness](/docs/backdrop-filter-brightness), [contrast](/docs/backdrop-filter-contrast), [grayscale](/docs/backdrop-filter-grayscale), [hue-rotate](/docs/backdrop-filter-hue-rotate), [invert](/docs/backdrop-filter-invert), [opacity](/docs/backdrop-filter-opacity), [saturate](/docs/backdrop-filter-saturate), and [sepia](/docs/backdrop-filter-sepia).

Use the `backdrop-filter-none` utility to remove all of the backdrop filters applied to an element:

```
<div class="backdrop-blur-md backdrop-brightness-150 md:backdrop-filter-none"></div>
```

Use the `backdrop-filter-[<value>]` syntax to set the backdrop filter based on a completely custom value:

```
<div class="backdrop-filter-[url('filters.svg#filter-id')] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-filter-(<custom-property>)` syntax:

```
<div class="backdrop-filter-(--my-backdrop-filter) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-filter-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `backdrop-filter` utility with a variant like `hover:*` to only apply the utility in that state:

```
<div class="backdrop-blur-sm hover:backdrop-filter-none ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

Prefix a `backdrop-filter` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-blur-sm md:backdrop-filter-none ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Removing filters](#removing-filters)
    -   [Using a custom value](#using-a-custom-value)
    -   [Applying on hover](#applying-on-hover)
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
