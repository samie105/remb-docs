---
title: "box-decoration-break"
source: "https://tailwindcss.com/docs/box-decoration-break"
canonical_url: "https://tailwindcss.com/docs/box-decoration-break"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:52:01.662Z"
content_hash: "f1fbc049e3cd4e1d31d98602567bda7f61d2afb5f1990910d315a431f2a35cf4"
menu_path: ["box-decoration-break"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/break-inside/index.md", "title": "break-inside"}
nav_next: {"path": "tailwind/docs/box-sizing/index.md", "title": "box-sizing"}
---

Utilities for controlling how element fragments should be rendered across multiple lines, columns, or pages.

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `box-decoration-slice` and `box-decoration-clone` utilities to control whether properties like background, border, border-image, box-shadow, clip-path, margin, and padding should be rendered as if the element were one continuous fragment, or distinct blocks:

box-decoration-slice

box-decoration-clone

```
<span class="box-decoration-slice bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">  Hello<br />World</span><span class="box-decoration-clone bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">  Hello<br />World</span>
```

### [Responsive design](#responsive-design)

Prefix a `box-decoration-break` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="box-decoration-clone md:box-decoration-slice ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
