---
title: "Migrating from the classic React Client"
source: "https://trpc.io/docs/client/tanstack-react-query/migrating"
canonical_url: "https://trpc.io/docs/client/tanstack-react-query/migrating"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:29.554Z"
content_hash: "c826eee52d827d6e28a7a1a278814c07244112bf8a67a5f6531b53e85344dfca"
menu_path: ["Migrating from the classic React Client"]
section_path: []
nav_prev: {"path": "trpc/docs/client/tanstack-react-query/index.md", "title": "TanStack React Query"}
nav_next: {"path": "trpc/docs/client/tanstack-react-query/server-components/index.md", "title": "Set up with React Server Components"}
---

There are a few approaches to migrate over, and this library is a significant departure from the classic client, so we're not expecting anybody to do it in one shot. But you will probably want to try a combination of...

## Codemod migration[​](#codemod-migration "Direct link to Codemod migration")

info

The codemod is a work in progress and we're looking for help to make it better. If you're interested in contributing to the codemod, please see [Julius' comment here](https://github.com/trpc/trpc/pull/6262#issuecomment-2651959435).

We're working on a codemod to help you migrate your existing codebase over to the new client. This is already available to try but we need your feedback and contributions to improve it. Codemods are very tricky to get right so we're looking for your help to make it as effective as possible.

Run our upgrade CLI:

sh

`npx @trpc/upgrade`

When prompted, select the transforms `Migrate Hooks to xxxOptions API` and `Migrate context provider setup`.

## Gradual migration[​](#gradual-migration "Direct link to Gradual migration")

The new and classic clients are compatible with each other and [can live together in the same application](https://github.com/juliusmarminge/trpc-interop/blob/main/src/client.tsx). This means you can start migrating by using the new client in new parts of your application, and gradually migrate over existing usage as you see fit. Most importantly, Query Keys are identical, which means you can use the new client and classic client together and still rely on TanStack Query's caching.

### Migrating Queries[​](#migrating-queries "Direct link to Migrating Queries")

A classic query would look like this

tsx

`import { trpc } from './trpc';`

`function Users() {`

  `const greetingQuery = trpc.greeting.useQuery({ name: 'Jerry' });`

  `// greetingQuery.data === 'Hello Jerry'`

`}`

and changes to

tsx

`import { useQuery } from '@tanstack/react-query';`

`import { useTRPC } from './trpc';`

`function Users() {`

  `const trpc = useTRPC();`

  `const greetingQuery = useQuery(trpc.greeting.queryOptions({ name: 'Jerry' }));`

  `// greetingQuery.data === 'Hello Jerry'`

`}`

### Migrating Invalidations and other QueryClient usages[​](#migrating-invalidations-and-other-queryclient-usages "Direct link to Migrating Invalidations and other QueryClient usages")

A classic invalidation pattern would look like this

tsx

`import { trpc } from './trpc';`

`function Users() {`

  `const utils = trpc.useUtils();`

  `async function invalidateGreeting() {`

    `await utils.greeting.invalidate({ name: 'Jerry' });`

  `}`

`}`

and changes to

tsx

`import { useQueryClient } from '@tanstack/react-query';`

`import { useTRPC } from './trpc';`

`function Users() {`

  `const trpc = useTRPC();`

  `const queryClient = useQueryClient();`

  `async function invalidateGreeting() {`

    `await queryClient.invalidateQueries(`

      `trpc.greeting.queryFilter({ name: 'Jerry' }),`

    `);`

  `}`

`}`

This is the same for any QueryClient usage, instead of using tRPC's `useUtils` you can now follow the TanStack documentation directly

### Migrating Mutations[​](#migrating-mutations "Direct link to Migrating Mutations")

A classic mutation might look like this

tsx

`import { trpc } from './trpc';`

`function Users() {`

  `const createUserMutation = trpc.createUser.useMutation();`

  `createUserMutation.mutate({ name: 'Jerry' });`

`}`

and changes to

tsx

`import { useMutation } from '@tanstack/react-query';`

`import { useTRPC } from './trpc';`

`function Users() {`

  `const trpc = useTRPC();`

  `const createUserMutation = useMutation(trpc.createUser.mutationOptions());`

  `createUserMutation.mutate({ name: 'Jerry' });`

`}`


