---
title: "filter: brightness()"
source: "https://tailwindcss.com/docs/filter-brightness"
canonical_url: "https://tailwindcss.com/docs/filter-brightness"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:25:11.197Z"
content_hash: "90a3a27b36bcc89ad82eb45eb381b1120e2125af632fb92e88fbc3b97a732fbf"
menu_path: ["filter: brightness()"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/filter-blur/index.md", "title": "filter: blur()"}
nav_next: {"path": "tailwind/docs/filter-contrast/index.md", "title": "filter: contrast()"}
---

# filter: brightness()

Utilities for applying brightness filters to an element.

| Class | Styles |
| --- | --- |
| `brightness-<number>` | 
`filter: brightness(<number>%);`

 |
| `brightness-(<custom-property>)` | 

`filter: brightness(var(<custom-property>));`

 |
| `brightness-[<value>]` | 

`filter: brightness(<value>);`

 |

Use utilities like `brightness-50` and `brightness-100` to control an element's brightness:

brightness-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

brightness-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

brightness-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

brightness-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="brightness-50 ..." src="/img/mountains.jpg" /><img class="brightness-100 ..." src="/img/mountains.jpg" /><img class="brightness-125 ..." src="/img/mountains.jpg" /><img class="brightness-200 ..." src="/img/mountains.jpg" />
```

Use the `brightness-[<value>]` syntax to set the brightness based on a completely custom value:

```
<img class="brightness-[1.75] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `brightness-(<custom-property>)` syntax:

```
<img class="brightness-(--my-brightness) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `brightness-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `filter: brightness()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="brightness-110 md:brightness-150 ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

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
