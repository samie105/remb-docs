---
title: "filter"
source: "https://tailwindcss.com/docs/filter"
canonical_url: "https://tailwindcss.com/docs/filter"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:24:36.416Z"
content_hash: "71f88212b74635631f01ea0eef6bbf35bc98a3baf89fcf6c50af327645c7b710"
menu_path: ["filter"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/mask-type/index.md", "title": "mask-type"}
nav_next: {"path": "tailwind/docs/filter-blur/index.md", "title": "filter: blur()"}
---

# filter

Utilities for applying filters to an element.

| Class | Styles |
| --- | --- |
| `filter-none` | 
`filter: none;`

 |
| `filter-(<custom-property>)` | 

`filter: var(<custom-property>);`

 |
| `filter-[<value>]` | 

`filter: <value>;`

 |

Use utilities like `blur-xs` and `grayscale` to apply filters to an element:

blur-xs

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

grayscale

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

combined

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="blur-xs" src="/img/mountains.jpg" /><img class="grayscale" src="/img/mountains.jpg" /><img class="blur-xs grayscale" src="/img/mountains.jpg" />
```

You can combine the following filter utilities: [blur](../filter-blur/index.md), [brightness](../filter-brightness/index.md), [contrast](../filter-contrast/index.md), [drop-shadow](../filter-drop-shadow/index.md), [grayscale](../filter-grayscale/index.md), [hue-rotate](../filter-hue-rotate/index.md), [invert](../filter-invert/index.md), [saturate](../filter-saturate/index.md), and [sepia](../filter-sepia/index.md).

Use the `filter-none` utility to remove all of the filters applied to an element:

```
<img class="blur-md brightness-150 invert md:filter-none" src="/img/mountains.jpg" />
```

Use the `filter-[<value>]` syntax to set the filter based on a completely custom value:

```
<img class="filter-[url('filters.svg#filter-id')] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `filter-(<custom-property>)` syntax:

```
<img class="filter-(--my-filter) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `filter-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `filter` utility with a variant like `hover:*` to only apply the utility in that state:

```
<img class="blur-sm hover:filter-none ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

Prefix a `filter` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="blur-sm md:filter-none ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Removing filters](#removing-filters)
    -   [Using a custom value](#using-a-custom-value)
    -   [Applying on hover](#applying-on-hover)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
