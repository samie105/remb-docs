---
title: "AWS Lambda + API Gateway Adapter"
source: "https://trpc.io/docs/v10/server/adapters/aws-lambda"
canonical_url: "https://trpc.io/docs/v10/server/adapters/aws-lambda"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:29.256Z"
content_hash: "a5b7ef3ba361f328d890a327994182cc2def3bc1a06f34b1ad5bfb2a5f5432b2"
menu_path: ["AWS Lambda + API Gateway Adapter"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/quickstart/index.md", "title": "Quickstart"}
nav_next: {"path": "trpc/docs/v10/server/adapters/express/index.md", "title": "Express Adapter"}
---

## AWS Lambda adapter[​](#aws-lambda-adapter "Direct link to AWS Lambda adapter")

The AWS Lambda adapter is supported for API Gateway Rest API(v1) and HTTP API(v2) use cases.

## Example app[​](#example-app "Direct link to Example app")

Description

Links

API Gateway with NodeJS client.

*   [Source](https://github.com/trpc/trpc/tree/main/examples/lambda-api-gateway)

## How to add tRPC[​](#how-to-add-trpc "Direct link to How to add tRPC")

### 1\. Install deps[​](#1-install-deps "Direct link to 1. Install deps")

bash

`yarn add @trpc/server`

### 2\. Create a tRPC router[​](#2-create-a-trpc-router "Direct link to 2. Create a tRPC router")

Implement your tRPC router. A sample router is given below:

server.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { z } from 'zod';`

`export const t = initTRPC.create();`

`const appRouter = t.router({`

  `getUser: t.procedure.input(z.string()).query((opts) => {`

    `opts.input; // string`

    `return { id: opts.input, name: 'Bilbo' };`

  `}),`

`});`

`// export type definition of API`

`export type AppRouter = typeof appRouter;`

### 3\. Use the Amazon API Gateway adapter[​](#3-use-the-amazon-api-gateway-adapter "Direct link to 3. Use the Amazon API Gateway adapter")

tRPC includes an adapter for API Gateway out of the box. This adapter lets you run your routes through the API Gateway handler.

server.ts

ts

`import { CreateAWSLambdaContextOptions, awsLambdaRequestHandler } from '@trpc/server/adapters/aws-lambda';`

`const appRouter = /* ... */;`

`// created for each request`

`const createContext = ({`

  `event,`

  `context,`

`}: CreateAWSLambdaContextOptions<APIGatewayProxyEventV2>) => ({}) // no context`

`type Context = Awaited<ReturnType<typeof createContext>>;`

`export const handler = awsLambdaRequestHandler({`

  `router: appRouter,`

  `createContext,`

`})`

Build & deploy your code, now use your API Gateway URL to call your function.

Endpoint

HTTP URI

`getUser`

`GET https://<execution-api-link>/getUser?input=INPUT`

where `INPUT` is a URI-encoded JSON string.

#### A word about payload format version[​](#a-word-about-payload-format-version "Direct link to A word about payload format version")

API Gateway has two different event data formats when it invokes a Lambda. For REST APIs they should be version "1.0"(`APIGatewayProxyEvent`), but you can choose which for HTTP APIs by stating either version "1.0" or "2.0".

*   Version 1.0: `APIGatewayProxyEvent`
*   Version 2.0: `APIGatewayProxyEventV2`

To infer what version you might have, supply the context as following:

ts

`function createContext({`

  `event,`

  `context,`

`}: CreateAWSLambdaContextOptions<APIGatewayProxyEvent>) {`

  `...`

`}`

`// CreateAWSLambdaContextOptions<APIGatewayProxyEvent> or CreateAWSLambdaContextOptions<APIGatewayProxyEventV2>`

[Read more here about payload format version](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)


