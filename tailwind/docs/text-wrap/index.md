---
title: "text-wrap"
source: "https://tailwindcss.com/docs/text-wrap"
canonical_url: "https://tailwindcss.com/docs/text-wrap"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:13:24.670Z"
content_hash: "510548616b38d6b113e3e8dcc896e9f2595f2e3b7b2690c585ed69d6fd77a4ce"
menu_path: ["text-wrap"]
section_path: []
content_language: "en"
nav_prev: {"path": "tailwind/docs/text-overflow/index.md", "title": "text-overflow"}
nav_next: {"path": "tailwind/docs/text-indent/index.md", "title": "text-indent"}
---

Utilities for controlling how text wraps within an element.

## [Examples](#examples)

### [Allowing text to wrap](#allowing-text-to-wrap)

Use the `text-wrap` utility to wrap overflowing text onto multiple lines at logical points in the text:

Beloved Manhattan soup stand closes

New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand unexpectedly shutters, following a series of events that have left the community puzzled.

```
<article class="text-wrap">  <h3>Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

### [Preventing text from wrapping](#preventing-text-from-wrapping)

Use the `text-nowrap` utility to prevent text from wrapping, allowing it to overflow if necessary:

```
<article class="text-nowrap">  <h3>Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

### [Balanced text wrapping](#balanced-text-wrapping)

Use the `text-balance` utility to distribute the text evenly across each line:

Beloved Manhattan soup stand closes

New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand unexpectedly shutters, following a series of events that have left the community puzzled.

```
<article>  <h3 class="text-balance">Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

For performance reasons browsers limit text balancing to blocks that are ~6 lines or less, making it best suited for headings.

### [Pretty text wrapping](#pretty-text-wrapping)

Use the `text-pretty` utility to prefer better text wrapping and layout at the expense of speed. Behavior varies across browsers but often involves approaches like preventing orphans (a single word on its own line) at the end of a text block:

Beloved Manhattan soup stand closes

New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand unexpectedly shutters, following a series of events that have left the community puzzled.

```
<article>  <h3 class="text-pretty">Beloved Manhattan soup stand closes</h3>  <p>New Yorkers are facing the winter chill...</p></article>
```

### [Responsive design](#responsive-design)

Prefix a `text-wrap` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<h1 class="text-pretty md:text-balance ...">  <!-- ... --></h1>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
