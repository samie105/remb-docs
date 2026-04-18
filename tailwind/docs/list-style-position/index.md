---
title: "list-style-position"
source: "https://tailwindcss.com/docs/list-style-position"
canonical_url: "https://tailwindcss.com/docs/list-style-position"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:39.976Z"
content_hash: "a8ab6948d17a96c4d5d2663e2bc55dbfd546655e4f54d8f64ce8d6ad205e74d0"
menu_path: ["list-style-position"]
section_path: []
nav_prev: {"path": "tailwind/docs/list-style-image/index.md", "title": "list-style-image"}
nav_next: {"path": "tailwind/docs/list-style-type/index.md", "title": "list-style-type"}
---

# list-style-position

Utilities for controlling the position of bullets and numbers in lists.

Class

Styles

`list-inside`

`list-style-position: inside;`

`list-outside`

`list-style-position: outside;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `list-inside` and `list-outside` to control the position of the markers and text indentation in a list:

list-inside

*   5 cups chopped Porcini mushrooms
*   1/2 cup of olive oil
*   3lb of celery

list-outside

*   5 cups chopped Porcini mushrooms
*   1/2 cup of olive oil
*   3lb of celery

```
<ul class="list-inside">  <li>5 cups chopped Porcini mushrooms</li>  <!-- ... --></ul><ul class="list-outside">  <li>5 cups chopped Porcini mushrooms</li>  <!-- ... --></ul>
```

### [Responsive design](#responsive-design)

Prefix a `list-style-position` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<ul class="list-outside md:list-inside ...">  <!-- ... --></ul>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)


