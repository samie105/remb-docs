---
title: "REPL"
source: "https://bun.com/docs/runtime/repl"
canonical_url: "https://bun.com/docs/runtime/repl"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:15.697Z"
content_hash: "9102c929f5953a8eb5d2fb181bc85b80d586a91180575ee0c73d9894af65dfcb"
menu_path: ["REPL"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/redis/index.md", "title": "Redis"}
nav_next: {"path": "bun/bun/docs/runtime/s3/index.md", "title": "S3"}
---

# 42

bun repl -p "await fetch('https://example.com').then(r => r.status)"
# 200

bun repl -p "{ a: 1, b: 2 }"
# { a: 1, b: 2 }
```

This uses the same transforms as the interactive REPL, so a bare object literal like `{ a: 1 }` is treated as an object expression instead of a block statement. The process exits after the event loop drains (pending timers and I/O complete first). On error, the process exits with code `1`.
