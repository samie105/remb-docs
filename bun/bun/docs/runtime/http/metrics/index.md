---
title: "Metrics"
source: "https://bun.com/docs/runtime/http/metrics"
canonical_url: "https://bun.com/docs/runtime/http/metrics"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:03.571Z"
content_hash: "943e4d2e92cbc31fc10be5391622e923ca12b34e2cac43f5a902eee7b016e0e9"
menu_path: ["Metrics"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/http/error-handling/index.md", "title": "Error Handling"}
nav_next: {"path": "bun/bun/docs/runtime/http/routing/index.md", "title": "Routing"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

### 

[​

](#server-pendingrequests-and-server-pendingwebsockets)

`server.pendingRequests` and `server.pendingWebSockets`

Monitor server activity with built-in counters:

```
const server = Bun.serve({
  fetch(req, server) {
    return new Response(
      `Active requests: ${server.pendingRequests}\n` + `Active WebSockets: ${server.pendingWebSockets}`,
    );
  },
});
```

### 

[​

](#server-subscribercount-topic)

`server.subscriberCount(topic)`

Get count of subscribers for a WebSocket topic:

```
const server = Bun.serve({
  fetch(req, server) {
    const chatUsers = server.subscriberCount("chat");
    return new Response(`${chatUsers} users in chat`);
  },
  websocket: {
    message(ws) {
      ws.subscribe("chat");
    },
  },
});
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/http/metrics.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/http/metrics>)

[

Error Handling

Previous

](/docs/runtime/http/error-handling)[

Fetch

Next

](/docs/runtime/networking/fetch)
