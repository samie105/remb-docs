---
title: "Experimental Intellisense for content collections"
source: "https://docs.astro.build/en/reference/experimental-flags/content-intellisense/"
canonical_url: "https://docs.astro.build/en/reference/experimental-flags/content-intellisense/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:02.906Z"
content_hash: "90e196985e7f3a77cd21c19cc4a0258fd7fafaf2aff732be8e21c79fdaad7dfa"
menu_path: ["Experimental Intellisense for content collections"]
section_path: []
nav_prev: {"path": "astro/en/reference/experimental-flags/client-prerender/index.md", "title": "Experimental client prerendering"}
nav_next: {"path": "astro/en/reference/experimental-flags/chrome-devtools-workspace/index.md", "title": "Experimental Chrome DevTools workspace"}
---

# Experimental Intellisense for content collections

**Type:** `boolean`  
**Default:** `false`  

**Added in:** `astro@4.14.0`

Enables Intellisense features (e.g. code completion, quick hints) for your content collection entries in compatible editors.

When enabled, this feature will generate and add JSON schemas to the `.astro` directory in your project. These files can be used by the Astro language server to provide Intellisense inside content files (`.md`, `.mdx`, `.mdoc`).

```
import { defineConfig } from 'astro/config';
export default defineConfig({  experimental: {    contentIntellisense: true,  },});
```

To use this feature with the Astro VS Code extension, you must also enable the `astro.content-intellisense` option in your VS Code settings. For editors using the Astro language server directly, pass the `contentIntellisense: true` initialization parameter to enable this feature.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
