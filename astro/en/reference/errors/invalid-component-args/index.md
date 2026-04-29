---
title: "Invalid component arguments."
source: "https://docs.astro.build/en/reference/errors/invalid-component-args/"
canonical_url: "https://docs.astro.build/en/reference/errors/invalid-component-args/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:07.644Z"
content_hash: "6c49f843ca691c72f407873273431b38d64028d0a0e59882bffbde5df354a089"
menu_path: ["Invalid component arguments."]
section_path: []
nav_prev: {"path": "../incorrect-strategy-for-i18n/index.md", "title": "You can't use the current function with the current strategy"}
nav_next: {"path": "../invalid-content-entry-data-error/index.md", "title": "Content entry data does not match schema."}
---

# Invalid component arguments.

> **Example error messages:**  
> InvalidComponentArgs: Invalid arguments passed to `<MyAstroComponent>` component.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro components cannot be rendered manually via a function call, such as `Component()` or `{items.map(Component)}`. Prefer the component syntax `<Component />` or `{items.map(item => <Component {...item} />)}`.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
