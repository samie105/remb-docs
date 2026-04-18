---
title: "Next.js Adapter"
source: "https://trpc.io/docs/server/adapters/nextjs"
canonical_url: "https://trpc.io/docs/server/adapters/nextjs"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:14.797Z"
content_hash: "56af26b0fd5e06e2ad3dfd5b79c4a0248b0e16753c24a5177e251de9f73e00e0"
menu_path: ["Next.js Adapter"]
section_path: []
nav_prev: {"path": "trpc/docs/server/adapters/fastify/index.md", "title": "Fastify Adapter"}
nav_next: {"path": "trpc/docs/server/adapters/fetch/index.md", "title": "Fetch / Edge Runtimes Adapter"}
---

Serving your tRPC router in a Next.js project is straight-forward. Just create an API handler in `pages/api/trpc/[trpc].ts` as shown below:

pages/api/trpc/\[trpc\].ts

ts

`import { createNextApiHandler } from '@trpc/server/adapters/next';`

`import { createContext } from '../../../server/trpc/context';`

`import { appRouter } from '../../../server/trpc/router/_app';`

`export default createNextApiHandler({`

  `router: appRouter,`

  `createContext,`

`});`

While you can usually just "set and forget" the API Handler as shown above, sometimes you might want to modify it further.

The API handler created by `createNextApiHandler` and equivalents in other frameworks is just a function that takes `req` and `res` objects. This means you can also modify those objects before passing them to the handler, for example to [enable CORS](trpc/docs/client/cors/index.md).

pages/api/trpc/\[trpc\].ts

ts

`import type { NextApiRequest, NextApiResponse } from 'next';`

`import { createNextApiHandler } from '@trpc/server/adapters/next';`

`import { createContext } from '../../../server/trpc/context';`

`import { appRouter } from '../../../server/trpc/router/_app';`

`// create the API handler, but don't return it yet`

`const nextApiHandler = createNextApiHandler({`

  `router: appRouter,`

  `createContext,`

`});`

`// https://nextjs.org/docs/api-routes/introduction`

`export default async function handler(`

  `req: NextApiRequest,`

  `res: NextApiResponse,`

`) {`

  `// We can use the response object to enable CORS`

  `res.setHeader('Access-Control-Allow-Origin', '*');`

  `res.setHeader('Access-Control-Request-Method', '*');`

  `res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET');`

  `res.setHeader('Access-Control-Allow-Headers', '*');`

  `// If you need to make authenticated CORS calls then`

  `// remove what is above and uncomment the below code`

  `// Allow-Origin has to be set to the requesting domain that you want to send the credentials back to`

  `// res.setHeader('Access-Control-Allow-Origin', 'http://example:6006');`

  `// res.setHeader('Access-Control-Request-Method', '*');`

  `// res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET');`

  `// res.setHeader('Access-Control-Allow-Headers', 'content-type');`

  `// res.setHeader('Referrer-Policy', 'no-referrer');`

  `// res.setHeader('Access-Control-Allow-Credentials', 'true');`

  `if (req.method === 'OPTIONS') {`

    `res.writeHead(200);`

    `return res.end();`

  `}`

  `// finally pass the request on to the tRPC handler`

  `return nextApiHandler(req, res);`

`}`

If you're using the Next.js **App Router**, use the [fetch adapter](trpc/docs/server/adapters/fetch/index.md) instead, as App Router route handlers are based on the Web standard `Request` and `Response` objects. See the [App Router setup guide](trpc/docs/client/nextjs/app-router-setup/index.md) for a complete walkthrough.

app/api/trpc/\[trpc\]/route.ts

ts

`import { fetchRequestHandler } from '@trpc/server/adapters/fetch';`

`import { createTRPCContext } from '../../trpc/init';`

`import { appRouter } from '../../trpc/routers/_app';`

`const handler = (req: Request) =>`

  `fetchRequestHandler({`

    `endpoint: '/api/trpc',`

    `req,`

    `router: appRouter,`

    `createContext: createTRPCContext,`

  `});`

`export { handler as GET, handler as POST };`


