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
nav_prev: {"path": "../unauthorized/index.md", "title": "unauthorized.js"}
nav_next: {"path": "app-icons/index.md", "title": "favicon, icon, and apple-icon"}
---

# Metadata Files API Reference

Last updated April 23, 2026

This section of the docs covers **Metadata file conventions**. File-based metadata can be defined by adding special metadata files to route segments.

Each file convention can be defined using a static file (e.g. `opengraph-image.jpg`), or a dynamic variant that uses code to generate the file (e.g. `opengraph-image.js`).

Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.

> **Good to know**:
> 
> -   Special Route Handlers like [`sitemap.ts`](/docs/app/api-reference/file-conventions/metadata/sitemap), [`opengraph-image.tsx`](/docs/app/api-reference/file-conventions/metadata/opengraph-image), and [`icon.tsx`](/docs/app/api-reference/file-conventions/metadata/app-icons), and other [metadata files](/docs/app/api-reference/file-conventions/metadata) are cached by default.
> -   If using along with [`proxy.ts`](/docs/app/api-reference/file-conventions/proxy), [configure the matcher](/docs/app/api-reference/file-conventions/proxy#matcher) to exclude the metadata files.

[

### favicon, icon, and apple-icon

API Reference for the Favicon, Icon and Apple Icon file conventions.

](/docs/app/api-reference/file-conventions/metadata/app-icons)[

### manifest.json

API Reference for manifest.json file.

](/docs/app/api-reference/file-conventions/metadata/manifest)[

### opengraph-image and twitter-image

API Reference for the Open Graph Image and Twitter Image file conventions.

](/docs/app/api-reference/file-conventions/metadata/opengraph-image)[

### robots.txt

API Reference for robots.txt file.

](/docs/app/api-reference/file-conventions/metadata/robots)[

### sitemap.xml

API Reference for the sitemap.xml file.

](/docs/app/api-reference/file-conventions/metadata/sitemap)

Was this helpful?
