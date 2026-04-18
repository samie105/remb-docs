---
title: "place-items"
source: "https://tailwindcss.com/docs/place-items"
canonical_url: "https://tailwindcss.com/docs/place-items"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:26.877Z"
content_hash: "46b7a55038484787adc7c7457c38fdd3b47b7614e7d62b6394daf8e40848795a"
menu_path: ["place-items"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  place-items

Flexbox & Grid

# place-items

Utilities for controlling how items are justified and aligned at the same time.

Class

Styles

`place-items-start`

`place-items: start;`

`place-items-end`

`place-items: end;`

`place-items-end-safe`

`place-items: safe end;`

`place-items-center`

`place-items: center;`

`place-items-center-safe`

`place-items: safe center;`

`place-items-baseline`

`place-items: baseline;`

`place-items-stretch`

`place-items: stretch;`

## [Examples](#examples)

### [Start](#start)

Use `place-items-start` to place grid items on the start of their grid areas on both axes:

01

02

03

04

05

06

```
<div class="grid grid-cols-3 place-items-start gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

### [End](#end)

Use `place-items-end` to place grid items on the end of their grid areas on both axes:

01

02

03

04

05

06

```
<div class="grid h-56 grid-cols-3 place-items-end gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

### [Center](#center)

Use `place-items-center` to place grid items on the center of their grid areas on both axes:

01

02

03

04

05

06

```
<div class="grid h-56 grid-cols-3 place-items-center gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

### [Stretch](#stretch)

Use `place-items-stretch` to stretch items along their grid areas on both axes:

01

02

03

04

05

06

```
<div class="grid h-56 grid-cols-3 place-items-stretch gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

## [Responsive design](#responsive-design)

Prefix a `place-items` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid place-items-start md:place-items-center ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Start](#start)
    *   [End](#end)
    *   [Center](#center)
    *   [Stretch](#stretch)
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
