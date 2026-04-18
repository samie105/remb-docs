---
title: "max-height"
source: "https://tailwindcss.com/docs/max-height"
canonical_url: "https://tailwindcss.com/docs/max-height"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:44.354Z"
content_hash: "b76620e598acbcaaf7b1eda6c8b7527a43974b19aea6f7f98cfc1f9514baca1e"
menu_path: ["max-height"]
section_path: []
nav_prev: {"path": "tailwind/docs/min-height/index.md", "title": "min-height"}
nav_next: {"path": "tailwind/docs/inline-size/index.md", "title": "inline-size"}
---

Utilities for setting the maximum height of an element.

Class

Styles

`max-h-<number>`

`max-height: calc(var(--spacing) * <number>);`

`max-h-<fraction>`

`max-height: calc(<fraction> * 100%);`

`max-h-none`

`max-height: none;`

`max-h-px`

`max-height: 1px;`

`max-h-full`

`max-height: 100%;`

`max-h-screen`

`max-height: 100vh;`

`max-h-dvh`

`max-height: 100dvh;`

`max-h-dvw`

`max-height: 100dvw;`

`max-h-lvh`

`max-height: 100lvh;`

`max-h-lvw`

`max-height: 100lvw;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use `max-h-<number>` utilities like `max-h-24` and `max-h-64` to set an element to a fixed maximum height based on the spacing scale:

max-h-80

max-h-64

max-h-48

max-h-40

max-h-32

max-h-24

```
<div class="h-96 ...">  <div class="h-full max-h-80 ...">max-h-80</div>  <div class="h-full max-h-64 ...">max-h-64</div>  <div class="h-full max-h-48 ...">max-h-48</div>  <div class="h-full max-h-40 ...">max-h-40</div>  <div class="h-full max-h-32 ...">max-h-32</div>  <div class="h-full max-h-24 ...">max-h-24</div></div>
```

### [Using a percentage](#using-a-percentage)

Use `max-h-full` or `max-h-<fraction>` utilities like `max-h-1/2` and `max-h-2/5` to give an element a percentage-based maximum height:

max-h-9/10

max-h-3/4

max-h-1/2

max-h-1/4

max-h-full

```
<div class="h-96 ...">  <div class="h-full max-h-9/10 ...">max-h-9/10</div>  <div class="h-full max-h-3/4 ...">max-h-3/4</div>  <div class="h-full max-h-1/2 ...">max-h-1/2</div>  <div class="h-full max-h-1/4 ...">max-h-1/4</div>  <div class="h-full max-h-full ...">max-h-full</div></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `max-h-[<value>]` syntax to set the maximum height based on a completely custom value:

```
<div class="max-h-[220px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `max-h-(<custom-property>)` syntax:

```
<div class="max-h-(--my-max-height) ...">  <!-- ... --></div>
```

This is just a shorthand for `max-h-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `max-height` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="h-48 max-h-full md:max-h-screen ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `max-h-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](tailwind/docs/theme/index.md).

