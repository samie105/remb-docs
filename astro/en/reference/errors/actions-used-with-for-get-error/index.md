---
title: "An invalid Action query string was passed by a form."
source: "https://docs.astro.build/en/reference/errors/actions-used-with-for-get-error/"
canonical_url: "https://docs.astro.build/en/reference/errors/actions-used-with-for-get-error/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:26.503Z"
content_hash: "d510a2a3755207eac3d2b5579d4623562ee3d9e4857876cfc3ab7906f3a82c43"
menu_path: ["An invalid Action query string was passed by a form."]
section_path: []
nav_prev: {"path": "../actions-returned-invalid-data-error/index.md", "title": "Action handler returned invalid data."}
nav_next: {"path": "../actions-without-server-output-error/index.md", "title": "Actions must be used with server output."}
---

# An invalid Action query string was passed by a form.

> **ActionsUsedWithForGetError**: Action ACTION\_NAME was called from a form using a GET request, but only POST requests are supported. This often occurs if `method="POST"` is missing on the form.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Action was called from a form using a GET request, but only POST requests are supported. This often occurs if `method="POST"` is missing on the form.

**See Also:**

*   [Actions RFC](https://github.com/withastro/roadmap/blob/actions/proposals/0046-actions.md)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
