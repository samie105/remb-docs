---
title: "hyphens"
source: "https://tailwindcss.com/docs/hyphens"
canonical_url: "https://tailwindcss.com/docs/hyphens"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:15:10.032Z"
content_hash: "ee74ebafe99fcd68b3830480d0158f43a7102e05adef5ee42bffa60478c67751"
menu_path: ["hyphens"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/overflow-wrap/index.md", "title": "overflow-wrap"}
nav_next: {"path": "tailwind/docs/content/index.md", "title": "content"}
---

# hyphens

Utilities for controlling how words should be hyphenated.

| Class | Styles |
| --- | --- |
| `hyphens-none` | 
`hyphens: none;`

 |
| `hyphens-manual` | 

`hyphens: manual;`

 |
| `hyphens-auto` | 

`hyphens: auto;`

 |

Use the `hyphens-none` utility to prevent words from being hyphenated even if the line break suggestion `&shy;` is used:

Officially recognized by the Duden dictionary as the longest word in German, Kraftfahrzeug­haftpflichtversicherung is a 36 letter word for motor vehicle liability insurance.

```
<p class="hyphens-none">  ... Kraftfahrzeug&shy;haftpflichtversicherung is a ...</p>
```

Use the `hyphens-manual` utility to only set hyphenation points where the line break suggestion `&shy;` is used:

Officially recognized by the Duden dictionary as the longest word in German, Kraftfahrzeug­haftpflichtversicherung is a 36 letter word for motor vehicle liability insurance.

```
<p class="hyphens-manual">  ... Kraftfahrzeug&shy;haftpflichtversicherung is a ...</p>
```

This is the default browser behavior.

Use the `hyphens-auto` utility to allow the browser to automatically choose hyphenation points based on the language:

Officially recognized by the Duden dictionary as the longest word in German, Kraftfahrzeughaftpflichtversicherung is a 36 letter word for motor vehicle liability insurance.

```
<p class="hyphens-auto" lang="de">  ... Kraftfahrzeughaftpflichtversicherung is a ...</p>
```

The line break suggestion `&shy;` will be preferred over automatic hyphenation points.

Prefix a `hyphens` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="hyphens-none md:hyphens-auto ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Preventing hyphenation](#preventing-hyphenation)
    -   [Manual hyphenation](#manual-hyphenation)
    -   [Automatic hyphenation](#automatic-hyphenation)
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
