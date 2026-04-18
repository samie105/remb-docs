---
title: "pointer-events"
source: "https://tailwindcss.com/docs/pointer-events"
canonical_url: "https://tailwindcss.com/docs/pointer-events"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:16:11.040Z"
content_hash: "b3b1a4ee5403d38ca3267f5d3ea41b0286f46b0e62058dd730a635c22e79aefc"
menu_path: ["pointer-events"]
section_path: []
nav_prev: {"path": "tailwind/docs/field-sizing/index.md", "title": "field-sizing"}
nav_next: {"path": "tailwind/docs/resize/index.md", "title": "resize"}
---

# pointer-events

Utilities for controlling whether an element responds to pointer events.

Class

Styles

`pointer-events-auto`

`pointer-events: auto;`

`pointer-events-none`

`pointer-events: none;`

## [Examples](#examples)

### [Ignoring pointer events](#ignoring-pointer-events)

Use the `pointer-events-none` utility to make an element ignore pointer events, like `:hover` and `click` events:

Click the search icons to see the expected behavior

pointer-events-auto

pointer-events-none

```
<div class="relative ...">  <div class="pointer-events-auto absolute ...">    <svg class="absolute h-5 w-5 text-gray-400">      <!-- ... -->    </svg>  </div>  <input type="text" placeholder="Search" class="..." /></div><div class="relative ...">  <div class="pointer-events-none absolute ...">    <svg class="absolute h-5 w-5 text-gray-400">      <!-- ... -->    </svg>  </div>  <input type="text" placeholder="Search" class="..." /></div>
```

The pointer events will still trigger on child elements and pass-through to elements that are "beneath" the target.

### [Restoring pointer events](#restoring-pointer-events)

Use the `pointer-events-auto` utility to revert to the default browser behavior for pointer events:

```
<div class="pointer-events-none md:pointer-events-auto ...">  <!-- ... --></div>
```

### On this page

*   [Quick reference](#quick-reference)
*   [Examples](#examples)
    *   [Ignoring pointer events](#ignoring-pointer-events)
    *   [Restoring pointer events](#restoring-pointer-events)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)

