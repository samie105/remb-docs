---
title: "rotate"
source: "https://tailwindcss.com/docs/rotate"
canonical_url: "https://tailwindcss.com/docs/rotate"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:34:25.541Z"
content_hash: "8e273dbc9cafe36916db1e651d15f959c79b3d1788f30849f6dfc47b35b97dcb"
menu_path: ["rotate"]
section_path: []
content_language: "en"
---
Utilities for rotating elements.

## [Examples](#examples)

### [Basic example](#basic-example)

Use `rotate-<number>` utilities like `rotate-45` and `rotate-90` to rotate an element by degrees:

```
<img class="rotate-45 ..." src="/img/mountains.jpg" /><img class="rotate-90 ..." src="/img/mountains.jpg" /><img class="rotate-210 ..." src="/img/mountains.jpg" />
```

### [Using negative values](#using-negative-values)

Use `-rotate-<number>` utilities like `-rotate-45` and `-rotate-90` to rotate an element counterclockwise by degrees:

```
<img class="-rotate-45 ..." src="/img/mountains.jpg" /><img class="-rotate-90 ..." src="/img/mountains.jpg" /><img class="-rotate-210 ..." src="/img/mountains.jpg" />
```

### [Rotating in 3D space](#rotating-in-3d-space)

Use `rotate-x-<number>`, `rotate-y-<number>`, and `rotate-z-<number>` utilities like `rotate-x-50`, `-rotate-y-30`, and `rotate-z-45` together to rotate an element in 3D space:

```
<img class="rotate-x-50 rotate-z-45 ..." src="/img/mountains.jpg" /><img class="rotate-x-15 -rotate-y-30 ..." src="/img/mountains.jpg" /><img class="rotate-y-25 rotate-z-30 ..." src="/img/mountains.jpg" />
```

### [Using a custom value](#using-a-custom-value)

Use the `rotate-[<value>]` syntax to set the rotation based on a completely custom value:

```
<img class="rotate-[3.142rad] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `rotate-(<custom-property>)` syntax:

```
<img class="rotate-(--my-rotation) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `rotate-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `rotate` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="rotate-45 md:rotate-60 ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).
