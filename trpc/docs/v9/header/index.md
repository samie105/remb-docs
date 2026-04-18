---
title: "Custom header"
source: "https://trpc.io/docs/v9/header"
canonical_url: "https://trpc.io/docs/v9/header"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:04.839Z"
content_hash: "96359f5ed6078b7ef53e9a6e7130f6fc47b8ebf0280cc7eedd41424a1c827a01"
menu_path: ["Custom header"]
section_path: []
---
Version: 9.x

The headers option can be customized in config when using `withTRPC` in nextjs or `createClient` in react.js.

`headers` can be both an object or a function. If it's a function it will gets called dynamically every http request.

`   import type { AppRouter } from '@/server/routers/app';  import { withTRPC } from '@trpc/next';  import { AppType } from 'next/dist/shared/lib/utils';  export let token: string;  const MyApp: AppType = ({ Component, pageProps }) => {    return <Component {...pageProps} />;  };  export default withTRPC<AppRouter>({    config(config) {      return {        links: [          httpBatchLink({            /** headers are called on every request */            headers: () => {              return {                Authorization: token,              };            },          }),        ],      };    },  })(MyApp);   `

`   import type { AppRouter } from '@/server/routers/app';  import { withTRPC } from '@trpc/next';  import { AppType } from 'next/dist/shared/lib/utils';  export let token: string;  const MyApp: AppType = ({ Component, pageProps }) => {    return <Component {...pageProps} />;  };  export default withTRPC<AppRouter>({    config(config) {      return {        links: [          httpBatchLink({            /** headers are called on every request */            headers: () => {              return {                Authorization: token,              };            },          }),        ],      };    },  })(MyApp);   `

### Example with auth login[​](#example-with-auth-login "Direct link to Example with auth login")

`   const loginMut = trpc.useMutation(['auth.login'], {    onSuccess({ accessToken }) {      token = accessToken;    },  });   `

`   const loginMut = trpc.useMutation(['auth.login'], {    onSuccess({ accessToken }) {      token = accessToken;    },  });   `

The `token` can be whatever you want it to be. It's entirely up to you whether that's just a client-side variable that you update the value of on success or whether you store the token and pull it from local storage.

*   [Example with auth login](#example-with-auth-login)
