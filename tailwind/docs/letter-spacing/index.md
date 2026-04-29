---
title: "letter-spacing"
source: "https://tailwindcss.com/docs/letter-spacing"
canonical_url: "https://tailwindcss.com/docs/letter-spacing"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:09:21.399Z"
content_hash: "5a3349ba512da613ffa4481ca5b273c858fa79f5023259d082f2204ceb93d75d"
menu_path: ["letter-spacing"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/font-feature-settings/index.md", "title": "font-feature-settings"}
nav_next: {"path": "tailwind/docs/line-clamp/index.md", "title": "line-clamp"}
---

# letter-spacing

Utilities for controlling the tracking, or letter spacing, of an element.

| Class | Styles |
| --- | --- |
| `tracking-tighter` | 
`letter-spacing: var(--tracking-tighter); /* -0.05em */`

 |
| `tracking-tight` | 

`letter-spacing: var(--tracking-tight); /* -0.025em */`

 |
| `tracking-normal` | 

`letter-spacing: var(--tracking-normal); /* 0em */`

 |
| `tracking-wide` | 

`letter-spacing: var(--tracking-wide); /* 0.025em */`

 |
| `tracking-wider` | 

`letter-spacing: var(--tracking-wider); /* 0.05em */`

 |
| `tracking-widest` | 

`letter-spacing: var(--tracking-widest); /* 0.1em */`

 |
| `tracking-(<custom-property>)` | 

`letter-spacing: var(<custom-property>);`

 |
| `tracking-[<value>]` | 

`letter-spacing: <value>;`

 |

Use utilities like `tracking-tight` and `tracking-wide` to set the letter spacing of an element:

tracking-tight

The quick brown fox jumps over the lazy dog.

tracking-normal

The quick brown fox jumps over the lazy dog.

tracking-wide

The quick brown fox jumps over the lazy dog.

```
<p class="tracking-tight ...">The quick brown fox ...</p><p class="tracking-normal ...">The quick brown fox ...</p><p class="tracking-wide ...">The quick brown fox ...</p>
```

Using negative values doesn't make a ton of sense with the named letter spacing scale Tailwind includes out of the box, but if you've customized your scale to use numbers it can be useful:

```
@theme {  --tracking-1: 0em;  --tracking-2: 0.025em;  --tracking-3: 0.05em;  --tracking-4: 0.1em;}
```

To use a negative letter spacing value, prefix the class name with a dash to convert it to a negative value:

```
<p class="-tracking-2">The quick brown fox ...</p>
```

Use the `tracking-[<value>]` syntax to set the letter spacing based on a completely custom value:

```
<p class="tracking-[.25em] ...">  Lorem ipsum dolor sit amet...</p>
```

For CSS variables, you can also use the `tracking-(<custom-property>)` syntax:

```
<p class="tracking-(--my-tracking) ...">  Lorem ipsum dolor sit amet...</p>
```

This is just a shorthand for `tracking-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `letter-spacing` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="tracking-tight md:tracking-wide ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

Use the `--tracking-*` theme variables to customize the letter spacing utilities in your project:

```
@theme {  --tracking-tightest: -0.075em; }
```

Now the `tracking-tightest` utility can be used in your markup:

```
<p class="tracking-tightest">  Lorem ipsum dolor sit amet...</p>
```

Learn more about customizing your theme in the [theme documentation](../theme/index.md#customizing-your-theme).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using negative values](#using-negative-values)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)
-   [Customizing your theme](#customizing-your-theme)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
