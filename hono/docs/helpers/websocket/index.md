---
title: "WebSocket Helper ​"
source: "https://hono.dev/docs/helpers/websocket"
canonical_url: "https://hono.dev/docs/helpers/websocket"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:49.089Z"
content_hash: "c72ec4d6769a08c530b06aabcce1c9bcc6209e92a7e33d933bf5d77f4fb5215f"
menu_path: ["WebSocket Helper ​"]
section_path: []
---
WebSocket Helper is a helper for server-side WebSockets in Hono applications. Currently Cloudflare Workers / Pages, Deno, and Bun adapters are available.

## Import [​](#import)

Cloudflare WorkersDenoBun

ts

```
import { Hono } from 'hono'
import { upgradeWebSocket } from 'hono/cloudflare-workers'
```

ts

```
import { Hono } from 'hono'
import { upgradeWebSocket } from 'hono/deno'
```

ts

```
import { Hono } from 'hono'
import { upgradeWebSocket, websocket } from 'hono/bun'

// ...

export default {
  fetch: app.fetch,
  websocket,
}
```

If you use Node.js, you can use [@hono/node-ws](https://github.com/honojs/middleware/tree/main/packages/node-ws).

## `upgradeWebSocket()` [​](#upgradewebsocket)

`upgradeWebSocket()` returns a handler for handling WebSocket.

ts

```
const app = new Hono()

app.get(
  '/ws',
  upgradeWebSocket((c) => {
    return {
      onMessage(event, ws) {
        console.log(`Message from client: ${event.data}`)
        ws.send('Hello from server!')
      },
      onClose: () => {
        console.log('Connection closed')
      },
    }
  })
)
```

Available events:

*   `onOpen` - Currently, Cloudflare Workers does not support it.
*   `onMessage`
*   `onClose`
*   `onError`

WARNING

If you use middleware that modifies headers (e.g., applying CORS) on a route that uses WebSocket Helper, you may encounter an error saying you can't modify immutable headers. This is because `upgradeWebSocket()` also changes headers internally.

Therefore, please be cautious if you are using WebSocket Helper and middleware at the same time.

## RPC-mode [​](#rpc-mode)

Handlers defined with WebSocket Helper support RPC mode.

ts

```
// server.ts
const wsApp = app.get(
  '/ws',
  upgradeWebSocket((c) => {
    //...
  })
)

export type WebSocketApp = typeof wsApp

// client.ts
const client = hc<WebSocketApp>('http://localhost:8787')
const socket = client.ws.$ws() // A WebSocket object for a client
```

## Examples [​](#examples)

See the examples using WebSocket Helper.

### Server and Client [​](#server-and-client)

ts

```
// server.ts
import { Hono } from 'hono'
import { upgradeWebSocket } from 'hono/cloudflare-workers'

const app = new Hono().get(
  '/ws',
  upgradeWebSocket(() => {
    return {
      onMessage: (event) => {
        console.log(event.data)
      },
    }
  })
)

export default app
```

ts

```
// client.ts
import { hc } from 'hono/client'
import type app from './server'

const client = hc<typeof app>('http://localhost:8787')
const ws = client.ws.$ws(0)

ws.addEventListener('open', () => {
  setInterval(() => {
    ws.send(new Date().toString())
  }, 1000)
})
```

### Bun with JSX [​](#bun-with-jsx)

tsx

```
import { Hono } from 'hono'
import { upgradeWebSocket, websocket } from 'hono/bun'
import { html } from 'hono/html'

const app = new Hono()

app.get('/', (c) => {
  return c.html(
    <html>
      <head>
        <meta charset='UTF-8' />
      </head>
      <body>
        <div id='now-time'></div>
        {html`
          <script>
            const ws = new WebSocket('ws://localhost:3000/ws')
            const $nowTime = document.getElementById('now-time')
            ws.onmessage = (event) => {
              $nowTime.textContent = event.data
            }
          </script>
        `}
      </body>
    </html>
  )
})

const ws = app.get(
  '/ws',
  upgradeWebSocket((c) => {
    let intervalId
    return {
      onOpen(_event, ws) {
        intervalId = setInterval(() => {
          ws.send(new Date().toString())
        }, 200)
      },
      onClose() {
        clearInterval(intervalId)
      },
    }
  })
)

export default {
  fetch: app.fetch,
  websocket,
}
```
