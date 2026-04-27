---
title: "filter: hue-rotate()"
source: "https://tailwindcss.com/docs/filter-hue-rotate"
canonical_url: "https://tailwindcss.com/docs/filter-hue-rotate"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:26:21.434Z"
content_hash: "0ad29f2ebf7b3df9d2f602772b477f5997fbe71494a2379c94c3742a43561e13"
menu_path: ["filter: hue-rotate()"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Filters
2.  hue-rotate

Filters

# filter: hue-rotate()

Utilities for applying hue-rotate filters to an element.

| Class | Styles |
| --- | --- |
| `hue-rotate-<number>` | 
`filter: hue-rotate(<number>deg);`

 |
| `-hue-rotate-<number>` | 

`filter: hue-rotate(calc(<number>deg * -1));`

 |
| `hue-rotate-(<custom-property>)` | 

`filter: hue-rotate(var(<custom-property>));`

 |
| `hue-rotate-[<value>]` | 

`filter: hue-rotate(<value>);`

 |

Use utilities like `hue-rotate-90` and `hue-rotate-180` to rotate the hue of an element by degrees:

hue-rotate-15

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

hue-rotate-90

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

hue-rotate-180

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

hue-rotate-270

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="hue-rotate-15" src="/img/mountains.jpg" /><img class="hue-rotate-90" src="/img/mountains.jpg" /><img class="hue-rotate-180" src="/img/mountains.jpg" /><img class="hue-rotate-270" src="/img/mountains.jpg" />
```

Use utilities like `-hue-rotate-15` and `-hue-rotate-45` to set a negative hue rotate value:

\-hue-rotate-15

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

\-hue-rotate-45

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

\-hue-rotate-90

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="-hue-rotate-15" src="/img/mountains.jpg" /><img class="-hue-rotate-45" src="/img/mountains.jpg" /><img class="-hue-rotate-90" src="/img/mountains.jpg" />
```

Use the `hue-rotate-[<value>]` syntax to set the hue rotation based on a completely custom value:

```
<img class="hue-rotate-[3.142rad] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `hue-rotate-(<custom-property>)` syntax:

```
<img class="hue-rotate-(--my-hue-rotate) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `hue-rotate-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `filter: hue-rotate()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="hue-rotate-60 md:hue-rotate-0 ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using negative values](#using-negative-values)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
