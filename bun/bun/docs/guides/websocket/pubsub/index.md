---
title: "Build a publish-subscribe WebSocket server"
source: "https://bun.com/docs/guides/websocket/pubsub"
canonical_url: "https://bun.com/docs/guides/websocket/pubsub"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:29.625Z"
content_hash: "a76e2f3926c929f58f5681a76b4df3be3ded3e5ebfd1e03dafc03c6b5b645ed7"
menu_path: ["Build a publish-subscribe WebSocket server"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/websocket/compression/index.md", "title": "Enable compression for WebSocket messages"}
nav_next: {"path": "bun/bun/docs/guides/websocket/context/index.md", "title": "Set per-socket contextual data on a WebSocket"}
---

Bun’s server-side `WebSocket` API provides a native pub-sub API. Sockets can be subscribed to a set of named channels using `socket.subscribe(<name>)`; messages can be published to a channel using `socket.publish(<name>, <message>)`. This code snippet implements a single-channel chat server.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const server = Bun.serve({
  fetch(req, server) {
    const cookies = req.headers.get("cookie");
    const username = getUsernameFromCookies(cookies);
    const success = server.upgrade(req, { data: { username } });
    if (success) return undefined;

    return new Response("Hello world");
  },
  websocket: {
    // TypeScript: specify the type of ws.data like this
    data: {} as { username: string },

    open(ws) {
      const msg = `${ws.data.username} has entered the chat`;
      ws.subscribe("the-group-chat");
      server.publish("the-group-chat", msg);
    },
    message(ws, message) {
      // the server re-broadcasts incoming messages to everyone
      server.publish("the-group-chat", `${ws.data.username}: ${message}`);
    },
    close(ws) {
      const msg = `${ws.data.username} has left the chat`;
      server.publish("the-group-chat", msg);
      ws.unsubscribe("the-group-chat");
    },
  },
});

console.log(`Listening on ${server.hostname}:${server.port}`);
```

Was this page helpful?


