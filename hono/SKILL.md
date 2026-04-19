# Hono Developer Documentation Skill Guide

## Overview
Hono is a lightweight, high-performance web framework for JavaScript and TypeScript, designed to run seamlessly across modern runtimes (like Cloudflare Workers, Deno, Node.js, and more). It emphasizes speed, web standards (Fetch-based API), portability, and an excellent developer experience for building APIs and web apps.

---

## Key Concepts

- **Router**: Hono's core is its router, supporting fast and flexible route matching for handling HTTP requests ([Routers](hono/docs/concepts/routers/index.md)).
- **Middleware**: Composable units for request/response transformation, authentication, error handling, etc. ([Middleware](hono/docs/concepts/middleware/index.md)).
- **Web Standard APIs**: Near-native web APIs (`Request`, `Response`, etc.), making Hono code portable and familiar ([Web Standard](hono/docs/concepts/web-standard/index.md)).
- **Context (`c`)**: Passed to handlers, providing access to request/response, params, and helpers ([Context](hono/docs/api/context/index.md)).
- **Platform Adaptability**: Hono runs the same codebase on many cloud/serverless providers and runtimes ([Getting Started](hono/docs/getting-started/basic/index.md)).
- **RPC & Stacks**: Build full-stack or RPC-based apps while benefiting from Hono’s minimalism ([Hono Stacks](hono/docs/concepts/stacks/index.md)).
- **Built-in & Helper Modules**: Helpers for testing, cookies, JWT, CSS-in-JS, streaming, etc. ([Helpers](hono/docs/helpers/accepts/index.md), [Middleware Built-ins](hono/docs/middleware/builtin/cors/index.md)).

---

## Docs Navigation Guide

**Finding What You Need:**
- **Project Philosophy/Intent:** [Motivation](hono/docs/concepts/motivation/index.md)
- **Core Concepts/Internal Design:** [Concepts](hono/docs/concepts/routers/index.md), [Middleware](hono/docs/concepts/middleware/index.md)
- **Environment/Deployment-Specific Guides:** [Getting Started](hono/docs/getting-started/basic/index.md) and runtime-specific subpages
- **API Reference:** [API Directory](hono/docs/api/hono/index.md) and related pages
- **Usage Patterns/Recipes:** [Guides](hono/docs/guides/create-hono/index.md) (middleware, testing, validation, etc.)
- **Helpers and Middleware:** [Helpers Index](hono/docs/helpers/accepts/index.md), [Middleware Built-in](hono/docs/middleware/builtin/cors/index.md)
- **Troubleshooting/Common Issues:** [FAQs](hono/docs/guides/faq/index.md)

**Sections Explained:**
- `concepts/`: Philosophy, routing, standards; start here for theory or internals.
- `getting-started/`: Environment/platform setup and demos for many runtimes.
- `api/`: Reference for all core interfaces (routing, context, requests).
- `guides/`: How-to topics, best practices, and advanced patterns.
- `helpers/`: Utility modules and common helpers.
- `middleware/`: Built-in and third-party middleware docs.

---

## Top Pages & One-Line Summaries

- [Motivation](hono/docs/concepts/motivation/index.md)  
  Why Hono exists; what problems it aims to solve.
- [Routers](hono/docs/concepts/routers/index.md)  
  Hono’s router design, fast RegExpRouter, and routing internals.
- [Web Standard](hono/docs/concepts/web-standard/index.md)  
  How Hono leverages modern web standards (Fetch API, etc.).
- [Middleware](hono/docs/concepts/middleware/index.md)  
  Middleware fundamentals, composition, and lifecycle overview.
- [Basic Getting Started](hono/docs/getting-started/basic/index.md)  
  First steps with Hono in any environment.
- [Cloudflare Workers Setup](hono/docs/getting-started/cloudflare-workers/index.md)  
  Starting a Hono app on Cloudflare Workers.
- [Deno Setup](hono/docs/getting-started/deno/index.md)  
  Using Hono with Deno and Deno Deploy.
- [AWS Lambda Setup](hono/docs/getting-started/aws-lambda/index.md)  
  Deploying Hono to AWS Lambda (Node.js 18+).
- [Service Worker Support](hono/docs/getting-started/service-worker/index.md)  
  Running Hono as a service worker for PWA/edge cases.
- [App API](hono/docs/api/hono/index.md)  
  Core Hono application API (main entry point class).
- [Routing API](hono/docs/api/routing/index.md)  
  Route definition and matching details.
- [Context API](hono/docs/api/context/index.md)  
  Handler context object: request, response, params, etc.
- [HonoRequest API](hono/docs/api/request/index.md)  
  Request wrapper: params, headers, form data, etc.
- [Middleware – Built-in Directory](hono/docs/middleware/builtin/cors/index.md)  
  Core middlewares, e.g. CORS, auth, compression (see directory for all).
- [Helpers Index (e.g. Cookie, JWT, Route)](hono/docs/helpers/cookie/index.md)  
  Utility/helper modules for common needs.
- [Testing Guide](hono/docs/guides/testing/index.md)  
  Patterns and helpers for testing Hono apps.
- [FAQ](hono/docs/guides/faq/index.md)  
  Common problems, usage questions, and troubleshooting.

---

## Gotchas & Structure Quirks

- Many environment/platform guides live under `getting-started/` as _peers_, not subpages—scan the full section to find your target (e.g., Deno, AWS Lambda, Cloudflare Workers, Netlify, etc.).
- Middleware is covered both conceptually ([Concepts/Middleware](hono/docs/concepts/middleware/index.md)) and practically ([middleware/builtin/](hono/docs/middleware/builtin/cors/index.md)).
- Helper modules (cookies, JWT, CSS, SSG, etc.) are *not* listed in the main guides—see `helpers/` for these utilities.
- Some doc pages are minimal or stub-like; check the *Guides* or *API* sections if a page doesn't answer your question in depth.
- There is extensive overlap between the Concepts and API sections for topics like Context & Routing—use both as needed.
- For reference on third-party middleware, see [3rd-party Middleware](hono/docs/middleware/third-party/index.md).

---