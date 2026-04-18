---
title: "Headers"
source: "https://trpc.io/docs/client/headers"
canonical_url: "https://trpc.io/docs/client/headers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:38.963Z"
content_hash: "193901ba691e08cc471b193493bd5d5debecd550acec113bb81beeef9f3cbe7f"
menu_path: ["Headers"]
section_path: []
nav_prev: {"path": "trpc/docs/client/cors/index.md", "title": "Send cookies cross-origin"}
nav_next: {"path": "trpc/docs/client/links/index.md", "title": "Links Overview"}
---

Version: 11.x

The headers option may be used with any of our HTTP links: [`httpBatchLink`](trpc/docs/client/links/httpBatchLink/index.md), [`httpBatchStreamLink`](trpc/docs/client/links/httpBatchStreamLink/index.md), [`httpLink`](trpc/docs/client/links/httpLink/index.md), or [`httpSubscriptionLink`](trpc/docs/client/links/httpSubscriptionLink/index.md).

`headers` can be both an object or a function. If it's a function it will get called dynamically for every HTTP request.

`   import { createTRPCClient, httpBatchLink } from '@trpc/client';  import type { AppRouter } from './server';  let token: string;  export function setToken(newToken: string) {    /**     * You can also save the token to cookies, and initialize from     * cookies above.     */    token = newToken;  }  export const trpc = createTRPCClient<AppRouter>({    links: [      httpBatchLink({        url: 'http://localhost:3000',        /**         * Headers will be called on each request.         */        headers() {          return {            Authorization: token,          };        },      }),    ],  });   `

`   import { createTRPCClient, httpBatchLink } from '@trpc/client';  import type { AppRouter } from './server';  let token: string;  export function setToken(newToken: string) {    /**     * You can also save the token to cookies, and initialize from     * cookies above.     */    token = newToken;  }  export const trpc = createTRPCClient<AppRouter>({    links: [      httpBatchLink({        url: 'http://localhost:3000',        /**         * Headers will be called on each request.         */        headers() {          return {            Authorization: token,          };        },      }),    ],  });   `

### Example with auth login[​](#example-with-auth-login "Direct link to Example with auth login")

`   const result = await trpc.auth.login.mutate({ username: 'user', password: 'pass' });  setToken(result.accessToken);   `

`   const result = await trpc.auth.login.mutate({ username: 'user', password: 'pass' });  setToken(result.accessToken);   `

The `token` can be whatever you want it to be. It's entirely up to you whether that's just a client-side variable that you update the value of on success or whether you store the token and pull it from local storage.

*   [Example with auth login](#example-with-auth-login)
