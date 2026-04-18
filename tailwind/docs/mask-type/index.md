---
title: "mask-type"
source: "https://tailwindcss.com/docs/mask-type"
canonical_url: "https://tailwindcss.com/docs/mask-type"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:32.869Z"
content_hash: "5e4dbfcc22c08a317d3eff521b11e9ca040825753c9c5ec8107b721a5b44e4d1"
menu_path: ["mask-type"]
section_path: []
---
Utilities for controlling how an SVG mask is interpreted.

Class

Styles

`mask-type-alpha`

`mask-type: alpha;`

`mask-type-luminance`

`mask-type: luminance;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `mask-type-alpha` and `mask-type-luminance` utilities to control the type of an SVG mask:

mask-type-alpha

mask-type-luminance

```
<svg>  <mask id="blob1" class="mask-type-alpha fill-gray-700/70">    <path d="..."></path>  </mask>  <image href="/img/mountains.jpg" height="100%" width="100%" mask="url(#blob1)" /></svg><svg>  <mask id="blob2" class="mask-type-luminance fill-gray-700/70">    <path d="..."></path>  </mask>  <image href="/img/mountains.jpg" height="100%" width="100%" mask="url(#blob2)" /></svg>
```

When using `mask-type-luminance` the luminance value of the SVG mask determines visibility, so sticking with grayscale colors will produce the most predictable results. With `mask-alpha`, the opacity of the SVG mask determines the visibility of the masked element.

### [Responsive design](#responsive-design)

Prefix a `mask-type` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<mask class="mask-type-alpha md:mask-type-luminance ...">  <!-- ... --></mask>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).
