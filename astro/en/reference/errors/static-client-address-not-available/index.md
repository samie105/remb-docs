---
title: "Astro.clientAddress is not available in prerendered pages."
source: "https://docs.astro.build/en/reference/errors/static-client-address-not-available/"
canonical_url: "https://docs.astro.build/en/reference/errors/static-client-address-not-available/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:39.671Z"
content_hash: "78cb927f51c902a2cdef58494c89755fa3b5f7bc2125c3b38071e4a0f03d7542"
menu_path: ["Astro.clientAddress is not available in prerendered pages."]
section_path: []
nav_prev: {"path": "astro/en/reference/errors/session-without-supported-adapter-output-error/index.md", "title": "Sessions cannot be used with an adapter that doesn't support server output."}
nav_next: {"path": "astro/en/reference/errors/static-redirect-not-available/index.md", "title": "Astro.redirect is not available in static mode."}
---

# Astro.clientAddress is not available in prerendered pages.

> **StaticClientAddressNotAvailable**: `Astro.clientAddress` is only available on pages that are server-rendered.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `Astro.clientAddress` property is only available when [Server-side rendering](../../../guides/on-demand-rendering/index.md) is enabled.

To get the user’s IP address in static mode, different APIs such as [Ipify](https://www.ipify.org/) can be used in a [Client-side script](../../../guides/client-side-scripts/index.md) or it may be possible to get the user’s IP using a serverless function hosted on your hosting provider.

**See Also:**

*   [Enabling SSR in Your Project](../../../guides/on-demand-rendering/index.md)
*   [Astro.clientAddress](../../api-reference/index.md#clientaddress)

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
