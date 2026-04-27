---
title: "grid-auto-flow"
source: "https://tailwindcss.com/docs/grid-auto-flow"
canonical_url: "https://tailwindcss.com/docs/grid-auto-flow"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:59:02.516Z"
content_hash: "c469b40cd663fd4227ed7fe51b0e1d48dda3d363bcf14668c9a77b00772d3567"
menu_path: ["grid-auto-flow"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  grid-auto-flow

Flexbox & Grid

# grid-auto-flow

Utilities for controlling how elements in a grid are auto-placed.

| Class | Styles |
| --- | --- |
| `grid-flow-row` | 
`grid-auto-flow: row;`

 |
| `grid-flow-col` | 

`grid-auto-flow: column;`

 |
| `grid-flow-dense` | 

`grid-auto-flow: dense;`

 |
| `grid-flow-row-dense` | 

`grid-auto-flow: row dense;`

 |
| `grid-flow-col-dense` | 

`grid-auto-flow: column dense;`

 |

Use utilities like `grid-flow-col` and `grid-flow-row-dense` to control how the auto-placement algorithm works for a grid layout:

01

02

03

04

05

```
<div class="grid grid-flow-row-dense grid-cols-3 grid-rows-3 ...">  <div class="col-span-2">01</div>  <div class="col-span-2">02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Prefix a `grid-auto-flow` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid grid-flow-col md:grid-flow-row ...">  <!-- ... --></div>
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
