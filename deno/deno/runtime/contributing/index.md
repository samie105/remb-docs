---
title: "Contributing and support"
source: "https://docs.deno.com/runtime/contributing/"
canonical_url: "https://docs.deno.com/runtime/contributing/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:42.123Z"
content_hash: "9067ffc88952b4146f1b6abbf2ebbe837e6330d346248283559070da90ad3404"
menu_path: ["Contributing and support"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/docker/index.md", "title": "Deno and Docker"}
nav_next: {"path": "deno/deno/runtime/contributing/architecture/index.md", "title": "Architecture Overview"}
---

# Basic usage
samply record -r 20000 deno run -A main.js
```

You can analyze the generated flamegraph to identify:

*   Hot spots where most CPU time is spent
*   Unexpected function calls
*   Potential areas for optimization

When submitting performance-related contributions, including profiling data can help the team to understand and validate your improvements.

