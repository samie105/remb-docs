---
title: "text-transform"
source: "https://tailwindcss.com/docs/text-transform"
canonical_url: "https://tailwindcss.com/docs/text-transform"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:12:49.976Z"
content_hash: "6b3feb9e5eba8b2658b31d13c6f713f93d127e17e174fc3d8254f7e7d76a11c9"
menu_path: ["text-transform"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Typography
2.  text-transform

Typography

# text-transform

Utilities for controlling the capitalization of text.

| Class | Styles |
| --- | --- |
| `uppercase` | 
`text-transform: uppercase;`

 |
| `lowercase` | 

`text-transform: lowercase;`

 |
| `capitalize` | 

`text-transform: capitalize;`

 |
| `normal-case` | 

`text-transform: none;`

 |

Use the `uppercase` utility to uppercase the text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="uppercase">The quick brown fox ...</p>
```

Use the `lowercase` utility to lowercase the text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="lowercase">The quick brown fox ...</p>
```

Use the `capitalize` utility to capitalize text of an element:

The quick brown fox jumps over the lazy dog.

```
<p class="capitalize">The quick brown fox ...</p>
```

Use the `normal-case` utility to preserve the original text casing of an element—typically used to reset capitalization at different breakpoints:

The quick brown fox jumps over the lazy dog.

```
<p class="normal-case">The quick brown fox ...</p>
```

Prefix a `text-transform` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="capitalize md:uppercase ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Uppercasing text](#uppercasing-text)
    -   [Lowercasing text](#lowercasing-text)
    -   [Capitalizing text](#capitalizing-text)
    -   [Resetting text casing](#resetting-text-casing)
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
