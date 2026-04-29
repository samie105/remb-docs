---
title: "Response Caching"
source: "https://trpc.io/docs/v10/server/caching"
canonical_url: "https://trpc.io/docs/v10/server/caching"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:45.279Z"
content_hash: "34de0be4d37337043ae4b821d7133406898ea553e43ebfa7f60a56bcc75db2e7"
menu_path: ["Response Caching"]
section_path: []
nav_prev: {"path": "../authorization/index.md", "title": "Authorization"}
nav_next: {"path": "../context/index.md", "title": "Context"}
---

The below examples uses [Vercel's edge caching](https://vercel.com/docs/edge-network/caching) to serve data to your users as fast as possible.

If you turn on SSR in your app, you might discover that your app loads slowly on, for instance, Vercel, but you can actually statically render your whole app without using SSG; [read this Twitter thread](https://twitter.com/alexdotjs/status/1386274093041950722) for more insights.

utils/trpc.tsx

tsx

`import { httpBatchLink } from '@trpc/client';`

`import { createTRPCNext } from '@trpc/next';`

`import type { AppRouter } from '../server/routers/_app';`

`export const trpc = createTRPCNext<AppRouter>({`

  `config(config) {`

    `if (typeof window !== 'undefined') {`

      `return {`

        `links: [`

          `httpBatchLink({`

            `url: '/api/trpc',`

          `}),`

        `],`

      `};`

    `}`

    `const url = process.env.VERCEL_URL`

      `` ? `https://${process.env.VERCEL_URL}/api/trpc` ``

      `: 'http://localhost:3000/api/trpc';`

    `return {`

      `links: {`

        `http: httpBatchLink({`

          `url,`

        `}),`

      `},`

    `};`

  `},`

  `ssr: true,`

  `responseMeta(opts) {`

    `const { clientErrors } = opts;`

    `if (clientErrors.length) {`

      `// propagate http first error from API calls`

      `return {`

        `status: clientErrors[0].data?.httpStatus ?? 500,`

      `};`

    `}`

    `// cache request for 1 day + revalidate once every second`

    `const ONE_DAY_IN_SECONDS = 60 * 60 * 24;`

    `return {`

      `headers: {`

        ``'cache-control': `s-maxage=1, stale-while-revalidate=${ONE_DAY_IN_SECONDS}`,``

      `},`

    `};`

  `},`

`});`

Since all queries are normal HTTP `GET`s, we can use normal HTTP headers to cache responses, make the responses snappy, give your database a rest, and easily scale your API to gazillions of users.

server.ts

tsx

`import { initTRPC } from '@trpc/server';`

`import * as trpcNext from '@trpc/server/adapters/next';`

`export const createContext = async ({`

  `req,`

  `res,`

`}: trpcNext.CreateNextContextOptions) => {`

  `return {`

    `req,`

    `res,`

    `prisma,`

  `};`

`};`

`type Context = Awaited<ReturnType<typeof createContext>>;`

`export const t = initTRPC.context<Context>().create();`

`const waitFor = async (ms: number) =>`

  `new Promise((resolve) => setTimeout(resolve, ms));`

`export const appRouter = t.router({`

  `public: t.router({`

    `slowQueryCached: t.procedure.query(async (opts) => {`

      `await waitFor(5000); // wait for 5s`

      `return {`

        `lastUpdated: new Date().toJSON(),`

      `};`

    `}),`

  `}),`

`});`

`// Exporting type _type_ AppRouter only exposes types that can be used for inference`

`// https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export`

`export type AppRouter = typeof appRouter;`

`// export API handler`

`export default trpcNext.createNextApiHandler({`

  `router: appRouter,`

  `createContext,`

  `responseMeta(opts) {`

    `const { ctx, paths, errors, type } = opts;`

    ``// assuming you have all your public routes with the keyword `public` in them``

    `const allPublic = paths && paths.every((path) => path.includes('public'));`

    `// checking that no procedures errored`

    `const allOk = errors.length === 0;`

    `// checking we're doing a query request`

    `const isQuery = type === 'query';`

    `if (ctx?.res && allPublic && allOk && isQuery) {`

      `// cache request for 1 day + revalidate once every second`

      `const ONE_DAY_IN_SECONDS = 60 * 60 * 24;`

      `return {`

        `headers: {`

          ``'cache-control': `s-maxage=1, stale-while-revalidate=${ONE_DAY_IN_SECONDS}`,``

        `},`

      `};`

    `}`

    `return {};`

  `},`

`});`
