---
title: "flex-grow"
source: "https://tailwindcss.com/docs/flex-grow"
canonical_url: "https://tailwindcss.com/docs/flex-grow"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:29.432Z"
content_hash: "f4b4af9dd64f845eef18259a23ddd5aebfa67d54147b73449bc54850d167c0a2"
menu_path: ["flex-grow"]
section_path: []
nav_prev: {"path": "tailwind/docs/flex/index.md", "title": "flex"}
nav_next: {"path": "tailwind/docs/flex-shrink/index.md", "title": "flex-shrink"}
---

# flex-grow

Utilities for controlling how flex items grow.

Class

Styles

`grow`

`flex-grow: 1;`

`grow-<number>`

`flex-grow: <number>;`

`grow-[<value>]`

`flex-grow: <value>;`

`grow-(<custom-property>)`

`flex-grow: var(<custom-property>);`

## [Examples](#examples)

### [Allowing items to grow](#allowing-items-to-grow)

Use `grow` to allow a flex item to grow to fill any available space:

01

02

03

```
<div class="flex ...">  <div class="size-14 flex-none ...">01</div>  <div class="size-14 grow ...">02</div>  <div class="size-14 flex-none ...">03</div></div>
```

### [Growing items based on factor](#growing-items-based-on-factor)

Use `grow-<number>` utilities like `grow-3` to make flex items grow proportionally based on their growth factor, allowing them to fill the available space relative to each other:

01

02

03

```
<div class="flex ...">  <div class="size-14 grow-3 ...">01</div>  <div class="size-14 grow-7 ...">02</div>  <div class="size-14 grow-3 ...">03</div></div>
```

### [Preventing items from growing](#preventing-items-from-growing)

Use `grow-0` to prevent a flex item from growing:

01

02

03

```
<div class="flex ...">  <div class="size-14 grow ...">01</div>  <div class="size-14 grow-0 ...">02</div>  <div class="size-14 grow ...">03</div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `grow-[<value>]` syntax to set the flex grow factor based on a completely custom value:

```
<div class="grow-[25vw] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `grow-(<custom-property>)` syntax:

```
<div class="grow-(--my-grow) ...">  <!-- ... --></div>
```

This is just a shorthand for `grow-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `flex-grow` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grow md:grow-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Allowing items to grow](#allowing-items-to-grow)
    *   [Growing items based on factor](#growing-items-based-on-factor)
    *   [Preventing items from growing](#preventing-items-from-growing)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
