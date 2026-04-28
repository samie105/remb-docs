---
title: "min-height"
source: "https://tailwindcss.com/docs/min-height"
canonical_url: "https://tailwindcss.com/docs/min-height"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:04:44.191Z"
content_hash: "5d7648abe5c8bdbc63ce9fae20b80f8db87a917985fcf541db404611d9938497"
menu_path: ["min-height"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/height/index.md", "title": "height"}
nav_next: {"path": "tailwind/docs/max-height/index.md", "title": "max-height"}
---

Utilities for setting the minimum height of an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `min-h-<number>` utilities like `min-h-24` and `min-h-64` to set an element to a fixed minimum height based on the spacing scale:

min-h-96

min-h-80

min-h-64

min-h-48

min-h-40

min-h-32

min-h-24

```
<div class="h-20 ...">  <div class="min-h-80 ...">min-h-80</div>  <div class="min-h-64 ...">min-h-64</div>  <div class="min-h-48 ...">min-h-48</div>  <div class="min-h-40 ...">min-h-40</div>  <div class="min-h-32 ...">min-h-32</div>  <div class="min-h-24 ...">min-h-24</div></div>
```

### [Using a percentage](#using-a-percentage)

Use `min-h-full` or `min-h-<fraction>` utilities like `min-h-1/2`, and `min-h-2/5` to give an element a percentage-based minimum height:

min-h-full

min-h-9/10

min-h-3/4

min-h-1/2

min-h-1/3

```
<div class="min-h-full ...">min-h-full</div><div class="min-h-9/10 ...">min-h-9/10</div><div class="min-h-3/4 ...">min-h-3/4</div><div class="min-h-1/2 ...">min-h-1/2</div><div class="min-h-1/3 ...">min-h-1/3</div>
```

### [Using a custom value](#using-a-custom-value)

Use the `min-h-[<value>]` syntax to set the minimum height based on a completely custom value:

```
<div class="min-h-[220px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `min-h-(<custom-property>)` syntax:

```
<div class="min-h-(--my-min-height) ...">  <!-- ... --></div>
```

This is just a shorthand for `min-h-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `min-height` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="h-24 min-h-0 md:min-h-full ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `min-h-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](tailwind/docs/theme/index.md).
