---
title: "scroll-behavior"
source: "https://tailwindcss.com/docs/scroll-behavior"
canonical_url: "https://tailwindcss.com/docs/scroll-behavior"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:38:31.710Z"
content_hash: "ff8d7d7442d4d25b17863454a4ec1aafac0427269593f8e8d02ee7931b0230fe"
menu_path: ["scroll-behavior"]
section_path: []
content_language: "en"
nav_prev: {"path": "../resize/index.md", "title": "resize"}
nav_next: {"path": "../scroll-margin/index.md", "title": "scroll-margin"}
---

# scroll-behavior

Utilities for controlling the scroll behavior of an element.

| Class | Styles |
| --- | --- |
| `scroll-auto` | 
`scroll-behavior: auto;`

 |
| `scroll-smooth` | 

`scroll-behavior: smooth;`

 |

Use the `scroll-smooth` utility to enable smooth scrolling within an element:

```
<html class="scroll-smooth">  <!-- ... --></html>
```

Setting the `scroll-behavior` only affects scroll events that are triggered by the browser.

Use the `scroll-auto` utility to revert to the default browser behavior for scrolling:

```
<html class="scroll-smooth md:scroll-auto">  <!-- ... --></html>
```

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Using smooth scrolling](#using-smooth-scrolling)
    -   [Using normal scrolling](#using-normal-scrolling)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
