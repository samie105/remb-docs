---
title: "allowedDevOrigins"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:06:47.863Z"
content_hash: "db880b51ce476d121a11cc41de2053a695c4b77c54bf11fe963147d922431d53"
menu_path: ["allowedDevOrigins"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/adapterPath/index.md", "title": "adapterPath"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/appDir/index.md", "title": "appDir"}
---

# allowedDevOrigins

Last updated April 15, 2026

Next.js blocks cross-origin requests to dev-only assets and endpoints during development by default to prevent unauthorized access.

To configure a Next.js application to allow requests from origins other than the hostname the server was initialized with (`localhost` by default), use the `allowedDevOrigins` config option.

`allowedDevOrigins` lets you set additional origins that can request the dev server in development mode. For example, to use `local-origin.dev` instead of only `localhost`, open `next.config.js` and add the `allowedDevOrigins` config:

next.config.js

```
module.exports = {
  allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
}
```

[Previous

adapterPath

](/docs/app/api-reference/config/next-config-js/adapterPath)

[Next

appDir

](/docs/app/api-reference/config/next-config-js/appDir)

Was this helpful?

supported.

Send




