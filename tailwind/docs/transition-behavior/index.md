---
title: "transition-behavior"
source: "https://tailwindcss.com/docs/transition-behavior"
canonical_url: "https://tailwindcss.com/docs/transition-behavior"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:32:05.942Z"
content_hash: "2491c8524d8d94add99dd136e93597710c9c09e54f99d8eeb18cdccb29ec7303"
menu_path: ["transition-behavior"]
section_path: []
content_language: "en"
nav_prev: {"path": "../transition-property/index.md", "title": "transition-property"}
nav_next: {"path": "../transition-duration/index.md", "title": "transition-duration"}
---

Utilities to control the behavior of CSS transitions.

## [Examples](#examples)

### [Basic example](#basic-example)

Use the `transition-discrete` utility to start transitions when changing properties with a discrete set of values, such as elements that change from `hidden` to `block`:

Interact with the checkboxes to see the expected behavior

transition-normal

transition-discrete

```
<label class="peer ...">  <input type="checkbox" checked /></label><button class="hidden transition-all not-peer-has-checked:opacity-0 peer-has-checked:block ...">  I hide</button><label class="peer ...">  <input type="checkbox" checked /></label><button class="hidden transition-all transition-discrete not-peer-has-checked:opacity-0 peer-has-checked:block ...">  I fade out</button>
```

### [Responsive design](#responsive-design)

Prefix a `transition-behavior` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<button class="transition-discrete md:transition-normal ...">  <!-- ... --></button>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
