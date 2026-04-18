---
title: "outline-style"
source: "https://tailwindcss.com/docs/outline-style"
canonical_url: "https://tailwindcss.com/docs/outline-style"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:27.666Z"
content_hash: "896783c46e5fe09111a5358ebdfd069f55d1609af820a0ebde3cb40eed18ee31"
menu_path: ["outline-style"]
section_path: []
nav_prev: {"path": "tailwind/docs/outline-color/index.md", "title": "outline-color"}
nav_next: {"path": "tailwind/docs/outline-offset/index.md", "title": "outline-offset"}
---

Utilities for controlling the style of an element's outline.

Class

Styles

`outline-solid`

`outline-style: solid;`

`outline-dashed`

`outline-style: dashed;`

`outline-dotted`

`outline-style: dotted;`

`outline-double`

`outline-style: double;`

`outline-none`

`outline-style: none;`

`outline-hidden`

`outline: 2px solid transparent; outline-offset: 2px;`

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `outline-solid` and `outline-dashed` to set the style of an element's outline:

outline-solid

outline-dashed

outline-dotted

outline-double

```
<button class="outline-2 outline-offset-2 outline-solid ...">Button A</button><button class="outline-2 outline-offset-2 outline-dashed ...">Button B</button><button class="outline-2 outline-offset-2 outline-dotted ...">Button C</button><button class="outline-3 outline-offset-2 outline-double ...">Button D</button>
```

### [Hiding an outline](#hiding-an-outline)

Use the `outline-hidden` utility to hide the default browser outline on focused elements, while still preserving the outline in forced colors mode:

Try emulating \`forced-colors: active\` in your developer tools to see the behavior

```
<input class="focus:border-indigo-600 focus:outline-hidden ..." type="text" />
```

It is highly recommended to apply your own focus styling for accessibility when using this utility.

### [Removing outlines](#removing-outlines)

Use the `outline-none` utility to completely remove the default browser outline on focused elements:

```
<div class="focus-within:outline-2 focus-within:outline-indigo-600 ...">  <textarea class="outline-none ..." placeholder="Leave a comment..." />  <button class="..." type="button">Post</button></div>
```

It is highly recommended to apply your own focus styling for accessibility when using this utility.

### [Responsive design](#responsive-design)

Prefix an `outline-style` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="outline md:outline-dashed ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).
