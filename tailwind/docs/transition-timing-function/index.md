---
title: "transition-timing-function"
source: "https://tailwindcss.com/docs/transition-timing-function"
canonical_url: "https://tailwindcss.com/docs/transition-timing-function"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:32:40.577Z"
content_hash: "932a94f71d6d6713355f3890820059e1c2b7e02124cec86bfb1063fc410480ac"
menu_path: ["transition-timing-function"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/transition-duration/index.md", "title": "transition-duration"}
nav_next: {"path": "tailwind/docs/transition-delay/index.md", "title": "transition-delay"}
---

# transition-timing-function

Utilities for controlling the easing of CSS transitions.

| Class | Styles |
| --- | --- |
| `ease-linear` | 
`transition-timing-function: linear;`

 |
| `ease-in` | 

`transition-timing-function: var(--ease-in); /* cubic-bezier(0.4, 0, 1, 1) */`

 |
| `ease-out` | 

`transition-timing-function: var(--ease-out); /* cubic-bezier(0, 0, 0.2, 1) */`

 |
| `ease-in-out` | 

`transition-timing-function: var(--ease-in-out); /* cubic-bezier(0.4, 0, 0.2, 1) */`

 |
| `ease-initial` | 

`transition-timing-function: initial;`

 |
| `ease-(<custom-property>)` | 

`transition-timing-function: var(<custom-property>);`

 |
| `ease-[<value>]` | 

`transition-timing-function: <value>;`

 |

Use utilities like `ease-in` and `ease-out` to control the easing curve of an element's transition:

Hover each button to see the expected behavior

ease-in

ease-out

ease-in-out

```
<button class="duration-300 ease-in ...">Button A</button><button class="duration-300 ease-out ...">Button B</button><button class="duration-300 ease-in-out ...">Button C</button>
```

Use the `ease-[<value>]` syntax to set the transition timing function based on a completely custom value:

```
<button class="ease-[cubic-bezier(0.95,0.05,0.795,0.035)] ...">  <!-- ... --></button>
```

For CSS variables, you can also use the `ease-(<custom-property>)` syntax:

```
<button class="ease-(--my-ease) ...">  <!-- ... --></button>
```

This is just a shorthand for `ease-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `transition-timing-function` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<button class="ease-out md:ease-in ...">  <!-- ... --></button>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

Use the `--ease-*` theme variables to customize the transition timing function utilities in your project:

```
@theme {  --ease-in-expo: cubic-bezier(0.95, 0.05, 0.795, 0.035); }
```

Now the `ease-in-expo` utility can be used in your markup:

```
<button class="ease-in-expo">  <!-- ... --></button>
```

Learn more about customizing your theme in the [theme documentation](../theme/index.md#customizing-your-theme).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)
-   [Customizing your theme](#customizing-your-theme)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
