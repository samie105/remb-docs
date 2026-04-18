---
title: "Integrating With Supabase Auth"
source: "https://supabase.com/docs/guides/functions/auth-legacy-jwt"
canonical_url: "https://supabase.com/docs/guides/functions/auth-legacy-jwt"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:37.444Z"
content_hash: "a475af2f17207ed0405a84dcd1106f86b7b6e5a8d2d562f381543571c3b4c038"
menu_path: ["Edge Functions","Edge Functions","More","More","More","Supabase Auth","Supabase Auth","Legacy JWT secret","Legacy JWT secret"]
section_path: ["Edge Functions","Edge Functions","More","More","More","Supabase Auth","Supabase Auth","Legacy JWT secret","Legacy JWT secret"]
nav_prev: {"path": "supabase/docs/guides/functions/architecture/index.md", "title": "Edge Functions Architecture"}
nav_next: {"path": "supabase/docs/guides/functions/ai-models/index.md", "title": "Running AI Models"}
---

# 

Integrating With Supabase Auth

## 

Integrate Supabase Auth with Edge Functions

* * *

Edge Functions work with [Supabase Auth](/docs/guides/auth).

This allows you to:

*   Automatically identify users through Legacy JWT tokens
*   Enforce Row Level Security policies
*   Integrate with your existing auth flow

## Setting up auth context[#](#setting-up-auth-context)

When a user makes a request to an Edge Function, you can use the `Authorization` header to set the Auth context in the Supabase client and enforce Row Level Security policies.

```
1import { createClient } from 'npm:@supabase/supabase-js@2'23Deno.serve(async (req: Request) => {4  const supabaseClient = createClient(5    Deno.env.get('SUPABASE_URL') ?? '',6    Deno.env.get('SUPABASE_ANON_KEY') ?? '',7    // Create client with Auth context of the user that called the function.8    // This way your row-level-security (RLS) policies are applied.9    {10      global: {11        headers: { Authorization: req.headers.get('Authorization')! },12      },13    }14  );1516  //...17})
```

This context setting happens in the `Deno.serve()` callback argument, so that the `Authorization` header is set for each individual request scope.

* * *

## Fetching the user[#](#fetching-the-user)

By getting the JWT from the `Authorization` header, you can provide the token to `getUser()` to fetch the user object to obtain metadata for the logged in user.

```
1Deno.serve(async (req: Request) => {2  // ...3  const authHeader = req.headers.get('Authorization')!4  const token = authHeader.replace('Bearer ', '')5  const { data } = await supabaseClient.auth.getUser(token)6  // ...7})
```

* * *

## Row Level Security[#](#row-level-security)

After initializing a Supabase client with the Auth context, all queries will be executed with the context of the user. For database queries, this means [Row Level Security](/docs/guides/database/postgres/row-level-security) will be enforced.

```
1import { createClient } from 'npm:@supabase/supabase-js@2'23Deno.serve(async (req: Request) => {4  // ...5  // This query respects RLS - users only see rows they have access to6  const { data, error } = await supabaseClient.from('profiles').select('*');78  if (error) {9    return new Response('Database error', { status: 500 })10  }1112  // ...13})
```

* * *

## Example[#](#example)

See the full [example on GitHub](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/select-from-table-with-auth-rls/index.ts).

```
1// Follow this setup guide to integrate the Deno language server with your editor:2// https://deno.land/manual/getting_started/setup_your_environment3// This enables autocomplete, go to definition, etc.45import { createClient } from 'npm:supabase-js@2'6// New approach (v2.95.0+)7import { corsHeaders } from 'jsr:@supabase/supabase-js@2/cors'8// For older versions:9// import { corsHeaders } from '../_shared/cors.ts'1011console.log(`Function "select-from-table-with-auth-rls" up and running!`)1213Deno.serve(async (req: Request) => {14  // This is needed if you're planning to invoke your function from a browser.15  if (req.method === 'OPTIONS') {16    return new Response('ok', { headers: corsHeaders })17  }1819  try {20    // Create a Supabase client with the Auth context of the logged in user.21    const supabaseClient = createClient(22      // Supabase API URL - env var exported by default.23      Deno.env.get('SUPABASE_URL') ?? '',24      // Supabase API ANON KEY - env var exported by default.25      Deno.env.get('SUPABASE_ANON_KEY') ?? '',26      // Create client with Auth context of the user that called the function.27      // This way your row-level-security (RLS) policies are applied.28      {29        global: {30          headers: { Authorization: req.headers.get('Authorization')! },31        },32      }33    )3435    // First get the token from the Authorization header36    const token = req.headers.get('Authorization').replace('Bearer ', '')3738    // Now we can get the session or user object39    const {40      data: { user },41    } = await supabaseClient.auth.getUser(token)4243    // And we can run queries in the context of our authenticated user44    const { data, error } = await supabaseClient.from('users').select('*')45    if (error) throw error4647    return new Response(JSON.stringify({ user, data }), {48      headers: { ...corsHeaders, 'Content-Type': 'application/json' },49      status: 200,50    })51  } catch (error) {52    return new Response(JSON.stringify({ error: error.message }), {53      headers: { ...corsHeaders, 'Content-Type': 'application/json' },54      status: 400,55    })56  }57})5859// To invoke:60// curl -i --location --request POST 'http://localhost:54321/functions/v1/select-from-table-with-auth-rls' \61//   --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24ifQ.625_WdcF3KHqz5amU0x2X5WWHP-OEs_4qj0ssLNHzTs' \62//   --header 'Content-Type: application/json' \63//   --data '{"name":"Functions"}'
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/select-from-table-with-auth-rls/index.ts)

