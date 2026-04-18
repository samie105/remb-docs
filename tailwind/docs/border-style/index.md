---
title: "border-style"
source: "https://tailwindcss.com/docs/border-style"
canonical_url: "https://tailwindcss.com/docs/border-style"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:49.797Z"
content_hash: "35f91d1288619279dc20b95567d8ba238981c8e6af8998625b5d8932fa016752"
menu_path: ["border-style"]
section_path: []
nav_prev: {"path": "tailwind/docs/border-color/index.md", "title": "border-color"}
nav_next: {"path": "tailwind/docs/outline-width/index.md", "title": "outline-width"}
---

# border-style

Utilities for controlling the style of an element's borders.

Class

Styles

`border-solid`

`border-style: solid;`

`border-dashed`

`border-style: dashed;`

`border-dotted`

`border-style: dotted;`

`border-double`

`border-style: double;`

`border-hidden`

`border-style: hidden;`

`border-none`

`border-style: none;`

`divide-solid`

`& > :not(:last-child) { border-style: solid; }`

`divide-dashed`

`& > :not(:last-child) { border-style: dashed; }`

`divide-dotted`

`& > :not(:last-child) { border-style: dotted; }`

`divide-double`

`& > :not(:last-child) { border-style: double; }`

`divide-hidden`

`& > :not(:last-child) { border-style: hidden; }`

`divide-none`

`& > :not(:last-child) { border-style: none; }`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `border-solid` and `border-dotted` to control an element's border style:

border-solid

border-dashed

border-dotted

border-double

```
<div class="border-2 border-solid ..."></div><div class="border-2 border-dashed ..."></div><div class="border-2 border-dotted ..."></div><div class="border-4 border-double ..."></div>
```

### [Removing a border](#removing-a-border)

Use the `border-none` utility to remove an existing border from an element:

```
<button class="border-none ...">Save Changes</button>
```

This is most commonly used to remove a border style that was applied at a smaller breakpoint.

### [Setting the divider style](#setting-the-divider-style)

Use utilities like `divide-dashed` and `divide-dotted` to control the border style between child elements:

01

02

03

```
<div class="grid grid-cols-3 divide-x-3 divide-dashed divide-indigo-500">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Responsive design](#responsive-design)

Prefix a `border-style` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="border-solid md:border-dotted ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Removing a border](#removing-a-border)
    *   [Setting the divider style](#setting-the-divider-style)
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
