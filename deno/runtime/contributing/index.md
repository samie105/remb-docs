---
title: "Contributing and support"
source: "https://docs.deno.com/runtime/contributing/"
canonical_url: "https://docs.deno.com/runtime/contributing/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:17:52.404Z"
content_hash: "6ade55c8bf1f85254456175cf22b1abbe13e9ed5040cf2b2bb75095cfd20862d"
menu_path: ["Contributing and support"]
section_path: []
content_language: "en"
nav_prev: {"path": "../reference/docker/index.md", "title": "Deno and Docker"}
nav_next: {"path": "architecture/index.md", "title": "Architecture Overview"}
---

# Basic usage
samply record -r 20000 deno run -A main.js
```

You can analyze the generated flamegraph to identify:

-   Hot spots where most CPU time is spent
-   Unexpected function calls
-   Potential areas for optimization

When submitting performance-related contributions, including profiling data can help the team to understand and validate your improvements.
