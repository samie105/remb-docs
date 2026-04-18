---
title: "Bun Redis with Upstash"
source: "https://bun.com/docs/guides/ecosystem/upstash"
canonical_url: "https://bun.com/docs/guides/ecosystem/upstash"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:57.544Z"
content_hash: "78fa8d5fd4c7877c8f726f3deae271f8483cd3b70017a1721c037bf3c9ce9452"
menu_path: ["Bun Redis with Upstash"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/systemd/index.md", "title": "Run Bun as a daemon with systemd"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/vite/index.md", "title": "Build a frontend using Vite and Bun"}
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

[Upstash](https://upstash.com/) is a fully managed Redis database as a service. Upstash works with the Redis® API, which means you can use Bun’s native Redis client to connect to your Upstash database.

TLS is enabled by default for all Upstash Redis databases.

* * *

1

[

](#)

Create a new project

Create a new project by running `bun init`:

terminal

```
bun init bun-upstash-redis
cd bun-upstash-redis
```

2

[

](#)

Create an Upstash Redis database

Go to the [Upstash dashboard](https://console.upstash.com/) and create a new Redis database. After completing the [getting started guide](https://upstash.com/docs/redis/overall/getstarted), you’ll see your database page with connection information.The database page displays two connection methods; HTTP and TLS. For Bun’s Redis client, you need the **TLS** connection details. This URL starts with `rediss://`.

![Upstash Redis database page](https://mintcdn.com/bun-1dd33a4e/ONaGWxnTD93zNXCt/images/guides/upstash-1.png?fit=max&auto=format&n=ONaGWxnTD93zNXCt&q=85&s=bf927cfe3f0c675c100ae9a2af1d687c)

3

[

](#)

Connect using Bun's Redis client

You can connect to Upstash by setting environment variables with Bun’s default `redis` client.Set the `REDIS_URL` environment variable in your `.env` file using the Redis endpoint (not the REST URL):

.env

```
REDIS_URL=rediss://********@********.upstash.io:6379
```

Bun’s Redis client reads connection information from `REDIS_URL` by default:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import { redis } from "bun";

// Reads from process.env.REDIS_URL automatically
await redis.set("counter", "0"); 
```

Alternatively, you can create a custom client using `RedisClient`:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import { RedisClient } from "bun";

const redis = new RedisClient(process.env.REDIS_URL); 
```

4

[

](#)

Use the Redis client

You can now use the Redis client to interact with your Upstash Redis database:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import { redis } from "bun";

// Get a value
let counter = await redis.get("counter");

// Set a value if it doesn't exist
if (!counter) {
	await redis.set("counter", "0");
}

// Increment the counter
await redis.incr("counter");

// Get the updated value
counter = await redis.get("counter");
console.log(counter);
```

```
1
```

The Redis client automatically handles connections in the background. No need to manually connect or disconnect for basic operations.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/upstash.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/upstash>)

[

Build a frontend using Vite and Bun

Previous

](/docs/guides/ecosystem/vite)[

Common HTTP server usage

Next

](/docs/guides/http/server)

![Upstash Redis database page](https://mintcdn.com/bun-1dd33a4e/ONaGWxnTD93zNXCt/images/guides/upstash-1.png?w=840&fit=max&auto=format&n=ONaGWxnTD93zNXCt&q=85&s=e4b82c4ea36c2c04effd217639cd81f7)

