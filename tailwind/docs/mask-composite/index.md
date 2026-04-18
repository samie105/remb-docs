---
title: "mask-composite"
source: "https://tailwindcss.com/docs/mask-composite"
canonical_url: "https://tailwindcss.com/docs/mask-composite"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:19.635Z"
content_hash: "9aff3b5c5bdaf852844aee4105a73037336719f4bac05829026a5933e39d7908"
menu_path: ["mask-composite"]
section_path: []
nav_prev: {"path": "tailwind/docs/mask-clip/index.md", "title": "mask-clip"}
nav_next: {"path": "tailwind/docs/mask-image/index.md", "title": "mask-image"}
---

Utilities for controlling how multiple masks are combined together.

Class

Styles

`mask-add`

`mask-composite: add;`

`mask-subtract`

`mask-composite: subtract;`

`mask-intersect`

`mask-composite: intersect;`

`mask-exclude`

`mask-composite: exclude;`

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

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).
