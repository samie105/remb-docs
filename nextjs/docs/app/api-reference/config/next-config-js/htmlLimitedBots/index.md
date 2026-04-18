---
title: "htmlLimitedBots"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:39.332Z"
content_hash: "70e26de144bb71013c45f3fe651cf1c5cd48d45bf8bbceb33b9c147b50d66170"
menu_path: ["htmlLimitedBots"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/headers/index.md", "title": "headers"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/httpAgentOptions/index.md", "title": "httpAgentOptions"}
---

# htmlLimitedBots

Last updated April 15, 2026

The `htmlLimitedBots` config allows you to specify a list of user agents that should receive blocking metadata instead of [streaming metadata](/docs/app/api-reference/functions/generate-metadata#streaming-metadata).

next.config.ts

TypeScript

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
 
export default config
```

## Default list[](#default-list)

Next.js includes a default list of HTML limited bots, including:

*   Google crawlers (e.g. Mediapartners-Google, AdsBot-Google, Google-PageRenderer)
*   Bingbot
*   Twitterbot
*   Slackbot

See the full list [here](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts).

Specifying a `htmlLimitedBots` config will override the Next.js' default list. However, this is advanced behavior, and the default should be sufficient for most cases.

next.config.ts

TypeScript

JavaScriptTypeScript

```
const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
 
export default config
```

## Disabling[](#disabling)

To fully disable streaming metadata:

next.config.ts

```
import type { NextConfig } from 'next'
 
const config: NextConfig = {
  htmlLimitedBots: /.*/,
}
 
export default config
```

## Version History[](#version-history)

Version

Changes

15.2.0

`htmlLimitedBots` option introduced.

[Previous

headers

](/docs/app/api-reference/config/next-config-js/headers)

[Next

httpAgentOptions

](/docs/app/api-reference/config/next-config-js/httpAgentOptions)

Was this helpful?

supported.

Send




