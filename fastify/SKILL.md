## Overview

Fastify is a high-performance, low-overhead web framework for Node.js built on a plugin-first architecture. It emphasizes JSON Schema validation, a deterministic request-reply lifecycle, and encapsulation by default. An agent needs to know it to build scalable APIs and navigate its hook-driven plugin system.

## Mental Model

Fastify treats every feature as a plugin, forming a tree of encapsulated contexts where decorators extend functionality and hooks intercept the request-reply lifecycle. The framework relies on zero-cost abstractions, strict JSON Schema validation, and a deterministic plugin loading order. Canonical pages: `fastify/docs/latest/Guides/Getting-Started/index.md`, `fastify/docs/latest/Guides/Plugins-Guide/index.md`, `fastify/docs/latest/Reference/Hooks/index.md`, `fastify/docs/latest/Reference/Lifecycle/index.md`.

## Learning Paths

- **New Developer:** `fastify/docs/latest/Guides/Getting-Started/index.md` → `fastify/docs/latest/Guides/Plugins-Guide/index.md` → `fastify/docs/latest/Reference/Routes/index.md`
- **Production Engineer:** `fastify/docs/latest/Guides/Database/index.md` → `fastify/docs/latest/Reference/Validation-and-Serialization/index.md` → `fastify/docs/latest/Guides/Delay-Accepting-Requests/index.md` → `fastify/docs/latest/Guides/Benchmarking/index.md`
- **Framework Contributor:** `fastify/docs/latest/Reference/Hooks/index.md` → `fastify/docs/latest/Reference/Lifecycle/index.md` → `fastify/docs/latest/Reference/Decorators/index.md` → `fastify/docs/latest/Reference/Plugins/index.md` → `fastify/docs/latest/Guides/Contributing/index.md`

## Concept Map

- **Server & Basics**
  - Getting Started → `fastify/docs/latest/Guides/Getting-Started/index.md`
  - Routes → `fastify/docs/latest/Reference/Routes/index.md`
  - Request / Reply → `fastify/docs/latest/Reference/Request/index.md`, `fastify/docs/latest/Reference/Reply/index.md`
- **Plugin Architecture**
  - Plugins Guide → `fastify/docs/latest/Guides/Plugins-Guide/index.md`
  - Encapsulation & Scope → `fastify/docs/latest/Reference/Plugins/index.md`
  - Decorators → `fastify/docs/latest/Reference/Decorators/index.md`
  - Ecosystem → `fastify/docs/latest/Guides/Ecosystem/index.md`
- **Lifecycle & Hooks**
  - Hooks → `fastify/docs/latest/Reference/Hooks/index.md`
  - Lifecycle → `fastify/docs/latest/Reference/Lifecycle/index.md`
- **Validation & Types**
  - Validation and Serialization → `fastify/docs/latest/Reference/Validation-and-Serialization/index.md`
  - Fluent Schema → `fastify/docs/latest/Guides/Fluent-Schema/index.md`
  - Type Providers → `fastify/docs/latest/Reference/Type-Providers/index.md`
- **Operations & Reliability**
  - Benchmarking → `fastify/docs/latest/Guides/Benchmarking/index.md`
  - Delay Accepting Requests → `fastify/docs/latest/Guides/Delay-Accepting-Requests/index.md`
  - Detecting Client Abort → `fastify/docs/latest/Guides/Detecting-When-Clients-Abort/index.md`
  - Logging → `fastify/docs/latest/Reference/Logging/index.md`
- **Data & Migration**
  - Database → `fastify/docs/latest/Guides/Database/index.md`
  - Migration Guides → `fastify/docs/latest/Guides/Migration-Guide-V3/index.md`, `fastify/docs/latest/Guides/Migration-Guide-V4/index.md`, `fastify/docs/latest/Guides/Migration-Guide-V5/index.md`
  - LTS → `fastify/docs/latest/Reference/LTS/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Build your first server | `fastify/docs/latest/Guides/Getting-Started/index.md` |
| Master plugins and encapsulation | `fastify/docs/latest/Guides/Plugins-Guide/index.md` |
| Intercept the request lifecycle | `fastify/docs/latest/Reference/Hooks/index.md` |
| Validate requests and serialize responses | `fastify/docs/latest/Reference/Validation-and-Serialization/index.md` |
| Use TypeScript type providers | `fastify/docs/latest/Reference/Type-Providers/index.md` |
| Connect to a database | `fastify/docs/latest/Guides/Database/index.md` |
| Benchmark performance | `fastify/docs/latest/Guides/Benchmarking/index.md` |
| Handle client disconnects | `fastify/docs/latest/Guides/Detecting-When-Clients-Abort/index.md` |
| Delay accepting requests on startup | `fastify/docs/latest/Guides/Delay-Accepting-Requests/index.md` |
| Migrate to a new major version | `fastify/docs/latest/Guides/Migration-Guide-V5/index.md` |
| Extend the Fastify instance | `fastify/docs/latest/Reference/Decorators/index.md` |
| Understand the request lifecycle | `fastify/docs/latest/Reference/Lifecycle/index.md` |

## Top Must-Know Pages

1. `fastify/docs/latest/Guides/Getting-Started/index.md` — Install Fastify and create your first server and plugin.
2. `fastify/docs/latest/Guides/Plugins-Guide/index.md` — Core guide to the plugin system, decorators, hooks, and encapsulation.
3. `fastify/docs/latest/Reference/Hooks/index.md` — Complete reference for request/reply and application lifecycle hooks.
4. `fastify/docs/latest/Reference/Lifecycle/index.md` — Detailed visual reference of the Fastify request/response lifecycle.
5. `fastify/docs/latest/Reference/Plugins/index.md` — Deep dive into plugin registration, scope handling, and distribution.
6. `fastify/docs/latest/Reference/Validation-and-Serialization/index.md` — How to validate inputs and serialize outputs with JSON Schema.
7. `fastify/docs/latest/Reference/Decorators/index.md` — Extend Fastify instances and encapsulation contexts with custom functionality.
8. `fastify/docs/latest/Guides/Database/index.md` — Integrate MySQL, Postgres, Redis, and MongoDB into your application.
9. `fastify/docs/latest/Guides/Benchmarking/index.md` — Performance testing workflows for current branches and Node.js versions.
10. `fastify/docs/latest/Guides/Migration-Guide-V5/index.md` — Latest breaking changes, LTS cycle, and V5 upgrade requirements.