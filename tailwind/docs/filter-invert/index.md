---
title: "filter: invert()"
source: "https://tailwindcss.com/docs/filter-invert"
canonical_url: "https://tailwindcss.com/docs/filter-invert"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:26:53.060Z"
content_hash: "ddd2630a265cab2bc7b7822ba194fe6cb536edc98630ee68b3fd92e6e7f89d98"
menu_path: ["filter: invert()"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Filters
2.  invert

Filters

# filter: invert()

Utilities for applying invert filters to an element.

| Class | Styles |
| --- | --- |
| `invert` | 
`filter: invert(100%);`

 |
| `invert-<number>` | 

`filter: invert(<number>%);`

 |
| `invert-(<custom-property>)` | 

`filter: invert(var(<custom-property>));`

 |
| `invert-[<value>]` | 

`filter: invert(<value>);`

 |

Use utilities like `invert` and `invert-20` to control the color inversion of an element:

invert-0

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

invert-20

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

invert

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="invert-0" src="/img/mountains.jpg" /><img class="invert-20" src="/img/mountains.jpg" /><img class="invert" src="/img/mountains.jpg" />
```

Use the `invert-[<value>]` syntax to set the color inversion based on a completely custom value:

```
<img class="invert-[.25] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `invert-(<custom-property>)` syntax:

```
<img class="invert-(--my-inversion) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `invert-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `filter: invert()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="invert md:invert-0 ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
