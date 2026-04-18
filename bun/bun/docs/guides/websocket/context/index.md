---
title: "Set per-socket contextual data on a WebSocket"
source: "https://bun.com/docs/guides/websocket/context"
canonical_url: "https://bun.com/docs/guides/websocket/context"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:31.040Z"
content_hash: "ee9273cba2457d78bc2dcd8b93d2ff7e44bd02c8441abed64f297d39d413282f"
menu_path: ["Set per-socket contextual data on a WebSocket"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/websocket/compression/index.md", "title": "Enable compression for WebSocket messages"}
nav_next: {"path": "bun/bun/docs/guides/websocket/pubsub/index.md", "title": "Build a publish-subscribe WebSocket server"}
---

When building a WebSocket server, it’s typically necessary to store some identifying information or context associated with each connected client. With [Bun.serve()](bun/bun/docs/runtime/http/websockets/index.md#contextual-data), this “contextual data” is set when the connection is initially upgraded by passing a `data` parameter in the `server.upgrade()` call.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
Bun.serve({
  fetch(req, server) {
    const success = server.upgrade(req, {
      data: {
        socketId: Math.random(),
      },
    });
    if (success) return undefined;

    // handle HTTP request normally
    // ...
  },
  websocket: {
    // TypeScript: specify the type of ws.data like this
    data: {} as { socketId: number },

    // define websocket handlers
    async message(ws, message) {
      // the contextual data is available as the `data` property
      // on the WebSocket instance
      console.log(`Received ${message} from ${ws.data.socketId}}`);
    },
  },
});
```

* * *

It’s common to read cookies/headers from the incoming request to identify the connecting client.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
type WebSocketData = {
  createdAt: number;
  token: string;
  userId: string;
};

Bun.serve({
  async fetch(req, server) {
    // use a library to parse cookies
    const cookies = parseCookies(req.headers.get("Cookie"));
    const token = cookies["X-Token"];
    const user = await getUserFromToken(token);

    const upgraded = server.upgrade(req, {
      data: {
        createdAt: Date.now(),
        token: cookies["X-Token"],
        userId: user.id,
      },
    });

    if (upgraded) return undefined;
  },
  websocket: {
    // TypeScript: specify the type of ws.data like this
    data: {} as WebSocketData,

    async message(ws, message) {
      // save the message to a database
      await saveMessageToDatabase({
        message: String(message),
        userId: ws.data.userId,
      });
    },
  },
});
```

Was this page helpful?
