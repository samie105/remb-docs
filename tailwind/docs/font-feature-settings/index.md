---
title: "font-feature-settings"
source: "https://tailwindcss.com/docs/font-feature-settings"
canonical_url: "https://tailwindcss.com/docs/font-feature-settings"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:08:49.475Z"
content_hash: "8ceb5430d76ed99a9ee043219d119811538730e2dd2106502b0af144aa1d1ca4"
menu_path: ["font-feature-settings"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Typography
2.  font-feature-settings

Typography

# font-feature-settings

Utilities for controlling advanced typographic features.

| Class | Styles |
| --- | --- |
| `font-features-[<value>]` | 
`font-feature-settings: <value>;`

 |
| `font-features-(<custom-property>)` | 

`font-feature-settings: var(<custom-property>);`

 |

Use the `font-features-[<value>]` utility to enable OpenType features in fonts that support them:

```
<p class="font-features-['smcp'] ...">This text uses small caps.</p>
```

You can enable multiple OpenType features by separating them with commas:

```
<p class="font-features-['smcp','onum'] ...">This text uses small caps and oldstyle numbers.</p>
```

Use the `font-features-(<custom-property>)` syntax to apply font feature settings from a CSS variable:

```
<p class="font-features-(--my-features) ...">  <!-- ... --></p>
```

Prefix a `font-feature-settings` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="font-features-['tnum'] md:font-features-['smcp'] ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Enabling multiple features](#enabling-multiple-features)
    -   [Using CSS variables](#using-css-variables)
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
