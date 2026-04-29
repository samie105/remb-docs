---
title: "vertical-align"
source: "https://tailwindcss.com/docs/vertical-align"
canonical_url: "https://tailwindcss.com/docs/vertical-align"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:13:59.828Z"
content_hash: "8596080ea1606072aaa2df0703d711ca745f90187d182922686e775ccd7775de"
menu_path: ["vertical-align"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/text-indent/index.md", "title": "text-indent"}
nav_next: {"path": "tailwind/docs/white-space/index.md", "title": "white-space"}
---

# vertical-align

Utilities for controlling the vertical alignment of an inline or table-cell box.

| Class | Styles |
| --- | --- |
| `align-baseline` | 
`vertical-align: baseline;`

 |
| `align-top` | 

`vertical-align: top;`

 |
| `align-middle` | 

`vertical-align: middle;`

 |
| `align-bottom` | 

`vertical-align: bottom;`

 |
| `align-text-top` | 

`vertical-align: text-top;`

 |
| `align-text-bottom` | 

`vertical-align: text-bottom;`

 |
| `align-sub` | 

`vertical-align: sub;`

 |
| `align-super` | 

`vertical-align: super;`

 |
| `align-(<custom-property>)` | 

`vertical-align: var(<custom-property>);`

 |
| `align-[<value>]` | 

`vertical-align: <value>;`

 |

Use the `align-baseline` utility to align the baseline of an element with the baseline of its parent:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-baseline">The quick brown fox...</span>
```

Use the `align-top` utility to align the top of an element and its descendants with the top of the entire line:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-top">The quick brown fox...</span>
```

Use the `align-middle` utility to align the middle of an element with the baseline plus half the x-height of the parent:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-middle">The quick brown fox...</span>
```

Use the `align-bottom` utility to align the bottom of an element and its descendants with the bottom of the entire line:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-bottom">The quick brown fox...</span>
```

Use the `align-text-top` utility to align the top of an element with the top of the parent element's font:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-text-top">The quick brown fox...</span>
```

Use the `align-text-bottom` utility to align the bottom of an element with the bottom of the parent element's font:

The quick brown fox jumps over the lazy dog.

```
<span class="inline-block align-text-bottom">The quick brown fox...</span>
```

Use the `align-[<value>]` syntax to set the vertical alignment based on a completely custom value:

```
<span class="align-[4px] ...">  <!-- ... --></span>
```

For CSS variables, you can also use the `align-(<custom-property>)` syntax:

```
<span class="align-(--my-alignment) ...">  <!-- ... --></span>
```

This is just a shorthand for `align-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `vertical-align` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<span class="align-middle md:align-top ...">  <!-- ... --></span>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Aligning to baseline](#aligning-to-baseline)
    -   [Aligning to top](#aligning-to-top)
    -   [Aligning to middle](#aligning-to-middle)
    -   [Aligning to bottom](#aligning-to-bottom)
    -   [Aligning to parent top](#aligning-to-parent-top)
    -   [Aligning to parent bottom](#aligning-to-parent-bottom)
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
