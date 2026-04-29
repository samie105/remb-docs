---
title: "backdrop-filter: hue-rotate()"
source: "https://tailwindcss.com/docs/backdrop-filter-hue-rotate"
canonical_url: "https://tailwindcss.com/docs/backdrop-filter-hue-rotate"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:29:12.143Z"
content_hash: "d713b556f440c950c0e008b69a05c3463868a7b04992cd2828ee09679d6ab2bc"
menu_path: ["backdrop-filter: hue-rotate()"]
section_path: []
content_language: "en"
nav_prev: {"path": "../backdrop-filter-grayscale/index.md", "title": "backdrop-filter: grayscale()"}
nav_next: {"path": "../backdrop-filter-invert/index.md", "title": "backdrop-filter: invert()"}
---

Utilities for applying backdrop hue-rotate filters to an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `backdrop-hue-rotate-90` and `backdrop-hue-rotate-180` to rotate the hue of an element's backdrop:

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-hue-rotate-90 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-hue-rotate-180 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 backdrop-hue-rotate-270 ..."></div></div>
```

### [Using negative values](#using-negative-values)

Use utilities like `-backdrop-hue-rotate-90` and `-backdrop-hue-rotate-180` to set a negative backdrop hue rotation value:

```
<div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 -backdrop-hue-rotate-15 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 -backdrop-hue-rotate-45 ..."></div></div><div class="bg-[url(/img/mountains.jpg)]">  <div class="bg-white/30 -backdrop-hue-rotate-90 ..."></div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `backdrop-hue-rotate-[<value>]` syntax to set the backdrop hue rotation based on a completely custom value:

```
<div class="backdrop-hue-rotate-[3.142rad] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `backdrop-hue-rotate-(<custom-property>)` syntax:

```
<div class="backdrop-hue-rotate-(--my-backdrop-hue-rotation) ...">  <!-- ... --></div>
```

This is just a shorthand for `backdrop-hue-rotate-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `backdrop-filter: hue-rotate()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backdrop-hue-rotate-15 md:backdrop-hue-rotate-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
