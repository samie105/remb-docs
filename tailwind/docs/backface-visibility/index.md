---
title: "backface-visibility"
source: "https://tailwindcss.com/docs/backface-visibility"
canonical_url: "https://tailwindcss.com/docs/backface-visibility"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:33:15.588Z"
content_hash: "44ce990787cb218e02418a4df61323f1b99e5d1fac40354809acd76ab751bc1d"
menu_path: ["backface-visibility"]
section_path: []
content_language: "en"
---
Utilities for controlling if an element's backface is visible.

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `backface-visible` utility to show the backface of an element, like a cube, even when it's rotated away from view:

backface-hidden

backface-visible

```
<div class="size-20 ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 backface-hidden ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 backface-hidden ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 backface-hidden ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 backface-hidden ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 backface-hidden ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 backface-hidden ...">6</div></div><div class="size-20 ...">  <div class="translate-z-12 rotate-x-0 bg-sky-300/75 backface-visible ...">1</div>  <div class="-translate-z-12 rotate-y-18 bg-sky-300/75 backface-visible ...">2</div>  <div class="translate-x-12 rotate-y-90 bg-sky-300/75 backface-visible ...">3</div>  <div class="-translate-x-12 -rotate-y-90 bg-sky-300/75 backface-visible ...">4</div>  <div class="-translate-y-12 rotate-x-90 bg-sky-300/75 backface-visible ...">5</div>  <div class="translate-y-12 -rotate-x-90 bg-sky-300/75 backface-visible ...">6</div></div>
```

### [Responsive design](#responsive-design)

Prefix a `backface-visibility` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="backface-visible md:backface-hidden ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).
