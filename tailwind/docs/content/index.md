---
title: "content"
source: "https://tailwindcss.com/docs/content"
canonical_url: "https://tailwindcss.com/docs/content"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:15:44.711Z"
content_hash: "345605381e8fb61ef3f357e7fa2526ec8189765ef69510b2b77d3d0113d5f759"
menu_path: ["content"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/hyphens/index.md", "title": "hyphens"}
nav_next: {"path": "tailwind/docs/background-attachment/index.md", "title": "background-attachment"}
---

# content

Utilities for controlling the content of the before and after pseudo-elements.

| Class | Styles |
| --- | --- |
| `content-[<value>]` | 
`content: <value>;`

 |
| `content-(<custom-property>)` | 

`content: var(<custom-property>);`

 |
| `content-none` | 

`content: none;`

 |

Use the `content-[<value>]` syntax, along with the `before` and `after` variants, to set the contents of the `::before` and `::after` pseudo-elements:

Higher resolution means more than just a better-quality image. With a Retina 6K display, [Pro Display XDR](https://www.apple.com/pro-display-xdr/) gives you nearly 40 percent more screen real estate than a 5K display.

```
<p>Higher resolution means more than just a better-quality image. With aRetina 6K display, <a class="text-blue-600 after:content-['_↗']" href="...">Pro Display XDR</a> gives you nearly 40 percent more screen real estate thana 5K display.</p>
```

Use the `content-[attr(<name>)]` syntax to reference a value stored in an attribute using the `attr()` CSS function:

```
<p before="Hello World" class="before:content-[attr(before)] ...">  <!-- ... --></p>
```

Since whitespace denotes the end of a class in HTML, replace any spaces in an arbitrary value with an underscore:

```
<p class="before:content-['Hello_World'] ..."></p>
```

If you need to include an actual underscore, you can do this by escaping it with a backslash:

```
<p class="before:content-['Hello\_World']"></p>
```

Use the `content-(<custom-property>)` syntax to control the contents of the `::before` and `::after` pseudo-elements using a CSS variable:

```
<p class="content-(--my-content)"></p>
```

This is just a shorthand for `content-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `content` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="before:content-['Mobile'] md:before:content-['Desktop'] ..."></p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Basic example](#basic-example)
    -   [Referencing an attribute value](#referencing-an-attribute-value)
    -   [Using spaces and underscores](#using-spaces-and-underscores)
    -   [Using a CSS variable](#using-a-css-variable)
    -   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
