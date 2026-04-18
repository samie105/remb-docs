---
title: "transform-style"
source: "https://tailwindcss.com/docs/transform-style"
canonical_url: "https://tailwindcss.com/docs/transform-style"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:23.021Z"
content_hash: "2a8358ca600cb1e741e0f85ab55bc76e6216895ec11b0385e29d2b4fa0504680"
menu_path: ["transform-style"]
section_path: []
---
Transforms

Utilities for controlling if an elements children are placed in 3D space.

Class

Styles

`transform-3d`

`transform-style: preserve-3d;`

`transform-flat`

`transform-style: flat;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use `transform-3d` to position children in 3D space:

transform-flat

1

2

3

4

5

6

transform-3d

1

2

3

4

5

6

```
<div class="size-20 transform-flat ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div><div class="size-20 transform-3d ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 ...">6</div></div>
```

Without this, any children will only be transformed in 2D space and not in 3D space.

### [Responsive design](#responsive-design)

Prefix a `transform-style` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="transform-3d md:transform-flat ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).
