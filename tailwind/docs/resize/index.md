---
title: "resize"
source: "https://tailwindcss.com/docs/resize"
canonical_url: "https://tailwindcss.com/docs/resize"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:16:11.430Z"
content_hash: "b420b151f94e991b6a5ed884b5f1c77a8658ea03a57eb257ac77cea6b789b5e9"
menu_path: ["resize"]
section_path: []
nav_prev: {"path": "tailwind/docs/pointer-events/index.md", "title": "pointer-events"}
nav_next: {"path": "tailwind/docs/scroll-behavior/index.md", "title": "scroll-behavior"}
---

# resize

Utilities for controlling how an element can be resized.

Class

Styles

`resize-none`

`resize: none;`

`resize`

`resize: both;`

`resize-y`

`resize: vertical;`

`resize-x`

`resize: horizontal;`

## [Examples](#examples)

### [Resizing in all directions](#resizing-in-all-directions)

Use `resize` to make an element horizontally and vertically resizable:

Drag the textarea handle in the demo to see the expected behavior

```
<textarea class="resize rounded-md ..."></textarea>
```

### [Resizing vertically](#resizing-vertically)

Use `resize-y` to make an element vertically resizable:

Drag the textarea handle in the demo to see the expected behavior

```
<textarea class="resize-y rounded-md ..."></textarea>
```

### [Resizing horizontally](#resizing-horizontally)

Use `resize-x` to make an element horizontally resizable:

Drag the textarea handle in the demo to see the expected behavior

```
<textarea class="resize-x rounded-md ..."></textarea>
```

### [Prevent resizing](#prevent-resizing)

Use `resize-none` to prevent an element from being resizable:

Notice that the textarea handle is gone

```
<textarea class="resize-none rounded-md"></textarea>
```

### [Responsive design](#responsive-design)

Prefix a `resize` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="resize-none md:resize ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Resizing in all directions](#resizing-in-all-directions)
    *   [Resizing vertically](#resizing-vertically)
    *   [Resizing horizontally](#resizing-horizontally)
    *   [Prevent resizing](#prevent-resizing)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)


