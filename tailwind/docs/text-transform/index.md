---
title: "text-transform"
source: "https://tailwindcss.com/docs/text-transform"
canonical_url: "https://tailwindcss.com/docs/text-transform"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:31.336Z"
content_hash: "75824e73618d7732b10acfb090b4dbfb97d512cad135ae301d0d0c77256348f8"
menu_path: ["text-transform"]
section_path: []
nav_prev: {"path": "tailwind/docs/text-underline-offset/index.md", "title": "text-underline-offset"}
nav_next: {"path": "tailwind/docs/text-overflow/index.md", "title": "text-overflow"}
---

# text-transform

Utilities for controlling the capitalization of text.

Class

Styles

`uppercase`

`text-transform: uppercase;`

`lowercase`

`text-transform: lowercase;`

`capitalize`

`text-transform: capitalize;`

`normal-case`

`text-transform: none;`

## [Examples](#examples)

### [Uppercasing text](#uppercasing-text)

Use the `uppercase` utility to uppercase the text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="uppercase">The quick brown fox ...</p>
```

### [Lowercasing text](#lowercasing-text)

Use the `lowercase` utility to lowercase the text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="lowercase">The quick brown fox ...</p>
```

### [Capitalizing text](#capitalizing-text)

Use the `capitalize` utility to capitalize text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="capitalize">The quick brown fox ...</p>
```

### [Resetting text casing](#resetting-text-casing)

Use the `normal-case` utility to preserve the original text casing of an element—typically used to reset capitalization at different breakpoints:

The quick brown fox jumps over the lazy dog.

```
<p class="normal-case">The quick brown fox ...</p>
```

### [Responsive design](#responsive-design)

Prefix a `text-transform` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="capitalize md:uppercase ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Uppercasing text](#uppercasing-text)
    *   [Lowercasing text](#lowercasing-text)
    *   [Capitalizing text](#capitalizing-text)
    *   [Resetting text casing](#resetting-text-casing)
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

