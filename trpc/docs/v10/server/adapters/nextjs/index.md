---
title: "Next.js Adapter"
source: "https://trpc.io/docs/v10/server/adapters/nextjs"
canonical_url: "https://trpc.io/docs/v10/server/adapters/nextjs"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:18.237Z"
content_hash: "b3e6824a3efd4f2adaa50ba25957affc1ac122c57fc4e093d3506d73f70b2e79"
menu_path: ["Next.js Adapter"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/server/adapters/fastify/index.md", "title": "Fastify Adapter"}
nav_next: {"path": "trpc/docs/v10/server/adapters/standalone/index.md", "title": "Standalone Adapter"}
---

Serving your tRPC router in a Next.js project is straight-forward. Just create an API handler in `pages/api/trpc/[trpc].ts` as shown below:

pages/api/trpc/\[trpc\].ts

ts

`import { createNextApiHandler } from '@trpc/server/adapters/next';`

`import { createContext } from '../../../server/trpc/context';`

`import { appRouter } from '../../../server/trpc/router/_app';`

`// @link https://nextjs.org/docs/api-routes/introduction`

`export default createNextApiHandler({`

  `router: appRouter,`

  `createContext,`

`});`

While you can usually just "set and forget" the API Handler as shown above, sometimes you might want to modify it further.

The API handler created by `createNextApiHandler` and equivalents in other frameworks is just a function that takes `req` and `res` objects. This means you can also modify those objects before passing them to the handler, for example to [enable CORS](trpc/docs/client/cors/index.md).

pages/api/trpc/\[trpc\].ts

ts

`import { createNextApiHandler } from '@trpc/server/adapters/next';`

`import { createContext } from '../../../server/trpc/context';`

`import { appRouter } from '../../../server/trpc/router/_app';`

`// create the API handler, but don't return it yet`

`const nextApiHandler = createNextApiHandler({`

  `router: appRouter,`

  `createContext,`

`});`

`// @link https://nextjs.org/docs/api-routes/introduction`

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

If you're trying out the Next.js App Router and want to use [route handlers](https://beta.nextjs.org/docs/routing/route-handlers), you can do so by using the [fetch](trpc/docs/v10/server/adapters/fetch/index.md) adapter, as they build on web standard Request and Response objects:

app/api/trpc/\[trpc\]/route.ts

ts

`import { fetchRequestHandler } from '@trpc/server/adapters/fetch';`

`import { appRouter } from '~/server/api/router';`

`const handler = (req: Request) =>`

  `fetchRequestHandler({`

    `endpoint: '/api/trpc',`

    `req,`

    `router: appRouter,`

    `createContext: () => ({ ... })`

  `});`

`export { handler as GET, handler as POST };`
