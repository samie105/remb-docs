---
title: "transition-delay"
source: "https://tailwindcss.com/docs/transition-delay"
canonical_url: "https://tailwindcss.com/docs/transition-delay"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:32:41.079Z"
content_hash: "edce5e82828e9dfbaa9e0501c05dd91e5642198577b3af9b35fe6a9cad763e02"
menu_path: ["transition-delay"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/transition-timing-function/index.md", "title": "transition-timing-function"}
nav_next: {"path": "tailwind/docs/animation/index.md", "title": "animation"}
---

# transition-delay

Utilities for controlling the delay of CSS transitions.

| Class | Styles |
| --- | --- |
| `delay-<number>` | 
`transition-delay: <number>ms;`

 |
| `delay-(<custom-property>)` | 

`transition-delay: var(<custom-property>);`

 |
| `delay-[<value>]` | 

`transition-delay: <value>;`

 |

Use utilities like `delay-150` and `delay-700` to set the transition delay of an element in milliseconds:

Hover each button to see the expected behavior

delay-150

delay-300

delay-700

```
<button class="transition delay-150 duration-300 ease-in-out ...">Button A</button><button class="transition delay-300 duration-300 ease-in-out ...">Button B</button><button class="transition delay-700 duration-300 ease-in-out ...">Button C</button>
```

For situations where the user has specified that they prefer reduced motion, you can conditionally apply animations and transitions using the `motion-safe` and `motion-reduce` variants:

```
<button type="button" class="delay-300 motion-reduce:delay-0 ...">  <!-- ... --></button>
```

Use the `delay-[<value>]` syntax to set the transition delay based on a completely custom value:

```
<button class="delay-[1s,250ms] ...">  <!-- ... --></button>
```

For CSS variables, you can also use the `delay-(<custom-property>)` syntax:

```
<button class="delay-(--my-delay) ...">  <!-- ... --></button>
```

This is just a shorthand for `delay-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `transition-delay` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<button class="delay-150 md:delay-300 ...">  <!-- ... --></button>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Supporting reduced motion](#supporting-reduced-motion)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
