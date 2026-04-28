---
title: "break-inside"
source: "https://tailwindcss.com/docs/break-inside"
canonical_url: "https://tailwindcss.com/docs/break-inside"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:51:40.177Z"
content_hash: "82236875a3ea93e284181f66c7c0e64cff5fff0440b5b2d41a0bcc9b2de9a787"
menu_path: ["break-inside"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/break-before/index.md", "title": "break-before"}
nav_next: {"path": "tailwind/docs/box-decoration-break/index.md", "title": "box-decoration-break"}
---

# break-inside

Utilities for controlling how a column or page should break within an element.

| Class | Styles |
| --- | --- |
| `break-inside-auto` | 
`break-inside: auto;`

 |
| `break-inside-avoid` | 

`break-inside: avoid;`

 |
| `break-inside-avoid-page` | 

`break-inside: avoid-page;`

 |
| `break-inside-avoid-column` | 

`break-inside: avoid-column;`

 |

Use utilities like `break-inside-column` and `break-inside-avoid-page` to control how a column or page break should behave within an element:

```
<div class="columns-2">  <p>Well, let me tell you something, ...</p>  <p class="break-inside-avoid-column">Sure, go ahead, laugh...</p>  <p>Maybe we can live without...</p>  <p>Look. If you think this is...</p></div>
```

Prefix a `break-inside` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="break-inside-avoid-column md:break-inside-auto ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
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
