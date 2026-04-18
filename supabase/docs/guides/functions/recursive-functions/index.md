---
title: "Recursive / Nested Function Calls"
source: "https://supabase.com/docs/guides/functions/recursive-functions"
canonical_url: "https://supabase.com/docs/guides/functions/recursive-functions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:15.015Z"
content_hash: "31d7a2cda8cb2a67c8ad4aa9d69acf928a080aa2f0af282fca1c6457c655e911"
menu_path: ["Edge Functions","Edge Functions","Platform","Platform","Recursive/Nested function calls","Recursive/Nested function calls"]
section_path: ["Edge Functions","Edge Functions","Platform","Platform","Recursive/Nested function calls","Recursive/Nested function calls"]
---
# 

Recursive / Nested Function Calls

## 

Understanding rate limits when Edge Functions invoke each other

* * *

Edge Functions can call other Edge Functions using `fetch()`. This enables powerful patterns like function chaining, fan-out/fan-in workflows, and recursive processing. To protect platform stability and prevent runaway amplification, Supabase rate limits these internal function-to-function calls.

## What gets rate limited[#](#what-gets-rate-limited)

Rate limiting applies to **outbound `fetch()` calls** made by your Edge Functions to other Edge Functions within your project. This includes:

*   **Direct recursion**: A function calling itself
*   **Function chaining**: Function A calling Function B
*   **Circular calls**: Function A calling Function B, which calls Function A
*   **Fan-out patterns**: A function calling multiple other functions concurrently

Inbound requests to your Edge Functions and requests to external APIs (e.g., Stripe, OpenAI) are **not** subject to this rate limit. Only outbound calls from one Edge Function to another Edge Function are counted.

## Rate limit budget[#](#rate-limit-budget)

Each request chain has a budget of at least **5,000 requests per minute**. In busier regions, this budget may be higher. All function-to-function calls within the same request chain share this budget.

For example, if Function A calls Function B, and Function B calls Function C, all three calls count toward the same budget pool.

## Handling rate limit errors[#](#handling-rate-limit-errors)

When the rate limit is exceeded, calling another Edge Function throws a `RateLimitError`. This error includes a `retryAfterMs` property indicating how long to wait (in milliseconds) before retrying. You should catch this error and handle it gracefully:

```
1import { createClient } from 'jsr:@supabase/supabase-js@2'23const supabase = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_ANON_KEY')!)45Deno.serve(async (req) => {6  try {7    const { data, error } = await supabase.functions.invoke('other-function', {8      body: { foo: 'bar' },9    })1011    if (error) throw error1213    return new Response(JSON.stringify(data), {14      headers: { 'Content-Type': 'application/json' },15    })16  } catch (err) {17    if (err instanceof Deno.errors.RateLimitError) {18      // Use retryAfterMs to tell the client when to retry19      const retryAfterSeconds = Math.ceil(err.retryAfterMs / 1000)20      return new Response(21        JSON.stringify({ error: 'Service temporarily unavailable. Please retry later.' }),22        {23          status: 429,24          headers: {25            'Content-Type': 'application/json',26            'Retry-After': retryAfterSeconds.toString(),27          },28        }29      )30    }31    throw err32  }33})
```

You can also use `retryAfterMs` to implement automatic retries within your function:

```
1import { createClient } from 'jsr:@supabase/supabase-js@2'23const supabase = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_ANON_KEY')!)45async function invokeWithRetry(functionName: string, payload: object, maxRetries = 3) {6  for (let attempt = 0; attempt < maxRetries; attempt++) {7    try {8      const { data, error } = await supabase.functions.invoke(functionName, {9        body: payload,10      })11      if (error) throw error12      return data13    } catch (err) {14      if (err instanceof Deno.errors.RateLimitError && attempt < maxRetries - 1) {15        // Wait for the recommended duration before retrying16        await new Promise((resolve) => setTimeout(resolve, err.retryAfterMs))17        continue18      }19      throw err20    }21  }22}
```

## Tips for avoiding rate limits[#](#tips-for-avoiding-rate-limits)

### 1\. Batch operations instead of individual calls[#](#1-batch-operations-instead-of-individual-calls)

Instead of calling a function once per item, batch multiple items into a single call:

```
1// ❌ Avoid: One call per item2for (const item of items) {3  await supabase.functions.invoke('process-item', { body: item })4}56// ✅ Better: Batch items into one call7await supabase.functions.invoke('process-items', { body: { items } })
```

### 2\. Limit recursion depth[#](#2-limit-recursion-depth)

If your function is recursive, set a maximum depth to prevent unbounded call chains:

```
1Deno.serve(async (req) => {2  const { depth = 0, data } = await req.json()34  if (depth >= 5) {5    // Stop recursion at max depth6    return new Response(JSON.stringify({ result: data }))7  }89  // Process and recurse with incremented depth10  const processed = processData(data)11  const { data: result } = await supabase.functions.invoke('my-function', {12    body: { depth: depth + 1, data: processed },13  })1415  return new Response(JSON.stringify(result))16})
```

### 3\. Use queues for large workloads[#](#3-use-queues-for-large-workloads)

For processing large datasets, consider using [Supabase Queues](/docs/guides/queues) instead of recursive function calls. Queues handle backpressure automatically and are better suited for high-volume workloads.

### 4\. Use shared libraries instead of separate functions[#](#4-use-shared-libraries-instead-of-separate-functions)

Instead of creating separate Edge Functions that call each other, create a shared library of functions and import them directly. This avoids HTTP overhead and rate limits entirely:

```
1// supabase/functions/_shared/transform.ts2export function validate(data: any) {3  // validation logic4}56export function transform(data: any) {7  // transformation logic8}910export async function save(data: any) {11  // save logic12}
```

```
1// supabase/functions/process-data/index.ts2import { validate, transform, save } from '../_shared/transform.ts'34Deno.serve(async (req) => {5  const data = await req.json()6  const validated = validate(data)7  const transformed = transform(validated)8  const result = await save(transformed)9  return new Response(JSON.stringify(result))10})
```

### 5\. Add delays for non-urgent processing[#](#5-add-delays-for-non-urgent-processing)

If immediate processing isn't required, add delays between calls to spread the load:

```
1async function processWithDelay(items: any[]) {2  for (const item of items) {3    await supabase.functions.invoke('process-item', { body: item })4    await new Promise((resolve) => setTimeout(resolve, 100)) // 100ms delay5  }6}
```

## Common patterns and their impact[#](#common-patterns-and-their-impact)

Pattern

Budget consumption

Recommendation

Simple chain (A to B to C)

Low

Generally safe

Fan-out (A to B, C, D, E)

Moderate

Limit concurrency

Deep recursion (A to A to A...)

High

Set max depth

Unbounded loops

Very high

Avoid, use queues

## Increasing rate limits[#](#increasing-rate-limits)

Currently, all plans have the same rate limit budget. We are working on introducing custom limits for different use cases.

If you need a higher rate limit for your project, [contact support](/dashboard/support/new) with details about your use case.
