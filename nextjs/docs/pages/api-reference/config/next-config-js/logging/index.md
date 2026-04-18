---
title: "logging"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/logging"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/logging"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:55.118Z"
content_hash: "f5c9a562ef3d37a9ff9ed9088393b152bd3eae60ba3980696a0920d98e4ae1a8"
menu_path: ["logging"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/images/index.md", "title": "images"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/onDemandEntries/index.md", "title": "onDemandEntries"}
---

# logging

Last updated April 15, 2026

## Options[](#options)

### Incoming Requests[](#incoming-requests)

By default all the incoming requests will be logged in the console during development. You can use the `incomingRequests` option to decide which requests to ignore. Since this is only logged in development, this option doesn't affect production builds.

next.config.js

```
module.exports = {
  logging: {
    incomingRequests: {
      ignore: [/\api\/v1\/health/],
    },
  },
}
```

Or you can disable incoming request logging by setting `incomingRequests` to `false`.

next.config.js

```
module.exports = {
  logging: {
    incomingRequests: false,
  },
}
```

### Browser Console Logs[](#browser-console-logs)

You can forward browser console logs (such as `console.log`, `console.warn`, `console.error`) to the terminal during development. This is useful for debugging client-side code without needing to check the browser's developer tools.

next.config.js

```
module.exports = {
  logging: {
    browserToTerminal: true,
  },
}
```

#### Options[](#options-1)

The `browserToTerminal` option accepts the following values:

Value

Description

`'warn'`

Forward only warnings and errors, by default

`'error'`

Forward only errors

`true`

Forward all console output (log, info, warn, error)

`false`

Disable browser log forwarding

next.config.js

```
module.exports = {
  logging: {
    browserToTerminal: 'warn',
  },
}
```

#### Source Location[](#source-location)

When enabled, browser logs include source location information (file path and line number) by default. For example:

pages/index.tsx

```
export default function Home() {
  return (
    <button
      type="button"
      onClick={() => {
        console.log('Hello World')
      }}
    >
      Click me
    </button>
  )
}
```

Clicking the button prints this message to the terminal:

Terminal

```
[browser] Hello World (pages/index.tsx:6:17)
```

### Disabling Logging[](#disabling-logging)

In addition, you can disable the development logging by setting `logging` to `false`.

next.config.js

```
module.exports = {
  logging: false,
}
```

## Version History[](#version-history)

Version

Changes

`v16.2.0`

`browserToTerminal` added (moved from `experimental.browserDebugInfoInTerminal`)

`v15.4.0`

`experimental.browserDebugInfoInTerminal` introduced

`v15.2.0`

`incomingRequests` added

`v15.0.0`

`logging: false` option added, `fetches.hmrRefreshes` added for App Router

`v14.0.0`

`logging.fetches` moved to stable for App Router

Was this helpful?

supported.

Send
