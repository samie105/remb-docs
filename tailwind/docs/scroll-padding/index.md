---
title: "scroll-padding"
source: "https://tailwindcss.com/docs/scroll-padding"
canonical_url: "https://tailwindcss.com/docs/scroll-padding"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:39:06.961Z"
content_hash: "fa9ff50257c9f82c01665fd514119aeefc15e3d7903ae02e793d8dd0278e86cb"
menu_path: ["scroll-padding"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/scroll-margin/index.md", "title": "scroll-margin"}
nav_next: {"path": "tailwind/docs/scroll-snap-align/index.md", "title": "scroll-snap-align"}
---

Utilities for controlling an element's scroll offset within a snap container.

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `scroll-pt-<number>`, `scroll-pr-<number>`, `scroll-pb-<number>`, and `scroll-pl-<number>` utilities like `scroll-pl-4` and `scroll-pt-6` to set the scroll offset of an element within a snap container:

Scroll in the grid of images to see the expected behavior

```
<div class="snap-x scroll-pl-6 ...">  <div class="snap-start ...">    <img src="/img/vacation-01.jpg" />  </div>  <div class="snap-start ...">    <img src="/img/vacation-02.jpg" />  </div>  <div class="snap-start ...">    <img src="/img/vacation-03.jpg" />  </div>  <div class="snap-start ...">    <img src="/img/vacation-04.jpg" />  </div>  <div class="snap-start ...">    <img src="/img/vacation-05.jpg" />  </div></div>
```

### [Using logical properties](#using-logical-properties)

Use the `scroll-ps-<number>` and `scroll-pe-<number>` utilities to set the `scroll-padding-inline-start` and `scroll-padding-inline-end` logical properties, which map to either the left or right side based on the text direction:

Scroll in the grid of images to see the expected behavior

Left-to-right

Right-to-left

```
<div dir="ltr">  <div class="snap-x scroll-ps-6 ...">    <!-- ... -->  </div></div><div dir="rtl">  <div class="snap-x scroll-ps-6 ...">    <!-- ... -->  </div></div>
```

Use the `scroll-pbs-<number>` and `scroll-pbe-<number>` utilities to set the `scroll-padding-block-start` and `scroll-padding-block-end` logical properties, which map to either the top or bottom side based on the writing mode:

```
<div class="snap-y scroll-pbs-6 ...">  <!-- ... --></div>
```

### [Using negative values](#using-negative-values)

To use a negative scroll padding value, prefix the class name with a dash to convert it to a negative value:

```
<div class="-scroll-ps-6 snap-x ...">  <!-- ... --></div>
```

### [Using a custom value](#using-a-custom-value)

Use utilities like `scroll-pl-[<value>]` and `scroll-pe-[<value>]` to set the scroll padding based on a completely custom value:

```
<div class="scroll-pl-[24rem] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `scroll-pl-(<custom-property>)` syntax:

```
<div class="scroll-pl-(--my-scroll-padding) ...">  <!-- ... --></div>
```

This is just a shorthand for `scroll-pl-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `scroll-padding` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="scroll-p-8 md:scroll-p-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `scroll-p-<number>`,`scroll-px-<number>`,`scroll-py-<number>`,`scroll-ps-<number>`,`scroll-pe-<number>`,`scroll-pbs-<number>`,`scroll-pbe-<number>`,`scroll-pt-<number>`,`scroll-pr-<number>`,`scroll-pb-<number>`, and `scroll-pl-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](tailwind/docs/theme/index.md).
