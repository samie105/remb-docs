---
title: "content"
source: "https://tailwindcss.com/docs/content"
canonical_url: "https://tailwindcss.com/docs/content"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:22.202Z"
content_hash: "5a2a14a5e5c17b8e5c189f3f60b35e382d305422332baf0dafa4b4eea9936daf"
menu_path: ["content"]
section_path: []
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Typography
2.  content

Typography

# content

Utilities for controlling the content of the before and after pseudo-elements.

Class

Styles

`content-[<value>]`

`content: <value>;`

`content-(<custom-property>)`

`content: var(<custom-property>);`

`content-none`

`content: none;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `content-[<value>]` syntax, along with the `before` and `after` variants, to set the contents of the `::before` and `::after` pseudo-elements:

Higher resolution means more than just a better-quality image. With a Retina 6K display, [Pro Display XDR](https://www.apple.com/pro-display-xdr/) gives you nearly 40 percent more screen real estate than a 5K display.

```
<p>Higher resolution means more than just a better-quality image. With aRetina 6K display, <a class="text-blue-600 after:content-['_↗']" href="...">Pro Display XDR</a> gives you nearly 40 percent more screen real estate thana 5K display.</p>
```

### [Referencing an attribute value](#referencing-an-attribute-value)

Use the `content-[attr(<name>)]` syntax to reference a value stored in an attribute using the `attr()` CSS function:

```
<p before="Hello World" class="before:content-[attr(before)] ...">  <!-- ... --></p>
```

### [Using spaces and underscores](#using-spaces-and-underscores)

Since whitespace denotes the end of a class in HTML, replace any spaces in an arbitrary value with an underscore:

```
<p class="before:content-['Hello_World'] ..."></p>
```

If you need to include an actual underscore, you can do this by escaping it with a backslash:

```
<p class="before:content-['Hello\_World']"></p>
```

### [Using a CSS variable](#using-a-css-variable)

Use the `content-(<custom-property>)` syntax to control the contents of the `::before` and `::after` pseudo-elements using a CSS variable:

```
<p class="content-(--my-content)"></p>
```

This is just a shorthand for `content-[var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `content` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="before:content-['Mobile'] md:before:content-['Desktop'] ..."></p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Basic example](#basic-example)
    *   [Referencing an attribute value](#referencing-an-attribute-value)
    *   [Using spaces and underscores](#using-spaces-and-underscores)
    *   [Using a CSS variable](#using-a-css-variable)
    *   [Responsive design](#responsive-design)

![Build UIs that don’t suck — 5-day mini-course](/_next/static/media/course-promo.d3d6bc78.jpg)

5-day mini-course

Build UIs that don’t suck.

Short, tactical video lessons from the creator of Tailwind CSS, delivered directly to your inbox every day for a week.

[Get the free course](/build-uis-that-dont-suck)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
