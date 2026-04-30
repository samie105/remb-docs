---
title: "Vite Plugin"
source: "https://outray.dev/docs/vite-plugin"
canonical_url: "https://outray.dev/docs/vite-plugin"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:26:10.594Z"
content_hash: "a1d846214e4ec5a7d63b99220f93246116b82bbf35441bf84ac1aa19811c281e"
menu_path: ["Vite Plugin"]
section_path: []
nav_prev: {"path": "outray/docs/observability/index.md", "title": "Observability"}
nav_next: {"path": "outray/docs/nextjs-plugin/index.md", "title": "Next.js Plugin"}
---

## Vite Plugin

Automatically expose your Vite dev server via OutRay tunnel

The `@outray/vite` plugin automatically creates an OutRay tunnel when your Vite development server starts, giving you a public URL to share your local development environment.

```
npm install @outray/vite
```

```
pnpm add @outray/vite
```

```
yarn add @outray/vite
```

Add the plugin to your Vite configuration:

```
// vite.config.ts
import { defineConfig } from 'vite'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [outray()]
})
```

When you run `vite` or `npm run dev`, you'll see your tunnel URL printed alongside the local URL:

```
  ➜  Local:   http://localhost:5173/
  ➜  Tunnel:  https://abc123.outray.dev
```

The plugin accepts an options object to customize its behavior:

```
import { defineConfig } from 'vite'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [
    outray({
      subdomain: 'my-app',
      apiKey: process.env.OUTRAY_API_KEY,
    })
  ]
})
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

### [Custom Subdomain](#custom-subdomain)

Reserve a consistent subdomain for your project:

```
import { defineConfig } from 'vite'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [
    outray({
      subdomain: 'my-app',
      apiKey: process.env.OUTRAY_API_KEY,
    })
  ]
})
```

### [Custom Domain](#custom-domain)

Use your own domain for the tunnel:

```
import { defineConfig } from 'vite'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [
    outray({
      customDomain: 'dev.example.com',
      apiKey: process.env.OUTRAY_API_KEY,
    })
  ]
})
```

### [Conditional Enabling](#conditional-enabling)

Only enable the tunnel in certain environments:

```
import { defineConfig } from 'vite'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [
    outray({
      enabled: process.env.EXPOSE_TUNNEL === 'true',
    })
  ]
})
```

### [With Callbacks](#with-callbacks)

React to tunnel events in your application:

```
import { defineConfig } from 'vite'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [
    outray({
      onTunnelReady: (url) => {
        console.log(`Share this URL: ${url}`)
        // Copy to clipboard, send notification, etc.
      },
      onError: (error) => {
        console.error('Tunnel error:', error.message)
      },
      onReconnecting: () => {
        console.log('Connection lost, reconnecting...')
      },
    })
  ]
})
```

### [Silent Mode](#silent-mode)

Disable all tunnel logs:

```
import { defineConfig } from 'vite'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [
    outray({
      silent: true,
      onTunnelReady: (url) => {
        // Handle the URL silently
      },
    })
  ]
})
```

The plugin works seamlessly with all Vite-based frameworks:

### [React](#react)

```
// vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [react(), outray()]
})
```

### [Vue](#vue)

```
// vite.config.ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [vue(), outray()]
})
```

### [Svelte](#svelte)

```
// vite.config.ts
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [svelte(), outray()]
})
```

### [SolidJS](#solidjs)

```
// vite.config.ts
import { defineConfig } from 'vite'
import solid from 'vite-plugin-solid'
import outray from '@outray/vite'

export default defineConfig({
  plugins: [solid(), outray()]
})
```

The plugin supports Vite versions 4.x, 5.x, 6.x, and 7.x.

### [Tunnel not starting](#tunnel-not-starting)

-   Ensure your Vite dev server is running on a TCP port (not a Unix socket)
-   Check that `OUTRAY_ENABLED` is not set to `"false"`
-   Verify your API key is valid if using a reserved subdomain

### [Authentication errors](#authentication-errors)

-   Run `outray login` in your terminal to authenticate
-   Or set the `OUTRAY_API_KEY` environment variable

### [Connection issues](#connection-issues)

-   Check your internet connection
-   Verify the server URL is correct (default: `wss://api.outray.dev/`)
-   The plugin will automatically attempt to reconnect on connection loss
