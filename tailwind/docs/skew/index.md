---
title: "skew"
source: "https://tailwindcss.com/docs/skew"
canonical_url: "https://tailwindcss.com/docs/skew"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:13:47.193Z"
content_hash: "89032970a7d325abb117b36e4a8e8d3f33765ccde41c114ab4e6ce178b9bbdf7"
menu_path: ["skew"]
section_path: []
nav_prev: {"path": "tailwind/docs/scale/index.md", "title": "scale"}
nav_next: {"path": "tailwind/docs/transform/index.md", "title": "transform"}
---

# skew

Utilities for skewing elements with transform.

Class

Styles

`skew-<number>`

`transform: skewX(<number>deg) skewY(<number>deg);`

`-skew-<number>`

`transform: skewX(-<number>deg) skewY(-<number>deg);`

`skew-(<custom-property>)`

`transform: skewX(var(<custom-property>)) skewY(var(<custom-property>));`

`skew-[<value>]`

`transform: skewX(<value>) skewY(<value>);`

`skew-x-<number>`

`transform: skewX(<number>deg));`

`-skew-x-<number>`

`transform: skewX(-<number>deg));`

`skew-x-(<custom-property>)`

`transform: skewX(var(<custom-property>));`

`skew-x-[<value>]`

`transform: skewX(<value>));`

`skew-y-<number>`

`transform: skewY(<number>deg);`

`-skew-y-<number>`

`transform: skewY(-<number>deg);`

`skew-y-(<custom-property>)`

`transform: skewY(var(<custom-property>));`

`skew-y-[<value>]`

`transform: skewY(<value>);`

## [Examples](#examples)

### [Basic example](#basic-example)

Use `skew-<number>` utilities like `skew-4` and `skew-10` to skew an element on both axes:

skew-3

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

skew-6

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

skew-12

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="skew-3 ..." src="/img/mountains.jpg" /><img class="skew-6 ..." src="/img/mountains.jpg" /><img class="skew-12 ..." src="/img/mountains.jpg" />
```

### [Using negative values](#using-negative-values)

Use `-skew-<number>` utilities like `-skew-4` and `-skew-10` to skew an element on both axes:

\-skew-3

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

\-skew-6

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

\-skew-12

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="-skew-3 ..." src="/img/mountains.jpg" /><img class="-skew-6 ..." src="/img/mountains.jpg" /><img class="-skew-12 ..." src="/img/mountains.jpg" />
```

### [Skewing on the x-axis](#skewing-on-the-x-axis)

Use `skew-x-<number>` utilities like `skew-x-4` and `-skew-x-10` to skew an element on the x-axis:

\-skew-x-12

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

skew-x-6

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

skew-x-12

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="-skew-x-12 ..." src="/img/mountains.jpg" /><img class="skew-x-6 ..." src="/img/mountains.jpg" /><img class="skew-x-12 ..." src="/img/mountains.jpg" />
```

### [Skewing on the y-axis](#skewing-on-the-y-axis)

Use `skew-y-<number>` utilities like `skew-y-4` and `-skew-y-10` to skew an element on the y-axis:

\-skew-y-12

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

skew-y-6

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

skew-y-12

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="-skew-y-12 ..." src="/img/mountains.jpg" /><img class="skew-y-6 ..." src="/img/mountains.jpg" /><img class="skew-y-12 ..." src="/img/mountains.jpg" />
```

### [Using a custom value](#using-a-custom-value)

Use the `skew-[<value>]` syntax to set the skew based on a completely custom value:

```
<img class="skew-[3.142rad] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `skew-(<custom-property>)` syntax:

```
<img class="skew-(--my-skew) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `skew-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix `skewX()` and `skewY()` utilities with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="skew-3 md:skew-12 ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Using negative values](#using-negative-values)
    *   [Skewing on the x-axis](#skewing-on-the-x-axis)
    *   [Skewing on the y-axis](#skewing-on-the-y-axis)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
