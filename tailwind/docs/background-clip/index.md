---
title: "background-clip"
source: "https://tailwindcss.com/docs/background-clip"
canonical_url: "https://tailwindcss.com/docs/background-clip"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:56.426Z"
content_hash: "df9b92872ecd0803819d3db946a4add8ea4a4483c078284bde6e0cadfbdae12c"
menu_path: ["background-clip"]
section_path: []
nav_prev: {"path": "tailwind/docs/background-attachment/index.md", "title": "background-attachment"}
nav_next: {"path": "tailwind/docs/background-color/index.md", "title": "background-color"}
---

# background-clip

Utilities for controlling the bounding box of an element's background.

Class

Styles

`bg-clip-border`

`background-clip: border-box;`

`bg-clip-padding`

`background-clip: padding-box;`

`bg-clip-content`

`background-clip: content-box;`

`bg-clip-text`

`background-clip: text;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `bg-clip-border`, `bg-clip-padding`, and `bg-clip-content` utilities to control the bounding box of an element's background:

bg-clip-border

bg-clip-padding

bg-clip-content

```
<div class="border-4 bg-indigo-500 bg-clip-border p-3"></div><div class="border-4 bg-indigo-500 bg-clip-padding p-3"></div><div class="border-4 bg-indigo-500 bg-clip-content p-3"></div>
```

### [Cropping to text](#cropping-to-text)

Use the `bg-clip-text` utility to crop an element's background to match the shape of the text:

Hello world

```
<p class="bg-linear-to-r from-pink-500 to-violet-500 bg-clip-text text-5xl font-extrabold text-transparent ...">  Hello world</p>
```

### [Responsive design](#responsive-design)

Prefix a `background-clip` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="bg-clip-border md:bg-clip-padding ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Cropping to text](#cropping-to-text)
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

