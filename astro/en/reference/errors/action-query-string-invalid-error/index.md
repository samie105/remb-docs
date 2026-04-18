---
title: "An invalid Action query string was passed by a form."
source: "https://docs.astro.build/en/reference/errors/action-query-string-invalid-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/action-query-string-invalid-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:19.257Z"
content_hash: "3d5882fdbd4640043c1757007325e84f5ca2894c6371dc2d30cc2124aa5c50c7"
menu_path: ["An invalid Action query string was passed by a form."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/action-not-found-error/index.md", "title": "Action not found."}
nav_next: {"path": "astro/en/reference/errors/actions-cant-be-loaded/index.md", "title": "Can't load the Astro actions."}
---

# An invalid Action query string was passed by a form.

> **ActionQueryStringInvalidError**: The server received the query string `?_astroAction=ACTION_NAME`, but could not find an action with that name. If you changed an action’s name in development, remove this query param from your URL and refresh.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The server received the query string `?_astroAction=name`, but could not find an action with that name. Use the action function’s `.queryString` property to retrieve the form `action` URL.

**See Also:**

*   [Actions RFC](https://github.com/withastro/roadmap/blob/actions/proposals/0046-actions.md)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

