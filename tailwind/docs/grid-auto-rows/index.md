---
title: "grid-auto-rows"
source: "https://tailwindcss.com/docs/grid-auto-rows"
canonical_url: "https://tailwindcss.com/docs/grid-auto-rows"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:59:36.078Z"
content_hash: "1163f35ebddf6c69b33535921bbac7958c1576141b4ef9d4a9968d00c3cf981b"
menu_path: ["grid-auto-rows"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  grid-auto-rows

Flexbox & Grid

# grid-auto-rows

Utilities for controlling the size of implicitly-created grid rows.

| Class | Styles |
| --- | --- |
| `auto-rows-auto` | 
`grid-auto-rows: auto;`

 |
| `auto-rows-min` | 

`grid-auto-rows: min-content;`

 |
| `auto-rows-max` | 

`grid-auto-rows: max-content;`

 |
| `auto-rows-fr` | 

`grid-auto-rows: minmax(0, 1fr);`

 |
| `auto-rows-(<custom-property>)` | 

`grid-auto-rows: var(<custom-property>);`

 |
| `auto-rows-[<value>]` | 

`grid-auto-rows: <value>;`

 |

Use utilities like `auto-rows-min` and `auto-rows-max` to control the size of implicitly-created grid rows:

```
<div class="grid grid-flow-row auto-rows-max">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use the `auto-rows-[<value>]` syntax to set the size of implicitly-created grid rows based on a completely custom value:

```
<div class="auto-rows-[minmax(0,2fr)] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `auto-rows-(<custom-property>)` syntax:

```
<div class="auto-rows-(--my-auto-rows) ...">  <!-- ... --></div>
```

This is just a shorthand for `auto-rows-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `grid-auto-rows` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid grid-flow-row auto-rows-max md:auto-rows-min ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
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
