---
title: "transform-style"
source: "https://tailwindcss.com/docs/transform-style"
canonical_url: "https://tailwindcss.com/docs/transform-style"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:35:36.215Z"
content_hash: "efaff1565837bae6da9aa4bfa6d244481eb0fe8a611513be895f99af9898189a"
menu_path: ["transform-style"]
section_path: []
content_language: "en"
nav_prev: {"path": "../transform-origin/index.md", "title": "transform-origin"}
nav_next: {"path": "../translate/index.md", "title": "translate"}
---

Transforms

Utilities for controlling if an elements children are placed in 3D space.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `transform-3d` to position children in 3D space:

transform-flat

transform-3d

```
<div class="size-20 transform-flat ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div><div class="size-20 transform-3d ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div>
```

Without this, any children will only be transformed in 2D space and not in 3D space.

### [Responsive design](#responsive-design)

Prefix a `transform-style` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="transform-3d md:transform-flat ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
