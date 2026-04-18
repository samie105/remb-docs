---
title: "Handling Routing in Functions"
source: "https://supabase.com/docs/guides/functions/routing"
canonical_url: "https://supabase.com/docs/guides/functions/routing"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:23.570Z"
content_hash: "2cd5fe7a11285feaf1e5c48ce5e3d77928406bfea9dbf7026b731c992a96a1c7"
menu_path: ["Edge Functions","Edge Functions","Development","Development","Routing","Routing"]
section_path: ["Edge Functions","Edge Functions","Development","Development","Routing","Routing"]
nav_prev: {"path": "supabase/docs/guides/functions/regional-invocation/index.md", "title": "Regional Invocations"}
nav_next: {"path": "supabase/docs/guides/functions/secrets/index.md", "title": "Environment Variables"}
---

# 

Handling Routing in Functions

## 

Handle custom routing within Edge Functions.

* * *

Usually, an Edge Function is written to perform a single action (e.g. write a record to the database). However, if your app's logic is split into multiple Edge Functions, requests to each action may seem slower.

Each Edge Function needs to be booted before serving a request (known as cold starts). If an action is performed less frequently (e.g. deleting a record), there is a high chance of that function experiencing a cold start.

One way to reduce cold starts and increase performance is to combine multiple actions into a single Edge Function. This way only one instance needs to be booted and it can handle multiple requests to different actions.

This allows you to:

*   Reduce cold starts by combining multiple actions into one function
*   Build complete REST APIs in a single function
*   Improve performance by keeping one instance warm for multiple endpoints

* * *

For example, we can use a single Edge Function to create a typical CRUD API (create, read, update, delete records).

To combine multiple endpoints into a single Edge Function, you can use web application frameworks such as [Express](https://expressjs.com/), [Oak](https://oakserver.github.io/oak/), or [Hono](https://hono.dev).

* * *

## Basic routing example[#](#basic-routing-example)

Here's a simple hello world example using some popular web frameworks:

```
1import { Hono } from 'jsr:@hono/hono'23const app = new Hono()45app.post('/hello-world', async (c) => {6  const { name } = await c.req.json()7  return new Response(`Hello ${name}!`)8})910app.get('/hello-world', (c) => {11  return new Response('Hello World!')12})1314Deno.serve(app.fetch)
```

Within Edge Functions, paths should always be prefixed with the function name (in this case `hello-world`).

* * *

## Using route parameters[#](#using-route-parameters)

You can use route parameters to capture values at specific URL segments (e.g. `/tasks/:taskId/notes/:noteId`).

Keep in mind paths must be prefixed by function name. Route parameters can only be used after the function name prefix.

```
1interface Task {2  id: string3  name: string4}56let tasks: Task[] = []78const router = new Map<string, (req: Request) => Promise<Response>>()910async function getAllTasks(): Promise<Response> {11  return new Response(JSON.stringify(tasks))12}1314async function getTask(id: string): Promise<Response> {15  const task = tasks.find((t) => t.id === id)16  if (task) {17    return new Response(JSON.stringify(task))18  } else {19    return new Response('Task not found', { status: 404 })20  }21}2223async function createTask(req: Request): Promise<Response> {24  const id = Math.random().toString(36).substring(7)25  const task = { id, name: '' }26  tasks.push(task)27  return new Response(JSON.stringify(task), { status: 201 })28}2930async function updateTask(id: string, req: Request): Promise<Response> {31  const index = tasks.findIndex((t) => t.id === id)32  if (index !== -1) {33    tasks[index] = { ...tasks[index] }34    return new Response(JSON.stringify(tasks[index]))35  } else {36    return new Response('Task not found', { status: 404 })37  }38}3940async function deleteTask(id: string): Promise<Response> {41  const index = tasks.findIndex((t) => t.id === id)42  if (index !== -1) {43    tasks.splice(index, 1)44    return new Response('Task deleted successfully')45  } else {46    return new Response('Task not found', { status: 404 })47  }48}4950Deno.serve(async (req) => {51  const url = new URL(req.url)52  const method = req.method53  // Extract the last part of the path as the command54  const command = url.pathname.split('/').pop()55  // Assuming the last part of the path is the task ID56  const id = command57  try {58    switch (method) {59      case 'GET':60        if (id) {61          return getTask(id)62        } else {63          return getAllTasks()64        }65      case 'POST':66        return createTask(req)67      case 'PUT':68        if (id) {69          return updateTask(id, req)70        } else {71          return new Response('Bad Request', { status: 400 })72        }73      case 'DELETE':74        if (id) {75          return deleteTask(id)76        } else {77          return new Response('Bad Request', { status: 400 })78        }79      default:80        return new Response('Method Not Allowed', { status: 405 })81    }82  } catch (error) {83    return new Response(`Internal Server Error: ${error}`, { status: 500 })84  }85})
```

* * *

## URL Patterns API[#](#url-patterns-api)

If you prefer not to use a web framework, you can directly use [URL Pattern API](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API) within your Edge Functions to implement routing.

This works well for small apps with only a couple of routes:

```
1// ...23    )45    // For more details on URLPattern, check https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API6    const taskPattern = new URLPattern({ pathname: '/restful-tasks/:id' })7    const matchingPath = taskPattern.exec(url)8    const id = matchingPath ? matchingPath.pathname.groups.id : null910    let task = null11    if (method === 'POST' || method === 'PUT') {12      const body = await req.json()13      task = body.task14    }1516    // call relevant method based on method and id17    switch (true) {18      case id && method === 'GET':19        return getTask(supabaseClient, id as string)20      case id && method === 'PUT':21        return updateTask(supabaseClient, id as string, task)22      case id && method === 'DELETE':23        return deleteTask(supabaseClient, id as string)24      case method === 'POST':25        return createTask(supabaseClient, task)26      case method === 'GET':27        return getAllTasks(supabaseClient)2829    // ...
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/restful-tasks/index.ts)
