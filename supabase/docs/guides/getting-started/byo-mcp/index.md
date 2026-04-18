---
title: "Deploy MCP servers"
source: "https://supabase.com/docs/guides/getting-started/byo-mcp"
canonical_url: "https://supabase.com/docs/guides/getting-started/byo-mcp"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:06.071Z"
content_hash: "1eb6716b4e7ad9b54b579c62ff713569f3a23be5ea5ab173b0b8a8d4a581b31a"
menu_path: ["Start with Supabase","Start with Supabase","AI Tools","AI Tools","Deploy MCP servers","Deploy MCP servers"]
section_path: ["Start with Supabase","Start with Supabase","AI Tools","AI Tools","Deploy MCP servers","Deploy MCP servers"]
nav_prev: {"path": "supabase/docs/guides/getting-started/architecture/index.md", "title": "Architecture"}
nav_next: {"path": "supabase/docs/guides/getting-started/features/index.md", "title": "Features"}
---

# 

Deploy MCP servers

* * *

Build and deploy [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25) (MCP) servers on Supabase using [Edge Functions](/docs/guides/functions).

This guide covers MCP servers that do not require authentication. Auth support for MCP on Edge Functions is coming soon.

## Prerequisites[#](#prerequisites)

Before you begin, make sure you have:

*   [Docker](https://docs.docker.com/get-docker/) or a compatible runtime installed and running (required for local development)
*   [Deno](https://deno.land/) installed (Supabase Edge Functions runtime)
*   [Supabase CLI](/docs/guides/local-development) installed and authenticated
*   [Node.js 20 or later](https://nodejs.org/) (required by Supabase CLI)

## Deploy your MCP server[#](#deploy-your-mcp-server)

### Step 1: Create a new project[#](#step-1-create-a-new-project)

Start by creating a new Supabase project:

```
1mkdir my-mcp-server2cd my-mcp-server3supabase init
```

After this step, you should have a project directory with a `supabase` folder containing `config.toml` and an empty `functions` directory.

* * *

### Step 2: Create the MCP server function[#](#step-2-create-the-mcp-server-function)

Create a new Edge Function for your MCP server:

```
1supabase functions new mcp
```

This tutorial uses the [official MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) with the `WebStandardStreamableHTTPServerTransport`, but you can use any MCP framework that's compatible with the [Edge Runtime](/docs/guides/functions), such as [mcp-lite](https://github.com/fiberplane/mcp-lite) or [mcp-handler](https://github.com/vercel/mcp-handler).

Replace the contents of `supabase/functions/mcp/index.ts` with:

###### supabase/functions/mcp/index.ts

```
1// Setup type definitions for built-in Supabase Runtime APIs2import 'jsr:@supabase/functions-js/edge-runtime.d.ts'34import { McpServer } from 'npm:@modelcontextprotocol/sdk@1.25.3/server/mcp.js'5import { WebStandardStreamableHTTPServerTransport } from 'npm:@modelcontextprotocol/sdk@1.25.3/server/webStandardStreamableHttp.js'6import { Hono } from 'npm:hono@^4.9.7'7import { z } from 'npm:zod@^4.1.13'89// Create Hono app10const app = new Hono()1112// Create your MCP server13const server = new McpServer({14  name: 'mcp',15  version: '0.1.0',16})1718// Register a simple addition tool19server.registerTool(20  'add',21  {22    title: 'Addition Tool',23    description: 'Add two numbers together',24    inputSchema: { a: z.number(), b: z.number() },25  },26  ({ a, b }) => ({27    content: [{ type: 'text', text: String(a + b) }],28  })29)3031// Handle MCP requests32app.all('*', async (c) => {33  const transport = new WebStandardStreamableHTTPServerTransport()34  await server.connect(transport)35  return transport.handleRequest(c.req.raw)36})3738Deno.serve(app.fetch)
```

After this step, you should have a new file at `supabase/functions/mcp/index.ts`.

Within Edge Functions, paths are prefixed with the function name. If your function is named something other than `mcp`, configure Hono with a base path: `new Hono().basePath('/your-function-name')`.

* * *

### Step 3: Test locally[#](#step-3-test-locally)

Start the Supabase local development stack:

```
1supabase start
```

In a separate terminal, serve your function:

```
1supabase functions serve --no-verify-jwt mcp
```

Your MCP server is now running at:

```
1http://localhost:54321/functions/v1/mcp
```

The `--no-verify-jwt` flag disables JWT verification at the Edge Function layer so your MCP server can accept unauthenticated requests. Authenticated MCP support is coming soon.

#### Test with curl[#](#test-with-curl)

You can also test your MCP server directly with curl. Call the `add` tool:

```
1curl -X POST 'http://localhost:54321/functions/v1/mcp' \2  -H 'Content-Type: application/json' \3  -H 'Accept: application/json, text/event-stream' \4  -d '{5    "jsonrpc": "2.0",6    "id": 1,7    "method": "tools/call",8    "params": {9      "name": "add",10      "arguments": {11        "a": 5,12        "b": 313      }14    }15  }'
```

The MCP Streamable HTTP transport requires the `Accept: application/json, text/event-stream` header to indicate the client supports both JSON and Server-Sent Events responses.

**Expected response:**

The response uses Server-Sent Events (SSE) format:

```
1event: message2data: {"result":{"content":[{"type":"text","text":"8"}]},"jsonrpc":"2.0","id":1}
```

#### Test with MCP Inspector[#](#test-with-mcp-inspector)

Test your server with the official [MCP Inspector](https://github.com/modelcontextprotocol/inspector):

```
1npx -y @modelcontextprotocol/inspector
```

Use the local endpoint `http://localhost:54321/functions/v1/mcp` in the inspector UI to explore available tools and test them interactively.

After this step, you should have your MCP server running locally and be able to test the `add` tool in the MCP Inspector.

### Step 4: Deploy to production[#](#step-4-deploy-to-production)

When you're ready to deploy, link your project and deploy the function:

```
1supabase link --project-ref <your-project-ref>2supabase functions deploy --no-verify-jwt mcp
```

Your MCP server will be available at:

```
1https://<your-project-ref>.supabase.co/functions/v1/mcp
```

Update your MCP client configuration to use the production URL.

After this step, you have a fully deployed MCP server accessible from anywhere. You can test it using the MCP Inspector with your production URL.

## Examples[#](#examples)

You can find ready-to-use MCP server implementations here:

*   [Simple MCP server](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/mcp/simple-mcp-server) - Basic unauthenticated example

## Resources[#](#resources)

*   [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2025-11-25)
*   [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
*   [Supabase Edge Functions](/docs/guides/functions)
*   [OAuth 2.1 Server](/docs/guides/auth/oauth-server)
*   [MCP Authentication](/docs/guides/auth/oauth-server/mcp-authentication)
*   [Building MCP servers with mcp-lite](/docs/guides/functions/examples/mcp-server-mcp-lite) - Alternative lightweight framework


