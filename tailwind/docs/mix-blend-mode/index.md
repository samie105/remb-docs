---
title: "mix-blend-mode"
source: "https://tailwindcss.com/docs/mix-blend-mode"
canonical_url: "https://tailwindcss.com/docs/mix-blend-mode"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:21:38.620Z"
content_hash: "bd981f0c13cc36904969c2bc22327a2b4582bd469c387b065692ef107d0aaf3a"
menu_path: ["mix-blend-mode"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/opacity/index.md", "title": "opacity"}
nav_next: {"path": "tailwind/docs/background-blend-mode/index.md", "title": "background-blend-mode"}
---

Utilities for controlling how an element should blend with the background.

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

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
