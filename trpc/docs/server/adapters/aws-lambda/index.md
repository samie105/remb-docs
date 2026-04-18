---
title: "AWS Lambda + API Gateway Adapter"
source: "https://trpc.io/docs/server/adapters/aws-lambda"
canonical_url: "https://trpc.io/docs/server/adapters/aws-lambda"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:02.255Z"
content_hash: "86411297f959469829e8f56f18c62e9f436e084a2eaf92fbfad5a0e99315198f"
menu_path: ["AWS Lambda + API Gateway Adapter"]
section_path: []
---
## AWS Lambda adapter[​](#aws-lambda-adapter "Direct link to AWS Lambda adapter")

The AWS Lambda adapter is supported for API Gateway [REST API(v1)](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html) and [HTTP API(v2)](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html), and [Lambda Function URL](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html) use cases.

> `httpBatchLink` requires the router to work on a single API Gateway Resource (as shown in the [example](https://github.com/trpc/trpc/tree/main/examples/lambda-api-gateway)). If you'd like to have a Resource per procedure, you can use the `httpLink` instead ([more info](https://github.com/trpc/trpc/issues/5738#issuecomment-2130001522)).

## Example apps[​](#example-apps "Direct link to Example apps")

Description

Links

API Gateway with NodeJS client.

*   [Source](https://github.com/trpc/trpc/tree/main/examples/lambda-api-gateway)

API Gateway REST API with response streaming.

*   [Source](https://github.com/trpc/trpc/tree/main/examples/lambda-api-gateway-streaming)

## How to add tRPC[​](#how-to-add-trpc "Direct link to How to add tRPC")

### 1\. Install deps[​](#1-install-deps "Direct link to 1. Install deps")

bash

`yarn add @trpc/server`

AI Agents

If you use an AI coding agent, install tRPC skills for better code generation:

bash

`npx @tanstack/intent@latest install`

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

`import type { APIGatewayProxyEventV2 } from 'aws-lambda';`

`import type { CreateAWSLambdaContextOptions } from '@trpc/server/adapters/aws-lambda';`

`import { awsLambdaRequestHandler } from '@trpc/server/adapters/aws-lambda';`

`import { appRouter } from './router';`

`// created for each request`

`const createContext = ({`

  `event,`

  `context,`

`}: CreateAWSLambdaContextOptions<APIGatewayProxyEventV2>) => ({}); // no context`

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

  `// ...`

`}`

`// CreateAWSLambdaContextOptions<APIGatewayProxyEvent> or CreateAWSLambdaContextOptions<APIGatewayProxyEventV2>`

[Read more here about payload format version](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)

## AWS Lambda Response Streaming Adapter[​](#aws-lambda-response-streaming-adapter "Direct link to AWS Lambda Response Streaming Adapter")

AWS Lambda supports streaming responses to clients with both Lambda Function URLs and API Gateway REST APIs.

> Response streaming is supported for Lambda Function URLs and API Gateway REST APIs. For API Gateway REST APIs, you need to configure the integration with `responseTransferMode: STREAM`. [Read more about Lambda response streaming](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-response-streaming/) and [API Gateway response streaming](https://aws.amazon.com/blogs/compute/building-responsive-apis-with-amazon-api-gateway-response-streaming/).

### Response Streaming[​](#response-streaming "Direct link to Response Streaming")

The signature of a streaming handler is different from the default handler. The streaming handler additionally receives a writable stream parameter, `responseStream`, besides the default node handler parameters, `event` and `context`. To indicate that Lambda should stream your responses, you must wrap your function handler with the `awslambda.streamifyResponse()` decorator.

> Note that the `awslambda` namespace is automatically provided by the Lambda execution environment. You can import the types from `@types/aws-lambda` to augment the global namespace with the `awslambda` namespace.

server.ts

ts

`/// <reference types="aws-lambda" />`

`import type { APIGatewayProxyEventV2 } from 'aws-lambda';`

`import type { CreateAWSLambdaContextOptions } from '@trpc/server/adapters/aws-lambda';`

`import { awsLambdaStreamingRequestHandler } from '@trpc/server/adapters/aws-lambda';`

`import { appRouter } from './router';`

`// created for each request`

`const createContext = ({`

  `event,`

  `context,`

`}: CreateAWSLambdaContextOptions<APIGatewayProxyEventV2>) => ({`

  `// your context`

`});`

`type Context = Awaited<ReturnType<typeof createContext>>;`

`export const handler = awslambda.streamifyResponse(`

  `awsLambdaStreamingRequestHandler({`

    `router: appRouter,`

    `createContext,`

  `}),`

`);`
