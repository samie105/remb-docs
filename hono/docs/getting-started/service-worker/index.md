---
title: "Service Worker ​"
source: "https://hono.dev/docs/getting-started/service-worker"
canonical_url: "https://hono.dev/docs/getting-started/service-worker"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:48.140Z"
content_hash: "07256421602f9d7a54b3e77499f4a0f50bca9ee8999eb63e39877ef87354eabc"
menu_path: ["Service Worker ​"]
section_path: []
nav_prev: {"path": "../webassembly-wasi/index.md", "title": "WebAssembly (w/ WASI) \u200b"}
nav_next: {"path": "../nodejs/index.md", "title": "Node.js \u200b"}
---

[Service Worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) is a script that runs in the background of the browser to handle tasks like caching and push notifications. Using a Service Worker adapter, you can run applications made with Hono as [FetchEvent](https://developer.mozilla.org/en-US/docs/Web/API/FetchEvent) handler within the browser.

This page shows an example of creating a project using [Vite](https://vitejs.dev/).

## 1\. Setup [​](#_1-setup)

First, create and move to your project directory:

sh

```
mkdir my-app
cd my-app
```

Create the necessary files for the project. Make a `package.json` file with the following:

json

```
{
  "name": "my-app",
  "private": true,
  "scripts": {
    "dev": "vite dev"
  },
  "type": "module"
}
```

Similarly, create a `tsconfig.json` file with the following:

json

```
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "WebWorker"],
    "moduleResolution": "bundler"
  },
  "include": ["./"],
  "exclude": ["node_modules"]
}
```

Next, install the necessary modules.

npmyarnpnpmbun

sh

```
npm i hono
npm i -D vite
```

sh

```
yarn add hono
yarn add -D vite
```

sh

```
pnpm add hono
pnpm add -D vite
```

sh

```
bun add hono
bun add -D vite
```

## 2\. Hello World [​](#_2-hello-world)

Edit `index.html`:

html

```
<!doctype html>
<html>
  <body>
    <a href="/sw">Hello World by Service Worker</a>
    <script type="module" src="/main.ts"></script>
  </body>
</html>
```

`main.ts` is a script to register the Service Worker:

ts

```
function register() {
  navigator.serviceWorker
    .register('/sw.ts', { scope: '/sw', type: 'module' })
    .then(
      function (_registration) {
        console.log('Register Service Worker: Success')
      },
      function (_error) {
        console.log('Register Service Worker: Error')
      }
    )
}
function start() {
  navigator.serviceWorker
    .getRegistrations()
    .then(function (registrations) {
      for (const registration of registrations) {
        console.log('Unregister Service Worker')
        registration.unregister()
      }
      register()
    })
}
start()
```

In `sw.ts`, create an application using Hono and register it to the `fetch` event with the Service Worker adapter’s `handle` function. This allows the Hono application to intercept access to `/sw`.

ts

```
// To support types
// https://github.com/microsoft/TypeScript/issues/14877
declare const self: ServiceWorkerGlobalScope

import { Hono } from 'hono'
import { handle } from 'hono/service-worker'

const app = new Hono().basePath('/sw')
app.get('/', (c) => c.text('Hello World'))

self.addEventListener('fetch', handle(app))
```

### Using `fire()` [​](#using-fire)

The `fire()` function automatically calls `addEventListener('fetch', handle(app))` for you, making the code more concise.

ts

```
import { Hono } from 'hono'
import { fire } from 'hono/service-worker'

const app = new Hono().basePath('/sw')
app.get('/', (c) => c.text('Hello World'))

fire(app)
```

## 3\. Run [​](#_3-run)

Start the development server.

npmyarnpnpmbun

sh

```
npm run dev
```

sh

```
yarn dev
```

sh

```
pnpm run dev
```

sh

```
bun run dev
```

By default, the development server will run on port `5173`. Access `http://localhost:5173/` in your browser to complete the Service Worker registration. Then, access `/sw` to see the response from the Hono application.
