---
title: "Image not found."
source: "https://docs.astro.build/en/reference/errors/markdown-image-not-found/"
canonical_url: "https://docs.astro.build/en/reference/errors/markdown-image-not-found/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:40.652Z"
content_hash: "d4961c31be15e48e8cd232d23cdd0895d8a19509c71c256903a418145ecabbaa"
menu_path: ["Image not found."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/markdown-frontmatter-parse-error/index.md", "title": "Failed to parse Markdown frontmatter."}
nav_next: {"path": "astro/en/reference/errors/mdx-integration-missing-error/index.md", "title": "MDX integration missing."}
---

# Image not found.

> Could not find requested image `IMAGE_PATH` at `FULL_IMAGE_PATH`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not find an image you included in your Markdown content. Usually, this is simply caused by a typo in the path.

Images in Markdown are relative to the current file. To refer to an image that is located in the same folder as the `.md` file, the path should start with `./`

**See Also:**

*   [Images](../../../guides/images/index.md)

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
