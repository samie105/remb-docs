---
title: "Upstash Redis"
source: "https://supabase.com/docs/guides/functions/examples/upstash-redis"
canonical_url: "https://supabase.com/docs/guides/functions/examples/upstash-redis"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:58.689Z"
content_hash: "22de4de59e1fdcebc135ad0b7af60ab2815df0024710ad21dd7f6978157b9022"
menu_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Upstash Redis","Upstash Redis"]
section_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Upstash Redis","Upstash Redis"]
nav_prev: {"path": "supabase/docs/guides/functions/examples/telegram-bot/index.md", "title": "Building a Telegram Bot"}
nav_next: {"path": "supabase/docs/guides/functions/function-configuration/index.md", "title": "Function Configuration"}
---

# 

Upstash Redis

* * *

A Redis counter example that stores a [hash](https://redis.io/commands/hincrby/) of function invocation count per region. Find the code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/upstash-redis-counter).

## Redis database setup[#](#redis-database-setup)

Create a Redis database using the [Upstash Console](https://console.upstash.com/) or [Upstash CLI](https://github.com/upstash/cli).

Select the `Global` type to minimize the latency from all edge locations. Copy the `UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN` to your .env file.

You'll find them under **Details > REST API > .env**.

```
1cp supabase/functions/upstash-redis-counter/.env.example supabase/functions/upstash-redis-counter/.env
```

## Code[#](#code)

Make sure you have the latest version of the [Supabase CLI installed](/docs/guides/cli#installation).

Create a new function in your project:

```
1supabase functions new upstash-redis-counter
```

And add the code to the `index.ts` file:

```
1import { Redis } from 'https://deno.land/x/upstash_redis@v1.19.3/mod.ts'23console.log(`Function "upstash-redis-counter" up and running!`)45Deno.serve(async (_req) => {6  try {7    const redis = new Redis({8      url: Deno.env.get('UPSTASH_REDIS_REST_URL')!,9      token: Deno.env.get('UPSTASH_REDIS_REST_TOKEN')!,10    })1112    const deno_region = Deno.env.get('DENO_REGION')13    if (deno_region) {14      // Increment region counter15      await redis.hincrby('supa-edge-counter', deno_region, 1)16    } else {17      // Increment localhost counter18      await redis.hincrby('supa-edge-counter', 'localhost', 1)19    }2021    // Get all values22    const counterHash: Record<string, number> | null = await redis.hgetall('supa-edge-counter')23    const counters = Object.entries(counterHash!)24      .sort(([, a], [, b]) => b - a) // sort desc25      .reduce((r, [k, v]) => ({ total: r.total + v, regions: { ...r.regions, [k]: v } }), {26        total: 0,27        regions: {},28      })2930    return new Response(JSON.stringify({ counters }), { status: 200 })31  } catch (error) {32    return new Response(JSON.stringify({ error: error.message }), { status: 200 })33  }34})
```

## Run locally[#](#run-locally)

```
1supabase start2supabase functions serve --no-verify-jwt --env-file supabase/functions/upstash-redis-counter/.env
```

Navigate to [http://localhost:54321/functions/v1/upstash-redis-counter](http://localhost:54321/functions/v1/upstash-redis-counter).

## Deploy[#](#deploy)

```
1supabase functions deploy upstash-redis-counter --no-verify-jwt2supabase secrets set --env-file supabase/functions/upstash-redis-counter/.env
```
