---
title: "scale"
source: "https://tailwindcss.com/docs/scale"
canonical_url: "https://tailwindcss.com/docs/scale"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:34:26.069Z"
content_hash: "804ae1f8dd4ebc2aa14c227abbe6064259cb832aa5aa27910bcc560b1eedf3b9"
menu_path: ["scale"]
section_path: []
content_language: "en"
nav_prev: {"path": "../rotate/index.md", "title": "rotate"}
nav_next: {"path": "../skew/index.md", "title": "skew"}
---

Utilities for scaling elements.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `scale-<number>` utilities like `scale-75` and `scale-150` to scale an element by a percentage of its original size:

```
<img class="scale-75 ..." src="/img/mountains.jpg" /><img class="scale-100 ..." src="/img/mountains.jpg" /><img class="scale-125 ..." src="/img/mountains.jpg" />
```

### [Scaling on the x-axis](#scaling-on-the-x-axis)

Use the `scale-x-<number>` utilities like `scale-x-75` and `-scale-x-150` to scale an element on the x-axis by a percentage of its original width:

```
<img class="scale-x-75 ..." src="/img/mountains.jpg" /><img class="scale-x-100 ..." src="/img/mountains.jpg" /><img class="scale-x-125 ..." src="/img/mountains.jpg" />
```

### [Scaling on the y-axis](#scaling-on-the-y-axis)

Use the `scale-y-<number>` utilities like `scale-y-75` and `scale-y-150` to scale an element on the y-axis by a percentage of its original height:

```
<img class="scale-y-75 ..." src="/img/mountains.jpg" /><img class="scale-y-100 ..." src="/img/mountains.jpg" /><img class="scale-y-125 ..." src="/img/mountains.jpg" />
```

### [Using negative values](#using-negative-values)

Use `-scale-<number>`, `-scale-x-<number>` or `-scale-y-<number>` utilities like `-scale-x-75` and `-scale-125` to mirror and scale down an element by a percentage of its original size:

```
<img class="-scale-x-75 ..." src="/img/mountains.jpg" /><img class="-scale-100 ..." src="/img/mountains.jpg" /><img class="-scale-y-125 ..." src="/img/mountains.jpg" />
```

### [Using a custom value](#using-a-custom-value)

Use the `scale-[<value>]` syntax to set the scale based on a completely custom value:

```
<img class="scale-[1.7] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `scale-(<custom-property>)` syntax:

```
<img class="scale-(--my-scale) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `scale-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Applying on hover](#applying-on-hover)

Prefix a `scale` utility with a variant like `hover:*` to only apply the utility in that state:

```
<img class="scale-95 hover:scale-120 ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
