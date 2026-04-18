---
title: "color-scheme"
source: "https://tailwindcss.com/docs/color-scheme"
canonical_url: "https://tailwindcss.com/docs/color-scheme"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:15:33.424Z"
content_hash: "4a9ec441ef9725cf04e2d5ef292927c8a783b13f7021c9fa52ba355c4a1cff12"
menu_path: ["color-scheme"]
section_path: []
nav_prev: {"path": "tailwind/docs/caret-color/index.md", "title": "caret-color"}
nav_next: {"path": "tailwind/docs/cursor/index.md", "title": "cursor"}
---

# color-scheme

Utilities for controlling the color scheme of an element.

Class

Styles

`scheme-normal`

`color-scheme: normal;`

`scheme-dark`

`color-scheme: dark;`

`scheme-light`

`color-scheme: light;`

`scheme-light-dark`

`color-scheme: light dark;`

`scheme-only-dark`

`color-scheme: only dark;`

`scheme-only-light`

`color-scheme: only light;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `scheme-light` and `scheme-light-dark` to control how element should be rendered:

Try switching your system color scheme to see the difference

scheme-light

scheme-dark

scheme-light-dark

```
<div class="scheme-light ...">  <input type="date" /></div><div class="scheme-dark ...">  <input type="date" /></div><div class="scheme-light-dark ...">  <input type="date" /></div>
```

### [Applying in dark mode](#applying-in-dark-mode)

Prefix a `color-scheme` utility with a variant like `dark:*` to only apply the utility in that state:

```
<html class="scheme-light dark:scheme-dark ...">  <!-- ... --></html>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Applying in dark mode](#applying-in-dark-mode)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)


