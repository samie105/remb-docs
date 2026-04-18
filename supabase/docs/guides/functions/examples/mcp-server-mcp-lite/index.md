---
title: "Building an MCP Server with mcp-lite"
source: "https://supabase.com/docs/guides/functions/examples/mcp-server-mcp-lite"
canonical_url: "https://supabase.com/docs/guides/functions/examples/mcp-server-mcp-lite"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:35.767Z"
content_hash: "eda99eba8f8245f466aaa7f243d665e8cea14b4a152f2b936c9143e7819d7d81"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Building an MCP Server with mcp-lite","Building an MCP Server with mcp-lite"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Building an MCP Server with mcp-lite","Building an MCP Server with mcp-lite"]
nav_prev: {"path": "supabase/docs/guides/functions/examples/image-manipulation/index.md", "title": "Image Manipulation"}
nav_next: {"path": "supabase/docs/guides/functions/examples/og-image/index.md", "title": "Generating OG Images"}
---

# 

Building an MCP Server with mcp-lite

* * *

The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) enables Large Language Models (LLMs) to interact with external tools and data sources. With `mcp-lite`, you can build lightweight MCP servers that run on Supabase Edge Functions, giving your AI assistants the ability to execute custom tools at the edge.

This guide shows you how to scaffold, develop, and deploy an MCP server using mcp-lite on Supabase Edge Functions.

## What is mcp-lite?[#](#what-is-mcp-lite)

[mcp-lite](https://github.com/fiberplane/mcp-lite) is a lightweight, zero-dependency TypeScript framework for building MCP servers. It works everywhere the Fetch API is available, including Node, Bun, Cloudflare Workers, Deno, and Supabase Edge Functions.

## Why Supabase Edge Functions + mcp-lite?[#](#why-supabase-edge-functions--mcp-lite)

This combination offers several advantages:

*   **Zero cold starts**: Edge Functions stay warm for fast responses
*   **Global distribution**: Deploy once and run everywhere
*   **Direct database access**: Connect directly to your Supabase Postgres
*   **Minimal footprint**: mcp-lite has zero runtime dependencies
*   **Full type safety**: TypeScript support in Deno
*   **Simple deployment**: One command to production

## Prerequisites[#](#prerequisites)

You need:

*   [Docker](https://docs.docker.com/get-docker/) (to run Supabase locally)
*   [Deno](https://deno.land/) (Supabase Edge Functions runtime)
*   [Supabase CLI](/docs/guides/cli/getting-started)

## Create a new MCP server[#](#create-a-new-mcp-server)

Starting with `create-mcp-lite@0.3.0`, you can scaffold a complete MCP server that runs on Supabase Edge Functions:

```
1npm create mcp-lite@latest
```

When prompted, select **Supabase Edge Functions (MCP server)** from the template options.

The template creates a focused structure for Edge Functions development:

```
1my-mcp-server/2├── supabase/3│   ├── config.toml                    # Minimal Supabase config (Edge Functions only)4│   └── functions/5│       └── mcp-server/6│           ├── index.ts               # MCP server implementation7│           └── deno.json              # Deno imports and configuration8├── package.json9└── tsconfig.json
```

## Understanding the project structure[#](#understanding-the-project-structure)

### Minimal config.toml[#](#minimal-configtoml)

The template includes a minimal `config.toml` that runs only Edge Functions - no database, storage, or Studio UI. This keeps your local setup lightweight:

```
1# Minimal config for running only Edge Functions (no DB, storage, or studio)2project_id = "starter-mcp-supabase"34[api]5enabled = true6port = 5432178[edge_runtime]9enabled = true10policy = "per_worker"11deno_version = 2
```

You can always add more services as needed.

### Two Hono apps pattern[#](#two-hono-apps-pattern)

The template uses a specific pattern required by Supabase Edge Functions:

```
1// Root handler - matches the function name2const app = new Hono()34// MCP protocol handler5const mcpApp = new Hono()67mcpApp.get('/', (c) => {8  return c.json({9    message: 'MCP Server on Supabase Edge Functions',10    endpoints: {11      mcp: '/mcp',12      health: '/health',13    },14  })15})1617mcpApp.all('/mcp', async (c) => {18  const response = await httpHandler(c.req.raw)19  return response20})2122// Mount at /mcp-server (the function name)23app.route('/mcp-server', mcpApp)
```

This is required because Supabase routes all requests to `/<function-name>/*`. The outer `app` handles the function-level routing, while `mcpApp` handles your actual MCP endpoints.

### Deno import maps[#](#deno-import-maps)

The template uses Deno's import maps in `deno.json` to manage dependencies:

```
1{2  "compilerOptions": {3    "lib": ["deno.window", "deno.ns"],4    "strict": true5  },6  "imports": {7    "hono": "npm:hono@^4.6.14",8    "mcp-lite": "npm:mcp-lite@0.8.2",9    "zod": "npm:zod@^4.1.12"10  }11}
```

This gives you npm package access while staying in the Deno ecosystem.

## Local development[#](#local-development)

### Start Supabase[#](#start-supabase)

Navigate to your project directory and start Supabase services:

```
1supabase start
```

### Serve your function[#](#serve-your-function)

In a separate terminal, serve your MCP function locally:

```
1supabase functions serve --no-verify-jwt mcp-server
```

Or use the npm script (which runs the same command):

```
1npm run dev
```

Your MCP server is available at:

```
1http://localhost:54321/functions/v1/mcp-server/mcp
```

### Testing your server[#](#testing-your-server)

Test the MCP server by adding it to your Claude Code, Claude Desktop, Cursor, or your preferred MCP client.

Using Claude Code:

```
1claude mcp add my-mcp-server -t http http://localhost:54321/functions/v1/mcp-server/mcp
```

You can also test it using the MCP inspector:

```
1npx @modelcontextprotocol/inspector
```

Then add the MCP endpoint URL in the inspector UI.

## How it works[#](#how-it-works)

The MCP server setup is straightforward:

```
1import { McpServer, StreamableHttpTransport } from 'mcp-lite'2import { z } from 'zod'34// Create MCP server instance5const mcp = new McpServer({6  name: 'starter-mcp-supabase-server',7  version: '1.0.0',8  schemaAdapter: (schema) => z.toJSONSchema(schema as z.ZodType),9})1011// Define a tool12mcp.tool('sum', {13  description: 'Adds two numbers together',14  inputSchema: z.object({15    a: z.number(),16    b: z.number(),17  }),18  handler: (args: { a: number; b: number }) => ({19    content: [{ type: 'text', text: String(args.a + args.b) }],20  }),21})2223// Bind to HTTP transport24const transport = new StreamableHttpTransport()25const httpHandler = transport.bind(mcp)
```

## Adding more tools[#](#adding-more-tools)

Extend your MCP server by adding tools directly to the `mcp` instance. Here's an example of adding a database search tool:

```
1mcp.tool('searchDatabase', {2  description: 'Search your Supabase database',3  inputSchema: z.object({4    table: z.string(),5    query: z.string(),6  }),7  handler: async (args) => {8    // Access Supabase client here9    // const { data } = await supabase.from(args.table).select('*')10    return {11      content: [{ type: 'text', text: `Searching ${args.table}...` }],12    }13  },14})
```

You can add tools that:

*   Query your Supabase database
*   Access Supabase Storage for file operations
*   Call external APIs
*   Process data with custom logic
*   Integrate with other Supabase features

## Deploy to production[#](#deploy-to-production)

When ready, deploy to Supabase's global edge network:

```
1supabase functions deploy --no-verify-jwt mcp-server
```

Or use the npm script:

```
1npm run deploy
```

Your MCP server will be live at:

```
1https://your-project-ref.supabase.co/functions/v1/mcp-server/mcp
```

## Authentication considerations[#](#authentication-considerations)

The template uses `--no-verify-jwt` for quick development. This means authentication is not enforced by Supabase's JWT layer.

For production, you should implement authentication at the MCP server level following the [MCP Authorization specification](https://modelcontextprotocol.io/specification/draft/basic/authorization). This gives you control over who can access your MCP tools.

### Security best practices[#](#security-best-practices)

When deploying MCP servers:

*   **Don't expose sensitive data**: Use the server in development environments with non-production data
*   **Implement authentication**: Add proper authentication for production deployments
*   **Validate inputs**: Always validate and sanitize tool inputs
*   **Limit tool scope**: Only expose tools that are necessary for your use case
*   **Monitor usage**: Track tool calls and monitor for unusual activity

For more security guidance, see the [MCP security guide](/guides/getting-started/mcp#security-risks).

## What's next[#](#whats-next)

With your MCP server running on Supabase Edge Functions, you can:

*   Connect it to your Supabase database for data-driven tools
*   Use Supabase Auth to secure your endpoints
*   Access Supabase Storage for file operations
*   Deploy to multiple regions automatically
*   Scale to handle production traffic
*   Integrate with AI assistants like Claude, Cursor, or custom MCP clients

## Resources[#](#resources)

*   [mcp-lite on GitHub](https://github.com/fiberplane/mcp-lite)
*   [Model Context Protocol Spec](https://modelcontextprotocol.io/)
*   [Supabase Edge Functions Docs](/guides/functions)
*   [Deno Runtime Documentation](https://deno.land/)
*   [Fiberplane tutorial](https://blog.fiberplane.com/blog/mcp-lite-supabase-edge-functions/)

