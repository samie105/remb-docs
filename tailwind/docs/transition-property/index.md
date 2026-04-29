---
title: "transition-property"
source: "https://tailwindcss.com/docs/transition-property"
canonical_url: "https://tailwindcss.com/docs/transition-property"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:31:30.954Z"
content_hash: "5af7c16a794a569a07118418c02d50258cd8b8d7fc57b903321d6d9ce3c8f515"
menu_path: ["transition-property"]
section_path: []
content_language: "en"
nav_prev: {"path": "../caption-side/index.md", "title": "caption-side"}
nav_next: {"path": "../transition-behavior/index.md", "title": "transition-behavior"}
---

# transition-property

Utilities for controlling which CSS properties transition.

| Class | Styles |
| --- | --- |
| `transition` | 
`transition-property: color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`

 |
| `transition-all` | 

`transition-property: all; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`

 |
| `transition-colors` | 

`transition-property: color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`

 |
| `transition-opacity` | 

`transition-property: opacity; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`

 |
| `transition-shadow` | 

`transition-property: box-shadow; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`

 |
| `transition-transform` | 

`transition-property: transform, translate, scale, rotate; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`

 |
| `transition-none` | 

`transition-property: none;`

 |
| `transition-(<custom-property>)` | 

`transition-property: var(<custom-property>); transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`

 |
| `transition-[<value>]` | 

`transition-property: <value>; transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */ transition-duration: var(--default-transition-duration); /* 150ms */`

 |

Use utilities like `transition` and `transition-colors` to specify which properties should transition when they change:

Hover the button to see the expected behavior

```
<button class="bg-blue-500 transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 ...">  Save Changes</button>
```

For situations where the user has specified that they prefer reduced motion, you can conditionally apply animations and transitions using the `motion-safe` and `motion-reduce` variants:

```
<button class="transform transition hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none ...">  <!-- ... --></button>
```

Use the `transition-[<value>]` syntax to set the transition properties based on a completely custom value:

```
<button class="transition-[height] ...">  <!-- ... --></button>
```

For CSS variables, you can also use the `transition-(<custom-property>)` syntax:

```
<button class="transition-(--my-properties) ...">  <!-- ... --></button>
```

This is just a shorthand for `transition-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `transition-property` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<button class="transition-none md:transition-all ...">  <!-- ... --></button>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Supporting reduced motion](#supporting-reduced-motion)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
