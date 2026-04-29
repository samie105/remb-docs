---
title: "No matching renderer found."
source: "https://docs.astro.build/en/reference/errors/no-matching-renderer/"
canonical_url: "https://docs.astro.build/en/reference/errors/no-matching-renderer/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:09.184Z"
content_hash: "1a4ce2f0bc01ca0da9d23f7c35faf353dda6c4035f05f631fd69f8c9f2c02e23"
menu_path: ["No matching renderer found."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/no-matching-import/index.md", "title": "No import found for component."}
nav_next: {"path": "astro/en/reference/errors/no-matching-static-path-found/index.md", "title": "No static path found for requested path."}
---

# No matching renderer found.

> Unable to render `COMPONENT_NAME`. There are `RENDERER_COUNT` renderer(s) configured in your `astro.config.mjs` file, but none were able to server-side render `COMPONENT_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

None of the installed integrations were able to render the component you imported. Make sure to install the appropriate integration for the type of component you are trying to include in your page.

For JSX / TSX files, [@astrojs/react](../../../guides/integrations-guide/react/index.md), [@astrojs/preact](../../../guides/integrations-guide/preact/index.md) or [@astrojs/solid-js](../../../guides/integrations-guide/solid-js/index.md) can be used. For Vue and Svelte files, the [@astrojs/vue](../../../guides/integrations-guide/vue/index.md) and [@astrojs/svelte](../../../guides/integrations-guide/svelte/index.md) integrations can be used respectively

**See Also:**

*   [Frameworks components](../../../guides/framework-components/index.md)
*   [UI Frameworks](../../../guides/integrations/index.md#official-integrations)

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
