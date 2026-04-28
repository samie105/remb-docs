---
title: "perspective"
source: "https://tailwindcss.com/docs/perspective"
canonical_url: "https://tailwindcss.com/docs/perspective"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:33:50.858Z"
content_hash: "eeada3e930e5ebe629b83cf25251e3cd6de19ca3bdb77f6de726c3b043638acf"
menu_path: ["perspective"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/backface-visibility/index.md", "title": "backface-visibility"}
nav_next: {"path": "tailwind/docs/perspective-origin/index.md", "title": "perspective-origin"}
---

Utilities for controlling an element's perspective when placed in 3D space.

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `perspective-normal` and `perspective-distant` to control how close or how far away the z-plane is from the screen:

perspective-dramatic

perspective-normal

```
<div class="size-20 perspective-dramatic ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div><div class="size-20 perspective-normal ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div>
```

This is like moving a camera closer to or further away from an object.

### [Removing a perspective](#removing-a-perspective)

Use the `perspective-none` utility to remove a perspective transform from an element:

```
<div class="perspective-none ...">  <!-- ... --></div>
```

### [Using a custom value](#using-a-custom-value)

Use the `perspective-[<value>]` syntax to set the perspective based on a completely custom value:

```
<div class="perspective-[750px] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `perspective-(<custom-property>)` syntax:

```
<div class="perspective-(--my-perspective) ...">  <!-- ... --></div>
```

This is just a shorthand for `perspective-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `perspective` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="perspective-midrange md:perspective-dramatic ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

## [Customizing your theme](#customizing-your-theme)

Use the `--perspective-*` theme variables to customize the perspective utilities in your project:

```
@theme {  --perspective-remote: 1800px; }
```

Now the `perspective-remote` utility can be used in your markup:

```
<div class="perspective-remote">  <!-- ... --></div>
```

Learn more about customizing your theme in the [theme documentation](tailwind/docs/theme/index.md#customizing-your-theme).
