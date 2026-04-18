---
title: "align-self"
source: "https://tailwindcss.com/docs/align-self"
canonical_url: "https://tailwindcss.com/docs/align-self"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:49.382Z"
content_hash: "a6632226d6b45f1cd623a1f02cd2d88394cdb0746cb5c24bde3bcab9f6125e88"
menu_path: ["align-self"]
section_path: []
nav_prev: {"path": "tailwind/docs/align-items/index.md", "title": "align-items"}
nav_next: {"path": "tailwind/docs/place-content/index.md", "title": "place-content"}
---

Flexbox & Grid

Utilities for controlling how an individual flex or grid item is positioned along its container's cross axis.

Class

Styles

`self-auto`

`align-self: auto;`

`self-start`

`align-self: flex-start;`

`self-end`

`align-self: flex-end;`

`self-end-safe`

`align-self: safe flex-end;`

`self-center`

`align-self: center;`

`self-center-safe`

`align-self: safe center;`

`self-stretch`

`align-self: stretch;`

`self-baseline`

`align-self: baseline;`

`self-baseline-last`

`align-self: last baseline;`

## [Examples](#examples)

### [Auto](#auto)

Use the `self-auto` utility to align an item based on the value of the container's `align-items` property:

01

02

03

```
<div class="flex items-stretch ...">  <div>01</div>  <div class="self-auto ...">02</div>  <div>03</div></div>
```

### [Start](#start)

Use the `self-start` utility to align an item to the start of the container's cross axis, despite the container's `align-items` value:

01

02

03

```
<div class="flex items-stretch ...">  <div>01</div>  <div class="self-start ...">02</div>  <div>03</div></div>
```

### [Center](#center)

Use the `self-center` utility to align an item along the center of the container's cross axis, despite the container's `align-items` value:

01

02

03

```
<div class="flex items-stretch ...">  <div>01</div>  <div class="self-center ...">02</div>  <div>03</div></div>
```

### [End](#end)

Use the `self-end` utility to align an item to the end of the container's cross axis, despite the container's `align-items` value:

01

02

03

```
<div class="flex items-stretch ...">  <div>01</div>  <div class="self-end ...">02</div>  <div>03</div></div>
```

### [Stretch](#stretch)

Use the `self-stretch` utility to stretch an item to fill the container's cross axis, despite the container's `align-items` value:

01

02

03

```
<div class="flex items-stretch ...">  <div>01</div>  <div class="self-stretch ...">02</div>  <div>03</div></div>
```

### [Baseline](#baseline)

Use the `self-baseline` utility to align an item such that its baseline aligns with the baseline of the flex container's cross axis:

01

02

03

```
<div class="flex ...">  <div class="self-baseline pt-2 pb-6">01</div>  <div class="self-baseline pt-8 pb-12">02</div>  <div class="self-baseline pt-12 pb-4">03</div></div>
```

### [Last baseline](#last-baseline)

Use the `self-baseline-last` utility to align an item along the container's cross axis such that its baseline aligns with the last baseline in the container:

![](/_next/static/media/avatar.51a13c67.jpg)

Spencer Sharp

Working on the future of astronaut recruitment at Space Recruit.

[spacerecruit.com](#)

```
<div class="grid grid-cols-[1fr_auto]">  <div>    <img src="img/spencer-sharp.jpg" />    <h4>Spencer Sharp</h4>    <p class="self-baseline-last">Working on the future of astronaut recruitment at Space Recruit.</p>  </div>  <p class="self-baseline-last">spacerecruit.com</p></div>
```

This is useful for ensuring that text items align with each other, even if they have different heights.

### [Responsive design](#responsive-design)

Prefix an `align-self` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="self-auto md:self-end ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).


