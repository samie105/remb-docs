---
title: "min-block-size"
source: "https://tailwindcss.com/docs/min-block-size"
canonical_url: "https://tailwindcss.com/docs/min-block-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:11.488Z"
content_hash: "198a0981a542c61e3e8c1a8c7f928ab8ccccda42f3f472a144702490849fa407"
menu_path: ["min-block-size"]
section_path: []
---
Utilities for setting the minimum block size of an element.

Class

Styles

`min-block-<number>`

`min-block-size: calc(var(--spacing) * <number>);`

`min-block-<fraction>`

`min-block-size: calc(<fraction> * 100%);`

`min-block-px`

`min-block-size: 1px;`

`min-block-full`

`min-block-size: 100%;`

`min-block-screen`

`min-block-size: 100vh;`

`min-block-dvh`

`min-block-size: 100dvh;`

`min-block-dvw`

`min-block-size: 100dvw;`

`min-block-lvh`

`min-block-size: 100lvh;`

`min-block-lvw`

`min-block-size: 100lvw;`

`min-block-svw`

`min-block-size: 100svw;`

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

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

## [Customizing your theme](#customizing-your-theme)

The `min-block-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](https://tailwindcss.com/docs/theme).
