---
title: "Integrating with Supabase Storage"
source: "https://supabase.com/docs/guides/functions/storage-caching"
canonical_url: "https://supabase.com/docs/guides/functions/storage-caching"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:39.380Z"
content_hash: "673331fc6aac3b1da4fdd53babcb3d191f57c3f0e1a97741ff9db298982bb16c"
menu_path: ["Edge Functions","Edge Functions","Integrations","Integrations","Supabase Storage","Supabase Storage"]
section_path: ["Edge Functions","Edge Functions","Integrations","Integrations","Supabase Storage","Supabase Storage"]
nav_prev: {"path": "supabase/docs/guides/functions/status-codes/index.md", "title": "Status codes"}
nav_next: {"path": "supabase/docs/guides/functions/unit-test/index.md", "title": "Testing your Edge Functions"}
---

# 

Integrating with Supabase Storage

* * *

Edge Functions work seamlessly with [Supabase Storage](/docs/guides/storage). This allows you to:

*   Upload generated content directly from your functions
*   Implement cache-first patterns for better performance
*   Serve files with built-in CDN capabilities

* * *

## Basic file operations[#](#basic-file-operations)

Use the Supabase client to upload files directly from your Edge Functions. You'll need the service role key for server-side storage operations:

```
1import { createClient } from 'npm:@supabase/supabase-js@2'23Deno.serve(async (req) => {4  const supabaseAdmin = createClient(5    Deno.env.get('SUPABASE_URL') ?? '',6    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''7  )89  // Generate your content10  const fileContent = await generateImage()1112  // Upload to storage13  const { data, error } = await supabaseAdmin.storage14    .from('images')15    .upload(`generated/${filename}.png`, fileContent.body!, {16      contentType: 'image/png',17      cacheControl: '3600',18      upsert: false,19    })2021  if (error) {22    throw error23  }2425  return new Response(JSON.stringify({ path: data.path }))26})
```

Always use the `SUPABASE_SERVICE_ROLE_KEY` for server-side operations. Never expose this key in client-side code!

* * *

## Cache-first pattern[#](#cache-first-pattern)

Check storage before generating new content to improve performance:

```
1const STORAGE_URL = 'https://your-project.supabase.co/storage/v1/object/public/images'23Deno.serve(async (req) => {4  const url = new URL(req.url)5  const username = url.searchParams.get('username')67  try {8    // Try to get existing file from storage first9    const storageResponse = await fetch(`${STORAGE_URL}/avatars/${username}.png`)1011    if (storageResponse.ok) {12      // File exists in storage, return it directly13      return storageResponse14    }1516    // File doesn't exist, generate it17    const generatedImage = await generateAvatar(username)1819    // Upload to storage for future requests20    const { error } = await supabaseAdmin.storage21      .from('images')22      .upload(`avatars/${username}.png`, generatedImage.body!, {23        contentType: 'image/png',24        cacheControl: '86400', // Cache for 24 hours25      })2627    if (error) {28      console.error('Upload failed:', error)29    }3031    return generatedImage32  } catch (error) {33    return new Response('Error processing request', { status: 500 })34  }35})
```


