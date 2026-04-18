---
title: "flex"
source: "https://tailwindcss.com/docs/flex"
canonical_url: "https://tailwindcss.com/docs/flex"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:26.758Z"
content_hash: "94d0aa4b4d7d4276370fc60e4f4af18994016feb6f91d4df9ab671b128cdf255"
menu_path: ["flex"]
section_path: []
nav_prev: {"path": "tailwind/docs/flex-wrap/index.md", "title": "flex-wrap"}
nav_next: {"path": "tailwind/docs/flex-grow/index.md", "title": "flex-grow"}
---

# flex

Utilities for controlling how flex items both grow and shrink.

Class

Styles

`flex-<number>`

`flex: <number>;`

`flex-<fraction>`

`flex: calc(<fraction> * 100%);`

`flex-auto`

`flex: auto;`

`flex-initial`

`flex: 0 auto;`

`flex-none`

`flex: none;`

`flex-(<custom-property>)`

`flex: var(<custom-property>);`

`flex-[<value>]`

`flex: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use `flex-<number>` utilities like `flex-1` to allow a flex item to grow and shrink as needed, ignoring its initial size:

01

02

03

```
<div class="flex">  <div class="w-14 flex-none ...">01</div>  <div class="w-64 flex-1 ...">02</div>  <div class="w-32 flex-1 ...">03</div></div>
```

### [Initial](#initial)

Use `flex-initial` to allow a flex item to shrink but not grow, taking into account its initial size:

01

02

03

```
<div class="flex">  <div class="w-14 flex-none ...">01</div>  <div class="w-64 flex-initial ...">02</div>  <div class="w-32 flex-initial ...">03</div></div>
```

### [Auto](#auto)

Use `flex-auto` to allow a flex item to grow and shrink, taking into account its initial size:

01

02

03

```
<div class="flex ...">  <div class="w-14 flex-none ...">01</div>  <div class="w-64 flex-auto ...">02</div>  <div class="w-32 flex-auto ...">03</div></div>
```

### [None](#none)

Use `flex-none` to prevent a flex item from growing or shrinking:

01

02

03

```
<div class="flex ...">  <div class="w-14 flex-none ...">01</div>  <div class="w-32 flex-none ...">02</div>  <div class="flex-1 ...">03</div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `flex-[<value>]` syntax to set the flex shorthand property based on a completely custom value:

```
<div class="flex-[3_1_auto] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `flex-(<custom-property>)` syntax:

```
<div class="flex-(--my-flex) ...">  <!-- ... --></div>
```

This is just a shorthand for `flex-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `flex` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="flex-none md:flex-1 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Initial](#initial)
    *   [Auto](#auto)
    *   [None](#none)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)

