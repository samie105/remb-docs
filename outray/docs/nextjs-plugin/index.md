---
title: "Next.js Plugin"
source: "https://outray.dev/docs/nextjs-plugin"
canonical_url: "https://outray.dev/docs/nextjs-plugin"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:26:42.775Z"
content_hash: "49e28dd86cc1a510d74761e96cc140052f937396f69198c419fdbceaf71b7edc"
menu_path: ["Next.js Plugin"]
section_path: []
nav_prev: {"path": "outray/docs/vite-plugin/index.md", "title": "Vite Plugin"}
nav_next: {"path": "outray/docs/nestjs-plugin/index.md", "title": "NestJS Plugin"}
---

## Next.js Plugin

Automatically expose your Next.js dev server via OutRay tunnel

The `@outray/next` plugin automatically creates an OutRay tunnel when your Next.js development server starts, giving you a public URL to share your local development environment.

```
npm install @outray/next
```

```
pnpm add @outray/next
```

```
yarn add @outray/next
```

Wrap your Next.js configuration with the plugin:

```
// next.config.ts
import withOutray from '@outray/next'

export default withOutray({
  // your Next.js config
})
```

When you run `next dev` or `npm run dev`, you'll see your tunnel URL printed in the terminal:

```
  ➜  Local:   http://localhost:3000
  ➜  Tunnel:  https://abc123.outray.dev
```

The plugin accepts an options object as the second argument:

```
// next.config.ts
import withOutray from '@outray/next'

export default withOutray(
  {
    // your Next.js config
  },
  {
    subdomain: 'my-app',
    apiKey: process.env.OUTRAY_API_KEY,
  }
)
```

### [Options](#options)

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `subdomain` | `string` | — | Request a specific subdomain for your tunnel URL. Requires authentication. |
| `customDomain` | `string` | — | Use a custom domain. Must be configured in the OutRay dashboard first. |
| `apiKey` | `string` | `process.env.OUTRAY_API_KEY` | API key for authentication. |
| `serverUrl` | `string` | `wss://api.outray.dev/` | OutRay server WebSocket URL. Only change this for self-hosted instances. |
| `enabled` | `boolean` | `process.env.OUTRAY_ENABLED !== "false"` | Enable or disable the tunnel. |
| `silent` | `boolean` | `false` | Suppress tunnel status logs. |
| `onTunnelReady` | `(url: string) => void` | — | Callback fired when tunnel is successfully established. |
| `onError` | `(error: Error) => void` | — | Callback fired when tunnel encounters an error. |
| `onClose` | `() => void` | — | Callback fired when tunnel connection is closed. |
| `onReconnecting` | `() => void` | — | Callback fired when tunnel is attempting to reconnect. |

The plugin respects the following environment variables:

| Variable | Description |
| --- | --- |
| `OUTRAY_API_KEY` | API key for authentication (fallback for `apiKey` option) |
| `OUTRAY_SUBDOMAIN` | Subdomain to use (fallback for `subdomain` option) |
| `OUTRAY_SERVER_URL` | Server URL (fallback for `serverUrl` option) |
| `OUTRAY_ENABLED` | Set to `"false"` to disable the tunnel |
| `PORT` | The port your Next.js dev server runs on (default: 3000) |

### [Custom Subdomain](#custom-subdomain)

Reserve a consistent subdomain for your project:

```
// next.config.ts
import withOutray from '@outray/next'

export default withOutray(
  {
    // your Next.js config
  },
  {
    subdomain: 'my-app',
    apiKey: process.env.OUTRAY_API_KEY,
  }
)
```

### [Custom Domain](#custom-domain)

Use your own domain for the tunnel:

```
// next.config.ts
import withOutray from '@outray/next'

export default withOutray(
  {},
  {
    customDomain: 'dev.example.com',
    apiKey: process.env.OUTRAY_API_KEY,
  }
)
```

### [Conditional Enabling](#conditional-enabling)

Only enable the tunnel in certain environments:

```
// next.config.ts
import withOutray from '@outray/next'

export default withOutray(
  {},
  {
    enabled: process.env.EXPOSE_TUNNEL === 'true',
  }
)
```

### [With Callbacks](#with-callbacks)

React to tunnel events in your application:

```
// next.config.ts
import withOutray from '@outray/next'

export default withOutray(
  {},
  {
    onTunnelReady: (url) => {
      console.log(`Share this URL: ${url}`)
    },
    onError: (error) => {
      console.error('Tunnel error:', error.message)
    },
    onReconnecting: () => {
      console.log('Connection lost, reconnecting...')
    },
  }
)
```

### [Silent Mode](#silent-mode)

Disable all tunnel logs:

```
// next.config.ts
import withOutray from '@outray/next'

export default withOutray(
  {},
  {
    silent: true,
    onTunnelReady: (url) => {
      // Handle the URL silently
    },
  }
)
```

### [With Other Plugins](#with-other-plugins)

Compose with other Next.js plugins:

```
// next.config.ts
import withOutray from '@outray/next'
import withBundleAnalyzer from '@next/bundle-analyzer'

const config = {
  // your Next.js config
}

export default withOutray(
  withBundleAnalyzer({ enabled: process.env.ANALYZE === 'true' })(config),
  {
    subdomain: 'my-app',
  }
)
```

## [App Router & Pages Router](#app-router--pages-router)

The plugin works seamlessly with both Next.js App Router and Pages Router. No additional configuration is required.

The plugin supports Next.js versions 13.x, 14.x, and 15.x.

### [Tunnel not starting](#tunnel-not-starting)

-   Ensure you're running in development mode (`next dev`)
-   Check that `OUTRAY_ENABLED` is not set to `"false"`
-   Verify the `PORT` environment variable matches your dev server port

### [Authentication errors](#authentication-errors)

-   Run `outray login` in your terminal to authenticate
-   Or set the `OUTRAY_API_KEY` environment variable

### [Connection issues](#connection-issues)

-   Check your internet connection
-   Verify the server URL is correct (default: `wss://api.outray.dev/`)
-   The plugin will automatically attempt to reconnect on connection loss

### [Turbopack compatibility](#turbopack-compatibility)

The plugin works with both webpack and Turbopack. The tunnel is started during the webpack configuration phase, which runs even when using Turbopack for development.
