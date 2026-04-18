---
title: "mix-blend-mode"
source: "https://tailwindcss.com/docs/mix-blend-mode"
canonical_url: "https://tailwindcss.com/docs/mix-blend-mode"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:04:42.860Z"
content_hash: "a74dbf13a957303960d9a4815fd9a2eb4768f45a44dccde5ad6612ad190ed863"
menu_path: ["mix-blend-mode"]
section_path: []
nav_prev: {"path": "tailwind/docs/opacity/index.md", "title": "opacity"}
nav_next: {"path": "tailwind/docs/background-blend-mode/index.md", "title": "background-blend-mode"}
---

Utilities for controlling how an element should blend with the background.

Class

Styles

`mix-blend-normal`

`mix-blend-mode: normal;`

`mix-blend-multiply`

`mix-blend-mode: multiply;`

`mix-blend-screen`

`mix-blend-mode: screen;`

`mix-blend-overlay`

`mix-blend-mode: overlay;`

`mix-blend-darken`

`mix-blend-mode: darken;`

`mix-blend-lighten`

`mix-blend-mode: lighten;`

`mix-blend-color-dodge`

`mix-blend-mode: color-dodge;`

`mix-blend-color-burn`

`mix-blend-mode: color-burn;`

`mix-blend-hard-light`

`mix-blend-mode: hard-light;`

`mix-blend-soft-light`

`mix-blend-mode: soft-light;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `mix-blend-overlay` and `mix-blend-soft-light` to control how an element's content and background is blended with other content in the same stacking context:

```
<div class="flex justify-center -space-x-14">  <div class="bg-blue-500 mix-blend-multiply ..."></div>  <div class="bg-pink-500 mix-blend-multiply ..."></div></div>
```

### [Isolating blending](#isolating-blending)

Use the `isolate` utility on the parent element to create a new stacking context and prevent blending with content behind it:

```
<div class="isolate flex justify-center -space-x-14">  <div class="bg-yellow-500 mix-blend-multiply ..."></div>  <div class="bg-green-500 mix-blend-multiply ..."></div></div><div class="flex justify-center -space-x-14">  <div class="bg-yellow-500 mix-blend-multiply ..."></div>  <div class="bg-green-500 mix-blend-multiply ..."></div></div>
```

### [Responsive design](#responsive-design)

Prefix a `mix-blend-mode` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mix-blend-multiply md:mix-blend-overlay ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

