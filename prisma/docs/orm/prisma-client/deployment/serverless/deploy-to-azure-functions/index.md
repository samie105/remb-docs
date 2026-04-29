---
title: "Deploy to Azure Functions"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-azure-functions"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-azure-functions"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:43:50.503Z"
content_hash: "7451095437962905165bb31eba1ea995875f82b061fe6ce2f397813c640c132d"
menu_path: ["Deploy to Azure Functions"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/deployment/serverless/deploy-to-aws-lambda/index.md", "title": "Deploy to AWS Lambda"}
nav_next: {"path": "prisma/docs/orm/prisma-client/deployment/serverless/deploy-to-netlify/index.md", "title": "Deploy to Netlify"}
---

Learn how to deploy a Prisma Client based REST API to Azure Functions and connect to an Azure SQL database

This guide explains how to avoid common issues when deploying a Node.js-based function app to Azure using [Azure Functions](https://azure.microsoft.com/en-us/products/functions/).

Azure Functions is a serverless deployment platform. You do not need to maintain infrastructure to deploy your code. With Azure Functions, the fundamental building block is the [function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference?tabs=blob&pivots=programming-language-typescript). A function app provides an execution context in Azure in which your functions run. It is comprised of one or more individual functions that Azure manages, deploys, and scales together. You can organize and collectively manage multiple functions as a single logical unit.

-   An existing function app project with Prisma ORM

While Prisma ORM works well with Azure functions, there are a few things to take note of before deploying your application.

### [Connection pooling](#connection-pooling)

Generally, when you use a FaaS (Function as a Service) environment to interact with a database, every function invocation can result in a new connection to the database. This is not a problem with a constantly running Node.js server. Therefore, it is beneficial to pool DB connections to get better performance. To solve this issue, you can use [Prisma Postgres](https://www.prisma.io/docs/postgres). For other solutions, see the [connection management guide for serverless environments](../../../setup-and-configuration/databases-connections/index.md#serverless-environments-faas).

For more insight into Prisma Client's API, explore the function handlers and check out the [Prisma Client API Reference](../../../../reference/prisma-client-reference/index.md)
