---
title: "flex-wrap"
source: "https://tailwindcss.com/docs/flex-wrap"
canonical_url: "https://tailwindcss.com/docs/flex-wrap"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:50.187Z"
content_hash: "778d1f736ff074a024a3a286ff793676ec48ac630c695b3dedc093e4d5131f02"
menu_path: ["flex-wrap"]
section_path: []
nav_prev: {"path": "tailwind/docs/flex-direction/index.md", "title": "flex-direction"}
nav_next: {"path": "tailwind/docs/flex/index.md", "title": "flex"}
---

# flex-wrap

Utilities for controlling how flex items wrap.

Class

Styles

`flex-nowrap`

`flex-wrap: nowrap;`

`flex-wrap`

`flex-wrap: wrap;`

`flex-wrap-reverse`

`flex-wrap: wrap-reverse;`

## [Examples](#examples)

### [Don't wrap](#dont-wrap)

Use `flex-nowrap` to prevent flex items from wrapping, causing inflexible items to overflow the container if necessary:

01

02

03

```
<div class="flex flex-nowrap">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Wrap normally](#wrap-normally)

Use `flex-wrap` to allow flex items to wrap:

01

02

03

```
<div class="flex flex-wrap">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Wrap reversed](#wrap-reversed)

Use `flex-wrap-reverse` to wrap flex items in the reverse direction:

01

02

03

```
<div class="flex flex-wrap-reverse">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

### [Responsive design](#responsive-design)

Prefix a `flex-wrap` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="flex flex-wrap md:flex-wrap-reverse ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Don't wrap](#dont-wrap)
    *   [Wrap normally](#wrap-normally)
    *   [Wrap reversed](#wrap-reversed)
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


