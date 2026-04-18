---
title: "Legacy flags"
source: "https://docs.astro.build/en/reference/legacy-flags/"
canonical_url: "https://docs.astro.build/en/reference/legacy-flags/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:22.538Z"
content_hash: "ae0213f362605a694ed2a543f78865bf9ba28721ed9e77ba51719f0196f9b657"
menu_path: ["Legacy flags"]
section_path: []
---
# Legacy flags

To help some users migrate between versions of Astro, we occasionally introduce `legacy` flags.

These flags allow you to opt in to some deprecated or otherwise outdated behavior of Astro in the latest version, so that you can continue to upgrade and take advantage of new Astro releases until you are able to fully update your project code.

## `collectionsBackwardsCompat`

[Section titled “collectionsBackwardsCompat”](#collectionsbackwardscompat)

**Type:** `boolean`  
**Default:** `false`  

**Added in:** `astro@6.0.0`

The `legacy.collectionsBackwardsCompat` flag provides temporary backwards compatibility for projects unable to migrate to the Content Layer API introduced in v5.0.

```
export default defineConfig({  legacy: {    collectionsBackwardsCompat: true,  },});
```

This flag preserves some legacy v4 content collections features:

*   Supports `type: 'content'` and `type: 'data'` without loaders
*   Preserves legacy entry API: `entry.slug` and `entry.render()`
*   Uses path-based entry IDs instead of slug-based IDs

This is a temporary migration helper. Migrate collections to the Content Layer API, then disable this flag.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
