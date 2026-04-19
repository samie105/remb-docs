---
title: "No assign module variable"
source: "https://nextjs.org/docs/messages/no-assign-module-variable"
canonical_url: "https://nextjs.org/docs/messages/no-assign-module-variable"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:04.031Z"
content_hash: "e3badf5fbe59fe8b917060287ed767d1ba3ad3188979aed133d00ef7046fe1a8"
menu_path: ["No assign module variable"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/next-script-for-ga/index.md", "title": "Using Google Analytics with Next.js (through `@next/third-parties/google`)"}
nav_next: {"path": "nextjs/docs/messages/no-async-client-component/index.md", "title": "No async Client Component"}
---

# No assign module variable

> Prevent assignment to the `module` variable.

## Why This Error Occurred[](#why-this-error-occurred)

A value is being assigned to the `module` variable. The `module` variable is already used and it is highly likely that assigning to this variable will cause errors.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Use a different variable name:

example.js

```
let myModule = {...}
```

Was this helpful?

supported.

Send
