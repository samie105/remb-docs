---
title: "Production usage"
source: "https://redis.io/docs/latest/develop/clients/nodejs/produsage/"
canonical_url: "https://redis.io/docs/latest/develop/clients/nodejs/produsage/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:12:46.326Z"
content_hash: "fb814293bf5f163edf29fe6495e6fbe1932084ac73274b40fa1aca180503f517"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        node-redis guide (JavaScript)","→","node-redis guide (JavaScript)","→\n      \n        Production usage","→","Production usage"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        node-redis guide (JavaScript)","→","node-redis guide (JavaScript)","→\n      \n        Production usage","→","Production usage"]
nav_prev: {"path": "redis/docs/latest/develop/clients/nodejs/prob/index.md", "title": "Probabilistic data types"}
nav_next: {"path": "redis/docs/latest/develop/clients/nodejs/queryjson/index.md", "title": "Index and query documents"}
---

# Production usage

Get your Node.js app ready for production

This guide offers recommendations to get the best reliability and performance in your production environment.

## Checklist

Each item in the checklist below links to the section for a recommendation. Use the checklist icons to record your progress in implementing the recommendations.

## Recommendations

### Handling errors

Node-Redis provides [multiple events to handle various scenarios](https://github.com/redis/node-redis?tab=readme-ov-file#events), among which the most critical is the `error` event.

This event is triggered whenever an error occurs within the client, and it is very important to set a handler to listen for it. See [Error events](../error-handling/index.md#error-events) for more information and an example of setting an error handler.

### Handling reconnections

When the socket closes unexpectedly (without calling the `quit()` or `disconnect()` methods), the client can automatically restore the connection. A simple [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) strategy for reconnection is enabled by default, but you can replace this with your own custom strategy. See [Reconnect after disconnection](../connect/index.md#reconnect-after-disconnection) for more information.

### Timeouts

To set a timeout for a connection, use the `connectTimeout` option (the default timeout is 5 seconds):

```js
const client = createClient({
  socket: {
    // setting a 10-second timeout  
    connectTimeout: 10000 // in milliseconds
  }
});
client.on('error', error => console.error('Redis client error:', error));
```

You can also set timeouts for individual commands using `AbortController`:

```javascript
import { createClient, commandOptions } from 'redis';

const client = createClient({ url: 'redis://localhost:6379' });
await client.connect();

const ac = new AbortController();
const t = setTimeout(() => ac.abort(), 1000);
try {
  const val = await client.get(commandOptions({ signal: ac.signal }), key);
} finally {
  clearTimeout(t);
}
```

### Command execution reliability

By default, `node-redis` reconnects automatically when the connection is lost (but see [Handling reconnections](#handling-reconnections), if you want to customize this behavior). While the connection is down, any commands that you execute will be queued and sent to the server when the connection is restored. This might occasionally cause problems if the connection fails while a [non-idempotent](https://en.wikipedia.org/wiki/Idempotence) command is being executed. In this case, the command could change the data on the server without the client removing it from the queue. When the connection is restored, the command will be sent again, resulting in incorrect data.

If you need to avoid this situation, set the `disableOfflineQueue` option to `true` when you create the client. This will cause the client to discard unexecuted commands rather than queuing them:

```js
const client = createClient({
  disableOfflineQueue: true,
      .
      .
});
```

Use a separate connection with the queue disabled if you want to avoid queuing only for specific commands.

### Smart client handoffs

_Smart client handoffs (SCH)_ is a feature of Redis Cloud and Redis Software servers that lets them actively notify clients about planned server maintenance shortly before it happens. This lets a client take action to avoid disruptions in service.

See [Smart client handoffs](/docs/latest/develop/clients/sch/) for more information about SCH and [Connect using Smart client handoffs](../connect/index.md#connect-using-smart-client-handoffs-sch) for example code.

## On this page
