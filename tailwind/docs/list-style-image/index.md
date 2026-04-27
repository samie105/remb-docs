---
title: "list-style-image"
source: "https://tailwindcss.com/docs/list-style-image"
canonical_url: "https://tailwindcss.com/docs/list-style-image"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:09:58.252Z"
content_hash: "deaf08fe2e2921b84d70f8ba713a9fa7e4cce50b772ecc2d0a7ad03a95701bd3"
menu_path: ["list-style-image"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Typography
2.  list-style-image

Typography

# list-style-image

Utilities for controlling the marker images for list items.

| Class | Styles |
| --- | --- |
| `list-image-[<value>]` | 
`list-style-image: <value>;`

 |
| `list-image-(<custom-property>)` | 

`list-style-image: var(<custom-property>);`

 |
| `list-image-none` | 

`list-style-image: none;`

 |

Use the `list-image-[<value>]` syntax to control the marker image for list items:

-   5 cups chopped Porcini mushrooms
-   1/2 cup of olive oil
-   3lb of celery

```
<ul class="list-image-[url(/img/checkmark.png)]">  <li>5 cups chopped Porcini mushrooms</li>  <!-- ... --></ul>
```

Use the `list-image-(<custom-property>)` syntax to control the marker image for list items using a CSS variable:

```
<ul class="list-image-(--my-list-image)">  <!-- ... --></ul>
```

This is just a shorthand for `list-image-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Use the `list-image-none` utility to remove an existing marker image from list items:

```
<ul class="list-image-none">  <!-- ... --></ul>
```

Prefix a `list-style-image` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<ul class="list-image-none md:list-image-[url(/img/checkmark.png)] ...">  <!-- ... --></ul>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Using a CSS variable](#using-a-css-variable)
    -   [Removing a marker image](#removing-a-marker-image)
    -   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
