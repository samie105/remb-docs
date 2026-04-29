---
title: "color"
source: "https://tailwindcss.com/docs/color"
canonical_url: "https://tailwindcss.com/docs/color"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:11:06.440Z"
content_hash: "ff5b4008fcf5cae5697c2620322f702a8bd11541f6dfa44f3257b4ad3d3b4ab2"
menu_path: ["color"]
section_path: []
content_language: "en"
nav_prev: {"path": "../text-align/index.md", "title": "text-align"}
nav_next: {"path": "../text-decoration-line/index.md", "title": "text-decoration-line"}
---

Utilities for controlling the text color of an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `text-blue-600` and `text-sky-400` to control the text color of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="text-blue-600 dark:text-sky-400">The quick brown fox...</p>
```

### [Changing the opacity](#changing-the-opacity)

Use the color opacity modifier to control the text color opacity of an element:

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

```
<p class="text-blue-600/100 dark:text-sky-400/100">The quick brown fox...</p><p class="text-blue-600/75 dark:text-sky-400/75">The quick brown fox...</p><p class="text-blue-600/50 dark:text-sky-400/50">The quick brown fox...</p><p class="text-blue-600/25 dark:text-sky-400/25">The quick brown fox...</p>
```

### [Using a custom value](#using-a-custom-value)

Use the `text-[<value>]` syntax to set the text color based on a completely custom value:

```
<p class="text-[#50d71e] ...">  Lorem ipsum dolor sit amet...</p>
```

For CSS variables, you can also use the `text-(<custom-property>)` syntax:

```
<p class="text-(--my-color) ...">  Lorem ipsum dolor sit amet...</p>
```

This is just a shorthand for `text-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Applying on hover](#applying-on-hover)

Prefix a `color` utility with a variant like `hover:*` to only apply the utility in that state:

Hover over the text to see the expected behavior

Oh I gotta get on that [internet](https://en.wikipedia.org/wiki/Internet), I'm late on everything!

```
<p class="...">  Oh I gotta get on that  <a class="underline hover:text-blue-600 dark:hover:text-blue-400" href="https://en.wikipedia.org/wiki/Internet">internet</a>,  I'm late on everything!</p>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

### [Responsive design](#responsive-design)

Prefix a `color` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="text-blue-600 md:text-green-600 ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

Use the `--color-*` theme variables to customize the color utilities in your project:

```
@theme {  --color-regal-blue: #243c5a; }
```

Now the `text-regal-blue` utility can be used in your markup:

```
<p class="text-regal-blue">  Lorem ipsum dolor sit amet...</p>
```

Learn more about customizing your theme in the [theme documentation](../theme/index.md#customizing-your-theme).
