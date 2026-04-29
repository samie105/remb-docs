---
title: "Unable to set response."
source: "https://docs.astro.build/en/reference/errors/response-sent-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/response-sent-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:25.505Z"
content_hash: "733d867d780fcb1b9b5bf0f9cd65dfc41200a2d0ab810a173a6790072f9e06aa"
menu_path: ["Unable to set response."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/reserved-slot-name/index.md", "title": "Invalid slot name."}
nav_next: {"path": "astro/en/reference/errors/rewrite-encountered-an-error/index.md", "title": "Astro couldn't find the route to rewrite, or if was found but it emitted an error during the rendering phase."}
---

# Unable to set response.

> **ResponseSentError**: The response has already been sent to the browser and cannot be altered.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Making changes to the response, such as setting headers, cookies, and the status code can only be done in [page components](../../../basics/astro-pages/index.md).

**See Also:**

*   [HTML streaming](../../../guides/on-demand-rendering/index.md#html-streaming)

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
