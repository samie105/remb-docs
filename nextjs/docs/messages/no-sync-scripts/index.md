---
title: "No Sync Scripts"
source: "https://nextjs.org/docs/messages/no-sync-scripts"
canonical_url: "https://nextjs.org/docs/messages/no-sync-scripts"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:18:00.196Z"
content_hash: "20943e8fd62c1fc97f3d6bf83518c79d344678f6b8b9d33ffd080bd3ff27861c"
menu_path: ["No Sync Scripts"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../no-styled-jsx-in-document/index.md", "title": "No `styled-jsx` in `_document`"}
nav_next: {"path": "../no-title-in-document-head/index.md", "title": "No Title in Document Head"}
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

-   [Efficiently load third-party JavaScript](https://web.dev/efficiently-load-third-party-javascript/)

Was this helpful?
