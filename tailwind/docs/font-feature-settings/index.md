---
title: "font-feature-settings"
source: "https://tailwindcss.com/docs/font-feature-settings"
canonical_url: "https://tailwindcss.com/docs/font-feature-settings"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:01.299Z"
content_hash: "58956cb8d5f7274b234404f56cd14e9e29e6dd67b706d35d41e9917f1ce475cf"
menu_path: ["font-feature-settings"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Typography
2.  font-feature-settings

Typography

# font-feature-settings

Utilities for controlling advanced typographic features.

Class

Styles

`font-features-[<value>]`

`font-feature-settings: <value>;`

`font-features-(<custom-property>)`

`font-feature-settings: var(<custom-property>);`

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `font-features-[<value>]` utility to enable OpenType features in fonts that support them:

```
<p class="font-features-['smcp'] ...">This text uses small caps.</p>
```

### [Enabling multiple features](#enabling-multiple-features)

You can enable multiple OpenType features by separating them with commas:

```
<p class="font-features-['smcp','onum'] ...">This text uses small caps and oldstyle numbers.</p>
```

### [Using CSS variables](#using-css-variables)

Use the `font-features-(<custom-property>)` syntax to apply font feature settings from a CSS variable:

```
<p class="font-features-(--my-features) ...">  <!-- ... --></p>
```

### [Responsive design](#responsive-design)

Prefix a `font-feature-settings` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="font-features-['tnum'] md:font-features-['smcp'] ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Enabling multiple features](#enabling-multiple-features)
    *   [Using CSS variables](#using-css-variables)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
