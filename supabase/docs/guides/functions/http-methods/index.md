---
title: "Routing"
source: "https://supabase.com/docs/guides/functions/http-methods"
canonical_url: "https://supabase.com/docs/guides/functions/http-methods"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:42.624Z"
content_hash: "74dfcba7d5a1597d77789d2078458f32f35b807024d4c2fcb6f0c47c7a0d5625"
menu_path: ["Routing"]
section_path: []
nav_prev: {"path": "supabase/docs/guides/functions/function-configuration/index.md", "title": "Function Configuration"}
nav_next: {"path": "supabase/docs/guides/functions/limits/index.md", "title": "Limits"}
---

# 

Routing

## 

Handle different request types in a single function to create efficient APIs.

* * *

## Overview[#](#overview)

Edge Functions support **`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`**. This means you can build complete REST APIs in a single function:

```
1Deno.serve(async (req) => {2  const { method, url } = req3  const { pathname } = new URL(url)45  // Route based on method and path6  if (method === 'GET' && pathname === '/users') {7    return getAllUsers()8  } else if (method === 'POST' && pathname === '/users') {9    return createUser(req)10  }1112  return new Response('Not found', { status: 404 })13})
```

Edge Functions allow you to build APIs without needing separate functions for each endpoint. This reduces cold starts and simplifies deployment while keeping your code organized.

HTML content is not supported. `GET` requests that return `text/html` will be rewritten to `text/plain`. Edge Functions are designed for APIs and data processing, not serving web pages. Use Supabase for your backend API and your favorite frontend framework for HTML.

* * *

## Example[#](#example)

Here's a full example of a RESTful API built with Edge Functions.

```
1// Follow this setup guide to integrate the Deno language server with your editor:2// https://deno.land/manual/getting_started/setup_your_environment3// This enables autocomplete, go to definition, etc.45import { createClient, SupabaseClient } from 'npm:supabase-js@2'6// New approach (v2.95.0+)7import { corsHeaders } from 'jsr:@supabase/supabase-js@2/cors'8// For older versions, use hardcoded headers:9// const corsHeaders = {10//   'Access-Control-Allow-Origin': '*',11//   'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',12//   'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT, DELETE',13// }1415interface Task {16  name: string17  status: number18}1920async function getTask(supabaseClient: SupabaseClient, id: string) {21  const { data: task, error } = await supabaseClient.from('tasks').select('*').eq('id', id)22  if (error) throw error2324  return new Response(JSON.stringify({ task }), {25    headers: { ...corsHeaders, 'Content-Type': 'application/json' },26    status: 200,27  })28}2930async function getAllTasks(supabaseClient: SupabaseClient) {31  const { data: tasks, error } = await supabaseClient.from('tasks').select('*')32  if (error) throw error3334  return new Response(JSON.stringify({ tasks }), {35    headers: { ...corsHeaders, 'Content-Type': 'application/json' },36    status: 200,37  })38}3940async function deleteTask(supabaseClient: SupabaseClient, id: string) {41  const { error } = await supabaseClient.from('tasks').delete().eq('id', id)42  if (error) throw error4344  return new Response(JSON.stringify({}), {45    headers: { ...corsHeaders, 'Content-Type': 'application/json' },46    status: 200,47  })48}4950async function updateTask(supabaseClient: SupabaseClient, id: string, task: Task) {51  const { error } = await supabaseClient.from('tasks').update(task).eq('id', id)52  if (error) throw error5354  return new Response(JSON.stringify({ task }), {55    headers: { ...corsHeaders, 'Content-Type': 'application/json' },56    status: 200,57  })58}5960async function createTask(supabaseClient: SupabaseClient, task: Task) {61  const { error } = await supabaseClient.from('tasks').insert(task)62  if (error) throw error6364  return new Response(JSON.stringify({ task }), {65    headers: { ...corsHeaders, 'Content-Type': 'application/json' },66    status: 200,67  })68}6970Deno.serve(async (req) => {71  const { url, method } = req7273  // This is needed if you're planning to invoke your function from a browser.74  if (method === 'OPTIONS') {75    return new Response('ok', { headers: corsHeaders })76  }7778  try {79    // Create a Supabase client with the Auth context of the logged in user.80    const supabaseClient = createClient(81      // Supabase API URL - env var exported by default.82      Deno.env.get('SUPABASE_URL') ?? '',83      // Supabase API ANON KEY - env var exported by default.84      Deno.env.get('SUPABASE_ANON_KEY') ?? '',85      // Create client with Auth context of the user that called the function.86      // This way your row-level-security (RLS) policies are applied.87      {88        global: {89          headers: { Authorization: req.headers.get('Authorization')! },90        },91      }92    )9394    // For more details on URLPattern, check https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API95    const taskPattern = new URLPattern({ pathname: '/restful-tasks/:id' })96    const matchingPath = taskPattern.exec(url)97    const id = matchingPath ? matchingPath.pathname.groups.id : null9899    let task = null100    if (method === 'POST' || method === 'PUT') {101      const body = await req.json()102      task = body.task103    }104105    // call relevant method based on method and id106    switch (true) {107      case id && method === 'GET':108        return getTask(supabaseClient, id as string)109      case id && method === 'PUT':110        return updateTask(supabaseClient, id as string, task)111      case id && method === 'DELETE':112        return deleteTask(supabaseClient, id as string)113      case method === 'POST':114        return createTask(supabaseClient, task)115      case method === 'GET':116        return getAllTasks(supabaseClient)117      default:118        return getAllTasks(supabaseClient)119    }120  } catch (error) {121    console.error(error)122123    return new Response(JSON.stringify({ error: error.message }), {124      headers: { ...corsHeaders, 'Content-Type': 'application/json' },125      status: 400,126    })127  }128})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/restful-tasks/index.ts)

