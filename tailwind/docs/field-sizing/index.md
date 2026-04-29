---
title: "field-sizing"
source: "https://tailwindcss.com/docs/field-sizing"
canonical_url: "https://tailwindcss.com/docs/field-sizing"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:37:57.099Z"
content_hash: "f46aa07a1351cbc69e8be1471b27303f435849c0660a120d04946410defa28ed"
menu_path: ["field-sizing"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/cursor/index.md", "title": "cursor"}
nav_next: {"path": "tailwind/docs/pointer-events/index.md", "title": "pointer-events"}
---

# field-sizing

Utilities for controlling the sizing of form controls.

| Class | Styles |
| --- | --- |
| `field-sizing-fixed` | 
`field-sizing: fixed;`

 |
| `field-sizing-content` | 

`field-sizing: content;`

 |

Use the `field-sizing-content` utility to allow a form control to adjust its size based on the content:

Type in the input below to see the size change

Latex Salesman, Vanderlay Industries

```
<textarea class="field-sizing-content ..." rows="2">  Latex Salesman, Vanderlay Industries</textarea>
```

Use the `field-sizing-fixed` utility to make a form control use a fixed size:

Type in the input below to see the size remain the same

Latex Salesman, Vanderlay Industries

```
<textarea class="field-sizing-fixed w-80 ..." rows="2">  Latex Salesman, Vanderlay Industries</textarea>
```

Prefix a `field-sizing` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<input class="field-sizing-content md:field-sizing-fixed ..." />
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Sizing based on content](#sizing-based-on-content)
    -   [Using a fixed size](#using-a-fixed-size)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
