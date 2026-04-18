---
title: "Experimental client prerendering"
source: "https://docs.astro.build/en/reference/experimental-flags/client-prerender/"
canonical_url: "https://docs.astro.build/en/reference/experimental-flags/client-prerender/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:02.056Z"
content_hash: "946ba3bf6a03ece925a025ab57e888358b50e438a5c67aebdf827431c42e4323"
menu_path: ["Experimental client prerendering"]
section_path: []
nav_prev: {"path": "astro/en/reference/experimental-flags/route-caching/index.md", "title": "Experimental route caching"}
nav_next: {"path": "astro/en/reference/experimental-flags/content-intellisense/index.md", "title": "Experimental Intellisense for content collections"}
---

# Experimental client prerendering

**Type:** `boolean`  
**Default:** `false`  

**Added in:** `astro@4.2.0`

Enables pre-rendering your prefetched pages on the client in supported browsers.

This feature uses the experimental [Speculation Rules Web API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API) and enhances the default `prefetch` behavior globally to prerender links on the client. You may wish to review the [possible risks when prerendering on the client](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API#unsafe_prefetching) before enabling this feature.

Enable client side prerendering in your `astro.config.mjs` along with any desired `prefetch` configuration options:

```
import { defineConfig } from 'astro/config';
export default defineConfig({  prefetch: {    prefetchAll: true,    defaultStrategy: 'viewport',  },  experimental: {    clientPrerender: true,  },});
```

Continue to use the `data-astro-prefetch` attribute on any `<a />` link on your site to opt in to prefetching. Instead of appending a `<link>` tag to the head of the document or fetching the page with JavaScript, a `<script>` tag will be appended with the corresponding speculation rules.

Client side prerendering requires browser support. If the Speculation Rules API is not supported, `prefetch` will fallback to the supported strategy.

See the [Prefetch Guide](/en/guides/prefetch/) for more `prefetch` options and usage.

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

