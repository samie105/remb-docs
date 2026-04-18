---
title: "filter: saturate()"
source: "https://tailwindcss.com/docs/filter-saturate"
canonical_url: "https://tailwindcss.com/docs/filter-saturate"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:21.958Z"
content_hash: "ee176ad2bc70f3410096d15d08fa376e9ec9ddcfad2ade0166037f041d47ae0e"
menu_path: ["filter: saturate()"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Filters
2.  saturate

Filters

# filter: saturate()

Utilities for applying saturation filters to an element.

Class

Styles

`saturate-<number>`

`filter: saturate(<number>%);`

`saturate-(<custom-property>)`

`filter: saturate(var(<custom-property>));`

`saturate-[<value>]`

`filter: saturate(<value>);`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `saturate-50` and `saturate-100` to control an element's saturation:

saturate-50

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

saturate-100

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

saturate-150

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

saturate-200

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
<img class="saturate-50 ..." src="/img/mountains.jpg" /><img class="saturate-100 ..." src="/img/mountains.jpg" /><img class="saturate-150 ..." src="/img/mountains.jpg" /><img class="saturate-200 ..." src="/img/mountains.jpg" />
```

### [Using a custom value](#using-a-custom-value)

Use the `saturate-[<value>]` syntax to set the saturation based on a completely custom value:

```
<img class="saturate-[.25] ..." src="/img/mountains.jpg" />
```

For CSS variables, you can also use the `saturate-(<custom-property>)` syntax:

```
<img class="saturate-(--my-saturation) ..." src="/img/mountains.jpg" />
```

This is just a shorthand for `saturate-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `filter: saturate()` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<img class="saturate-50 md:saturate-150 ..." src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Using a custom value](#using-a-custom-value)
    *   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
