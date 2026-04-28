## Overview

Hono is a lightweight, edge-ready web framework built on Web Standards for runtimes including Cloudflare Workers, Deno, Bun, and Node.js. It offers an Express-like API with modern primitives such as JSX, middleware, and pluggable routers. An agent needs to know Hono to build fast, portable HTTP services and APIs that run anywhere JavaScript executes.

## Mental Model

Hono is built around a Web Standards `Request`/`Response` core where an `App` (`hono/docs/api/hono/index.md`) orchestrates a pipeline of middleware and handlers through a pluggable router layer (`hono/docs/api/routing/index.md`). Each incoming request instantiates a `Context` (`hono/docs/api/context/index.md`) that wraps the native request and provides response helpers, while the framework abstracts runtime differences via router implementations (`hono/docs/concepts/routers/index.md`).

## Learning Paths

**Getting Started**
1. `hono/docs/index.md` — Quick start and features.
2. `hono/docs/getting-started/basic/index.md` — Hello World and JSON responses.
3. `hono/docs/api/routing/index.md` — Basic routing patterns.
4. `hono/docs/api/context/index.md` — Request/response context.

**Production Ready**
1. `hono/docs/guides/validation/index.md` — Input validation patterns.
2. `hono/docs/middleware/builtin/basic-auth/index.md` — Authentication.
3. `hono/docs/middleware/builtin/secure-headers/index.md` — Security headers.
4. `hono/docs/api/exception/index.md` — Error handling.

**Reference Deep-Dive**
1. `hono/docs/concepts/routers/index.md` — Router internals.
2. `hono/docs/concepts/benchmarks/index.md` — Performance benchmarks.
3. `hono/docs/api/hono/index.md` — App API methods.
4. `hono/docs/api/request/index.md` — Request parsing helpers.

## Concept Map

- Getting Started
  - Landing & Quick Start: `hono/docs/index.md`
  - Basics & Hello World: `hono/docs/getting-started/basic/index.md`
- Application Core
  - App & Lifecycle: `hono/docs/api/hono/index.md`
  - Context & Response Helpers: `hono/docs/api/context/index.md`
  - Error Handling: `hono/docs/api/exception/index.md`
  - Presets: `hono/docs/api/presets/index.md`
- Routing & Requests
  - Routing Patterns: `hono/docs/api/routing/index.md`
  - Request Parsing: `hono/docs/api/request/index.md`
- Middleware
  - Basic Auth: `hono/docs/middleware/builtin/basic-auth/index.md`
  - Secure Headers: `hono/docs/middleware/builtin/secure-headers/index.md`
- Guides & Helpers
  - JSX: `hono/docs/guides/jsx/index.md`
  - Validation: `hono/docs/guides/validation/index.md`
  - HTML Helper: `hono/docs/helpers/html/index.md`
  - CSS Helper: `hono/docs/helpers/css/index.md`
  - Route Helper: `hono/docs/helpers/route/index.md`
- Concepts
  - Routers: `hono/docs/concepts/routers/index.md`
  - Benchmarks: `hono/docs/concepts/benchmarks/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Bootstrap a project or write Hello World | `hono/docs/getting-started/basic/index.md` |
| Understand the app lifecycle and methods | `hono/docs/api/hono/index.md` |
| Define routes with params or patterns | `hono/docs/api/routing/index.md` |
| Access request data (params, query, body) | `hono/docs/api/request/index.md` |
| Set status, headers, or body on a response | `hono/docs/api/context/index.md` |
| Throw or catch HTTP errors | `hono/docs/api/exception/index.md` |
| Validate incoming data | `hono/docs/guides/validation/index.md` |
| Render JSX or HTML | `hono/docs/guides/jsx/index.md` |
| Add basic authentication | `hono/docs/middleware/builtin/basic-auth/index.md` |
| Configure security headers | `hono/docs/middleware/builtin/secure-headers/index.md` |
| Compare router internals or performance | `hono/docs/concepts/routers/index.md`, `hono/docs/concepts/benchmarks/index.md` |

## Top Must-Know Pages

1. `hono/docs/index.md` — Landing page with quick start, features, and use-cases.
2. `hono/docs/getting-started/basic/index.md` — Starter guide covering Hello World and JSON responses.
3. `hono/docs/api/hono/index.md` — Core App API for methods, error handling, and fetch/fire lifecycle.
4. `hono/docs/api/routing/index.md` — Routing reference for path parameters, optional params, and regexp.
5. `hono/docs/api/context/index.md` — Context object reference for `req`, `status`, `header`, `body`, and `text`.
6. `hono/docs/api/request/index.md` — HonoRequest helpers for `param`, `query`, `header`, and `parseBody`.
7. `hono/docs/api/exception/index.md` — Throwing and handling HTTPExceptions with custom responses.
8. `hono/docs/guides/validation/index.md` — Validation patterns including Zod and Standard Schema middleware.
9. `hono/docs/concepts/routers/index.md` — Architecture of RegExp, Trie, Smart, Linear, and Pattern routers.
10. `hono/docs/guides/jsx/index.md` — JSX configuration, fragments, and raw HTML insertion.