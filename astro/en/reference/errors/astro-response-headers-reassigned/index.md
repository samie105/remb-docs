---
title: "Astro.response.headers must not be reassigned."
source: "https://docs.astro.build/en/reference/errors/astro-response-headers-reassigned/"
canonical_url: "https://docs.astro.build/en/reference/errors/astro-response-headers-reassigned/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:35.269Z"
content_hash: "8451d8a174333cb04bfb2b4ae3b055444ba2a16eb4b9da84cdef1e6f0ec01de0"
menu_path: ["Astro.response.headers must not be reassigned."]
section_path: []
nav_prev: {"path": "../astro-glob-used-outside/index.md", "title": "Astro.glob() used outside of an Astro file."}
nav_next: {"path": "../cache-not-enabled/index.md", "title": "Cache is not enabled."}
---

# Astro.response.headers must not be reassigned.

> **AstroResponseHeadersReassigned**: Individual headers can be added to and removed from `Astro.response.headers`, but it must not be replaced with another instance of `Headers` altogether.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when a value is being set as the `headers` field on the `ResponseInit` object available as `Astro.response`.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
