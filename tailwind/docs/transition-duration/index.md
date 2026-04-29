---
title: "transition-duration"
source: "https://tailwindcss.com/docs/transition-duration"
canonical_url: "https://tailwindcss.com/docs/transition-duration"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:32:06.319Z"
content_hash: "6f186d297e536d3f8e6980e05fd45c89fa78753a94d18e1786d1a101a2a7741f"
menu_path: ["transition-duration"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/transition-behavior/index.md", "title": "transition-behavior"}
nav_next: {"path": "tailwind/docs/transition-timing-function/index.md", "title": "transition-timing-function"}
---

# transition-duration

Utilities for controlling the duration of CSS transitions.

| Class | Styles |
| --- | --- |
| `duration-<number>` | 
`transition-duration: <number>ms;`

 |
| `duration-initial` | 

`transition-duration: initial;`

 |
| `duration-(<custom-property>)` | 

`transition-duration: var(<custom-property>);`

 |
| `duration-[<value>]` | 

`transition-duration: <value>;`

 |

Use utilities like `duration-150` and `duration-700` to set the transition duration of an element in milliseconds:

Hover each button to see the expected behavior

duration-150

duration-300

duration-700

```
<button class="transition duration-150 ease-in-out ...">Button A</button><button class="transition duration-300 ease-in-out ...">Button B</button><button class="transition duration-700 ease-in-out ...">Button C</button>
```

For situations where the user has specified that they prefer reduced motion, you can conditionally apply animations and transitions using the `motion-safe` and `motion-reduce` variants:

```
<button type="button" class="duration-300 motion-reduce:duration-0 ...">  <!-- ... --></button>
```

Use the `duration-[<value>]` syntax to set the transition duration based on a completely custom value:

```
<button class="duration-[1s,15s] ...">  <!-- ... --></button>
```

For CSS variables, you can also use the `duration-(<custom-property>)` syntax:

```
<button class="duration-(--my-duration) ...">  <!-- ... --></button>
```

This is just a shorthand for `duration-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `transition-duration` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<button class="duration-0 md:duration-150 ...">  <!-- ... --></button>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

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
