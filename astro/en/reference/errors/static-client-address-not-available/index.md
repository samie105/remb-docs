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
---
# Astro.clientAddress is not available in prerendered pages.

> **StaticClientAddressNotAvailable**: `Astro.clientAddress` is only available on pages that are server-rendered.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `Astro.clientAddress` property is only available when [Server-side rendering](/en/guides/on-demand-rendering/) is enabled.

To get the user’s IP address in static mode, different APIs such as [Ipify](https://www.ipify.org/) can be used in a [Client-side script](/en/guides/client-side-scripts/) or it may be possible to get the user’s IP using a serverless function hosted on your hosting provider.

**See Also:**

*   [Enabling SSR in Your Project](/en/guides/on-demand-rendering/)
*   [Astro.clientAddress](/en/reference/api-reference/#clientaddress)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
