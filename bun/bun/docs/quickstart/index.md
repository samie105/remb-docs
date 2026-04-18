---
title: "Quickstart"
source: "https://bun.com/docs/quickstart"
canonical_url: "https://bun.com/docs/quickstart"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:33.670Z"
content_hash: "9126a4769072094c734842f0a2806b2360495ba6a124776201aafffab7e0415a"
menu_path: ["Quickstart"]
section_path: []
nav_prev: {"path": "bun/bun/docs/project/roadmap/index.md", "title": "Roadmap"}
nav_next: {"path": "bun/bun/docs/runtime/auto-install/index.md", "title": "Auto-install"}
---

## Overview

Build a minimal HTTP server with `Bun.serve`, run it locally, then evolve it by installing a package.

* * *

1

2

3

4

5

🎉 Congratulations! You’ve built an HTTP server with Bun and installed a package.

* * *

## Run a script

Bun can also execute `"scripts"` from your `package.json`. Add the following script:

package.json

```
{
  "name": "quickstart",
  "module": "index.ts",
  "type": "module",
  "private": true,
  "scripts": { 
    "start": "bun run index.ts"
  }, 
  "devDependencies": {
    "@types/bun": "latest"
  },
  "peerDependencies": {
    "typescript": "^5"
  }
}
```

Then run it with `bun run start`.

terminal

```
bun run start
```

```
Listening on http://localhost:3000
```
