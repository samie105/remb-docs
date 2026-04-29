---
title: "mask-composite"
source: "https://tailwindcss.com/docs/mask-composite"
canonical_url: "https://tailwindcss.com/docs/mask-composite"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:22:14.360Z"
content_hash: "e7c61ff285b8bcdf52626a5cd7e44c034ce754275c05870f76c7101a3c1a2828"
menu_path: ["mask-composite"]
section_path: []
content_language: "en"
nav_prev: {"path": "../mask-clip/index.md", "title": "mask-clip"}
nav_next: {"path": "../mask-image/index.md", "title": "mask-image"}
---

Utilities for controlling how multiple masks are combined together.

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `mask-add` and `mask-intersect` to control how an element's masks are combined together:

mask-add

mask-subtract

mask-intersect

mask-exclude

```
<div class="mask-add mask-[url(/img/circle.png),url(/img/circle.png)] mask-[position:30%_50%,70%_50%] bg-[url(/img/mountains.jpg)]"></div><div class="mask-subtract mask-[url(/img/circle.png),url(/img/circle.png)] mask-[position:30%_50%,70%_50%] bg-[url(/img/mountains.jpg)]"></div><div class="mask-intersect mask-[url(/img/circle.png),url(/img/circle.png)] mask-[position:30%_50%,70%_50%] bg-[url(/img/mountains.jpg)]"></div><div class="mask-exclude mask-[url(/img/circle.png),url(/img/circle.png)] mask-[position:30%_50%,70%_50%] bg-[url(/img/mountains.jpg)]"></div>
```

### [Responsive design](#responsive-design)

Prefix a `mask-composite` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="mask-add md:mask-subtract ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
