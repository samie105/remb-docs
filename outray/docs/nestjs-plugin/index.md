---
title: "NestJS Plugin"
source: "https://outray.dev/docs/nestjs-plugin"
canonical_url: "https://outray.dev/docs/nestjs-plugin"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:26:44.430Z"
content_hash: "4c03aaa40875a2ef540ef2e35c4cb1539a0d8b5fe9235556f74c0103c7835c98"
menu_path: ["NestJS Plugin"]
section_path: []
nav_prev: {"path": "outray/docs/nextjs-plugin/index.md", "title": "Next.js Plugin"}
nav_next: {"path": "outray/docs/express-plugin/index.md", "title": "Express Plugin"}
---

## NestJS Plugin

Automatically expose your NestJS dev server via OutRay tunnel

The `@outray/nest` plugin automatically creates an OutRay tunnel when your NestJS application starts, giving you a public URL to share your local development environment.

```
npm install @outray/nest
```

```
pnpm add @outray/nest
```

```
yarn add @outray/nest
```

Add the plugin to your NestJS application's `main.ts`:

```
// main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Start the server
  await app.listen(3000);

  // Start the tunnel in development
  if (process.env.NODE_ENV !== 'production') {
    await outray(app);
  }
}
bootstrap();
```

When you run your NestJS server in development mode, you'll see your tunnel URL:

```
[Nest] Application is running on: http://localhost:3000
  ➜  Tunnel:  https://abc123.outray.dev
```

The plugin accepts an options object to customize its behavior:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  await outray(app, {
    subdomain: 'my-api',
    apiKey: process.env.OUTRAY_API_KEY,
  });
}
bootstrap();
```

### [Options](#options)

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `port` | `number | string` | Auto-detected | The local port your NestJS app is running on. Automatically detected from the app instance. |
| `subdomain` | `string` | — | Request a specific subdomain for your tunnel URL. Requires authentication. |
| `customDomain` | `string` | — | Use a custom domain. Must be configured in the OutRay dashboard first. |
| `apiKey` | `string` | `process.env.OUTRAY_API_KEY` | API key for authentication. |
| `serverUrl` | `string` | `wss://api.outray.dev/` | OutRay server WebSocket URL. Only change this for self-hosted instances. |
| `enabled` | `boolean` | `process.env.NODE_ENV !== 'production'` | Enable or disable the tunnel. Disabled by default in production. |
| `silent` | `boolean` | `false` | Suppress tunnel status logs. |
| `onTunnelReady` | `(url: string) => void` | — | Callback fired when tunnel is successfully established. |
| `onError` | `(error: Error) => void` | — | Callback fired when tunnel encounters an error. |
| `onClose` | `() => void` | — | Callback fired when tunnel connection is closed. |
| `onReconnecting` | `() => void` | — | Callback fired when tunnel is attempting to reconnect. |

The plugin respects the following environment variables:

| Variable | Description |
| --- | --- |
| `NODE_ENV` | Set to `production` to disable the tunnel automatically |
| `OUTRAY_API_KEY` | API key for authentication (fallback for `apiKey` option) |
| `OUTRAY_SUBDOMAIN` | Subdomain to use (fallback for `subdomain` option) |
| `OUTRAY_SERVER_URL` | Server URL (fallback for `serverUrl` option) |

### [Custom Subdomain](#custom-subdomain)

Reserve a consistent subdomain for your API:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  await outray(app, {
    subdomain: 'my-api',
    apiKey: process.env.OUTRAY_API_KEY,
  });
}
bootstrap();
```

### [Custom Domain](#custom-domain)

Use your own domain for the tunnel:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  await outray(app, {
    customDomain: 'api.example.com',
    apiKey: process.env.OUTRAY_API_KEY,
  });
}
bootstrap();
```

### [Conditional Enabling](#conditional-enabling)

Only enable the tunnel in certain environments:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  await outray(app, {
    enabled: process.env.EXPOSE_TUNNEL === 'true',
  });
}
bootstrap();
```

### [With Callbacks](#with-callbacks)

React to tunnel events in your application:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  await outray(app, {
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
}
bootstrap();
```

### [Silent Mode](#silent-mode)

Disable all tunnel logs:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  await outray(app, {
    silent: true,
    onTunnelReady: (url) => {
      // Handle the URL silently
    },
  });
}
bootstrap();
```

### [Explicit Port](#explicit-port)

If automatic port detection doesn't work, you can specify the port explicitly:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const port = process.env.PORT || 3000;
  await app.listen(port);

  await outray(app, {
    port: port,
  });
}
bootstrap();
```

Perfect for exposing your GraphQL API for testing:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  await outray(app, {
    subdomain: 'graphql-dev',
    onTunnelReady: (url) => {
      console.log(`GraphQL Playground: ${url}/graphql`);
    },
  });
}
bootstrap();
```

Perfect for testing webhooks from external services:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  await outray(app, {
    subdomain: 'webhook-test',
    onTunnelReady: (url) => {
      console.log(`Webhook endpoint: ${url}/webhooks/stripe`);
    },
  });
}
bootstrap();
```

The plugin includes full TypeScript definitions:

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { outray, OutrayPluginOptions } from '@outray/nest';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  const options: OutrayPluginOptions = {
    subdomain: 'my-api',
    apiKey: process.env.OUTRAY_API_KEY,
    onTunnelReady: (url: string) => {
      console.log(`Tunnel ready: ${url}`);
    },
  };

  await outray(app, options);
}
bootstrap();
```

The plugin supports NestJS versions 8.x, 9.x, 10.x, and 11.x.

The plugin:

1.  Detects the port from the NestJS application's HTTP server
2.  Establishes a WebSocket tunnel to OutRay servers
3.  Proxies all incoming HTTP requests to your local server
4.  Handles cleanup on process exit (SIGINT, SIGTERM)

### [Tunnel not starting](#tunnel-not-starting)

-   Ensure `NODE_ENV` is not set to `production`
-   Check that you've called `await app.listen()` before `await outray(app)`
-   Verify your server is listening on a TCP port

### [Port detection issues](#port-detection-issues)

If the plugin can't detect the port automatically:

-   Make sure you `await app.listen(port)` before calling `outray(app)`
-   Or pass the port explicitly: `outray(app, { port: 3000 })`

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
NODE_ENV=development npm run start:dev
```

Or ensure `enabled` is not set to `false`.
