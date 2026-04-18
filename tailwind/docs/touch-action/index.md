---
title: "touch-action"
source: "https://tailwindcss.com/docs/touch-action"
canonical_url: "https://tailwindcss.com/docs/touch-action"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:17:55.196Z"
content_hash: "3d73867504476035685f1c4057613f65109c9070553c3ae60ce9ffb534bbed9e"
menu_path: ["touch-action"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Interactivity
2.  touch-action

Interactivity

# touch-action

Utilities for controlling how an element can be scrolled and zoomed on touchscreens.

Class

Styles

`touch-auto`

`touch-action: auto;`

`touch-none`

`touch-action: none;`

`touch-pan-x`

`touch-action: pan-x;`

`touch-pan-left`

`touch-action: pan-left;`

`touch-pan-right`

`touch-action: pan-right;`

`touch-pan-y`

`touch-action: pan-y;`

`touch-pan-up`

`touch-action: pan-up;`

`touch-pan-down`

`touch-action: pan-down;`

`touch-pinch-zoom`

`touch-action: pinch-zoom;`

`touch-manipulation`

`touch-action: manipulation;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `touch-pan-y` and `touch-pinch-zoom` to control how an element can be scrolled (panned) and zoomed (pinched) on touchscreens:

Try panning these images on a touchscreen

touch-auto

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80)

touch-none

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80)

touch-pan-x

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80)

touch-pan-y

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=400&q=80)

```
<div class="h-48 w-full touch-auto overflow-auto ...">  <img class="h-auto w-[150%] max-w-none" src="..." /></div><div class="h-48 w-full touch-none overflow-auto ...">  <img class="h-auto w-[150%] max-w-none" src="..." /></div><div class="h-48 w-full touch-pan-x overflow-auto ...">  <img class="h-auto w-[150%] max-w-none" src="..." /></div><div class="h-48 w-full touch-pan-y overflow-auto ...">  <img class="h-auto w-[150%] max-w-none" src="..." /></div>
```

### [Responsive design](#responsive-design)

Prefix a `touch-action` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="touch-pan-x md:touch-auto ...">  <!-- ... --></div>
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
