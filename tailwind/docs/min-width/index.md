---
title: "min-width"
source: "https://tailwindcss.com/docs/min-width"
canonical_url: "https://tailwindcss.com/docs/min-width"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:03:38.232Z"
content_hash: "cad0ee118d2bf4e05e6dbf539470d46ecd72cf5390a55970cd14481d184f0f0b"
menu_path: ["min-width"]
section_path: []
content_language: "en"
nav_prev: {"path": "../width/index.md", "title": "width"}
nav_next: {"path": "../max-width/index.md", "title": "max-width"}
---

Sizing

Utilities for setting the minimum width of an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `min-w-<number>` utilities like `min-w-24` and `min-w-64` to set an element to a fixed minimum width based on the spacing scale:

min-w-80

min-w-64

min-w-48

min-w-40

min-w-32

min-w-24

```
<div class="w-20 ...">  <div class="min-w-80 ...">min-w-80</div>  <div class="min-w-64 ...">min-w-64</div>  <div class="min-w-48 ...">min-w-48</div>  <div class="min-w-40 ...">min-w-40</div>  <div class="min-w-32 ...">min-w-32</div>  <div class="min-w-24 ...">min-w-24</div></div>
```

### [Using a percentage](#using-a-percentage)

Use `min-w-full` or `min-w-<fraction>` utilities like `min-w-1/2` and `min-w-2/5` to give an element a percentage-based minimum width:

min-w-3/4

w-full

```
<div class="flex ...">  <div class="min-w-3/4 ...">min-w-3/4</div>  <div class="w-full ...">w-full</div></div>
```

### [Using the container scale](#using-the-container-scale)

Use utilities like `min-w-sm` and `min-w-xl` to set an element to a fixed minimum width based on the container scale:

min-w-lg

min-w-md

min-w-sm

min-w-xs

min-w-2xs

min-w-3xs

```
<div class="w-40 ...">  <div class="min-w-lg ...">min-w-lg</div>  <div class="min-w-md ...">min-w-md</div>  <div class="min-w-sm ...">min-w-sm</div>  <div class="min-w-xs ...">min-w-xs</div>  <div class="min-w-2xs ...">min-w-2xs</div>  <div class="min-w-3xs ...">min-w-3xs</div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `min-w-[<value>]` syntax to set the minimum width based on a completely custom value:

```
<div class="min-w-[220px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `min-w-(<custom-property>)` syntax:

```
<div class="min-w-(--my-min-width) ...">  <!-- ... --></div>
```

This is just a shorthand for `min-w-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `min-width` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="w-24 min-w-full md:min-w-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `min-w-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](../theme/index.md).
