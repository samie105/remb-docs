---
title: "Build a simple WebSocket server"
source: "https://bun.com/docs/guides/websocket/simple"
canonical_url: "https://bun.com/docs/guides/websocket/simple"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:33.247Z"
content_hash: "ecdce6c3289c2a4827b76d279d6f6224d884454462a03384a8ad577cde1884b2"
menu_path: ["Build a simple WebSocket server"]
section_path: []
---
Start a simple WebSocket server using [`Bun.serve`](https://bun.com/docs/runtime/http/server). Inside `fetch`, we attempt to upgrade incoming `ws:` or `wss:` requests to WebSocket connections.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const server = Bun.serve({
  fetch(req, server) {
    const success = server.upgrade(req);
    if (success) {
      // Bun automatically returns a 101 Switching Protocols
      // if the upgrade succeeds
      return undefined;
    }

    // handle HTTP request normally
    return new Response("Hello world!");
  },
  websocket: {
    // TypeScript: specify the type of ws.data like this
    data: {} as { authToken: string },

    // this is called when a message is received
    async message(ws, message) {
      console.log(`Received ${message}`);
      // send back a message
      ws.send(`You said: ${message}`);
    },
  },
});

console.log(`Listening on ${server.hostname}:${server.port}`);
```

Was this page helpful?
