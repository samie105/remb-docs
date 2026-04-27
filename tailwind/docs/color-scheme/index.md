---
title: "color-scheme"
source: "https://tailwindcss.com/docs/color-scheme"
canonical_url: "https://tailwindcss.com/docs/color-scheme"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:37:22.267Z"
content_hash: "56fc47b083f38a53e0623a4645914b8bc0c861aaa0bafbfcdcdfb76c5a68e281"
menu_path: ["color-scheme"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Interactivity
2.  color-scheme

Interactivity

# color-scheme

Utilities for controlling the color scheme of an element.

| Class | Styles |
| --- | --- |
| `scheme-normal` | 
`color-scheme: normal;`

 |
| `scheme-dark` | 

`color-scheme: dark;`

 |
| `scheme-light` | 

`color-scheme: light;`

 |
| `scheme-light-dark` | 

`color-scheme: light dark;`

 |
| `scheme-only-dark` | 

`color-scheme: only dark;`

 |
| `scheme-only-light` | 

`color-scheme: only light;`

 |

Use utilities like `scheme-light` and `scheme-light-dark` to control how element should be rendered:

Try switching your system color scheme to see the difference

scheme-light

scheme-dark

scheme-light-dark

```
<div class="scheme-light ...">  <input type="date" /></div><div class="scheme-dark ...">  <input type="date" /></div><div class="scheme-light-dark ...">  <input type="date" /></div>
```

Prefix a `color-scheme` utility with a variant like `dark:*` to only apply the utility in that state:

```
<html class="scheme-light dark:scheme-dark ...">  <!-- ... --></html>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Applying in dark mode](#applying-in-dark-mode)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
