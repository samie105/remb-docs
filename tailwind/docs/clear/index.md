---
title: "clear"
source: "https://tailwindcss.com/docs/clear"
canonical_url: "https://tailwindcss.com/docs/clear"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:13.436Z"
content_hash: "7529499bcee9a17816ae9cb0d45a8382759c94205e738a625a43cff54a9b665c"
menu_path: ["clear"]
section_path: []
nav_prev: {"path": "tailwind/docs/float/index.md", "title": "float"}
nav_next: {"path": "tailwind/docs/isolation/index.md", "title": "isolation"}
---

Utilities for controlling the wrapping of content around an element.

Class

Styles

`clear-left`

`clear: left;`

`clear-right`

`clear: right;`

`clear-both`

`clear: both;`

`clear-start`

`clear: inline-start;`

`clear-end`

`clear: inline-end;`

`clear-none`

`clear: none;`

## [Examples](#examples)

### [Clearing left](#clearing-left)

Use the `clear-left` utility to position an element below any preceding left-floated elements:

```
<article>  <img class="float-left ..." src="/img/snow-mountains.jpg" />  <img class="float-right ..." src="/img/green-mountains.jpg" />  <p class="clear-left ...">Maybe we can live without libraries...</p></article>
```

### [Clearing right](#clearing-right)

Use the `clear-right` utility to position an element below any preceding right-floated elements:

```
<article>  <img class="float-left ..." src="/img/green-mountains.jpg" />  <img class="float-right ..." src="/img/snow-mountains.jpg" />  <p class="clear-right ...">Maybe we can live without libraries...</p></article>
```

### [Clearing all](#clearing-all)

Use the `clear-both` utility to position an element below all preceding floated elements:

```
<article>  <img class="float-left ..." src="/img/snow-mountains.jpg" />  <img class="float-right ..." src="/img/green-mountains.jpg" />  <p class="clear-both ...">Maybe we can live without libraries...</p></article>
```

### [Using logical properties](#using-logical-properties)

Use the `clear-start` and `clear-end` utilities, which use [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts) to map to either the left or right side based on the text direction:

```
<article dir="rtl">  <img class="float-left ..." src="/img/green-mountains.jpg" />  <img class="float-right ..." src="/img/green-mountains.jpg" />  <p class="clear-end ...">...ربما يمكننا العيش بدون مكتبات،</p></article>
```

### [Disabling clears](#disabling-clears)

Use the `clear-none` utility to reset any clears that are applied to an element:

```
<article>  <img class="float-left ..." src="/img/green-mountains.jpg" />  <img class="float-right ..." src="/img/snow-mountains.jpg" />  <p class="clear-none ...">Maybe we can live without libraries...</p></article>
```

### [Responsive design](#responsive-design)

Prefix a `clear` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="clear-left md:clear-none ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

