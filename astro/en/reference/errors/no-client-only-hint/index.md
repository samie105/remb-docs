---
title: "Missing hint on client:only directive."
source: "https://docs.astro.build/en/reference/errors/no-client-only-hint/"
canonical_url: "https://docs.astro.build/en/reference/errors/no-client-only-hint/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:04.285Z"
content_hash: "00d8ce999b2e754652aff616dd97454e9b071510d4ec6ebb5def23fd909213c4"
menu_path: ["Missing hint on client:only directive."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/no-client-entrypoint/index.md", "title": "No client entrypoint specified in renderer."}
nav_next: {"path": "astro/en/reference/errors/no-image-metadata/index.md", "title": "Could not process image metadata."}
---

# Missing hint on client:only directive.

> **NoClientOnlyHint**: Unable to render `COMPONENT_NAME`. When using the `client:only` hydration strategy, Astro needs a hint to use the correct renderer.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`client:only` components are not run on the server, as such Astro does not know (and cannot guess) which renderer to use and require a hint. Like such:

```
  <SomeReactComponent client:only="react" />
```

**See Also:**

*   [`client:only`](/en/reference/directives-reference/#clientonly)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
