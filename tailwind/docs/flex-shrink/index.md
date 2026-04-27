---
title: "flex-shrink"
source: "https://tailwindcss.com/docs/flex-shrink"
canonical_url: "https://tailwindcss.com/docs/flex-shrink"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:57:20.637Z"
content_hash: "a728cd8eac6fd5325066ca7706e8fd962d50529f18c4dc6cae6463356c4c9540"
menu_path: ["flex-shrink"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  flex-shrink

Flexbox & Grid

# flex-shrink

Utilities for controlling how flex items shrink.

| Class | Styles |
| --- | --- |
| `shrink` | 
`flex-shrink: 1;`

 |
| `shrink-<number>` | 

`flex-shrink: <number>;`

 |
| `shrink-[<value>]` | 

`flex-shrink: <value>;`

 |
| `shrink-(<custom-property>)` | 

`flex-shrink: var(<custom-property>);`

 |

Use `shrink` to allow a flex item to shrink if needed:

01

02

03

```
<div class="flex ...">  <div class="h-14 w-14 flex-none ...">01</div>  <div class="h-14 w-64 shrink ...">02</div>  <div class="h-14 w-14 flex-none ...">03</div></div>
```

Use `shrink-0` to prevent a flex item from shrinking:

01

02

03

```
<div class="flex ...">  <div class="h-16 flex-1 ...">01</div>  <div class="h-16 w-32 shrink-0 ...">02</div>  <div class="h-16 flex-1 ...">03</div></div>
```

Use the `shrink-[<value>]` syntax to set the flex shrink factor based on a completely custom value:

```
<div class="shrink-[calc(100vw-var(--sidebar))] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `shrink-(<custom-property>)` syntax:

```
<div class="shrink-(--my-shrink) ...">  <!-- ... --></div>
```

This is just a shorthand for `shrink-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `flex-shrink` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="shrink md:shrink-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Allowing flex items to shrink](#allowing-flex-items-to-shrink)
    -   [Preventing items from shrinking](#preventing-items-from-shrinking)
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
