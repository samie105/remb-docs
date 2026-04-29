---
title: "list-style-type"
source: "https://tailwindcss.com/docs/list-style-type"
canonical_url: "https://tailwindcss.com/docs/list-style-type"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:10:31.887Z"
content_hash: "54d63c312cf565c2f89daf47d97b7aad825777b2cc3bcf03b7b7372f0b740bcf"
menu_path: ["list-style-type"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/list-style-position/index.md", "title": "list-style-position"}
nav_next: {"path": "tailwind/docs/text-align/index.md", "title": "text-align"}
---

# list-style-type

Utilities for controlling the marker style of a list.

| Class | Styles |
| --- | --- |
| `list-disc` | 
`list-style-type: disc;`

 |
| `list-decimal` | 

`list-style-type: decimal;`

 |
| `list-none` | 

`list-style-type: none;`

 |
| `list-(<custom-property>)` | 

`list-style-type: var(<custom-property>);`

 |
| `list-[<value>]` | 

`list-style-type: <value>;`

 |

Use utilities like `list-disc` and `list-decimal` to control the style of the markers in a list:

list-disc

-   Now this is a story all about how, my life got flipped-turned upside down
-   And I'd like to take a minute just sit right there
-   I'll tell you how I became the prince of a town called Bel-Air

list-decimal

-   Now this is a story all about how, my life got flipped-turned upside down
-   And I'd like to take a minute just sit right there
-   I'll tell you how I became the prince of a town called Bel-Air

list-none

-   Now this is a story all about how, my life got flipped-turned upside down
-   And I'd like to take a minute just sit right there
-   I'll tell you how I became the prince of a town called Bel-Air

```
<ul class="list-disc">  <li>Now this is a story all about how, my life got flipped-turned upside down</li>  <!-- ... --></ul><ol class="list-decimal">  <li>Now this is a story all about how, my life got flipped-turned upside down</li>  <!-- ... --></ol><ul class="list-none">  <li>Now this is a story all about how, my life got flipped-turned upside down</li>  <!-- ... --></ul>
```

Use the `list-[<value>]` syntax to set the marker based on a completely custom value:

```
<ol class="list-[upper-roman] ...">  <!-- ... --></ol>
```

For CSS variables, you can also use the `list-(<custom-property>)` syntax:

```
<ol class="list-(--my-marker) ...">  <!-- ... --></ol>
```

This is just a shorthand for `list-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `list-style-type` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<ul class="list-none md:list-disc ...">  <!-- ... --></ul>
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
