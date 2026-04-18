---
title: "Preview Options ​"
source: "https://vite.dev/config/preview-options"
canonical_url: "https://vite.dev/config/preview-options"
docset: "vite"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:13.938Z"
content_hash: "f739d5365be9d46bd56badbdb491a4b92b189134006c4520eb83d529305575ca"
menu_path: ["Preview Options ​"]
section_path: []
nav_prev: {"path": "vite/config/build-options/index.md", "title": "Build Options \u200b"}
nav_next: {"path": "vite/config/server-options/index.md", "title": "Server Options \u200b"}
---

Unless noted, the options in this section are only applied to preview.

## preview.host [​](#preview-host)

*   **Type:** `string | boolean`
*   **Default:** [`server.host`](vite/config/server-options/index.md#server-host)

Specify which IP addresses the server should listen on. Set this to `0.0.0.0` or `true` to listen on all addresses, including LAN and public addresses.

This can be set via the CLI using `--host 0.0.0.0` or `--host`.

NOTE

There are cases when other servers might respond instead of Vite. See [`server.host`](vite/config/server-options/index.md#server-host) for more details.

## preview.allowedHosts [​](#preview-allowedhosts)

*   **Type:** `string[] | true`
*   **Default:** [`server.allowedHosts`](vite/config/server-options/index.md#server-allowedhosts)

The hostnames that Vite is allowed to respond to.

See [`server.allowedHosts`](vite/config/server-options/index.md#server-allowedhosts) for more details.

## preview.port [​](#preview-port)

*   **Type:** `number`
*   **Default:** `4173`

Specify server port. Note if the port is already being used, Vite will automatically try the next available port so this may not be the actual port the server ends up listening on.

**Example:**

js

```
export default defineConfig({
  server: {
    port: 3030,
  },
  preview: {
    port: 8080,
  },
})
```

## preview.strictPort [​](#preview-strictport)

*   **Type:** `boolean`
*   **Default:** [`server.strictPort`](vite/config/server-options/index.md#server-strictport)

Set to `true` to exit if port is already in use, instead of automatically trying the next available port.

## preview.https [​](#preview-https)

*   **Type:** `https.ServerOptions`
*   **Default:** [`server.https`](vite/config/server-options/index.md#server-https)

Enable TLS + HTTP/2.

See [`server.https`](vite/config/server-options/index.md#server-https) for more details.

## preview.open [​](#preview-open)

*   **Type:** `boolean | string`
*   **Default:** [`server.open`](vite/config/server-options/index.md#server-open)

Automatically open the app in the browser on server start. When the value is a string, it will be used as the URL's pathname. If you want to open the server in a specific browser you like, you can set the env `process.env.BROWSER` (e.g. `firefox`). You can also set `process.env.BROWSER_ARGS` to pass additional arguments (e.g. `--incognito`).

`BROWSER` and `BROWSER_ARGS` are also special environment variables you can set in the `.env` file to configure it. See [the `open` package](https://github.com/sindresorhus/open#app) for more details.

## preview.proxy [​](#preview-proxy)

*   **Type:** `Record<string, string | ProxyOptions>`
*   **Default:** [`server.proxy`](vite/config/server-options/index.md#server-proxy)

Configure custom proxy rules for the preview server. Expects an object of `{ key: options }` pairs. If the key starts with `^`, it will be interpreted as a `RegExp`. The `configure` option can be used to access the proxy instance.

Uses [`http-proxy-3`](https://github.com/sagemathinc/http-proxy-3). Full options [here](https://github.com/sagemathinc/http-proxy-3#options).

## preview.cors [​](#preview-cors)

*   **Type:** `boolean | CorsOptions`
*   **Default:** [`server.cors`](vite/config/server-options/index.md#server-cors)

Configure CORS for the preview server.

See [`server.cors`](vite/config/server-options/index.md#server-cors) for more details.

## preview.headers [​](#preview-headers)

*   **Type:** `OutgoingHttpHeaders`

Specify server response headers.
