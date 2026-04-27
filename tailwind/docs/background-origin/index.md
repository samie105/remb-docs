---
title: "background-origin"
source: "https://tailwindcss.com/docs/background-origin"
canonical_url: "https://tailwindcss.com/docs/background-origin"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:16:54.874Z"
content_hash: "87a2f57ab5cf2bb948601fbdc6c22460ef316dcccc2de93ae0a05bc7983d9cfa"
menu_path: ["background-origin"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Backgrounds
2.  background-origin

Backgrounds

# background-origin

Utilities for controlling how an element's background is positioned relative to borders, padding, and content.

| Class | Styles |
| --- | --- |
| `bg-origin-border` | 
`background-origin: border-box;`

 |
| `bg-origin-padding` | 

`background-origin: padding-box;`

 |
| `bg-origin-content` | 

`background-origin: content-box;`

 |

Use the `bg-origin-border`, `bg-origin-padding`, and `bg-origin-content` utilities to control where an element's background is rendered:

bg-origin-border

bg-origin-padding

bg-origin-content

```
<div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-border p-3 ..."></div><div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-padding p-3 ..."></div><div class="border-4 bg-[url(/img/mountains.jpg)] bg-origin-content p-3 ..."></div>
```

Prefix a `background-origin` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="bg-origin-border md:bg-origin-padding ...">  <!-- ... --></div>
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
