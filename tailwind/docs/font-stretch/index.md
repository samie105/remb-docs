---
title: "font-stretch"
source: "https://tailwindcss.com/docs/font-stretch"
canonical_url: "https://tailwindcss.com/docs/font-stretch"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:08:15.455Z"
content_hash: "a34099a2a28e22893808cc5c19e9d2e4379c346f90a8b3d12d972d38552a445a"
menu_path: ["font-stretch"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/font-weight/index.md", "title": "font-weight"}
nav_next: {"path": "tailwind/docs/font-variant-numeric/index.md", "title": "font-variant-numeric"}
---

# font-stretch

Utilities for selecting the width of a font face.

| Class | Styles |
| --- | --- |
| `font-stretch-ultra-condensed` | 
`font-stretch: ultra-condensed; /* 50% */`

 |
| `font-stretch-extra-condensed` | 

`font-stretch: extra-condensed; /* 62.5% */`

 |
| `font-stretch-condensed` | 

`font-stretch: condensed; /* 75% */`

 |
| `font-stretch-semi-condensed` | 

`font-stretch: semi-condensed; /* 87.5% */`

 |
| `font-stretch-normal` | 

`font-stretch: normal; /* 100% */`

 |
| `font-stretch-semi-expanded` | 

`font-stretch: semi-expanded; /* 112.5% */`

 |
| `font-stretch-expanded` | 

`font-stretch: expanded; /* 125% */`

 |
| `font-stretch-extra-expanded` | 

`font-stretch: extra-expanded; /* 150% */`

 |
| `font-stretch-ultra-expanded` | 

`font-stretch: ultra-expanded; /* 200% */`

 |
| `font-stretch-<percentage>` | 

`font-stretch: <percentage>;`

 |
| `font-stretch-(<custom-property>)` | 

`font-stretch: var(<custom-property>);`

 |
| `font-stretch-[<value>]` | 

`font-stretch: <value>;`

 |

Use utilities like `font-stretch-condensed` and `font-stretch-expanded` to set the width of a font face:

font-stretch-extra-condensed

The quick brown fox jumps over the lazy dog.

font-stretch-condensed

The quick brown fox jumps over the lazy dog.

font-stretch-normal

The quick brown fox jumps over the lazy dog.

font-stretch-expanded

The quick brown fox jumps over the lazy dog.

font-stretch-extra-expanded

The quick brown fox jumps over the lazy dog.

```
<p class="font-stretch-extra-condensed">The quick brown fox...</p><p class="font-stretch-condensed">The quick brown fox...</p><p class="font-stretch-normal">The quick brown fox...</p><p class="font-stretch-expanded">The quick brown fox...</p><p class="font-stretch-extra-expanded">The quick brown fox...</p>
```

This only applies to fonts that have multiple width variations available, otherwise the browser selects the closest match.

Use `font-stretch-<percentage>` utilities like `font-stretch-50%` and `font-stretch-125%` to set the width of a font face using a percentage:

font-stretch-50%

The quick brown fox jumps over the lazy dog.

font-stretch-100%

The quick brown fox jumps over the lazy dog.

font-stretch-150%

The quick brown fox jumps over the lazy dog.

```
<p class="font-stretch-50%">The quick brown fox...</p><p class="font-stretch-100%">The quick brown fox...</p><p class="font-stretch-150%">The quick brown fox...</p>
```

Use the `font-stretch-[<value>]` syntax to set the font width based on a completely custom value:

```
<p class="font-stretch-[66.66%] ...">  Lorem ipsum dolor sit amet...</p>
```

For CSS variables, you can also use the `font-stretch-(<custom-property>)` syntax:

```
<p class="font-stretch-(--my-font-width) ...">  Lorem ipsum dolor sit amet...</p>
```

This is just a shorthand for `font-stretch-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `font-stretch` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="font-stretch-normal md:font-stretch-expanded ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using percentages](#using-percentages)
    -   [Using a custom value](#using-a-custom-value)
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
