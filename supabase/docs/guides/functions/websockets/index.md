---
title: "Handling WebSockets"
source: "https://supabase.com/docs/guides/functions/websockets"
canonical_url: "https://supabase.com/docs/guides/functions/websockets"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:51.188Z"
content_hash: "819f51f1365121ad1c2c7c873c739d8385162322118b875652d2436ba54695e5"
menu_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","WebSockets","WebSockets"]
section_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","WebSockets","WebSockets"]
nav_prev: {"path": "supabase/docs/guides/getting-started/ai-prompts/index.md", "title": "AI Prompts"}
nav_next: {"path": "supabase/docs/guides/getting-started/ai-skills/index.md", "title": "Agent Skills"}
---

# 

Handling WebSockets

## 

Handle WebSocket connections in Edge Functions.

* * *

Edge Functions supports hosting WebSocket servers that can facilitate bi-directional communications with browser clients.

This allows you to:

*   Build real-time applications like chat or live updates
*   Create WebSocket relay servers for external APIs
*   Establish both incoming and outgoing WebSocket connections

* * *

## Creating WebSocket servers[#](#creating-websocket-servers)

Here are some basic examples of setting up WebSocket servers using Deno and Node.js APIs.

```
1Deno.serve((req) => {2  const upgrade = req.headers.get('upgrade') || ''34  if (upgrade.toLowerCase() != 'websocket') {5    return new Response("request isn't trying to upgrade to WebSocket.", { status: 400 })6  }78  const { socket, response } = Deno.upgradeWebSocket(req)910  socket.onopen = () => console.log('socket opened')11  socket.onmessage = (e) => {12    console.log('socket message:', e.data)13    socket.send(new Date().toString())14  }1516  socket.onerror = (e) => console.log('socket errored:', e.message)17  socket.onclose = () => console.log('socket closed')1819  return response20})
```

* * *

### Outbound WebSockets[#](#outbound-websockets)

You can also establish an outbound WebSocket connection to another server from an Edge Function.

Combining it with incoming WebSocket servers, it's possible to use Edge Functions as a WebSocket proxy, for example as a [relay server](https://github.com/supabase-community/openai-realtime-console?tab=readme-ov-file#using-supabase-edge-functions-as-a-relay-server) for the [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime/overview).

```
1import { createServer } from "node:http";2import { WebSocketServer } from "npm:ws";3import { RealtimeClient } from "https://raw.githubusercontent.com/openai/openai-realtime-api-beta/refs/heads/main/lib/client.js";45// ...67const OPENAI_API_KEY = Deno.env.get("OPENAI_API_KEY");89const server = createServer();10// Since we manually created the HTTP server,11// turn on the noServer mode.12const wss = new WebSocketServer({ noServer: true });1314wss.on("connection", async (ws) => {15  console.log("socket opened");16  if (!OPENAI_API_KEY) {17    throw new Error("OPENAI_API_KEY is not set");18  }19  // Instantiate new client20  console.log(`Connecting with key "${OPENAI_API_KEY.slice(0, 3)}..."`);21  const client = new RealtimeClient({ apiKey: OPENAI_API_KEY });2223  // Relay: OpenAI Realtime API Event -> Browser Event24  client.realtime.on("server.*", (event) => {25    console.log(`Relaying "${event.type}" to Client`);26    ws.send(JSON.stringify(event));27  });28  client.realtime.on("close", () => ws.close());2930  // Relay: Browser Event -> OpenAI Realtime API Event31  // We need to queue data waiting for the OpenAI connection32  const messageQueue = [];33  const messageHandler = (data) => {34    try {35      const event = JSON.parse(data);36      console.log(`Relaying "${event.type}" to OpenAI`);37      client.realtime.send(event.type, event);38    } catch (e) {39      console.error(e.message);40      console.log(`Error parsing event from client: ${data}`);41    }42  };4344  ws.on("message", (data) => {45    if (!client.isConnected()) {46      messageQueue.push(data);47    } else {48      messageHandler(data);49    }50  });51  ws.on("close", () => client.disconnect());5253  // Connect to OpenAI Realtime API54  try {55    console.log(`Connecting to OpenAI...`);56    await client.connect();57  } catch (e) {58    console.log(`Error connecting to OpenAI: ${e.message}`);59    ws.close();60    return;61  }62  console.log(`Connected to OpenAI successfully!`);63  while (messageQueue.length) {64    messageHandler(messageQueue.shift());65  }66});6768server.on("upgrade", (req, socket, head) => {69  wss.handleUpgrade(req, socket, head, (ws) => {70    wss.emit("connection", ws, req);71  });72});7374server.listen(8080);
```

[View source](https://github.com/supabase-community/openai-realtime-console/blob/0f93657a71670704fbf77c48cf54d6c9eb956698/supabase/functions/relay/index.ts)

* * *

## Authentication[#](#authentication)

WebSocket browser clients don't have the option to send custom headers. Because of this, Edge Functions won't be able to perform the usual authorization header check to verify the JWT.

You can skip the default authorization header checks by explicitly providing `--no-verify-jwt` when serving and deploying functions.

To authenticate the user making WebSocket requests, you can pass the JWT in URL query params or via a custom protocol.

```
1import { createClient } from 'npm:@supabase/supabase-js@2'23const supabase = createClient(4  Deno.env.get('SUPABASE_URL'),5  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')6)78Deno.serve((req) => {9  const upgrade = req.headers.get('upgrade') || ''10  if (upgrade.toLowerCase() != 'WebSocket') {11    return new Response("request isn't trying to upgrade to WebSocket.", { status: 400 })12  }1314  // Please be aware query params may be logged in some logging systems.15  const url = new URL(req.url)16  const jwt = url.searchParams.get('jwt')1718  if (!jwt) {19    console.error('Auth token not provided')20    return new Response('Auth token not provided', { status: 403 })21  }2223  const { error, data } = await supabase.auth.getClaims()2425  if (error) {26    console.error(error)27    return new Response('Invalid token provided', { status: 403 })28  }2930  if (!data.user) {31    console.error('user is not authenticated')32    return new Response('User is not authenticated', { status: 403 })33  }3435  const { socket, response } = Deno.upgradeWebSocket(req)3637  socket.onopen = () => console.log('socket opened')38  socket.onmessage = (e) => {39    console.log('socket message:', e.data)40    socket.send(new Date().toString())41  }4243  socket.onerror = (e) => console.log('socket errored:', e.message)44  socket.onclose = () => console.log('socket closed')4546  return response47})
```

The maximum duration is capped based on the wall-clock, CPU, and memory limits. The Function will shutdown when it reaches one of these [limits](/docs/guides/functions/limits).

* * *

## Testing WebSockets locally[#](#testing-websockets-locally)

When testing Edge Functions locally with Supabase CLI, the instances are terminated automatically after a request is completed. This will prevent keeping WebSocket connections open.

To prevent that, you can update the `supabase/config.toml` with the following settings:

```
1[edge_runtime]2policy = "per_worker"
```

When running with `per_worker` policy, Function won't auto-reload on edits. You will need to manually restart it by running `supabase functions serve`.
