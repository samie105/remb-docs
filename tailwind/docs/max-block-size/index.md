---
title: "max-block-size"
source: "https://tailwindcss.com/docs/max-block-size"
canonical_url: "https://tailwindcss.com/docs/max-block-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:06:32.809Z"
content_hash: "5ef26d1a4bc7168ec06df4b954834dacdf7a761fb141dae4d7fe11afce546541"
menu_path: ["max-block-size"]
section_path: []
content_language: "en"
nav_prev: {"path": "../min-block-size/index.md", "title": "min-block-size"}
nav_next: {"path": "../font-family/index.md", "title": "font-family"}
---

Utilities for setting the maximum block size of an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `max-block-<number>` utilities like `max-block-24` and `max-block-64` to set an element to a fixed maximum block size based on the spacing scale:

max-block-80

max-block-64

max-block-48

max-block-40

max-block-32

```
<div class="block-96 ...">  <div class="block-full max-block-80 ...">max-block-80</div>  <div class="block-full max-block-64 ...">max-block-64</div>  <div class="block-full max-block-48 ...">max-block-48</div>  <div class="block-full max-block-40 ...">max-block-40</div>  <div class="block-full max-block-32 ...">max-block-32</div></div>
```

### [Using a percentage](#using-a-percentage)

Use `max-block-full` or `max-block-<fraction>` utilities like `max-block-1/2` and `max-block-2/5` to give an element a percentage-based maximum block size:

max-block-9/10

max-block-3/4

max-block-1/2

max-block-full

```
<div class="block-96 ...">  <div class="block-full max-block-9/10 ...">max-block-9/10</div>  <div class="block-full max-block-3/4 ...">max-block-3/4</div>  <div class="block-full max-block-1/2 ...">max-block-1/2</div>  <div class="block-full max-block-full ...">max-block-full</div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `max-block-[<value>]` syntax to set the maximum block size based on a completely custom value:

```
<div class="max-block-[220px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `max-block-(<custom-property>)` syntax:

```
<div class="max-block-(--my-max-block-size) ...">  <!-- ... --></div>
```

This is just a shorthand for `max-block-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `max-block-size` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="block-48 max-block-full md:max-block-screen ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `max-block-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](../theme/index.md).
