---
title: "Adapter does not support server output."
source: "https://docs.astro.build/en/reference/errors/adapter-support-output-mismatch/"
canonical_url: "https://docs.astro.build/en/reference/errors/adapter-support-output-mismatch/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:30.136Z"
content_hash: "2cf713ce6de24dfb7477c0e18f2a697720e198b3cb43c80cbd4179e9961cbb8c"
menu_path: ["Adapter does not support server output."]
section_path: []
---
# Adapter does not support server output.

> **AdapterSupportOutputMismatch**: The `ADAPTER_NAME` adapter is configured to output a static website, but the project contains server-rendered pages. Please install and configure the appropriate server adapter for your final deployment.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The currently configured adapter does not support server-side rendering, which is required for the current project setup.

Depending on your adapter, there may be a different entrypoint to use for server-side rendering. For example, the `@astrojs/vercel` adapter has a `@astrojs/vercel/static` entrypoint for static rendering, and a `@astrojs/vercel/serverless` entrypoint for server-side rendering.

**See Also:**

*   [Server-side Rendering](/en/guides/on-demand-rendering/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
