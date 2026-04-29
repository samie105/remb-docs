---
title: "max-inline-size"
source: "https://tailwindcss.com/docs/max-inline-size"
canonical_url: "https://tailwindcss.com/docs/max-inline-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:05:54.862Z"
content_hash: "2bbc3d776c526dd1bee0b06290aca38f6940896d401e717fed53d3657cc38906"
menu_path: ["max-inline-size"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/min-inline-size/index.md", "title": "min-inline-size"}
nav_next: {"path": "tailwind/docs/block-size/index.md", "title": "block-size"}
---

Sizing

Utilities for setting the maximum inline size of an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `max-inline-<number>` utilities like `max-inline-24` and `max-inline-64` to set an element to a fixed maximum inline size based on the spacing scale:

Resize the example to see the expected behavior

```
<div class="inline-full max-inline-96 ...">max-inline-96</div><div class="inline-full max-inline-80 ...">max-inline-80</div><div class="inline-full max-inline-64 ...">max-inline-64</div><div class="inline-full max-inline-48 ...">max-inline-48</div><div class="inline-full max-inline-40 ...">max-inline-40</div><div class="inline-full max-inline-32 ...">max-inline-32</div>
```

### [Using a percentage](#using-a-percentage)

Use `max-inline-full` or `max-inline-<fraction>` utilities like `max-inline-1/2` and `max-inline-2/5` to give an element a percentage-based maximum inline size:

Resize the example to see the expected behavior

```
<div class="inline-full max-inline-9/10 ...">max-inline-9/10</div><div class="inline-full max-inline-3/4 ...">max-inline-3/4</div><div class="inline-full max-inline-1/2 ...">max-inline-1/2</div><div class="inline-full max-inline-1/3 ...">max-inline-1/3</div>
```

### [Using the container scale](#using-the-container-scale)

Use utilities like `max-inline-sm` and `max-inline-xl` to set an element to a fixed maximum inline size based on the container scale:

Resize the example to see the expected behavior

```
<div class="max-inline-md ...">  <!-- ... --></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `max-inline-[<value>]` syntax to set the maximum inline size based on a completely custom value:

```
<div class="max-inline-[220px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `max-inline-(<custom-property>)` syntax:

```
<div class="max-inline-(--my-max-inline-size) ...">  <!-- ... --></div>
```

This is just a shorthand for `max-inline-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `max-inline-size` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="max-inline-sm md:max-inline-lg ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `max-inline-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](../theme/index.md).
