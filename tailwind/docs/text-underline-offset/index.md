---
title: "text-underline-offset"
source: "https://tailwindcss.com/docs/text-underline-offset"
canonical_url: "https://tailwindcss.com/docs/text-underline-offset"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:29.739Z"
content_hash: "fa42c5ec4f496fa4648217473c578fa81276b2a7b1d6cf9cd835e02c871702c1"
menu_path: ["text-underline-offset"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Typography
2.  text-underline-offset

Typography

# text-underline-offset

Utilities for controlling the offset of a text underline.

Class

Styles

`underline-offset-<number>`

`text-underline-offset: <number>px;`

`-underline-offset-<number>`

`text-underline-offset: calc(<number>px * -1);`

`underline-offset-auto`

`text-underline-offset: auto;`

`underline-offset-(<custom-property>)`

`text-underline-offset: var(<custom-property>);`

`underline-offset-[<value>]`

`text-underline-offset: <value>;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use `underline-offset-<number>` utilities like `underline-offset-2` and `underline-offset-4` to change the offset of a text underline:

underline-offset-1

The quick brown fox jumps over the lazy dog.

underline-offset-2

The quick brown fox jumps over the lazy dog.

underline-offset-4

The quick brown fox jumps over the lazy dog.

underline-offset-8

The quick brown fox jumps over the lazy dog.

```
<p class="underline underline-offset-1">The quick brown fox...</p><p class="underline underline-offset-2">The quick brown fox...</p><p class="underline underline-offset-4">The quick brown fox...</p><p class="underline underline-offset-8">The quick brown fox...</p>
```

### [Using a custom value](#using-a-custom-value)

Use the `underline-offset-[<value>]` syntax to set the text underline offset based on a completely custom value:

```
<p class="underline-offset-[3px] ...">  Lorem ipsum dolor sit amet...</p>
```

For CSS variables, you can also use the `underline-offset-(<custom-property>)` syntax:

```
<p class="underline-offset-(--my-underline-offset) ...">  Lorem ipsum dolor sit amet...</p>
```

This is just a shorthand for `underline-offset-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `text-underline-offset` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="underline md:underline-offset-4 ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
