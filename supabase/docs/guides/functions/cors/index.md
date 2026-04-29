---
title: "CORS (Cross-Origin Resource Sharing) support for Invoking from the browser"
source: "https://supabase.com/docs/guides/functions/cors"
canonical_url: "https://supabase.com/docs/guides/functions/cors"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:01.909Z"
content_hash: "79e30ce0038e006a260cf9cbf50247ee489efc2d208c6f2fdb7deb4f93b47f76"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","CORS support for invoking from the browser","CORS support for invoking from the browser"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","CORS support for invoking from the browser","CORS support for invoking from the browser"]
nav_prev: {"path": "../connect-to-postgres/index.md", "title": "Integrating with Supabase Database (Postgres)"}
nav_next: {"path": "../dart-edge/index.md", "title": "Dart Edge"}
---

# 

CORS (Cross-Origin Resource Sharing) support for Invoking from the browser

* * *

To invoke edge functions from the browser, you need to handle [CORS Preflight](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request) requests.

See the [example on GitHub](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/browser-with-cors/index.ts).

### Recommended setup[#](#recommended-setup)

**For `@supabase/supabase-js` v2.95.0 and later:** Import CORS headers directly from the SDK to ensure they stay synchronized with any new headers added to the client libraries.

Import `corsHeaders` from `@supabase/supabase-js/cors` to automatically get all required headers:

```
1import { corsHeaders } from '@supabase/supabase-js/cors'23console.log(`Function "browser-with-cors" up and running!`)45Deno.serve(async (req) => {6  // This is needed if you're planning to invoke your function from a browser.7  if (req.method === 'OPTIONS') {8    return new Response('ok', { headers: corsHeaders })9  }1011  try {12    const { name } = await req.json()13    const data = {14      message: `Hello ${name}!`,15    }1617    return new Response(JSON.stringify(data), {18      headers: { ...corsHeaders, 'Content-Type': 'application/json' },19      status: 200,20    })21  } catch (error) {22    return new Response(JSON.stringify({ error: error.message }), {23      headers: { ...corsHeaders, 'Content-Type': 'application/json' },24      status: 400,25    })26  }27})
```

This approach ensures that when new headers are added to the Supabase SDK, your Edge Functions automatically include them, preventing CORS errors.

#### For versions before 2.95.0[#](#for-versions-before-2950)

If you're using `@supabase/supabase-js` before v2.95.0, you'll need to hardcode the CORS headers. Add a `cors.ts` file within a [`_shared` folder](/docs/guides/functions/quickstart#organizing-your-edge-functions):

```
1export const corsHeaders = {2  'Access-Control-Allow-Origin': '*',3  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',4}
```

Then import it in your function:

```
1import { corsHeaders } from '../_shared/cors.ts'23// ... rest of your function code
```
