---
title: "Contributing and support"
source: "https://docs.deno.com/runtime/contributing/profiling/"
canonical_url: "https://docs.deno.com/runtime/contributing/profiling/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:14.959Z"
content_hash: "9067ffc88952b4146f1b6abbf2ebbe837e6330d346248283559070da90ad3404"
menu_path: ["Contributing and support"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/contributing/architecture/index.md", "title": "Architecture Overview"}
nav_next: {"path": "deno/deno/runtime/contributing/release_schedule/index.md", "title": "Release Schedule"}
---

# Basic usage
samply record -r 20000 deno run -A main.js
```

You can analyze the generated flamegraph to identify:

*   Hot spots where most CPU time is spent
*   Unexpected function calls
*   Potential areas for optimization

When submitting performance-related contributions, including profiling data can help the team to understand and validate your improvements.


