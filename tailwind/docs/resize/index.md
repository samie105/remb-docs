---
title: "resize"
source: "https://tailwindcss.com/docs/resize"
canonical_url: "https://tailwindcss.com/docs/resize"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:38:31.444Z"
content_hash: "6a08953b95456e80de552c304dbd0ca809cf0505ab47257a09c8f47701331cda"
menu_path: ["resize"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/pointer-events/index.md", "title": "pointer-events"}
nav_next: {"path": "tailwind/docs/scroll-behavior/index.md", "title": "scroll-behavior"}
---

# resize

Utilities for controlling how an element can be resized.

| Class | Styles |
| --- | --- |
| `resize-none` | 
`resize: none;`

 |
| `resize` | 

`resize: both;`

 |
| `resize-y` | 

`resize: vertical;`

 |
| `resize-x` | 

`resize: horizontal;`

 |

Use `resize` to make an element horizontally and vertically resizable:

Drag the textarea handle in the demo to see the expected behavior

```
<textarea class="resize rounded-md ..."></textarea>
```

Use `resize-y` to make an element vertically resizable:

Drag the textarea handle in the demo to see the expected behavior

```
<textarea class="resize-y rounded-md ..."></textarea>
```

Use `resize-x` to make an element horizontally resizable:

Drag the textarea handle in the demo to see the expected behavior

```
<textarea class="resize-x rounded-md ..."></textarea>
```

Use `resize-none` to prevent an element from being resizable:

Notice that the textarea handle is gone

```
<textarea class="resize-none rounded-md"></textarea>
```

Prefix a `resize` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="resize-none md:resize ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Resizing in all directions](#resizing-in-all-directions)
    -   [Resizing vertically](#resizing-vertically)
    -   [Resizing horizontally](#resizing-horizontally)
    -   [Prevent resizing](#prevent-resizing)
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
