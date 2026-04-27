---
title: "cursor"
source: "https://tailwindcss.com/docs/cursor"
canonical_url: "https://tailwindcss.com/docs/cursor"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:37:21.979Z"
content_hash: "d7db93ed4a9299cf613405cab169c091e64cb8c47e2e09238c66c790df7257aa"
menu_path: ["cursor"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Interactivity
2.  cursor

Interactivity

# cursor

Utilities for controlling the cursor style when hovering over an element.

| Class | Styles |
| --- | --- |
| `cursor-auto` | 
`cursor: auto;`

 |
| `cursor-default` | 

`cursor: default;`

 |
| `cursor-pointer` | 

`cursor: pointer;`

 |
| `cursor-wait` | 

`cursor: wait;`

 |
| `cursor-text` | 

`cursor: text;`

 |
| `cursor-move` | 

`cursor: move;`

 |
| `cursor-help` | 

`cursor: help;`

 |
| `cursor-not-allowed` | 

`cursor: not-allowed;`

 |
| `cursor-none` | 

`cursor: none;`

 |
| `cursor-context-menu` | 

`cursor: context-menu;`

 |

Use utilities like `cursor-pointer` and `cursor-grab` to control which cursor is displayed when hovering over an element:

Hover over each button to see the cursor change

```
<button class="cursor-pointer ...">Submit</button><button class="cursor-progress ...">Saving...</button><button class="cursor-not-allowed ..." disabled>Confirm</button>
```

Use the `cursor-[<value>]` syntax to set the cursor based on a completely custom value:

```
<button class="cursor-[url(hand.cur),_pointer] ...">  <!-- ... --></button>
```

For CSS variables, you can also use the `cursor-(<custom-property>)` syntax:

```
<button class="cursor-(--my-cursor) ...">  <!-- ... --></button>
```

This is just a shorthand for `cursor-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `cursor` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<button class="cursor-not-allowed md:cursor-auto ...">  <!-- ... --></button>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
