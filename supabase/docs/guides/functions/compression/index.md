---
title: "Handling Compressed Requests"
source: "https://supabase.com/docs/guides/functions/compression"
canonical_url: "https://supabase.com/docs/guides/functions/compression"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:53.662Z"
content_hash: "923a6e536f7346669f9b127095573aa508cc96cd89b4850a0562a6166ad79180"
menu_path: ["Handling Compressed Requests"]
section_path: []
nav_prev: {"path": "supabase/docs/guides/functions/background-tasks/index.md", "title": "Background Tasks"}
nav_next: {"path": "supabase/docs/guides/functions/connect-to-postgres/index.md", "title": "Integrating with Supabase Database (Postgres)"}
---

# 

Handling Compressed Requests

## 

Handling Gzip compressed requests.

* * *

To decompress Gzip bodies, you can use `gunzipSync` from the `node:zlib` API to decompress and then read the body.

```
1import { gunzipSync } from 'node:zlib'23Deno.serve(async (req) => {4  try {5    // Check if the request body is gzip compressed6    const contentEncoding = req.headers.get('content-encoding')7    if (contentEncoding !== 'gzip') {8      return new Response('Request body is not gzip compressed', {9        status: 400,10      })11    }1213    // Read the compressed body14    const compressedBody = await req.arrayBuffer()1516    // Decompress the body17    const decompressedBody = gunzipSync(new Uint8Array(compressedBody))1819    // Convert the decompressed body to a string20    const decompressedString = new TextDecoder().decode(decompressedBody)21    const data = JSON.parse(decompressedString)2223    // Process the decompressed body as needed24    console.log(`Received: ${JSON.stringify(data)}`)2526    return new Response('ok', {27      headers: { 'Content-Type': 'text/plain' },28    })29  } catch (error) {30    console.error('Error:', error)31    return new Response('Error processing request', { status: 500 })32  }33})
```

Edge functions have a runtime memory limit of 150MB. Overly large compressed payloads may result in an out-of-memory error.


