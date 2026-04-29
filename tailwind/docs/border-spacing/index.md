---
title: "border-spacing"
source: "https://tailwindcss.com/docs/border-spacing"
canonical_url: "https://tailwindcss.com/docs/border-spacing"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:30:56.408Z"
content_hash: "36d7e00b446d6e999f160550b225c860bd6d88f933f402584b68de5436d01d32"
menu_path: ["border-spacing"]
section_path: []
content_language: "en"
nav_prev: {"path": "../border-collapse/index.md", "title": "border-collapse"}
nav_next: {"path": "../table-layout/index.md", "title": "table-layout"}
---

Utilities for controlling the spacing between table borders.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `border-spacing-<number>` utilities like `border-spacing-2` and `border-spacing-x-3` to control the space between the borders of table cells with [separate borders](../border-collapse/index.md#separating-table-borders):

| State | City |
| --- | --- |
| Indiana | Indianapolis |
| Ohio | Columbus |
| Michigan | Detroit |

```
<table class="border-separate border-spacing-2 border border-gray-400 dark:border-gray-500">  <thead>    <tr>      <th class="border border-gray-300 dark:border-gray-600">State</th>      <th class="border border-gray-300 dark:border-gray-600">City</th>    </tr>  </thead>  <tbody>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Indiana</td>      <td class="border border-gray-300 dark:border-gray-700">Indianapolis</td>    </tr>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Ohio</td>      <td class="border border-gray-300 dark:border-gray-700">Columbus</td>    </tr>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Michigan</td>      <td class="border border-gray-300 dark:border-gray-700">Detroit</td>    </tr>  </tbody></table>
```

### [Using a custom value](#using-a-custom-value)

Use the `border-spacing-[<value>]` syntax to set the border spacing based on a completely custom value:

```
<table class="border-spacing-[7px] ...">  <!-- ... --></table>
```

For CSS variables, you can also use the `border-spacing-(<custom-property>)` syntax:

```
<table class="border-spacing-(--my-border-spacing) ...">  <!-- ... --></table>
```

This is just a shorthand for `border-spacing-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `border-spacing` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<table class="border-spacing-2 md:border-spacing-4 ...">  <!-- ... --></table>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

The `border-spacing-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
@theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](../theme/index.md).
