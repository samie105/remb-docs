---
title: "outline-offset"
source: "https://tailwindcss.com/docs/outline-offset"
canonical_url: "https://tailwindcss.com/docs/outline-offset"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:20:28.133Z"
content_hash: "918301c50159d2fc08be2e6b2be4cebe691d5a26009a3c60f704d2af8e002767"
menu_path: ["outline-offset"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/outline-style/index.md", "title": "outline-style"}
nav_next: {"path": "tailwind/docs/box-shadow/index.md", "title": "box-shadow"}
---

# outline-offset

Utilities for controlling the offset of an element's outline.

| Class | Styles |
| --- | --- |
| `outline-offset-<number>` | 
`outline-offset: <number>px;`

 |
| `-outline-offset-<number>` | 

`outline-offset: calc(<number>px * -1);`

 |
| `outline-offset-(<custom-property>)` | 

`outline-offset: var(<custom-property>);`

 |
| `outline-offset-[<value>]` | 

`outline-offset: <value>;`

 |

Use utilities like `outline-offset-2` and `outline-offset-4` to change the offset of an element's outline:

outline-offset-0

outline-offset-2

outline-offset-4

```
<button class="outline-2 outline-offset-0 ...">Button A</button><button class="outline-2 outline-offset-2 ...">Button B</button><button class="outline-2 outline-offset-4 ...">Button C</button>
```

Use the `outline-offset-[<value>]` syntax to set the outline offset based on a completely custom value:

```
<div class="outline-offset-[2vw] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `outline-offset-(<custom-property>)` syntax:

```
<div class="outline-offset-(--my-outline-offset) ...">  <!-- ... --></div>
```

This is just a shorthand for `outline-offset-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix an `outline-offset` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="outline md:outline-offset-2 ...">  <!-- ... --></div>
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
