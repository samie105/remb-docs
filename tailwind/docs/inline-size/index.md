---
title: "inline-size"
source: "https://tailwindcss.com/docs/inline-size"
canonical_url: "https://tailwindcss.com/docs/inline-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:05:19.017Z"
content_hash: "273b8edf185e8e327d52f7b0af85f1191562f31c076a59218de48db8c0124c16"
menu_path: ["inline-size"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/max-height/index.md", "title": "max-height"}
nav_next: {"path": "tailwind/docs/min-inline-size/index.md", "title": "min-inline-size"}
---

Sizing

Utilities for setting the inline size of an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `inline-<number>` utilities like `inline-24` and `inline-64` to set an element to a fixed inline size based on the spacing scale:

inline-96

inline-80

inline-64

inline-48

inline-40

inline-32

```
<div class="inline-96 ...">inline-96</div><div class="inline-80 ...">inline-80</div><div class="inline-64 ...">inline-64</div><div class="inline-48 ...">inline-48</div><div class="inline-40 ...">inline-40</div><div class="inline-32 ...">inline-32</div>
```

### [Using a percentage](#using-a-percentage)

Use `inline-full` or `inline-<fraction>` utilities like `inline-1/2` and `inline-2/5` to give an element a percentage-based inline size:

inline-1/2

inline-1/2

inline-2/5

inline-3/5

inline-1/3

inline-2/3

inline-full

```
<div class="flex ...">  <div class="inline-1/2 ...">inline-1/2</div>  <div class="inline-1/2 ...">inline-1/2</div></div><div class="flex ...">  <div class="inline-2/5 ...">inline-2/5</div>  <div class="inline-3/5 ...">inline-3/5</div></div><div class="flex ...">  <div class="inline-1/3 ...">inline-1/3</div>  <div class="inline-2/3 ...">inline-2/3</div></div><div class="inline-full ...">inline-full</div>
```

### [Using the container scale](#using-the-container-scale)

Use utilities like `inline-sm` and `inline-xl` to set an element to a fixed inline size based on the container scale:

inline-xl

inline-lg

inline-md

inline-sm

inline-xs

inline-2xs

inline-3xs

```
<div class="inline-xl ...">inline-xl</div><div class="inline-lg ...">inline-lg</div><div class="inline-md ...">inline-md</div><div class="inline-sm ...">inline-sm</div><div class="inline-xs ...">inline-xs</div><div class="inline-2xs ...">inline-2xs</div><div class="inline-3xs ...">inline-3xs</div>
```

### [Matching the viewport](#matching-the-viewport)

Use the `inline-screen` utility to make an element span the entire inline size of the viewport:

```
<div class="inline-screen">  <!-- ... --></div>
```

### [Resetting the inline size](#resetting-the-inline-size)

Use the `inline-auto` utility to remove an element's assigned inline size under a specific condition, like at a particular breakpoint:

```
<div class="inline-full md:inline-auto">  <!-- ... --></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `inline-[<value>]` syntax to set the inline size based on a completely custom value:

```
<div class="inline-[5px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `inline-(<custom-property>)` syntax:

```
<div class="inline-(--my-inline-size) ...">  <!-- ... --></div>
```

This is just a shorthand for `inline-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix an `inline-size` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="inline-1/2 md:inline-full ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `inline-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](tailwind/docs/theme/index.md).
