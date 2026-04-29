---
title: "place-self"
source: "https://tailwindcss.com/docs/place-self"
canonical_url: "https://tailwindcss.com/docs/place-self"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:02:28.356Z"
content_hash: "b0a3585fa56267adc03e1dd7b66f03496165d555c02ed88001d867065d8a4972"
menu_path: ["place-self"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/place-items/index.md", "title": "place-items"}
nav_next: {"path": "tailwind/docs/padding/index.md", "title": "padding"}
---

Utilities for controlling how an individual item is justified and aligned at the same time.

## [Examples](#examples)

### [Auto](#auto)

Use `place-self-auto` to align an item based on the value of the container's `place-items` property:

01

02

03

04

05

06

```
<div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-auto ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

### [Start](#start)

Use `place-self-start` to align an item to the start on both axes:

01

02

03

04

05

06

```
<div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-start ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

### [Center](#center)

Use `place-self-center` to align an item at the center on both axes:

01

02

03

04

05

06

```
<div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-center ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

### [End](#end)

Use `place-self-end` to align an item to the end on both axes:

01

02

03

04

05

06

```
<div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-end ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

### [Stretch](#stretch)

Use `place-self-stretch` to stretch an item on both axes:

01

02

03

04

05

06

```
<div class="grid grid-cols-3 gap-4 ...">  <div>01</div>  <div class="place-self-stretch ...">02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

### [Responsive design](#responsive-design)

Prefix a `place-self` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="place-self-start md:place-self-end ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
