---
title: "touch-action"
source: "https://tailwindcss.com/docs/touch-action"
canonical_url: "https://tailwindcss.com/docs/touch-action"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:40:18.500Z"
content_hash: "10da5a0567979d4ae0068ee64b31ca864a1cbd5762d38a1dad61965290c182ab"
menu_path: ["touch-action"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Interactivity
2.  touch-action

Interactivity

# touch-action

Utilities for controlling how an element can be scrolled and zoomed on touchscreens.

| Class | Styles |
| --- | --- |
| `touch-auto` | 
`touch-action: auto;`

 |
| `touch-none` | 

`touch-action: none;`

 |
| `touch-pan-x` | 

`touch-action: pan-x;`

 |
| `touch-pan-left` | 

`touch-action: pan-left;`

 |
| `touch-pan-right` | 

`touch-action: pan-right;`

 |
| `touch-pan-y` | 

`touch-action: pan-y;`

 |
| `touch-pan-up` | 

`touch-action: pan-up;`

 |
| `touch-pan-down` | 

`touch-action: pan-down;`

 |
| `touch-pinch-zoom` | 

`touch-action: pinch-zoom;`

 |
| `touch-manipulation` | 

`touch-action: manipulation;`

 |

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

Prefix a `touch-action` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="touch-pan-x md:touch-auto ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
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
