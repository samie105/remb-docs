---
title: "flex-shrink"
source: "https://tailwindcss.com/docs/flex-shrink"
canonical_url: "https://tailwindcss.com/docs/flex-shrink"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:28.054Z"
content_hash: "5a1ec35301e44be23bd83d85206009b823cad8408992b9b82dcb76ceda0ef68b"
menu_path: ["flex-shrink"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  flex-shrink

Flexbox & Grid

# flex-shrink

Utilities for controlling how flex items shrink.

Class

Styles

`shrink`

`flex-shrink: 1;`

`shrink-<number>`

`flex-shrink: <number>;`

`shrink-[<value>]`

`flex-shrink: <value>;`

`shrink-(<custom-property>)`

`flex-shrink: var(<custom-property>);`

## [Examples](#examples)

### [Allowing flex items to shrink](#allowing-flex-items-to-shrink)

Use `shrink` to allow a flex item to shrink if needed:

01

02

03

```
<div class="flex ...">  <div class="h-14 w-14 flex-none ...">01</div>  <div class="h-14 w-64 shrink ...">02</div>  <div class="h-14 w-14 flex-none ...">03</div></div>
```

### [Preventing items from shrinking](#preventing-items-from-shrinking)

Use `shrink-0` to prevent a flex item from shrinking:

01

02

03

```
<div class="flex ...">  <div class="h-16 flex-1 ...">01</div>  <div class="h-16 w-32 shrink-0 ...">02</div>  <div class="h-16 flex-1 ...">03</div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `shrink-[<value>]` syntax to set the flex shrink factor based on a completely custom value:

```
<div class="shrink-[calc(100vw-var(--sidebar))] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `shrink-(<custom-property>)` syntax:

```
<div class="shrink-(--my-shrink) ...">  <!-- ... --></div>
```

This is just a shorthand for `shrink-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `flex-shrink` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="shrink md:shrink-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Allowing flex items to shrink](#allowing-flex-items-to-shrink)
    *   [Preventing items from shrinking](#preventing-items-from-shrinking)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
