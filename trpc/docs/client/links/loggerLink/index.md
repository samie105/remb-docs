---
title: "Logger Link"
source: "https://trpc.io/docs/client/links/loggerLink"
canonical_url: "https://trpc.io/docs/client/links/loggerLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:12.828Z"
content_hash: "062850f0abc0bbbbe4800bb78df033b88893f875479b6d20288815bdc2305899"
menu_path: ["Logger Link"]
section_path: []
nav_prev: {"path": "trpc/docs/client/links/localLink/index.md", "title": "Local Link"}
nav_next: {"path": "trpc/docs/client/links/splitLink/index.md", "title": "Split Link"}
---

`loggerLink` is a link that lets you implement a logger for your tRPC client. It allows you to see more clearly what operations are queries, mutations, or subscriptions, their requests, and responses. The link, by default, prints a prettified log to the browser's console. However, you can customize the logging behavior and the way it prints to the console with your own implementations.

## Usage[​](#usage "Direct link to Usage")

You can import and add the `loggerLink` to the `links` array as such:

client/index.ts

ts

`import { createTRPCClient, httpBatchLink, loggerLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `/**`

     `* The function passed to enabled is an example in case you want to the link to`

     `* log to your console in development and only log errors in production`

     `*/`

    `loggerLink({`

      `enabled: (opts) =>`

        `(process.env.NODE_ENV === 'development' &&`

          `typeof window !== 'undefined') ||`

        `(opts.direction === 'down' && opts.result instanceof Error),`

    `}),`

    `httpBatchLink({`

      `url: 'http://localhost:3000',`

    `}),`

  `],`

`});`

## `loggerLink` Options[​](#loggerlink-options "Direct link to loggerlink-options")

The `loggerLink` function takes an options object that has the `LoggerLinkOptions` shape:

ts

`type LoggerLinkOptions<TRouter extends AnyRouter> = {`

  `logger?: LogFn<TRouter>;`

  `/**`

   `* It is a function that returns a condition that determines whether to enable the logger.`

   `* It is true by default.`

   `*/`

  `enabled?: EnabledFn<TRouter>;`

  `/**`

   `* Used in the built-in defaultLogger`

   `*/`

  `console?: ConsoleEsque;`

  `/**`

   `* Color mode used in the default logger.`

   `* @default typeof window === 'undefined' ? 'ansi' : 'css'`

   `*/`

  `colorMode?: 'ansi' | 'css' | 'none';`

  `/**`

   `* Include context in the log - defaults to false unless colorMode is 'css'`

   `*/`

  `withContext?: boolean;`

`};`

## Reference[​](#reference "Direct link to Reference")

You can check out the source code for this link on [GitHub.](https://github.com/trpc/trpc/blob/main/packages/client/src/links/loggerLink.ts)


