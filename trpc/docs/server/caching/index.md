---
title: "Response Caching"
source: "https://trpc.io/docs/server/caching"
canonical_url: "https://trpc.io/docs/server/caching"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:35.720Z"
content_hash: "c81f56ca2282ddb1b1c1643ec7633daa04a2902f6a0b6b7c051b5da4c2fb024a"
menu_path: ["Response Caching"]
section_path: []
nav_prev: {"path": "trpc/docs/server/authorization/index.md", "title": "Authorization"}
nav_next: {"path": "trpc/docs/server/context/index.md", "title": "Context"}
---

Since all tRPC queries are normal HTTP `GET` requests, you can use standard HTTP cache headers to cache responses. This can make responses snappy, give your database a rest, and help scale your API.

Most tRPC adapters support a `responseMeta` callback that lets you set HTTP headers (including cache headers) based on the procedures being called.

server.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { createHTTPServer } from '@trpc/server/adapters/standalone';`

`import type { CreateHTTPContextOptions } from '@trpc/server/adapters/standalone';`

`export const createContext = async (opts: CreateHTTPContextOptions) => {`

  `return {`

    `req: opts.req,`

    `res: opts.res,`

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

``// Exporting `type AppRouter` only exposes types that can be used for inference``

`// https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export`

`export type AppRouter = typeof appRouter;`

`// export API handler`

`const server = createHTTPServer({`

  `router: appRouter,`

  `createContext,`

  `responseMeta(opts) {`

    `const { paths, errors, type } = opts;`

    ``// assuming you have all your public routes with the keyword `public` in them``

    `const allPublic = paths && paths.every((path) => path.includes('public'));`

    `// checking that no procedures errored`

    `const allOk = errors.length === 0;`

    `// checking we're doing a query request`

    `const isQuery = type === 'query';`

    `if (allPublic && allOk && isQuery) {`

      `// cache request for 1 day + revalidate once every second`

      `const ONE_DAY_IN_SECONDS = 60 * 60 * 24;`

      `return {`

        `headers: new Headers([`

          `[`

            `'cache-control',`

            `` `s-maxage=1, stale-while-revalidate=${ONE_DAY_IN_SECONDS}`, ``

          `],`

        `]),`

      `};`

    `}`

    `return {};`

  `},`

`});`

`server.listen(3000);`
