---
title: "backdrop-filter: contrast()"
source: "https://tailwindcss.com/docs/backdrop-filter-contrast"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-contrast"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:28:36.831Z"
content_hash: "681b7917d297f5e27c36fff1c1d30b0e4c37d8f360fcb8d58d14a13738c0b257"
menu_path: ["backdrop-filter: contrast()"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Filters
2.  contrast

Filters

# backdrop-filter: contrast()

Utilities for applying backdrop contrast filters to an element.

| Class | Styles |
| --- | --- |
| `backdrop-contrast-<number>` | 
`backdrop-filter: contrast(<number>%);`

 |
| `backdrop-contrast-(<custom-property>)` | 

`backdrop-filter: contrast(var(<custom-property>));`

 |
| `backdrop-contrast-[<value>]` | 

`backdrop-filter: contrast(<value>);`

 |

Use utilities like `backdrop-contrast-50` and `backdrop-contrast-100` to control an element's backdrop contrast:

backdrop-contrast-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

backdrop-contrast-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-contrast-50 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-contrast-200 ..."></div></div>
```

Use the `backdrop-contrast-[<value>]` syntax to set the backdrop contrast based on a completely custom value:

```
<div class="backdrop-contrast-[.25] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-contrast-(<custom-property>)` syntax:

```
<div class="backdrop-contrast-(--my-backdrop-contrast) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-contrast-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `backdrop-filter: contrast()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-contrast-125 md:backdrop-contrast-150 ...">  <!-- ... --></div>
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
