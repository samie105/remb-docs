---
title: "align-content"
source: "https://tailwindcss.com/docs/align-content"
canonical_url: "https://tailwindcss.com/docs/align-content"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:01:14.819Z"
content_hash: "40b0493e675505b164344a3b8284462810df82af60a7af79dec38d2d60a56a12"
menu_path: ["align-content"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  align-content

Flexbox & Grid

# align-content

Utilities for controlling how rows are positioned in multi-row flex and grid containers.

| Class | Styles |
| --- | --- |
| `content-normal` | 
`align-content: normal;`

 |
| `content-center` | 

`align-content: center;`

 |
| `content-start` | 

`align-content: flex-start;`

 |
| `content-end` | 

`align-content: flex-end;`

 |
| `content-between` | 

`align-content: space-between;`

 |
| `content-around` | 

`align-content: space-around;`

 |
| `content-evenly` | 

`align-content: space-evenly;`

 |
| `content-baseline` | 

`align-content: baseline;`

 |
| `content-stretch` | 

`align-content: stretch;`

 |

Use `content-start` to pack rows in a container against the start of the cross axis:

01

02

03

04

05

```
<div class="grid h-56 grid-cols-3 content-start gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Use `content-center` to pack rows in a container in the center of the cross axis:

01

02

03

04

05

```
<div class="grid h-56 grid-cols-3 content-center gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Use `content-end` to pack rows in a container against the end of the cross axis:

01

02

03

04

05

```
<div class="grid h-56 grid-cols-3 content-end gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Use `content-between` to distribute rows in a container such that there is an equal amount of space between each line:

01

02

03

04

05

```
<div class="grid h-56 grid-cols-3 content-between gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Use `content-around` to distribute rows in a container such that there is an equal amount of space around each line:

01

02

03

04

05

```
<div class="grid h-56 grid-cols-3 content-around gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Use `content-evenly` to distribute rows in a container such that there is an equal amount of space around each item, but also accounting for the doubling of space you would normally see between each item when using `content-around`:

01

02

03

04

05

```
<div class="grid h-56 grid-cols-3 content-evenly gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Use `content-stretch` to allow content items to fill the available space along the container’s cross axis:

01

02

03

04

05

```
<div class="grid h-56 grid-cols-3 content-stretch gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Use `content-normal` to pack content items in their default position as if no `align-content` value was set:

01

02

03

04

05

```
<div class="grid h-56 grid-cols-3 content-normal gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div></div>
```

Prefix an `align-content` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grid content-start md:content-around ...">  <!-- ... --></div>
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
