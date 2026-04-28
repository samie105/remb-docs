---
title: "border-style"
source: "https://tailwindcss.com/docs/border-style"
canonical_url: "https://tailwindcss.com/docs/border-style"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:19:17.865Z"
content_hash: "1b45d5e896fece20c6941b2dee32a9b1a967c9b8178d943babf51fb3f2ba72d9"
menu_path: ["border-style"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/border-color/index.md", "title": "border-color"}
nav_next: {"path": "tailwind/docs/outline-width/index.md", "title": "outline-width"}
---

# border-style

Utilities for controlling the style of an element's borders.

| Class | Styles |
| --- | --- |
| `border-solid` | 
`border-style: solid;`

 |
| `border-dashed` | 

`border-style: dashed;`

 |
| `border-dotted` | 

`border-style: dotted;`

 |
| `border-double` | 

`border-style: double;`

 |
| `border-hidden` | 

`border-style: hidden;`

 |
| `border-none` | 

`border-style: none;`

 |
| `divide-solid` | 

`& > :not(:last-child) { border-style: solid; }`

 |
| `divide-dashed` | 

`& > :not(:last-child) { border-style: dashed; }`

 |
| `divide-dotted` | 

`& > :not(:last-child) { border-style: dotted; }`

 |
| `divide-double` | 

`& > :not(:last-child) { border-style: double; }`

 |
| `divide-hidden` | 

`& > :not(:last-child) { border-style: hidden; }`

 |
| `divide-none` | 

`& > :not(:last-child) { border-style: none; }`

 |

Use utilities like `border-solid` and `border-dotted` to control an element's border style:

border-solid

border-dashed

border-dotted

border-double

```
<div class="border-2 border-solid ..."></div><div class="border-2 border-dashed ..."></div><div class="border-2 border-dotted ..."></div><div class="border-4 border-double ..."></div>
```

Use the `border-none` utility to remove an existing border from an element:

```
<button class="border-none ...">Save Changes</button>
```

This is most commonly used to remove a border style that was applied at a smaller breakpoint.

Use utilities like `divide-dashed` and `divide-dotted` to control the border style between child elements:

01

02

03

```
<div class="grid grid-cols-3 divide-x-3 divide-dashed divide-indigo-500">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Prefix a `border-style` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="border-solid md:border-dotted ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Removing a border](#removing-a-border)
    -   [Setting the divider style](#setting-the-divider-style)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
