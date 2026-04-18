---
title: "Rate Limiting Edge Functions"
source: "https://supabase.com/docs/guides/functions/examples/rate-limiting"
canonical_url: "https://supabase.com/docs/guides/functions/examples/rate-limiting"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:40.133Z"
content_hash: "97b31857073e075aa53542e18e9297e1122e861cc4846d6cb46cf3da1836fb83"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Rate-limiting with Redis","Rate-limiting with Redis"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Rate-limiting with Redis","Rate-limiting with Redis"]
---
# 

Rate Limiting Edge Functions

* * *

[Redis](https://redis.io/about/) is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. It is optimized for atomic operations like incrementing a value, for example for a view counter or rate limiting. We can even rate limit based on the user ID from Supabase Auth!

[Upstash](https://upstash.com/) provides an HTTP/REST based Redis client which is ideal for serverless use-cases and therefore works well with Supabase Edge Functions.

Find the code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/upstash-redis-ratelimit).
