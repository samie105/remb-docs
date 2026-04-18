---
title: "Limits"
source: "https://supabase.com/docs/guides/functions/limits"
canonical_url: "https://supabase.com/docs/guides/functions/limits"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:46.590Z"
content_hash: "b0620eebc89ae4e39aca1ab491f3c642f2c79ace6626aab11024518e1597a63a"
menu_path: ["Edge Functions","Edge Functions","Platform","Platform","Limits","Limits"]
section_path: ["Edge Functions","Edge Functions","Platform","Platform","Limits","Limits"]
---
# 

Limits

## 

Limits applied Edge Functions in Supabase's hosted platform.

* * *

## Runtime limits[#](#runtime-limits)

*   Maximum Memory: 256MB
*   Maximum Duration (Wall clock limit): This is the duration an Edge Function worker will stay active. During this period, a worker can serve multiple requests or process background tasks.
    *   Free plan: 150s
    *   Paid plans: 400s
*   Maximum CPU Time: 2s (Amount of actual time spent on the CPU per request - does not include async I/O.)
*   Request idle timeout: 150s (If an Edge Function doesn't send a response before the timeout, 504 Gateway Timeout will be returned)

## Platform limits[#](#platform-limits)

*   Maximum Function Size: 20MB (After bundling using CLI)
*   Maximum no. of Functions per project:
    *   Free: 100
    *   Pro: 500
    *   Team: 1000
    *   Enterprise: Unlimited
*   Maximum log message length: 10,000 characters
*   Log event threshold: 100 events per 10 seconds
*   Recursive/Nested Function Calling: ~5000 requests per minute [more details](/docs/guides/functions/recursive-functions)

### Secrets[#](#secrets)

*   Maximum number of secrets per project: **100**
*   Secret name length: up to **256** characters
*   Maximum secret size: **48 KiB** (**24,576** characters)
*   Names must NOT start with the prefix `SUPABASE_` (this prefix is reserved).

## Other limits & restrictions[#](#other-limits--restrictions)

*   Outgoing connections to ports `25` and `587` are not allowed.
*   Serving of HTML content is only supported with [custom domains](/docs/reference/cli/supabase-domains) (Otherwise `GET` requests that return `text/html` will be rewritten to `text/plain`).
*   Web Worker API (or Node `vm` API) are not available.
*   Static files cannot be deployed using the API flag. You need to build them with [Docker on the CLI](/docs/guides/functions/quickstart#step-6-deploy-to-production).
*   Node Libraries that require multithreading are not supported. Examples: [`libvips`](https://github.com/libvips/libvips), [sharp](https://github.com/lovell/sharp).
