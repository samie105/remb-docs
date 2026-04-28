---
title: "flex-direction"
source: "https://tailwindcss.com/docs/flex-direction"
canonical_url: "https://tailwindcss.com/docs/flex-direction"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:56:12.741Z"
content_hash: "27174fb2907632e4cc2fd1dbfda938d86a5d9e5b41f82332dde495cc18eb50fe"
menu_path: ["flex-direction"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/flex-basis/index.md", "title": "flex-basis"}
nav_next: {"path": "tailwind/docs/flex-wrap/index.md", "title": "flex-wrap"}
---

# flex-direction

Utilities for controlling the direction of flex items.

| Class | Styles |
| --- | --- |
| `flex-row` | 
`flex-direction: row;`

 |
| `flex-row-reverse` | 

`flex-direction: row-reverse;`

 |
| `flex-col` | 

`flex-direction: column;`

 |
| `flex-col-reverse` | 

`flex-direction: column-reverse;`

 |

Use `flex-row` to position flex items horizontally in the same direction as text:

01

02

03

```
<div class="flex flex-row ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use `flex-row-reverse` to position flex items horizontally in the opposite direction:

01

02

03

```
<div class="flex flex-row-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use `flex-col` to position flex items vertically:

01

02

03

```
<div class="flex flex-col ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use `flex-col-reverse` to position flex items vertically in the opposite direction:

01

02

03

```
<div class="flex flex-col-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Prefix a `flex-direction` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="flex flex-col md:flex-row ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Row](#row)
    -   [Row reversed](#row-reversed)
    -   [Column](#column)
    -   [Column reversed](#column-reversed)
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
