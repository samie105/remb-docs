---
title: "Custom header"
source: "https://trpc.io/docs/v10/client/headers"
canonical_url: "https://trpc.io/docs/v10/client/headers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:11.558Z"
content_hash: "3d3ea21b40d41a60c6745867277e9efaaa40f31585f5c1b8b004b19ffc3d974e"
menu_path: ["Custom header"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/cors/index.md", "title": "Send cookies cross-origin"}
nav_next: {"path": "trpc/docs/v10/client/links/index.md", "title": "Links Overview"}
---

Version: 10.x

The headers option can be customized in the config when using the [`httpBatchLink`](../links/httpBatchLink/index.md) or the [`httpLink`](../links/httpLink/index.md).

`headers` can be both an object or a function. If it's a function it will get called dynamically for every HTTP request.

`   // Import the router type from your server file  import type { AppRouter } from '@/server/routers/app';  import { httpBatchLink } from '@trpc/client';  import { createTRPCNext } from '@trpc/next';  let token: string;  export function setToken(newToken: string) {    /**     * You can also save the token to cookies, and initialize from     * cookies above.     */    token = newToken;  }  export const trpc = createTRPCNext<AppRouter>({    config(config) {      return {        links: [          httpBatchLink({            url: 'http://localhost:3000/api/trpc',            /**             * Headers will be called on each request.             */            headers() {              return {                Authorization: token,              };            },          }),        ],      };    },  });   `

`   // Import the router type from your server file  import type { AppRouter } from '@/server/routers/app';  import { httpBatchLink } from '@trpc/client';  import { createTRPCNext } from '@trpc/next';  let token: string;  export function setToken(newToken: string) {    /**     * You can also save the token to cookies, and initialize from     * cookies above.     */    token = newToken;  }  export const trpc = createTRPCNext<AppRouter>({    config(config) {      return {        links: [          httpBatchLink({            url: 'http://localhost:3000/api/trpc',            /**             * Headers will be called on each request.             */            headers() {              return {                Authorization: token,              };            },          }),        ],      };    },  });   `

### Example with auth login[​](#example-with-auth-login "Direct link to Example with auth login")

`   const loginMut = trpc.auth.login.useMutation({    onSuccess(opts) {      token = opts.accessToken;    },  });   `

`   const loginMut = trpc.auth.login.useMutation({    onSuccess(opts) {      token = opts.accessToken;    },  });   `

The `token` can be whatever you want it to be. It's entirely up to you whether that's just a client-side variable that you update the value of on success or whether you store the token and pull it from local storage.

*   [Example with auth login](#example-with-auth-login)
