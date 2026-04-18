---
title: "transition-duration"
source: "https://tailwindcss.com/docs/transition-duration"
canonical_url: "https://tailwindcss.com/docs/transition-duration"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:57.076Z"
content_hash: "b4c08ec4ad30fc93ca7708dafa1e2796cff2b7f4d4b8c9e0e831ba15d82b05b4"
menu_path: ["transition-duration"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Transitions & Animation
2.  transition-duration

Transitions & Animation

# transition-duration

Utilities for controlling the duration of CSS transitions.

Class

Styles

`duration-<number>`

`transition-duration: <number>ms;`

`duration-initial`

`transition-duration: initial;`

`duration-(<custom-property>)`

`transition-duration: var(<custom-property>);`

`duration-[<value>]`

`transition-duration: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `duration-150` and `duration-700` to set the transition duration of an element in milliseconds:

Hover each button to see the expected behavior

duration-150

duration-300

duration-700

```
<button class="transition duration-150 ease-in-out ...">Button A</button><button class="transition duration-300 ease-in-out ...">Button B</button><button class="transition duration-700 ease-in-out ...">Button C</button>
```

### [Supporting reduced motion](#supporting-reduced-motion)

For situations where the user has specified that they prefer reduced motion, you can conditionally apply animations and transitions using the `motion-safe` and `motion-reduce` variants:

```
<button type="button" class="duration-300 motion-reduce:duration-0 ...">  <!-- ... --></button>
```

### [Using a custom value](#using-a-custom-value)

Use the `duration-[<value>]` syntax to set the transition duration based on a completely custom value:

```
<button class="duration-[1s,15s] ...">  <!-- ... --></button>
```

For CSS variables, you can also use the `duration-(<custom-property>)` syntax:

```
<button class="duration-(--my-duration) ...">  <!-- ... --></button>
```

This is just a shorthand for `duration-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `transition-duration` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<button class="duration-0 md:duration-150 ...">  <!-- ... --></button>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Supporting reduced motion](#supporting-reduced-motion)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
