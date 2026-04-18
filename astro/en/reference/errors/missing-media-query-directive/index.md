---
title: "Missing value for client:media directive."
source: "https://docs.astro.build/en/reference/errors/missing-media-query-directive/"
canonical_url: "https://docs.astro.build/en/reference/errors/missing-media-query-directive/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:51.199Z"
content_hash: "4ea2d5131f771b46cd9b53b2450e05ec5198c613a5cc6eb42486af76855afe78"
menu_path: ["Missing value for client:media directive."]
section_path: []
---
# Missing value for client:media directive.

> **MissingMediaQueryDirective**: Media query not provided for `client:media` directive. A media query similar to `client:media="(max-width: 600px)"` must be provided

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries) parameter is required when using the `client:media` directive.

```
<Counter client:media="(max-width: 640px)" />
```

**See Also:**

*   [`client:media`](/en/reference/directives-reference/#clientmedia)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
