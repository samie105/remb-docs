---
title: "text-decoration-style"
source: "https://tailwindcss.com/docs/text-decoration-style"
canonical_url: "https://tailwindcss.com/docs/text-decoration-style"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:12:14.865Z"
content_hash: "0a41f22ac593526bfcf5605dff2428bce94344349afb799ad05ec5203e26d38c"
menu_path: ["text-decoration-style"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/text-decoration-color/index.md", "title": "text-decoration-color"}
nav_next: {"path": "tailwind/docs/text-decoration-thickness/index.md", "title": "text-decoration-thickness"}
---

# text-decoration-style

Utilities for controlling the style of text decorations.

| Class | Styles |
| --- | --- |
| `decoration-solid` | 
`text-decoration-style: solid;`

 |
| `decoration-double` | 

`text-decoration-style: double;`

 |
| `decoration-dotted` | 

`text-decoration-style: dotted;`

 |
| `decoration-dashed` | 

`text-decoration-style: dashed;`

 |
| `decoration-wavy` | 

`text-decoration-style: wavy;`

 |

Use utilities like `decoration-dotted` and `decoration-dashed` to change the [text decoration](../text-decoration-line/index.md) style of an element:

decoration-solid

The quick brown fox jumps over the lazy dog.

decoration-double

The quick brown fox jumps over the lazy dog.

decoration-dotted

The quick brown fox jumps over the lazy dog.

decoration-dashed

The quick brown fox jumps over the lazy dog.

decoration-wavy

The quick brown fox jumps over the lazy dog.

```
<p class="underline decoration-solid">The quick brown fox...</p><p class="underline decoration-double">The quick brown fox...</p><p class="underline decoration-dotted">The quick brown fox...</p><p class="underline decoration-dashed">The quick brown fox...</p><p class="underline decoration-wavy">The quick brown fox...</p>
```

Prefix a `text-decoration-style` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="underline md:decoration-dashed ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

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
