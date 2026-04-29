---
title: "object-position"
source: "https://tailwindcss.com/docs/object-position"
canonical_url: "https://tailwindcss.com/docs/object-position"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:53:55.993Z"
content_hash: "3d15d0b9d648253a3487e7be9532c180cfbf0470d7bc8e10e438977ee5b04e8a"
menu_path: ["object-position"]
section_path: []
content_language: "en"
nav_prev: {"path": "../object-fit/index.md", "title": "object-fit"}
nav_next: {"path": "../overflow/index.md", "title": "overflow"}
---

Utilities for controlling how a replaced element's content should be positioned within its container.

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `object-left` and `object-bottom-right` to specify how a replaced element's content should be positioned within its container:

Hover over examples to see the full image

```
<img class="size-24 object-top-left ..." src="/img/mountains.jpg" /><img class="size-24 object-top ..." src="/img/mountains.jpg" /><img class="size-24 object-top-right ..." src="/img/mountains.jpg" /><img class="size-24 object-left ..." src="/img/mountains.jpg" /><img class="size-24 object-center ..." src="/img/mountains.jpg" /><img class="size-24 object-right ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom-left ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom ..." src="/img/mountains.jpg" /><img class="size-24 object-bottom-right ..." src="/img/mountains.jpg" />
```

### [Using a custom value](#using-a-custom-value)

Use the `object-[<value>]` syntax to set the object position based on a completely custom value:

```
<img class="object-[25%_75%] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `object-(<custom-property>)` syntax:

```
<img class="object-(--my-object) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `object-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix an `object-position` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="object-center md:object-top ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
