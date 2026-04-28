---
title: "text-decoration-thickness"
source: "https://tailwindcss.com/docs/text-decoration-thickness"
canonical_url: "https://tailwindcss.com/docs/text-decoration-thickness"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:12:15.470Z"
content_hash: "19f350f88c1dec6b402f6fd5c3da62c4a114b1ec3728d918ca5008274e4d7369"
menu_path: ["text-decoration-thickness"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/text-decoration-style/index.md", "title": "text-decoration-style"}
nav_next: {"path": "tailwind/docs/text-underline-offset/index.md", "title": "text-underline-offset"}
---

# text-decoration-thickness

Utilities for controlling the thickness of text decorations.

| Class | Styles |
| --- | --- |
| `decoration-<number>` | 
`text-decoration-thickness: <number>px;`

 |
| `decoration-from-font` | 

`text-decoration-thickness: from-font;`

 |
| `decoration-auto` | 

`text-decoration-thickness: auto;`

 |
| `decoration-(length:<custom-property>)` | 

`text-decoration-thickness: var(<custom-property>);`

 |
| `decoration-[<value>]` | 

`text-decoration-thickness: <value>;`

 |

Use `decoration-<number>` utilities like `decoration-2` and `decoration-4` to change the [text decoration](/docs/text-decoration-line) thickness of an element:

decoration-1

The quick brown fox jumps over the lazy dog.

decoration-2

The quick brown fox jumps over the lazy dog.

decoration-4

The quick brown fox jumps over the lazy dog.

```
<p class="underline decoration-1">The quick brown fox...</p><p class="underline decoration-2">The quick brown fox...</p><p class="underline decoration-4">The quick brown fox...</p>
```

Use the `decoration-[<value>]` syntax to set the text decoration thickness based on a completely custom value:

```
<p class="decoration-[0.25rem] ...">  Lorem ipsum dolor sit amet...</p>
```

For CSS variables, you can also use the `decoration-(length:<custom-property>)` syntax:

```
<p class="decoration-(length:--my-decoration-thickness) ...">  Lorem ipsum dolor sit amet...</p>
```

This is just a shorthand for `decoration-[length:var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `text-decoration-thickness` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="underline md:decoration-4 ...">  Lorem ipsum dolor sit amet...</p>
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
