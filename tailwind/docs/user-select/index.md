---
title: "user-select"
source: "https://tailwindcss.com/docs/user-select"
canonical_url: "https://tailwindcss.com/docs/user-select"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:40:53.395Z"
content_hash: "258f764c591944c6e9c0f6f491715fba2e3bc42e5c8a1ab1b4d0f8e552172bb7"
menu_path: ["user-select"]
section_path: []
content_language: "en"
nav_prev: {"path": "../touch-action/index.md", "title": "touch-action"}
nav_next: {"path": "../will-change/index.md", "title": "will-change"}
---

# user-select

Utilities for controlling whether the user can select text in an element.

| Class | Styles |
| --- | --- |
| `select-none` | 
`user-select: none;`

 |
| `select-text` | 

`user-select: text;`

 |
| `select-all` | 

`user-select: all;`

 |
| `select-auto` | 

`user-select: auto;`

 |

Use the `select-none` utility to prevent selecting text in an element and its children:

Try selecting the text to see the expected behavior

The quick brown fox jumps over the lazy dog.

```
<div class="select-none ...">The quick brown fox jumps over the lazy dog.</div>
```

Use the `select-text` utility to allow selecting text in an element and its children:

Try selecting the text to see the expected behavior

The quick brown fox jumps over the lazy dog.

```
<div class="select-text ...">The quick brown fox jumps over the lazy dog.</div>
```

Use the `select-all` utility to automatically select all the text in an element when a user clicks:

Try clicking the text to see the expected behavior

The quick brown fox jumps over the lazy dog.

```
<div class="select-all ...">The quick brown fox jumps over the lazy dog.</div>
```

Use the `select-auto` utility to use the default browser behavior for selecting text:

Try selecting the text to see the expected behavior

The quick brown fox jumps over the lazy dog.

```
<div class="select-auto ...">The quick brown fox jumps over the lazy dog.</div>
```

Prefix an `user-select` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="select-none md:select-all ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Disabling text selection](#disabling-text-selection)
    -   [Allowing text selection](#allowing-text-selection)
    -   [Selecting all text in one click](#selecting-all-text-in-one-click)
    -   [Using auto select behavior](#using-auto-select-behavior)
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
