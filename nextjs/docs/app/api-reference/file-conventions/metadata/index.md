---
title: "Metadata Files API Reference"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:08:52.266Z"
content_hash: "cdc56de1e46b72c960fb0314ff91e46a4dad2e1ba9c0575db93ed11a6d594589"
menu_path: ["Metadata Files API Reference"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/unauthorized/index.md", "title": "unauthorized.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/metadata/app-icons/index.md", "title": "favicon, icon, and apple-icon"}
---

# Metadata Files API Reference

Last updated April 23, 2026

This section of the docs covers **Metadata file conventions**. File-based metadata can be defined by adding special metadata files to route segments.

Each file convention can be defined using a static file (e.g. `opengraph-image.jpg`), or a dynamic variant that uses code to generate the file (e.g. `opengraph-image.js`).

Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.

> **Good to know**:
> 
> -   Special Route Handlers like [`sitemap.ts`](sitemap/index.md), [`opengraph-image.tsx`](opengraph-image/index.md), and [`icon.tsx`](app-icons/index.md), and other [metadata files](index.md) are cached by default.
> -   If using along with [`proxy.ts`](../proxy/index.md), [configure the matcher](../proxy/index.md#matcher) to exclude the metadata files.

[

### favicon, icon, and apple-icon

API Reference for the Favicon, Icon and Apple Icon file conventions.

](app-icons/index.md)[

### manifest.json

API Reference for manifest.json file.

](manifest/index.md)[

### opengraph-image and twitter-image

API Reference for the Open Graph Image and Twitter Image file conventions.

](opengraph-image/index.md)[

### robots.txt

API Reference for robots.txt file.

](robots/index.md)[

### sitemap.xml

API Reference for the sitemap.xml file.

](sitemap/index.md)

Was this helpful?
