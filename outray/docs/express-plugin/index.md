---
title: "Express Plugin"
source: "https://outray.dev/docs/express-plugin"
canonical_url: "https://outray.dev/docs/express-plugin"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:27:17.280Z"
content_hash: "e041b97c2f74bbb2d44b2deca442a418c89f8b4df85dca1a4da33560d2cde0ea"
menu_path: ["Express Plugin"]
section_path: []
nav_prev: {"path": "outray/docs/nestjs-plugin/index.md", "title": "NestJS Plugin"}
nav_next: {"path": "outray/docs/protocols/index.md", "title": "TCP & UDP Tunnels"}
---

## Express Plugin

Automatically expose your Express dev server via OutRay tunnel

The `@outray/express` plugin automatically creates an OutRay tunnel when your Express development server starts, giving you a public URL to share your local development environment.

```
npm install @outray/express
```

```
pnpm add @outray/express
```

```
yarn add @outray/express
```

Add the plugin to your Express application:

```
// index.js
import express from 'express';
import outray from '@outray/express';

const app = express();

// Apply OutRay middleware
outray(app);

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

When you run your Express server in development mode, you'll see your tunnel URL:

```
Server running on port 3000
  ➜  Tunnel:  https://abc123.outray.dev
```

The plugin accepts an options object to customize its behavior:

```
import express from 'express';
import outray from '@outray/express';

const app = express();

outray(app, {
  subdomain: 'my-api',
  apiKey: process.env.OUTRAY_API_KEY,
});

app.listen(3000);
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
| `NODE_ENV` | Set to `development` to enable the tunnel (production is disabled by default) |
| `OUTRAY_API_KEY` | API key for authentication (fallback for `apiKey` option) |
| `OUTRAY_SUBDOMAIN` | Subdomain to use (fallback for `subdomain` option) |
| `OUTRAY_SERVER_URL` | Server URL (fallback for `serverUrl` option) |
| `OUTRAY_ENABLED` | Set to `"false"` to disable the tunnel |

### [Custom Subdomain](#custom-subdomain)

Reserve a consistent subdomain for your API:

```
import express from 'express';
import outray from '@outray/express';

const app = express();

outray(app, {
  subdomain: 'my-api',
  apiKey: process.env.OUTRAY_API_KEY,
});

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.listen(3000);
```

### [Custom Domain](#custom-domain)

Use your own domain for the tunnel:

```
import express from 'express';
import outray from '@outray/express';

const app = express();

outray(app, {
  customDomain: 'api.example.com',
  apiKey: process.env.OUTRAY_API_KEY,
});

app.listen(3000);
```

### [Conditional Enabling](#conditional-enabling)

Only enable the tunnel in certain environments:

```
import express from 'express';
import outray from '@outray/express';

const app = express();

outray(app, {
  enabled: process.env.EXPOSE_TUNNEL === 'true',
});

app.listen(3000);
```

### [With Callbacks](#with-callbacks)

React to tunnel events in your application:

```
import express from 'express';
import outray from '@outray/express';

const app = express();

outray(app, {
  onTunnelReady: (url) => {
    console.log(`API accessible at: ${url}`);
    // Send to Slack, update config, etc.
  },
  onError: (error) => {
    console.error('Tunnel error:', error.message);
  },
  onReconnecting: () => {
    console.log('Connection lost, reconnecting...');
  },
});

app.listen(3000);
```

### [Silent Mode](#silent-mode)

Disable all tunnel logs:

```
import express from 'express';
import outray from '@outray/express';

const app = express();

outray(app, {
  silent: true,
  onTunnelReady: (url) => {
    // Handle the URL silently
  },
});

app.listen(3000);
```

### [Dynamic Port](#dynamic-port)

Works perfectly with dynamically assigned ports:

```
import express from 'express';
import outray from '@outray/express';

const app = express();

outray(app);

// Use port 0 for a random available port
const server = app.listen(0, () => {
  const port = server.address().port;
  console.log(`Server running on port ${port}`);
});
```

Perfect for exposing your local API for webhook testing:

```
import express from 'express';
import outray from '@outray/express';

const app = express();

outray(app, {
  subdomain: 'webhook-test',
  onTunnelReady: (url) => {
    console.log(`Webhook endpoint: ${url}/webhooks`);
  },
});

app.use(express.json());

app.post('/webhooks', (req, res) => {
  console.log('Received webhook:', req.body);
  res.json({ received: true });
});

app.listen(3000);
```

The plugin includes full TypeScript definitions:

```
import express, { Application } from 'express';
import outray, { OutrayPluginOptions } from '@outray/express';

const app: Application = express();

const options: OutrayPluginOptions = {
  subdomain: 'my-api',
  apiKey: process.env.OUTRAY_API_KEY,
  onTunnelReady: (url: string) => {
    console.log(`Tunnel ready: ${url}`);
  },
};

outray(app, options);

app.listen(3000);
```

The OutRay plugin doesn't interfere with your middleware stack. You can place it anywhere:

```
import express from 'express';
import outray from '@outray/express';
import cors from 'cors';
import helmet from 'helmet';

const app = express();

// Apply OutRay before or after other middleware
outray(app);

app.use(cors());
app.use(helmet());
app.use(express.json());

app.listen(3000);
```

The plugin supports Express versions 4.x and 5.x.

The plugin hooks into Express's `app.listen()` method to:

1.  Detect when your server starts listening
2.  Capture the port number (even for dynamic ports)
3.  Establish a WebSocket tunnel to OutRay servers
4.  Proxy all incoming HTTP requests to your local server

### [Tunnel not starting](#tunnel-not-starting)

-   Ensure `NODE_ENV` is set to `development`
-   Check that `OUTRAY_ENABLED` is not set to `"false"`
-   Verify your server is listening on a TCP port (not a Unix socket)

### [Authentication errors](#authentication-errors)

-   Run `outray login` in your terminal to authenticate
-   Or set the `OUTRAY_API_KEY` environment variable

### [Connection issues](#connection-issues)

-   Check your internet connection
-   Verify the server URL is correct (default: `wss://api.outray.dev/`)
-   The plugin will automatically attempt to reconnect on connection loss

### [Not seeing tunnel URL](#not-seeing-tunnel-url)

Make sure you're running in development mode:

```
NODE_ENV=development node app.js
```

Or add it to your package.json:

```
{
  "scripts": {
    "dev": "NODE_ENV=development node app.js"
  }
}
```
