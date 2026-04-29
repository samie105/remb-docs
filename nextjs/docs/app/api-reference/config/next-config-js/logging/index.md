---
title: "logging"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/logging"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/logging"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:06:42.901Z"
content_hash: "8846b0590769be729457b1c9ebf12c00fddb213cdc2be7a990d6521a788a1cb3"
menu_path: ["logging"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/inlineCss/index.md", "title": "inlineCss"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/mdxRs/index.md", "title": "mdxRs"}
---

# logging

Last updated April 23, 2026

## Options[](#options)

### Fetching[](#fetching)

You can configure the logging level and whether the full URL is logged to the console when running Next.js in development mode.

next.config.js

```
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

Any `fetch` requests that are restored from the [Server Components HMR cache](../serverComponentsHmrCache/index.md) are not logged by default. However, this can be enabled by setting `logging.fetches.hmrRefreshes` to `true`.

next.config.js

```
module.exports = {
  logging: {
    fetches: {
      hmrRefreshes: true,
    },
  },
}
```

### Server Functions[](#server-functions)

[Server Function](https://react.dev/reference/rsc/server-functions) invocations are logged by default during development. You can disable this by setting `logging.serverFunctions` to `false`.

next.config.js

```
module.exports = {
  logging: {
    serverFunctions: false,
  },
}
```

When enabled, the terminal displays each Server Function call with its function name, arguments, and duration:

Terminal

```
POST /
  └─ ƒ myAction(arg1, arg2) in 5ms app/actions.ts
```

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

| Value | Description |
| --- | --- |
| `'warn'` | Forward only warnings and errors, by default |
| `'error'` | Forward only errors |
| `true` | Forward all console output (log, info, warn, error) |
| `false` | Disable browser log forwarding |

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

app/page.tsx

```
'use client'
 
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
[browser] Hello World (app/page.tsx:8:17)
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

| Version | Changes |
| --- | --- |
| `v16.2.0` | `browserToTerminal` added (moved from `experimental.browserDebugInfoInTerminal`) |
| `v15.4.0` | `experimental.browserDebugInfoInTerminal` introduced |
| `v15.2.0` | `incomingRequests` added |
| `v15.0.0` | `logging: false` option added, `fetches.hmrRefreshes` added for App Router |
| `v14.0.0` | `logging.fetches` moved to stable for App Router |

Was this helpful?
