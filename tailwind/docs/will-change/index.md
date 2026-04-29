---
title: "will-change"
source: "https://tailwindcss.com/docs/will-change"
canonical_url: "https://tailwindcss.com/docs/will-change"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:40:53.037Z"
content_hash: "09cd06654a55ebe305a57cde86227c4d40ebf3a5b92d760f33698a400e59852c"
menu_path: ["will-change"]
section_path: []
content_language: "en"
nav_prev: {"path": "../user-select/index.md", "title": "user-select"}
nav_next: {"path": "../fill/index.md", "title": "fill"}
---

Utilities for optimizing upcoming animations of elements that are expected to change.

## [Examples](#examples)

### [Optimizing with will change](#optimizing-with-will-change)

Use the `will-change-scroll`, `will-change-contents` and `will-change-transform` utilities to optimize an element that's expected to change in the near future by instructing the browser to prepare the necessary animation before it actually begins:

```
<div class="overflow-auto will-change-scroll">  <!-- ... --></div>
```

It's recommended that you apply these utilities just before an element changes, and then remove it shortly after it finishes using `will-change-auto`.

The `will-change` property is intended to be used as a last resort when dealing with **known performance problems**. Avoid using these utilities too much, or simply in anticipation of performance issues, as it could actually cause the page to be less performant.

### [Using a custom value](#using-a-custom-value)

Use the `will-change-[<value>]` syntax to set the `will-change` property based on a completely custom value:

```
<div class="will-change-[top,left] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `will-change-(<custom-property>)` syntax:

```
<div class="will-change-(--my-properties) ...">  <!-- ... --></div>
```

This is just a shorthand for `will-change-[var(<custom-property>)]` that adds the `var()` function for you automatically.
