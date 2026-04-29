---
title: "No assign module variable"
source: "https://nextjs.org/docs/messages/no-assign-module-variable"
canonical_url: "https://nextjs.org/docs/messages/no-assign-module-variable"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:28.938Z"
content_hash: "609d77b9ee259ac294a59cad7766cd6ef35eed3f98d5c610aaa57c7cf69e031f"
menu_path: ["No assign module variable"]
section_path: []
version: "latest"
content_language: "en"
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
