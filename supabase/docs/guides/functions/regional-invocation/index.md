---
title: "Regional Invocations"
source: "https://supabase.com/docs/guides/functions/regional-invocation"
canonical_url: "https://supabase.com/docs/guides/functions/regional-invocation"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:15.745Z"
content_hash: "cd87082d72bd7c9a32206d2afd3d2b1efabb68c63ca0c605c32df4a80752a7f6"
menu_path: ["Edge Functions","Edge Functions","Platform","Platform","Regional invocations","Regional invocations"]
section_path: ["Edge Functions","Edge Functions","Platform","Platform","Regional invocations","Regional invocations"]
---
# 

Regional Invocations

## 

Execute Edge Functions in specific regions for optimal performance.

* * *

Edge Functions automatically execute in the region closest to the user making the request. This reduces network latency and provides faster responses.

However, if your function performs intensive database or storage operations, executing in the same region as your database often provides better performance:

*   **Bulk database operations:** Adding or editing many records
*   **File uploads:** Processing large files or multiple uploads
*   **Complex queries:** Operations requiring multiple database round trips

* * *

## Available regions[#](#available-regions)

The following regions are supported:

**Asia Pacific:**

*   `ap-northeast-1` (Tokyo)
*   `ap-northeast-2` (Seoul)
*   `ap-south-1` (Mumbai)
*   `ap-southeast-1` (Singapore)
*   `ap-southeast-2` (Sydney)

**North America:**

*   `ca-central-1` (Canada Central)
*   `us-east-1` (N. Virginia)
*   `us-west-1` (N. California)
*   `us-west-2` (Oregon)

**Europe:**

*   `eu-central-1` (Frankfurt)
*   `eu-west-1` (Ireland)
*   `eu-west-2` (London)
*   `eu-west-3` (Paris)

**South America:**

*   `sa-east-1` (São Paulo)

* * *

## Usage[#](#usage)

You can specify the region programmatically using the Supabase Client library, or using the `x-region` HTTP header.

```
1import { createClient, FunctionRegion } from '@supabase/supabase-js'23const { data, error } = await supabase.functions.invoke('function-name', {4  ...5  region: FunctionRegion.UsEast1, // Execute in us-east-1 region6})
```

In case you cannot add the `x-region` header to the request (e.g.: CORS requests, Webhooks), you can use `forceFunctionRegion` query parameter.

You can verify the execution region by looking at the `x-sb-edge-region` HTTP header in the response. You can also find it as metadata in [Edge Function Logs](/docs/guides/functions/logging).

* * *

## Region runtime information[#](#region-runtime-information)

Functions have access to the following environment variables:

SB\_REGION: The AWS region function was invoked

This is useful if you have read replicate and want to Postgres connect to a different replicate according of the Region.

* * *

## Region outages[#](#region-outages)

When you explicitly specify a region via the `x-region` header, requests will NOT be automatically re-routed to another region.

During outages, consider temporarily changing to a different region.

Test your function's performance with and without regional specification to determine if the benefits outweigh automatic region selection.
