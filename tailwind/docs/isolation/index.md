---
title: "isolation"
source: "https://tailwindcss.com/docs/isolation"
canonical_url: "https://tailwindcss.com/docs/isolation"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:10.143Z"
content_hash: "efa9dcaeb2a7d1a4381ded899d12813f19c82aa216c96ffbf3e605a52142b5a0"
menu_path: ["isolation"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Layout
2.  isolation

Layout

# isolation

Utilities for controlling whether an element should explicitly create a new stacking context.

Class

Styles

`isolate`

`isolation: isolate;`

`isolation-auto`

`isolation: auto;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `isolate` and `isolation-auto` utilities to control whether an element should explicitly create a new stacking context:

```
<div class="isolate ...">  <!-- ... --></div>
```

### [Responsive design](#responsive-design)

Prefix an `isolation` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="isolate md:isolation-auto ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
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
