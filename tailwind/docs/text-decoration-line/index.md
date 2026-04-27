---
title: "text-decoration-line"
source: "https://tailwindcss.com/docs/text-decoration-line"
canonical_url: "https://tailwindcss.com/docs/text-decoration-line"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:11:40.237Z"
content_hash: "90ad3d4da9d2265481d3e2c5ea1cf879613740594fc766f94af17da6f1e9b963"
menu_path: ["text-decoration-line"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Typography
2.  text-decoration-line

Typography

# text-decoration-line

Utilities for controlling the decoration of text.

| Class | Styles |
| --- | --- |
| `underline` | 
`text-decoration-line: underline;`

 |
| `overline` | 

`text-decoration-line: overline;`

 |
| `line-through` | 

`text-decoration-line: line-through;`

 |
| `no-underline` | 

`text-decoration-line: none;`

 |

Use the `underline` utility to add an underline to the text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="underline">The quick brown fox...</p>
```

Use the `overline` utility to add an overline to the text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="overline">The quick brown fox...</p>
```

Use the `line-through` utility to add a line through the text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="line-through">The quick brown fox...</p>
```

Use the `no-underline` utility to remove a line from the text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="no-underline">The quick brown fox...</p>
```

Prefix a `text-decoration-line` utility with a variant like `hover:*` to only apply the utility in that state:

Hover over the text to see the expected behavior

The [quick brown fox](https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog) jumps over the lazy dog.

```
<p>The <a href="..." class="no-underline hover:underline ...">quick brown fox</a> jumps over the lazy dog.</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

Prefix a `text-decoration-line` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<a class="no-underline md:underline ..." href="...">  <!-- ... --></a>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Underling text](#underling-text)
    -   [Adding an overline to text](#adding-an-overline-to-text)
    -   [Adding a line through text](#adding-a-line-through-text)
    -   [Removing a line from text](#removing-a-line-from-text)
    -   [Applying on hover](#applying-on-hover)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
