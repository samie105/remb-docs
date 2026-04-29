---
title: "Usage with Amazon Lambda through the API Gateway"
source: "https://trpc.io/docs/v9/aws-lambda"
canonical_url: "https://trpc.io/docs/v9/aws-lambda"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:15.251Z"
content_hash: "1c7ca15af3097f3ab2ff2c6f3314217753739f9a06aca36b87a69ed2423bfee0"
menu_path: ["Usage with Amazon Lambda through the API Gateway"]
section_path: []
nav_prev: {"path": "../awesome-trpc/index.md", "title": "Awesome tRPC Collection"}
nav_next: {"path": "../caching/index.md", "title": "Response Caching"}
---

## Amazon Lambda adapter[​](#amazon-lambda-adapter "Direct link to Amazon Lambda adapter")

The AWS Lambda adapter is supported for API Gateway Rest API(v1) and HTTP API(v2) use cases.

## Example app[​](#example-app "Direct link to Example app")

Description

URL

Links

API Gateway with NodeJS client.

_n/a_

*   [Source](https://github.com/trpc/trpc/tree/main/examples/lambda-api-gateway)

## How to add tRPC[​](#how-to-add-trpc "Direct link to How to add tRPC")

### 1\. Install deps[​](#1-install-deps "Direct link to 1. Install deps")

bash

`yarn add @trpc/server`

### 2\. Create a tRPC router[​](#2-create-a-trpc-router "Direct link to 2. Create a tRPC router")

Implement your tRPC router. A sample router is given below:

server.ts

ts

`import * as trpc from '@trpc/server';`

`import { z } from 'zod';`

`const appRouter = trpc.router().query('getUser', {`

  `input: z.string(),`

  `async resolve(req) {`

    `req.input; // string`

    `return { id: req.input, name: 'Bilbo' };`

  `},`

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

`}: CreateAWSLambdaContextOptions) => ({}) // no context`

`type Context = trpc.inferAsyncReturnType<typeof createContext>;`

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

API Gateway has two different event data formats when it invokes a Lambda. For REST APIs they should be version "1.0"(`APIGatewayProxyEvent`), but you can chose which for HTTP APIs by stating either version "1.0" or "2.0".

*   Version 1.0: `APIGatewayProxyEvent`
*   Version 2.0: `APIGatewayProxyEventV2`

To infer what version you might have, supply the context as following:

`function createContext({   event,   context, }: CreateAWSLambdaContextOptions<APIGatewayProxyEvent>) {   ... }  // CreateAWSLambdaContextOptions<APIGatewayProxyEvent> or CreateAWSLambdaContextOptions<APIGatewayProxyEventV2>`

[Read more here about payload format version](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
