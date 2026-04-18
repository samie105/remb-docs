---
title: "function Deno.jupyter.html"
source: "https://docs.deno.com/api/deno/~/Deno.jupyter.html"
canonical_url: "https://docs.deno.com/api/deno/~/Deno.jupyter.html"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:15.102Z"
content_hash: "fac35d1a2a73914642201f084cf24f350054c97c5f517aaefb7f346783545b92"
menu_path: ["function Deno.jupyter.html"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/help/index.md", "title": "Where to get help"}
nav_next: {"path": "deno/deno/api/deno/index.md", "title": "Deno Namespace APIs"}
---

# function Deno.jupyter.html

unstable

`[#](#function_html_0)html(  strings: TemplateStringsArray,  ...values: unknown[],  ): [Displayable](../././~/Deno.jupyter.Displayable)`

Show HTML in Jupyter frontends with a tagged template function.

Takes a template string and returns a displayable object for Jupyter frontends.

### Examples [#](#examples)

[#](#example_0)

```typescript
const { html } = Deno.jupyter;
html`<h1>Hello, world!</h1>`
```

### Parameters [#](#parameters)

### Return Type [#](#return-type)
