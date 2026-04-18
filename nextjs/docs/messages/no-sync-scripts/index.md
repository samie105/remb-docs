---
title: "No Sync Scripts"
source: "https://nextjs.org/docs/messages/no-sync-scripts"
canonical_url: "https://nextjs.org/docs/messages/no-sync-scripts"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:36.036Z"
content_hash: "ba131c508d04522c36de7b0e1cd4ecb0e500d5e0fe5daafe8a2726164f771601"
menu_path: ["No Sync Scripts"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-styled-jsx-in-document/index.md", "title": "No `styled-jsx` in `_document`"}
nav_next: {"path": "nextjs/docs/messages/no-title-in-document-head/index.md", "title": "No Title in Document Head"}
---

# No Sync Scripts

> Prevent synchronous scripts.

## Why This Error Occurred[](#why-this-error-occurred)

A synchronous script was used which can impact your webpage performance.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

### Script component (recommended)[](#script-component-recommended)

pages/index.js

```
import Script from 'next/script'
 
function Home() {
  return (
    <div class="container">
      <Script src="https://third-party-script.js"></Script>
      <div>Home Page</div>
    </div>
  )
}
 
export default Home
```

### Use `async` or `defer`[](#use-async-or-defer)

```
<script src="https://third-party-script.js" async />
<script src="https://third-party-script.js" defer />
```

## Useful Links[](#useful-links)

*   [Efficiently load third-party JavaScript](https://web.dev/efficiently-load-third-party-javascript/)

Was this helpful?

supported.

Send




