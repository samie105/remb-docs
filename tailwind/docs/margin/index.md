---
title: "margin"
source: "https://tailwindcss.com/docs/margin"
canonical_url: "https://tailwindcss.com/docs/margin"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:14.701Z"
content_hash: "d84cb67b2379e29385c7a0edf4c176949e900bd8a188c39eccb07f3bbefd02db"
menu_path: ["margin"]
section_path: []
nav_prev: {"path": "tailwind/docs/padding/index.md", "title": "padding"}
nav_next: {"path": "tailwind/docs/width/index.md", "title": "width"}
---

Utilities for controlling an element's margin.

Class

Styles

`m-<number>`

`margin: calc(var(--spacing) * <number>);`

`-m-<number>`

`margin: calc(var(--spacing) * -<number>);`

`m-auto`

`margin: auto;`

`m-px`

`margin: 1px;`

`-m-px`

`margin: -1px;`

`m-(<custom-property>)`

`margin: var(<custom-property>);`

`m-[<value>]`

`margin: <value>;`

`mx-<number>`

`margin-inline: calc(var(--spacing) * <number>);`

`-mx-<number>`

`margin-inline: calc(var(--spacing) * -<number>);`

`mx-auto`

`margin-inline: auto;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use `m-<number>` utilities like `m-4` and `m-8` to control the margin on all sides of an element:

m-8

```
<div class="m-8 ...">m-8</div>
```

### [Adding margin to a single side](#adding-margin-to-a-single-side)

Use `mt-<number>`, `mr-<number>`, `mb-<number>`, and `ml-<number>` utilities like `ml-2` and `mt-6` to control the margin on one side of an element:

mt-6

mr-4

mb-8

ml-2

```
<div class="mt-6 ...">mt-6</div><div class="mr-4 ...">mr-4</div><div class="mb-8 ...">mb-8</div><div class="ml-2 ...">ml-2</div>
```

### [Adding horizontal margin](#adding-horizontal-margin)

Use `mx-<number>` utilities like `mx-4` and `mx-8` to control the horizontal margin of an element:

mx-8

```
<div class="mx-8 ...">mx-8</div>
```

### [Adding vertical margin](#adding-vertical-margin)

Use `my-<number>` utilities like `my-4` and `my-8` to control the vertical margin of an element:

my-8

```
<div class="my-8 ...">my-8</div>
```

### [Using negative values](#using-negative-values)

To use a negative margin value, prefix the class name with a dash to convert it to a negative value:

\-mt-8

```
<div class="h-16 w-36 bg-sky-400 opacity-20 ..."></div><div class="-mt-8 bg-sky-300 ...">-mt-8</div>
```

### [Using logical properties](#using-logical-properties)

Use `ms-<number>` or `me-<number>` utilities like `ms-4` and `me-8` to set the `margin-inline-start` and `margin-inline-end` logical properties:

Left-to-right

ms-8

me-8

Right-to-left

ms-8

me-8

```
<div>  <div dir="ltr">    <div class="ms-8 ...">ms-8</div>    <div class="me-8 ...">me-8</div>  </div>  <div dir="rtl">    <div class="ms-8 ...">ms-8</div>    <div class="me-8 ...">me-8</div>  </div></div>
```

Use the `mbs-<number>` and `mbe-<number>` utilities to set the `margin-block-start` and `margin-block-end` logical properties, which map to either the top or bottom side based on the writing mode:

```
<div class="mbs-8 ...">mbs-8</div>
```

### [Adding space between children](#adding-space-between-children)

Use `space-x-<number>` or `space-y-<number>` utilities like `space-x-4` and `space-y-8` to control the space between elements:

01

02

03

```
<div class="flex space-x-4 ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

#### [Reversing children order](#reversing-children-order)

If your elements are in reverse order (using say `flex-row-reverse` or `flex-col-reverse`), use the `space-x-reverse` or `space-y-reverse` utilities to ensure the space is added to the correct side of each element:

01

02

03

```
<div class="flex flex-row-reverse space-x-4 space-x-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

#### [Limitations](#limitations)

The space utilities are really just a shortcut for adding margin to all-but-the-last-item in a group, and aren't designed to handle complex cases like grids, layouts that wrap, or situations where the children are rendered in a complex custom order rather than their natural DOM order.

For those situations, it's better to use the [gap utilities](tailwind/docs/gap/index.md) when possible, or add margin to every element with a matching negative margin on the parent.

Additionally, the space utilities are not designed to work together with the [divide utilities](tailwind/docs/border-width/index.md#between-children). For those situations, consider adding margin/padding utilities to the children instead.

### [Using a custom value](#using-a-custom-value)

Use utilities like `m-[<value>]`,`mx-[<value>]`, and `mb-[<value>]` to set the margin based on a completely custom value:

```
<div class="m-[5px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `m-(<custom-property>)` syntax:

```
<div class="m-(--my-margin) ...">  <!-- ... --></div>
```

This is just a shorthand for `m-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `margin` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mt-4 md:mt-8 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `m-<number>`,`mx-<number>`,`my-<number>`,`ms-<number>`,`me-<number>`,`mbs-<number>`,`mbe-<number>`,`mt-<number>`,`mr-<number>`,`mb-<number>`, and `ml-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](tailwind/docs/theme/index.md).

