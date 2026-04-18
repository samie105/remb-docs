---
title: "Aborting Procedure Calls"
source: "https://trpc.io/docs/v10/client/nextjs/aborting-procedure-calls"
canonical_url: "https://trpc.io/docs/v10/client/nextjs/aborting-procedure-calls"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:47.500Z"
content_hash: "aee42abf3e675b5949a177feaa5785cc602b2b433ed58b43fd8bc73392ed85d8"
menu_path: ["Aborting Procedure Calls"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/nextjs/index.md", "title": "Next.js Integration"}
nav_next: {"path": "trpc/docs/v10/client/nextjs/server-side-helpers/index.md", "title": "Server-Side Helpers"}
---

By default, tRPC does not cancel requests on unmount. If you want to opt into this behavior, you can provide `abortOnUnmount` in your configuration callback.

### Globally[​](#globally "Direct link to Globally")

client.ts

ts

`// @filename: utils.ts`

`import { createTRPCNext } from '@trpc/next';`

`export const trpc = createTRPCNext<AppRouter>({`

  `config() {`

    `return {`

      `// ...`

      `abortOnUnmount: true,`

    `};`

  `},`

`});`

### Per-request[​](#per-request "Direct link to Per-request")

You may also override this behavior at the request level.

client.ts

ts

`// @filename: pages/posts/[id].tsx`

`import { trpc } from '~/utils/trpc';`

`const PostViewPage: NextPageWithLayout = () => {`

  `const id = useRouter().query.id as string;`

  `const postQuery = trpc.post.byId.useQuery({ id }, { trpc: { abortOnUnmount: true } });`

  `return (...)`

`}`

