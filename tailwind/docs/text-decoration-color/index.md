---
title: "text-decoration-color"
source: "https://tailwindcss.com/docs/text-decoration-color"
canonical_url: "https://tailwindcss.com/docs/text-decoration-color"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:11:41.307Z"
content_hash: "370bcced80db52b844987936ff3bc26b8c799df15538d1522215aaf4b01eb86f"
menu_path: ["text-decoration-color"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/text-decoration-line/index.md", "title": "text-decoration-line"}
nav_next: {"path": "tailwind/docs/text-decoration-style/index.md", "title": "text-decoration-style"}
---

Utilities for controlling the color of text decorations.

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `decoration-sky-500` and `decoration-pink-500` to change the [text decoration](tailwind/docs/text-decoration-line/index.md) color of an element:

```
<p>  I’m Derek, an astro-engineer based in Tattooine. I like to build X-Wings  at <a class="underline decoration-sky-500">My Company, Inc</a>. Outside  of work, I like to <a class="underline decoration-pink-500">watch pod-racing</a>  and have <a class="underline decoration-indigo-500">light-saber</a> fights.</p>
```

### [Changing the opacity](#changing-the-opacity)

Use the color opacity modifier to control the text decoration color opacity of an element:

```
<p>  I’m Derek, an astro-engineer based in Tattooine. I like to build X-Wings  at <a class="underline decoration-sky-500/30">My Company, Inc</a>. Outside  of work, I like to <a class="underline decoration-pink-500/30">watch pod-racing</a>  and have <a class="underline decoration-indigo-500/30">light-saber</a> fights.</p>
```

### [Using a custom value](#using-a-custom-value)

Use the `decoration-[<value>]` syntax to set the text decoration color based on a completely custom value:

```
<p class="decoration-[#50d71e] ...">  Lorem ipsum dolor sit amet...</p>
```

For CSS variables, you can also use the `decoration-(<custom-property>)` syntax:

```
<p class="decoration-(--my-color) ...">  Lorem ipsum dolor sit amet...</p>
```

This is just a shorthand for `decoration-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Applying on hover](#applying-on-hover)

Prefix a `text-decoration-color` utility with a variant like `hover:*` to only apply the utility in that state:

Hover over the text to see the expected behavior

```
<p>The <a href="..." class="underline hover:decoration-pink-500 ...">quick brown fox</a> jumps over the lazy dog.</p>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

### [Responsive design](#responsive-design)

Prefix a `text-decoration-color` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="underline decoration-sky-600 md:decoration-blue-400 ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

Use the `--color-*` theme variables to customize the color utilities in your project:

```
@theme {  --color-regal-blue: #243c5a; }
```

Now the `decoration-regal-blue` utility can be used in your markup:

```
<p class="decoration-regal-blue">  Lorem ipsum dolor sit amet...</p>
```

Learn more about customizing your theme in the [theme documentation](tailwind/docs/theme/index.md#customizing-your-theme).
