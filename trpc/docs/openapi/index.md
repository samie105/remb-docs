---
title: "OpenAPI (alpha)"
source: "https://trpc.io/docs/openapi"
canonical_url: "https://trpc.io/docs/openapi"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:57.746Z"
content_hash: "2d18322ee4331a6aa751a71053941ce5fba5f78e85e14acd26b89a0898bf898b"
menu_path: ["OpenAPI (alpha)"]
section_path: []
nav_prev: {"path": "trpc/docs/rpc/index.md", "title": "HTTP RPC Specification"}
nav_next: {"path": "trpc/docs/server/adapters/index.md", "title": "Overview"}
---

caution

This package is in alpha. APIs may change without notice.

The `@trpc/openapi` package generates an OpenAPI 3.1 specification from your tRPC router. Use the spec to:

*   Generate a typed API client in any language
*   Call tRPC endpoints via HTTP tools like Postman or Insomnia
*   Enable AI agent integrations such as MCP servers

## Install[​](#install "Direct link to Install")

bash

`pnpm add @trpc/openapi`

AI Agents

If you use an AI coding agent, install tRPC skills for better code generation:

bash

`npx @tanstack/intent@latest install`

note

`@trpc/openapi` is currently versioned like 11.x.x-alpha, and should work with any recent tRPC v11 version, but as always we recommend aligning the version numbers

## Adapting your tRPC setup[​](#adapting-your-trpc-setup "Direct link to Adapting your tRPC setup")

The generator works with your existing router — no annotations or decorators required. A few things to be aware of:

*   **No output types needed** — unlike other OpenAPI tools, `.output()` schemas are optional. The generator infers return types from your implementation automatically.
*   **Transformers** — if your server uses a [data transformer](trpc/docs/server/data-transformers/index.md), your OpenAPI clients must use the same one. See [Transformers](#transformers) for setup and cross-language options.
*   **Subscriptions** — currently excluded from the generated spec. SSE support is planned.
*   **Descriptions** — Zod `.describe()` calls and JSDoc comments on types, routers, and procedures, all become `description` fields in the spec.

## Generate the spec[​](#generate-the-spec "Direct link to Generate the spec")

### CLI[​](#cli "Direct link to CLI")

bash

`pnpm exec trpc-openapi ./src/server/router.ts`

Option

Default

Description

`-e, --export <name>`

`AppRouter`

Name of the exported router type

`-o, --output <file>`

`openapi.json`

Output file path

`--title <text>`

`tRPC API`

OpenAPI `info.title`

`--version <ver>`

`0.0.0`

OpenAPI `info.version`

bash

`pnpm exec trpc-openapi ./src/server/router.ts -o api.json --title "My API" --version 1.0.0`

### Programmatic[​](#programmatic "Direct link to Programmatic")

scripts/generate-openapi.ts

ts

`import { generateOpenAPIDocument } from '@trpc/openapi';`

`const doc = generateOpenAPIDocument('./src/server/router.ts', {`

  `exportName: 'AppRouter',`

  `title: 'My API',`

  `version: '1.0.0',`

`});`

The generator statically analyses your router's TypeScript types — it never executes your code.

## Generate a client from the spec[​](#generate-a-client-from-the-spec "Direct link to Generate a client from the spec")

Any OpenAPI client generator should work, but the most tested integration is with [Hey API](https://heyapi.dev/openapi-ts/get-started).

A generated client will produce typed SDK functions matching your tRPC procedures:

*   **Queries** → `GET /procedure.path`
*   **Mutations** → `POST /procedure.path`
*   **Subscriptions** are ignored (SSE coming soon)

### Hey API (TypeScript)[​](#hey-api-typescript "Direct link to Hey API (TypeScript)")

[Hey API Documentation](https://heyapi.dev/)

bash

`pnpm add @trpc/openapi @hey-api/openapi-ts`

Out of the box, an OpenAPI-generated client won't know about your transformer setup or how to encode query parameters. The `@trpc/openapi/heyapi` package provides a `configureTRPCHeyApiClient` helper that bridges this gap — it configures request serialisation, response parsing, and error deserialization so the generated SDK works correctly with tRPC endpoints.

#### Without a transformer[​](#without-a-transformer "Direct link to Without a transformer")

You can generate your client using Hey API's CLI or programmatic API in this case

bash

`pnpm exec openapi-ts -i openapi.json -o ./generated`

Next a little configuration is required at runtime:

src/usage.ts

ts

`import { configureTRPCHeyApiClient } from '@trpc/openapi/heyapi';`

`import { client } from './generated/client.gen';`

`import { Sdk } from './generated/sdk.gen';`

`configureTRPCHeyApiClient(client, {`

  `baseUrl: 'http://localhost:3000',`

`});`

`const sdk = new Sdk({ client });`

`const result = await sdk.greeting({ query: { input: { name: 'World' } } });`

`const user = await sdk.user.create({ body: { name: 'Bob', age: 30 } });`

#### With a transformer (superjson, devalue, etc.)[​](#with-a-transformer-superjson-devalue-etc "Direct link to With a transformer (superjson, devalue, etc.)")

warning

If your backend uses a [data transformer](trpc/docs/server/data-transformers/index.md) like `superjson`, you **must** pass it to the client config. Without this, Dates, Maps, Sets, and other non-JSON types may be silently wrong.

First generate your client code using Hey API's programmatic API, this way you can use `createTRPCHeyApiTypeResolvers` to ensure your emitted types are correct:

src/client.ts

ts

`import { createClient } from '@hey-api/openapi-ts';`

`import { createTRPCHeyApiTypeResolvers } from '@trpc/openapi/heyapi';`

`const openApiJson = './path/to/openapi.json'`

`const outputDir = './generated'`

`await createClient({`

  `input: openApiJson,`

  `output: outputDir,`

  `plugins: [`

    `{`

      `name: '@hey-api/typescript',`

      `// Important: this ensures that your emitted types like Dates are correct`

      `'~resolvers': createTRPCHeyApiTypeResolvers(),`

    `},`

    `{`

      `name: '@hey-api/sdk',`

      `operations: { strategy: 'single' },`

    `},`

  `],`

`});`

At runtime configure the generated client with your transformer, you can then pass native types directly and get them back deserialised:

src/usage.ts

ts

`import { configureTRPCHeyApiClient } from '@trpc/openapi/heyapi';`

`import superjson from 'superjson';`

`import { client } from './generated/client.gen';`

`configureTRPCHeyApiClient(client, {`

  `baseUrl: 'http://localhost:3000',`

  `// Important, this transformer must match your tRPC API's transformer:`

  `transformer: superjson,`

`});`

`const sdk = new Sdk({ client });`

`const event = await sdk.getEvent({`

  `query: { input: { id: 'evt_1', at: new Date('2025-06-15T10:00:00Z') } },`

`});`

`// event.data.result.data.at is a Date object ✅`

`const created = await sdk.createEvent({`

  `body: { name: 'Conference', at: new Date('2025-09-01T09:00:00Z') },`

`});`

### Using a different generator or language[​](#using-a-different-generator-or-language "Direct link to Using a different generator or language")

The generated OpenAPI spec works with any OpenAPI-compatible client generator which can:

*   Emit accurate types for classes like Date
*   Support customising Search Params and request/response body serialization

To integrate correctly with tRPC's protocol, you need to set up your generated client to do two things:

*   **Transformers** — If your tRPC API uses a transformer, the client must serialise inputs and deserialise outputs using the same format
*   **Query Inputs** — GET requests encode input as `?input=<JSON>`, not as individual query parameters

See the [Hey API config source](https://github.com/trpc/trpc/blob/f346e9bb97ff3c8a7e874f59110a47730293097a/packages/openapi/src/heyapi/index.ts) for a complete reference implementation.

### Transformers[​](#transformers "Direct link to Transformers")

tRPC [data transformers](trpc/docs/server/data-transformers/index.md) let you send rich types like `Date`, `Map`, `Set`, and `BigInt` over the wire. When using the OpenAPI client, the same transformer must be configured on both the server and client so that inputs are serialised and outputs are deserialised correctly.

Any transformer that implements the tRPC `DataTransformer` interface (`serialize` / `deserialize`) works with `configureTRPCHeyApiClient`. Below are some tested options.

#### SuperJSON[​](#superjson "Direct link to SuperJSON")

The most popular transformer for TypeScript-to-TypeScript setups. Handles `Date`, `Map`, `Set`, `BigInt`, `RegExp`, and more.

bash

`pnpm add superjson`

src/server.ts

ts

`import { initTRPC } from '@trpc/server';`

`import superjson from 'superjson';`

`const t = initTRPC.create({ transformer: superjson });`

src/client.ts

ts

`import { configureTRPCHeyApiClient } from '@trpc/openapi/heyapi';`

`import superjson from 'superjson';`

`import { client } from './generated/client.gen';`

`configureTRPCHeyApiClient(client, {`

  `baseUrl: 'http://localhost:3000',`

  `transformer: superjson,`

`});`

See the [superjson test](https://github.com/trpc/trpc/blob/main/packages/openapi/test/generate.test.ts) for a full end-to-end example.

#### MongoDB Extended JSON v2[​](#mongodb-extended-json-v2 "Direct link to MongoDB Extended JSON v2")

[EJSON](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/#mongodb-extended-json-v2-usage) is a good choice when you need cross-language support. The `bson` npm package provides `EJSON.serialize` / `EJSON.deserialize` which map directly to a tRPC `DataTransformer`.

Available in: C, C#, C++, Go, Java, Node.js, Perl, PHP, Python, Ruby, Scala

bash

`pnpm add bson`

src/transformer.ts

ts

`import { EJSON } from 'bson';`

`import type { TRPCDataTransformer } from '@trpc/server';`

`export const ejsonTransformer: TRPCDataTransformer = {`

  `serialize: (value) => EJSON.serialize(value),`

  `deserialize: (value) => EJSON.deserialize(value as Document),`

`};`

src/client.ts

ts

`import { configureTRPCHeyApiClient } from '@trpc/openapi/heyapi';`

`import { client } from './generated/client.gen';`

`import { ejsonTransformer } from './transformer';`

`configureTRPCHeyApiClient(client, {`

  `baseUrl: 'http://localhost:3000',`

  `transformer: ejsonTransformer,`

`});`

See the [MongoDB EJSON test](https://github.com/trpc/trpc/blob/main/packages/openapi/test/mongoEjson.test.ts) for a full end-to-end example.

#### Amazon Ion[​](#amazon-ion "Direct link to Amazon Ion")

[Amazon Ion](https://amazon-ion.github.io/ion-docs/) is a richly-typed data format with broad language support. It doesn't directly support the `TRPCDataTransformer` interface and requires a bit of boilerplate to make work with tRPC in JS/TS, but may be a good choice for your own system.

Available in: C, C#, D, Go, Java, JavaScript, PHP, Python, Rust

bash

`pnpm add ion-js`

See the [Amazon Ion test](https://github.com/trpc/trpc/blob/main/packages/openapi/test/amazonIon.test.ts) for the transformer implementation, boilerplate, and a full end-to-end example.

#### Writing a custom transformer[​](#writing-a-custom-transformer "Direct link to Writing a custom transformer")

Any object with `serialize` and `deserialize` methods works:

ts

`import type { TRPCDataTransformer } from '@trpc/server';`

`const myTransformer: TRPCDataTransformer = {`

  `serialize: (value) => {`

    `/* encode rich types */`

  `},`

  `deserialize: (value) => {`

    `/* decode them back */`

  `},`

`};`

Pass it to both `initTRPC.create({ transformer })` on the server and `configureTRPCHeyApiClient(client, { transformer })` on the client. See the [data transformers docs](trpc/docs/server/data-transformers/index.md) for more details.

### Full example[​](#full-example "Direct link to Full example")

For a complete, runnable project that ties all of these steps together, see the [openapi-codegen example](https://github.com/trpc/trpc/tree/main/examples/openapi-codegen).

## API changelog and breaking-change checks with `oasdiff`[​](#api-changelog-and-breaking-change-checks-with-oasdiff "Direct link to api-changelog-and-breaking-change-checks-with-oasdiff")

After generating OpenAPI specs, you can compare two versions with [`oasdiff`](https://github.com/oasdiff/oasdiff).

For installation options (Homebrew, Docker, binaries, etc), see the official docs:

*   [oasdiff install docs](https://github.com/oasdiff/oasdiff/blob/main/docs/README.md)
*   [oasdiff changelog and breaking checks](https://github.com/oasdiff/oasdiff/blob/main/docs/BREAKING-CHANGES.md)

Using this you can quick generate changelogs or detect inadvertent breaking changes to APIs to help plan and coordinate releases

sh

`# Get a complete changelog including minor and breaking changes`

`$ oasdiff changelog packages/openapi/test/routers/superjsonRouter.openapi.json /tmp/superjsonRouter.openapi.next.json`

`3 changes: 2 error, 0 warning, 1 info`

`error [new-required-request-property] in API POST /createEvent`

  `added the new required request property 'location'`

`error [api-path-removed-without-deprecation] in API GET /getBigInt`

  `api path removed without deprecation`

`info [endpoint-added] in API GET /health`

  `endpoint added`

`# Get a list of breaking changes if any`

`$ oasdiff breaking packages/openapi/test/routers/superjsonRouter.openapi.json /tmp/superjsonRouter.openapi.next.json`

`2 changes: 2 error, 0 warning, 0 info`

`error [new-required-request-property] in API POST /createEvent`

  `added the new required request property 'location'`

`error [api-path-removed-without-deprecation] in API GET /getBigInt`

  `api path removed without deprecation`


