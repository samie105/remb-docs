---
title: "aspect-ratio"
source: "https://tailwindcss.com/docs/aspect-ratio"
canonical_url: "https://tailwindcss.com/docs/aspect-ratio"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:50:32.011Z"
content_hash: "7e501b09ce3b10f2792b05a74cb60a9a75001990861d003e2c26b63b94bd4bfd"
menu_path: ["aspect-ratio"]
section_path: []
content_language: "en"
nav_prev: {"path": "../preflight/index.md", "title": "Preflight"}
nav_next: {"path": "../columns/index.md", "title": "columns"}
---

# aspect-ratio

Utilities for controlling the aspect ratio of an element.

| Class | Styles |
| --- | --- |
| `aspect-<ratio>` | 
`aspect-ratio: <ratio>;`

 |
| `aspect-square` | 

`aspect-ratio: 1 / 1;`

 |
| `aspect-video` | 

`aspect-ratio: var(--aspect-video); /* 16 / 9 */`

 |
| `aspect-auto` | 

`aspect-ratio: auto;`

 |
| `aspect-(<custom-property>)` | 

`aspect-ratio: var(<custom-property>);`

 |
| `aspect-[<value>]` | 

`aspect-ratio: <value>;`

 |

Use `aspect-<ratio>` utilities like `aspect-3/2` to give an element a specific aspect ratio:

Resize the example to see the expected behavior

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1200&q=80)

```
<img class="aspect-3/2 object-cover ..." src="/img/villas.jpg" />
```

Use the `aspect-video` utility to give a video element a 16 / 9 aspect ratio:

Resize the example to see the expected behavior

```
<iframe class="aspect-video ..." src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

Use the `aspect-[<value>]` syntax to set the aspect ratio based on a completely custom value:

```
<img class="aspect-[calc(4*3+1)/3] ..." src="/img/villas.jpg" />
```

For CSS variables, you can also use the `aspect-(<custom-property>)` syntax:

```
<img class="aspect-(--my-aspect-ratio) ..." src="/img/villas.jpg" />
```

This is just a shorthand for `aspect-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix an `aspect-ratio` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<iframe class="aspect-video md:aspect-square ..." src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

Use the `--aspect-*` theme variables to customize the aspect ratio utilities in your project:

```
@theme {  --aspect-retro: 4 / 3; }
```

Now the `aspect-retro` utility can be used in your markup:

```
<iframe class="aspect-retro" src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

Learn more about customizing your theme in the [theme documentation](/docs/theme#customizing-your-theme).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a video aspect ratio](#using-a-video-aspect-ratio)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)
-   [Customizing your theme](#customizing-your-theme)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
