---
title: "align-items"
source: "https://tailwindcss.com/docs/align-items"
canonical_url: "https://tailwindcss.com/docs/align-items"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:01:19.343Z"
content_hash: "717ade59d52e8a88ce26d84a4fc71ee486f74cd3ba51878196f758c82a8bf0c3"
menu_path: ["align-items"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  align-items

Flexbox & Grid

# align-items

Utilities for controlling how flex and grid items are positioned along a container's cross axis.

| Class | Styles |
| --- | --- |
| `items-start` | 
`align-items: flex-start;`

 |
| `items-end` | 

`align-items: flex-end;`

 |
| `items-end-safe` | 

`align-items: safe flex-end;`

 |
| `items-center` | 

`align-items: center;`

 |
| `items-center-safe` | 

`align-items: safe center;`

 |
| `items-baseline` | 

`align-items: baseline;`

 |
| `items-baseline-last` | 

`align-items: last baseline;`

 |
| `items-stretch` | 

`align-items: stretch;`

 |

Use the `items-stretch` utility to stretch items to fill the container's cross axis:

01

02

03

```
<div class="flex items-stretch ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

Use the `items-start` utility to align items to the start of the container's cross axis:

01

02

03

```
<div class="flex items-start ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

Use the `items-center` utility to align items along the center of the container's cross axis:

01

02

03

```
<div class="flex items-center ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

Use the `items-end` utility to align items to the end of the container's cross axis:

01

02

03

```
<div class="flex items-end ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

Use the `items-baseline` utility to align items along the container's cross axis such that all of their baselines align:

01

02

03

```
<div class="flex items-baseline ...">  <div class="pt-2 pb-6">01</div>  <div class="pt-8 pb-12">02</div>  <div class="pt-12 pb-4">03</div></div>
```

Use the `items-baseline-last` utility to align items along the container's cross axis such that all of their baselines align with the last baseline in the container:

![](/_next/static/media/avatar.51a13c67.jpg)

Spencer Sharp

Working on the future of astronaut recruitment at Space Recruit.

[spacerecruit.com](#)

![](https://images.unsplash.com/photo-1590895340509-793cb98788c9?q=80&w=256&h=256&&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

Alex Reed

A multidisciplinary designer.

[alex-reed.com](#)

```
<div class="grid grid-cols-[1fr_auto] items-baseline-last">  <div>    <img src="img/spencer-sharp.jpg" />    <h4>Spencer Sharp</h4>    <p>Working on the future of astronaut recruitment at Space Recruit.</p>  </div>  <p>spacerecruit.com</p></div>
```

This is useful for ensuring that text items align with each other, even if they have different heights.

Prefix an `align-items` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="flex items-stretch md:items-center ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Stretch](#stretch)
    -   [Start](#start)
    -   [Center](#center)
    -   [End](#end)
    -   [Baseline](#baseline)
    -   [Last baseline](#last-baseline)
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
