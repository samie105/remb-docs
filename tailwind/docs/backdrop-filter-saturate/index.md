---
title: "backdrop-filter: saturate()"
source: "https://tailwindcss.com/docs/backdrop-filter-saturate"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-saturate"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:29:48.372Z"
content_hash: "f17f4fc6dfbc321b46287988c59474b90393c78eb0fd25b444bfd583ef4841b3"
menu_path: ["backdrop-filter: saturate()"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Filters
2.  saturate

Filters

# backdrop-filter: saturate()

Utilities for applying backdrop saturation filters to an element.

| Class | Styles |
| --- | --- |
| `backdrop-saturate-<number>` | 
`backdrop-filter: saturate(<number>%);`

 |
| `backdrop-saturate-(<custom-property>)` | 

`backdrop-filter: saturate(var(<custom-property>));`

 |
| `backdrop-saturate-[<value>]` | 

`backdrop-filter: saturate(<value>);`

 |

Use utilities like `backdrop-saturate-50` and `backdrop-saturate-100` utilities to control the saturation of an element's backdrop:

backdrop-saturate-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-saturate-125

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-saturate-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-saturate-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-saturate-125 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-saturate-200 ..."></div></div>
```

Use the `backdrop-saturate-[<value>]` syntax to set the backdrop saturation based on a completely custom value:

```
<div class="backdrop-saturate-[.25] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-saturate-(<custom-property>)` syntax:

```
<div class="backdrop-saturate-(--my-backdrop-saturation) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-saturate-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `backdrop-filter: saturate()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-saturate-50 md:backdrop-saturate-150 ...">  <!-- ... --></div>
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
