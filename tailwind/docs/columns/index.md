---
title: "columns"
source: "https://tailwindcss.com/docs/columns"
canonical_url: "https://tailwindcss.com/docs/columns"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:50:52.854Z"
content_hash: "82787c55b3ca2b392702e7a32eb1c5eea8e8649bedc52e8ffebec4c35010412c"
menu_path: ["columns"]
section_path: []
content_language: "en"
---
Layout

Utilities for controlling the number of columns within an element.

## [Examples](#examples)

### [Setting by number](#setting-by-number)

Use `columns-<number>` utilities like `columns-3` to set the number of columns that should be created for the content within an element:

The column width will automatically adjust to accommodate the specified number of columns.

### [Setting by width](#setting-by-width)

Use utilities like `columns-xs` and `columns-sm` to set the ideal column width for the content within an element:

```
<div class="columns-3xs ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

When setting the column width, the number of columns automatically adjusts to ensure they don't get too narrow.

### [Setting the column gap](#setting-the-column-gap)

Use the `gap-<width>` utilities to specify the width between columns:

Learn more about the gap utilities in the [gap documentation](https://tailwindcss.com/docs/gap).

### [Using a custom value](#using-a-custom-value)

Use the `columns-[<value>]` syntax to set the columns based on a completely custom value:

```
<div class="columns-[30vw] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `columns-(<custom-property>)` syntax:

```
<div class="columns-(--my-columns) ...">  <!-- ... --></div>
```

This is just a shorthand for `columns-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `columns` utility with a breakpoint variant like `sm:` to only apply the utility at small screen sizes and above:

```
<div class="columns-2 gap-4 sm:columns-3 sm:gap-8 ...">  <img class="aspect-3/2 ..." src="/img/mountains-1.jpg" />  <img class="aspect-square ..." src="/img/mountains-2.jpg" />  <img class="aspect-square ..." src="/img/mountains-3.jpg" />  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

## [Customizing your theme](#customizing-your-theme)

Use the `--container-*` theme variables to customize the fixed-width column utilities in your project:

```
@theme {  --container-4xs: 14rem; }
```

Now the `columns-4xs` utility can be used in your markup:

```
<div class="columns-4xs">  <!-- ... --></div>
```

Learn more about customizing your theme in the [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme).
