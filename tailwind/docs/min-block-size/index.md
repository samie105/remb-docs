---
title: "min-block-size"
source: "https://tailwindcss.com/docs/min-block-size"
canonical_url: "https://tailwindcss.com/docs/min-block-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:06:30.012Z"
content_hash: "84b89c50d455ee4351f23ede4bb0124e0708528afe912ecf29ab40d88abe01ab"
menu_path: ["min-block-size"]
section_path: []
content_language: "en"
nav_prev: {"path": "../block-size/index.md", "title": "block-size"}
nav_next: {"path": "../max-block-size/index.md", "title": "max-block-size"}
---

Utilities for setting the minimum block size of an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `min-block-<number>` utilities like `min-block-24` and `min-block-64` to set an element to a fixed minimum block size based on the spacing scale:

min-block-96

min-block-80

min-block-64

min-block-48

min-block-40

min-block-32

```
<div class="block-20 ...">  <div class="min-block-80 ...">min-block-80</div>  <div class="min-block-64 ...">min-block-64</div>  <div class="min-block-48 ...">min-block-48</div>  <div class="min-block-40 ...">min-block-40</div>  <div class="min-block-32 ...">min-block-32</div></div>
```

### [Using a percentage](#using-a-percentage)

Use `min-block-full` or `min-block-<fraction>` utilities like `min-block-1/2`, and `min-block-2/5` to give an element a percentage-based minimum block size:

min-block-full

min-block-9/10

min-block-3/4

min-block-1/2

min-block-1/3

```
<div class="min-block-full ...">min-block-full</div><div class="min-block-9/10 ...">min-block-9/10</div><div class="min-block-3/4 ...">min-block-3/4</div><div class="min-block-1/2 ...">min-block-1/2</div><div class="min-block-1/3 ...">min-block-1/3</div>
```

### [Using a custom value](#using-a-custom-value)

Use the `min-block-[<value>]` syntax to set the minimum block size based on a completely custom value:

```
<div class="min-block-[220px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `min-block-(<custom-property>)` syntax:

```
<div class="min-block-(--my-min-block-size) ...">  <!-- ... --></div>
```

This is just a shorthand for `min-block-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `min-block-size` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="block-24 min-block-0 md:min-block-full ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `min-block-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](../theme/index.md).
