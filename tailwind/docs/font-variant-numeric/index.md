---
title: "font-variant-numeric"
source: "https://tailwindcss.com/docs/font-variant-numeric"
canonical_url: "https://tailwindcss.com/docs/font-variant-numeric"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:08:48.332Z"
content_hash: "33c223bd857d1c0251addf014d896f3b9c92743969e7c0d92679f3a6ad45d29c"
menu_path: ["font-variant-numeric"]
section_path: []
content_language: "en"
nav_prev: {"path": "../font-stretch/index.md", "title": "font-stretch"}
nav_next: {"path": "../font-feature-settings/index.md", "title": "font-feature-settings"}
---

# font-variant-numeric

Utilities for controlling the variant of numbers.

| Class | Styles |
| --- | --- |
| `normal-nums` | 
`font-variant-numeric: normal;`

 |
| `ordinal` | 

`font-variant-numeric: ordinal;`

 |
| `slashed-zero` | 

`font-variant-numeric: slashed-zero;`

 |
| `lining-nums` | 

`font-variant-numeric: lining-nums;`

 |
| `oldstyle-nums` | 

`font-variant-numeric: oldstyle-nums;`

 |
| `proportional-nums` | 

`font-variant-numeric: proportional-nums;`

 |
| `tabular-nums` | 

`font-variant-numeric: tabular-nums;`

 |
| `diagonal-fractions` | 

`font-variant-numeric: diagonal-fractions;`

 |
| `stacked-fractions` | 

`font-variant-numeric: stacked-fractions;`

 |

Use the `ordinal` utility to enable special glyphs for the ordinal markers in fonts that support them:

1st

```
<p class="ordinal ...">1st</p>
```

Use the `slashed-zero` utility to force a zero with a slash in fonts that support them:

0

```
<p class="slashed-zero ...">0</p>
```

Use the `lining-nums` utility to use numeric glyphs that are aligned by their baseline in fonts that support them:

1234567890

```
<p class="lining-nums ...">1234567890</p>
```

Use the `oldstyle-nums` utility to use numeric glyphs where some numbers have descenders in fonts that support them:

1234567890

```
<p class="oldstyle-nums ...">1234567890</p>
```

Use the `proportional-nums` utility to use numeric glyphs that have proportional widths in fonts that support them:

12121

90909

```
<p class="proportional-nums ...">12121</p><p class="proportional-nums ...">90909</p>
```

Use the `tabular-nums` utility to use numeric glyphs that have uniform/tabular widths in fonts that support them:

12121

90909

```
<p class="tabular-nums ...">12121</p><p class="tabular-nums ...">90909</p>
```

Use the `diagonal-fractions` utility to replace numbers separated by a slash with common diagonal fractions in fonts that support them:

1/2 3/4 5/6

```
<p class="diagonal-fractions ...">1/2 3/4 5/6</p>
```

Use the `stacked-fractions` utility to replace numbers separated by a slash with common stacked fractions in fonts that support them:

1/2 3/4 5/6

```
<p class="stacked-fractions ...">1/2 3/4 5/6</p>
```

The `font-variant-numeric` utilities are composable so you can enable multiple variants by combining them:

Subtotal

$100.00

Tax

$14.50

Total

$114.50

```
<dl class="...">  <dt class="...">Subtotal</dt>  <dd class="text-right slashed-zero tabular-nums ...">$100.00</dd>  <dt class="...">Tax</dt>  <dd class="text-right slashed-zero tabular-nums ...">$14.50</dd>  <dt class="...">Total</dt>  <dd class="text-right slashed-zero tabular-nums ...">$114.50</dd></dl>
```

Use the `normal-nums` property to reset numeric font variants:

```
<p class="slashed-zero tabular-nums md:normal-nums ...">  <!-- ... --></p>
```

Prefix a `font-variant-numeric` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="proportional-nums md:tabular-nums ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Using ordinal glyphs](#using-ordinal-glyphs)
    -   [Using slashed zeroes](#using-slashed-zeroes)
    -   [Using lining figures](#using-lining-figures)
    -   [Using oldstyle figures](#using-oldstyle-figures)
    -   [Using proportional figures](#using-proportional-figures)
    -   [Using tabular figures](#using-tabular-figures)
    -   [Using diagonal fractions](#using-diagonal-fractions)
    -   [Using stacked fractions](#using-stacked-fractions)
    -   [Stacking multiple utilities](#stacking-multiple-utilities)
    -   [Resetting numeric font variants](#resetting-numeric-font-variants)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
