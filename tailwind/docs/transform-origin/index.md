---
title: "transform-origin"
source: "https://tailwindcss.com/docs/transform-origin"
canonical_url: "https://tailwindcss.com/docs/transform-origin"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:35:35.796Z"
content_hash: "31984e1822d12fb4b9f03beef4fcad981fcbd0cd8aa7a671185f8d489cd81a4f"
menu_path: ["transform-origin"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Transforms
2.  transform-origin

Transforms

# transform-origin

Utilities for specifying the origin for an element's transformations.

| Class | Styles |
| --- | --- |
| `origin-center` | 
`transform-origin: center;`

 |
| `origin-top` | 

`transform-origin: top;`

 |
| `origin-top-right` | 

`transform-origin: top right;`

 |
| `origin-right` | 

`transform-origin: right;`

 |
| `origin-bottom-right` | 

`transform-origin: bottom right;`

 |
| `origin-bottom` | 

`transform-origin: bottom;`

 |
| `origin-bottom-left` | 

`transform-origin: bottom left;`

 |
| `origin-left` | 

`transform-origin: left;`

 |
| `origin-top-left` | 

`transform-origin: top left;`

 |
| `origin-(<custom-property>)` | 

`transform-origin: var(<custom-property>);`

 |
| `origin-[<value>]` | 

`transform-origin: <value>;`

 |

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

Use the `origin-[<value>]` syntax to set the transform origin based on a completely custom value:

```
<img class="origin-[33%_75%] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `origin-(<custom-property>)` syntax:

```
<img class="origin-(--my-transform-origin) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `origin-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `transform-origin` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="origin-center md:origin-top ..." src="/img/mountains.jpg" />
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
