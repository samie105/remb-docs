---
title: "Generating OG Images"
source: "https://supabase.com/docs/guides/functions/examples/og-image"
canonical_url: "https://supabase.com/docs/guides/functions/examples/og-image"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:37.461Z"
content_hash: "38bd6ed95e6410cee5e76e03b46be2274ae516776adff9f66af59dea75cb2404"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Generating OG images","Generating OG images"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Generating OG images","Generating OG images"]
---
# 

Generating OG Images

* * *

Generate Open Graph images with Deno and Supabase Edge Functions. [View on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/opengraph).

## Code[#](#code)

Create a `handler.tsx` file to construct the OG image in React:

```
1import React from 'https://esm.sh/react@18.2.0'2import { ImageResponse } from 'https://deno.land/x/og_edge@0.0.4/mod.ts'34export default function handler(req: Request) {5  return new ImageResponse(6    <div7      style={{8        width: '100%',9        height: '100%',10        display: 'flex',11        alignItems: 'center',12        justifyContent: 'center',13        fontSize: 128,14        background: 'lavender',15      }}16    >17      Hello OG Image!18    </div>19  )20}
```

Create an `index.ts` file to execute the handler on incoming requests:

```
1import handler from './handler.tsx'23console.log('Hello from og-image Function!')45Deno.serve(handler)
```
