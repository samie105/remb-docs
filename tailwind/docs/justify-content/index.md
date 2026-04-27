---
title: "justify-content"
source: "https://tailwindcss.com/docs/justify-content"
canonical_url: "https://tailwindcss.com/docs/justify-content"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:00:10.691Z"
content_hash: "c177b1d52977262ce575dea1e35d03e8cb2cc16091495fcbd91a33fe7539a503"
menu_path: ["justify-content"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  justify-content

Flexbox & Grid

# justify-content

Utilities for controlling how flex and grid items are positioned along a container's main axis.

| Class | Styles |
| --- | --- |
| `justify-start` | 
`justify-content: flex-start;`

 |
| `justify-end` | 

`justify-content: flex-end;`

 |
| `justify-end-safe` | 

`justify-content: safe flex-end;`

 |
| `justify-center` | 

`justify-content: center;`

 |
| `justify-center-safe` | 

`justify-content: safe center;`

 |
| `justify-between` | 

`justify-content: space-between;`

 |
| `justify-around` | 

`justify-content: space-around;`

 |
| `justify-evenly` | 

`justify-content: space-evenly;`

 |
| `justify-stretch` | 

`justify-content: stretch;`

 |
| `justify-baseline` | 

`justify-content: baseline;`

 |
| `justify-normal` | 

`justify-content: normal;`

 |

Use the `justify-start` utility to justify items against the start of the container's main axis:

01

02

03

```
<div class="flex justify-start ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use the `justify-center` or `justify-center-safe` utilities to justify items along the center of the container's main axis:

Resize the container to see the alignment behavior

justify-center

01

02

03

04

justify-center-safe

01

02

03

04

justify-center

```
<div class="flex justify-center ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

justify-center-safe

```
<div class="flex justify-center-safe ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div></div>
```

When there is not enough space available, the `justify-center-safe` utility will align items to the start of the container instead of the center.

Use the `justify-end` or `justify-end-safe` utilities to justify items against the end of the container's main axis:

Resize the container to see the alignment behavior

justify-end

01

02

03

04

justify-end-safe

01

02

03

04

justify-end

```
<div class="flex justify-end ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>03</div></div>
```

justify-end-safe

```
<div class="flex justify-end-safe ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>03</div></div>
```

When there is not enough space available, the `justify-end-safe` utility will align items to the start of the container instead of the end.

Use the `justify-between` utility to justify items along the container's main axis such that there is an equal amount of space between each item:

01

02

03

```
<div class="flex justify-between ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use the `justify-around` utility to justify items along the container's main axis such that there is an equal amount of space on each side of each item:

01

02

03

```
<div class="flex justify-around ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use the `justify-evenly` utility to justify items along the container's main axis such that there is an equal amount of space around each item, but also accounting for the doubling of space you would normally see between each item when using `justify-around`:

01

02

03

```
<div class="flex justify-evenly ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use the `justify-stretch` utility to allow auto-sized content items to fill the available space along the container's main axis:

01

02

03

```
<div class="grid grid-cols-[4rem_auto_4rem] justify-stretch ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Use the `justify-normal` utility to pack content items in their default position as if no `justify-content` value was set:

01

02

03

```
<div class="flex justify-normal ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

Prefix a `justify-content` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="flex justify-start md:justify-between ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Start](#start)
    -   [Center](#center)
    -   [End](#end)
    -   [Space between](#space-between)
    -   [Space around](#space-around)
    -   [Space evenly](#space-evenly)
    -   [Stretch](#stretch)
    -   [Normal](#normal)
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
