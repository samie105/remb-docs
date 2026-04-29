---
title: "isolation"
source: "https://tailwindcss.com/docs/isolation"
canonical_url: "https://tailwindcss.com/docs/isolation"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:53:22.157Z"
content_hash: "cee47cf25eab482a913bda5bf3a4f5119944ecafcfdbbf74ed29b1d604ee2df8"
menu_path: ["isolation"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/clear/index.md", "title": "clear"}
nav_next: {"path": "tailwind/docs/object-fit/index.md", "title": "object-fit"}
---

# isolation

Utilities for controlling whether an element should explicitly create a new stacking context.

| Class | Styles |
| --- | --- |
| `isolate` | 
`isolation: isolate;`

 |
| `isolation-auto` | 

`isolation: auto;`

 |

Use the `isolate` and `isolation-auto` utilities to control whether an element should explicitly create a new stacking context:

```
<div class="isolate ...">  <!-- ... --></div>
```

Prefix an `isolation` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="isolate md:isolation-auto ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
