---
title: "Functions and directives"
source: "https://tailwindcss.com/docs/functions-and-directives"
canonical_url: "https://tailwindcss.com/docs/functions-and-directives"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:49:57.947Z"
content_hash: "a407ff5b9aad75c4fd16a143f78e057e12c2713a84de63216853c8650394f5dd"
menu_path: ["Functions and directives"]
section_path: []
content_language: "en"
nav_prev: {"path": "../detecting-classes-in-source-files/index.md", "title": "Detecting classes in source files"}
nav_next: {"path": "../preflight/index.md", "title": "Preflight"}
---

A reference for the custom functions and directives Tailwind exposes to your CSS.

## [Directives](#directives)

Directives are custom Tailwind-specific [at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/At-rule) you can use in your CSS that offer special functionality for Tailwind CSS projects.

### [@import](#import-directive)

Use the `@import` directive to inline import CSS files, including Tailwind itself:

### [@theme](#theme-directive)

Use the `@theme` directive to define your project's custom design tokens, like fonts, colors, and breakpoints:

```
@theme {  --font-display: "Satoshi", "sans-serif";  --breakpoint-3xl: 120rem;  --color-avocado-100: oklch(0.99 0 0);  --color-avocado-200: oklch(0.98 0.04 113.22);  --color-avocado-300: oklch(0.94 0.11 115.03);  --color-avocado-400: oklch(0.92 0.19 114.08);  --color-avocado-500: oklch(0.84 0.18 117.33);  --color-avocado-600: oklch(0.53 0.12 118.34);  --ease-fluid: cubic-bezier(0.3, 0, 0, 1);  --ease-snappy: cubic-bezier(0.2, 0, 0, 1);  /* ... */}
```

Learn more about customizing your theme in the [theme variables documentation](../theme/index.md).

### [@source](#source-directive)

Use the `@source` directive to explicitly specify source files that aren't picked up by Tailwind's automatic content detection:

```
@source "../node_modules/@my-company/ui-lib";
```

Learn more about automatic content detection in the [detecting classes in source files documentation](../detecting-classes-in-source-files/index.md).

### [@utility](#utility-directive)

Use the `@utility` directive to add custom utilities to your project that work with variants like `hover`, `focus` and `lg`:

```
@utility tab-4 {  tab-size: 4;}
```

Learn more about registering custom utilities in the [adding custom utilities documentation](../adding-custom-styles/index.md#adding-custom-utilities).

### [@variant](#variant-directive)

Use the `@variant` directive to apply a Tailwind variant to styles in your CSS:

```
.my-element {  background: white;  @variant dark {    background: black;  }}
```

Learn more using variants in the [using variants documentation](../adding-custom-styles/index.md#using-variants).

### [@custom-variant](#custom-variant-directive)

Use the `@custom-variant` directive to add a custom variant in your project:

```
@custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

This lets you write utilities `theme-midnight:bg-black` and `theme-midnight:text-white`.

Learn more about adding custom variants in the [adding custom variants documentation](../adding-custom-styles/index.md#adding-custom-variants).

### [@apply](#apply-directive)

Use the `@apply` directive to inline any existing utility classes into your own custom CSS:

```
.select2-dropdown {  @apply rounded-b-lg shadow-md;}.select2-search {  @apply rounded border border-gray-300;}.select2-results__group {  @apply text-lg font-bold text-gray-900;}
```

This is useful when you need to write custom CSS (like to override the styles in a third-party library) but still want to work with your design tokens and use the same syntax you’re used to using in your HTML.

### [@reference](#reference-directive)

If you want to use `@apply` or `@variant` in the `<style>` block of a Vue or Svelte component, or within CSS modules, you will need to import your theme variables, custom utilities, and custom variants to make those values available in that context.

To do this without duplicating any CSS in your output, use the `@reference` directive to import your main stylesheet for reference without actually including the styles:

```
<template>  <h1>Hello world!</h1></template><style>  @reference "../../app.css";  h1 {    @apply text-2xl font-bold text-red-500;  }</style>
```

If you’re just using the default theme with no customizations (e.g. by using things like `@theme`, `@custom-variant`, `@plugin`, etc…), you can import `tailwindcss` directly:

```
<template>  <h1>Hello world!</h1></template><style>  @reference "tailwindcss";  h1 {    @apply text-2xl font-bold text-red-500;  }</style>
```

### [Subpath Imports](#subpath-imports)

When using the CLI, Vite, or PostCSS the directives `@import`, `@reference`, `@plugin`, and `@config` all support [subpath imports](https://nodejs.org/api/packages.html#subpath-imports) which work similarly to bundler and TypeScript path aliases:

```
{  // ...  "imports": {    "#app.css": "./src/css/app.css"  }}
```

```
<template>  <h1>Hello world!</h1></template><style>  @reference "#app.css";  h1 {    @apply text-2xl font-bold text-red-500;  }</style>
```

## [Functions](#functions)

Tailwind provides the following build-time functions to make working with colors and the spacing scale easier.

### [\--alpha()](#alpha-function)

Use the `--alpha()` function to adjust the opacity of a color:

```
.my-element {  color: --alpha(var(--color-lime-300) / 50%);}
```

```
.my-element {  color: color-mix(in oklab, var(--color-lime-300) 50%, transparent);}
```

### [\--spacing()](#spacing-function)

Use the `--spacing()` function to generate a spacing value based on your theme:

```
.my-element {  margin: --spacing(4);}
```

```
.my-element {  margin: calc(var(--spacing) * 4);}
```

This can also be useful in arbitrary values, especially in combination with `calc()`:

```
<div class="py-[calc(--spacing(4)-1px)]">  <!-- ... --></div>
```

## [Compatibility](#compatibility)

The following directives and functions exist solely for compatibility with Tailwind CSS v3.x.

The `@config` and `@plugin` directives may be used in conjunction with `@theme`, `@utility`, and other CSS-driven features. This can be used to incrementally move over your theme, custom configuration, utilities, variants, and presets to CSS. Things defined in CSS will be merged where possible and otherwise take precedence over those defined in configs, presets, and plugins.

### [@config](#config-directive)

Use the `@config` directive to load a legacy JavaScript-based configuration file:

```
@config "../../tailwind.config.js";
```

The `corePlugins`, `safelist`, and `separator` options from the JavaScript-based config are not supported in v4.0. To safelist utilities in v4 use [`@source inline()`](../detecting-classes-in-source-files/index.md#safelisting-specific-utilities).

### [@plugin](#plugin-directive)

Use the `@plugin` directive to load a legacy JavaScript-based plugin:

```
@plugin "@tailwindcss/typography";
```

The `@plugin` directive accepts either a package name or a local path.

### [theme()](#theme-function)

Use the `theme()` function to access your Tailwind theme values using dot notation:

```
.my-element {  margin: theme(spacing.12);}
```

This function is deprecated, and we recommend [using CSS theme variables](../theme/index.md#using-your-theme-variables) instead.
