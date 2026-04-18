---
title: "Deploy Prisma ORM"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/deploy-prisma"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/deploy-prisma"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:55.913Z"
content_hash: "03e655e472215c125c9269c2db31605bbf2c2d8cf7d30125e8bc1e9871cf284f"
menu_path: ["Deploy Prisma ORM"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/deployment/deploy-migrations-from-a-local-environment/index.md", "title": "Deploy migrations from a local environment"}
nav_next: {"path": "prisma/docs/orm/prisma-client/observability-and-logging/logging/index.md", "title": "Logging"}
---

Deployment

Learn more about the different deployment paradigms for Node.js applications and how they affect deploying an application using Prisma Client

Projects using Prisma Client can be deployed to many different cloud platforms. Given the variety of cloud platforms and different names, it's noteworthy to mention the different deployment paradigms, as they affect the way you deploy an application using Prisma Client.

Each paradigm has different tradeoffs that affect the performance, scalability, and operational costs of your application.

Moreover, the user traffic pattern of your application is also an important factor to consider. For example, any application with consistent user traffic may be better suited for a [continuously running paradigm](#traditional-servers), whereas an application with sudden spikes may be better suited to [serverless](#serverless-functions).

### [Traditional servers](#traditional-servers)

Your application is [traditionally deployed](prisma/docs/orm/prisma-client/deployment/traditional/deploy-to-heroku/index.md) if a Node.js process is continuously running and handles multiple requests at the same time. Your application could be deployed to a Platform-as-a-Service (PaaS) like [Heroku](prisma/docs/orm/prisma-client/deployment/traditional/deploy-to-heroku/index.md), [Koyeb](prisma/docs/orm/prisma-client/deployment/traditional/deploy-to-koyeb/index.md), or [Render](prisma/docs/orm/prisma-client/deployment/traditional/deploy-to-render/index.md); as a Docker container to Kubernetes; or as a Node.js process on a virtual machine or bare metal server.

See also: [Connection management in long-running processes](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md#long-running-processes)

### [Serverless Functions](#serverless-functions)

Your application is [serverless](prisma/docs/orm/prisma-client/deployment/serverless/deploy-to-vercel/index.md) if the Node.js processes of your application (or subsets of it broken into functions) are started as requests come in, and each function only handles one request at a time. Your application would most likely be deployed to a Function-as-a-Service (FaaS) offering, such as [AWS Lambda](prisma/docs/orm/prisma-client/deployment/serverless/deploy-to-aws-lambda/index.md) or [Azure Functions](prisma/docs/orm/prisma-client/deployment/serverless/deploy-to-azure-functions/index.md)

Serverless environments have the concept of warm starts, which means that for subsequent invocations of the same function, it may use an already existing container that has the allocated processes, memory, file system (`/tmp` is writable on AWS Lambda), and even DB connection still available.

Typically, any piece of code [outside the handler](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) remains initialized.

See also: [Connection management in serverless environments](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md#serverless-environments-faas)

### [Edge Functions](#edge-functions)

Your application is [edge deployed](prisma/docs/orm/prisma-client/deployment/edge/overview/index.md) if your application is [serverless](#serverless-functions) and the functions are distributed across one or more regions close to the user.

Typically, edge environments also have a different runtime than a traditional or serverless environment, leading to common APIs being unavailable.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/deployment/deploy-prisma.mdx)
