---
title: "No client entrypoint specified in renderer."
source: "https://docs.astro.build/en/reference/errors/no-client-entrypoint/"
canonical_url: "https://docs.astro.build/en/reference/errors/no-client-entrypoint/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:03.019Z"
content_hash: "a41637654b0dce897bd39d3f564106acb3ccccc2f61c06daa456ffdaa76b81b6"
menu_path: ["No client entrypoint specified in renderer."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/no-adapter-installed/index.md", "title": "Cannot use Server-side Rendering without an adapter."}
nav_next: {"path": "astro/en/reference/errors/no-client-only-hint/index.md", "title": "Missing hint on client:only directive."}
---

# No client entrypoint specified in renderer.

> **NoClientEntrypoint**: `COMPONENT_NAME` component has a `client:CLIENT_DIRECTIVE` directive, but no client entrypoint was provided by `RENDERER_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro tried to hydrate a component on the client, but the renderer used does not provide a client entrypoint to use to hydrate.

**See Also:**

*   [addRenderer option](/en/reference/integrations-reference/#addrenderer-option)
*   [Hydrating framework components](/en/guides/framework-components/#hydrating-interactive-components)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

